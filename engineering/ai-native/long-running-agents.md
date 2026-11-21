---
type: note
title: Long-Running Agents
description: "Why the chat-window agent loop hits a ceiling, and the durability layer (context, state, self-verification) long-running agents need."
tags: [ai-engineering, agentic-workflows, architecture, reading]
topic: engineering/ai-native
status: notes
level: intermediate
related:
  - engineering/ai-native/harness-engineering.md
  - engineering/ai-native/loop-driven-development.md
  - engineering/ai-native/agent-backpressure-loops.md
  - engineering/ai-native/eval-driven-ai-development.md
  - engineering/ai-native/ai-native-engineering-stack.md
  - engineering/ai-native/ai-native-engineering-overview.md
  - engineering/ai-native/ci-speed-with-ai-agents.md
  - languages-and-frameworks/go-agentic-language.md
  - reading/multi-agent-coding-coordination.md
  - engineering/ai-native/agentic-autonomy-levels.md
  - case-studies/oracle-ai-agent-memory.md
  - engineering/ai-native/light-and-dark-factories.md
  - engineering/ai-native/harness-design-experiments.md
  - case-studies/stripe-kai-agent-platform.md
  - case-studies/ramp-inspect-agent-platform.md
  - case-studies/cursor-agent-swarm-economics.md
  - reading/reactive-reducer-orchestration.md
  - case-studies/github-copilot-rust-migration.md
  - reading/ultimate-self-extending-harness.md
  - engineering/architecture/agents-as-distributed-systems.md
  - sre/ai-sre-and-the-incident-path.md
  - engineering/ai-native/ai-gateway-control-plane.md
  - engineering/ai-native/accountability-for-unread-code.md
  - engineering/architecture/cell-based-architecture.md
  - engineering/practices/database-migration-strategies.md
  - engineering/ai-native/agentic-sdlc.md
  - engineering/ai-native/agentic-code-review.md
  - case-studies/doordash-flag-cleanup-agents.md
source: "https://addyo.substack.com/p/long-running-agents; https://generativeprogrammer.com/p/the-evolution-of-agentic-loops"
updated: 2026-11-21
---

# Long-Running Agents

Addy Osmani argues that the chat-window agent loop is hitting a ceiling: the next
step is agents that operate **autonomously over hours, days, or weeks** while
staying coherent, recovering from failure, and accumulating context. His central
claim is that the gap between a chat agent and a production long-running agent is
"mostly in the state, sessions, and structured handoffs wrapped around the model,
**not the model itself**." Where [Harness Engineering](harness-engineering.md)
describes the *anatomy* of the harness program, this note is about the
*durability* dimension — what changes when the run is long.

## Three meanings

"Long-running" conflates three distinct things:

- **Long-horizon reasoning** — planning and executing many dependent steps. Osmani
  cites METR's finding that models' task time-horizon has doubled roughly every
  seven months, and *forecasts* (treat as projections, not facts) day-scale tasks
  by ~2028 and year-scale by ~2034.
- **Long-running execution** — a process running for hours/days across thousands of
  model invocations. Primarily an **engineering (harness)** problem.
- **Persistent agency** — an agent identity that outlives individual tasks,
  accumulating memory and preferences across sessions.

## The three walls

| Wall | Problem |
|---|---|
| **Finite context** | Even a 1M-token window fills, and **context rot** degrades quality well before the hard limit. A 24-hour run fits no foreseeable window. |
| **No persistent state** | Without explicit persistence, every session handoff is "a new engineer arriving with no memory of the previous shift". |
| **No self-verification** | Models skew positive grading their own work — asked "are you done?" they say yes too often (declaring completion at ~30%). |

Plus the production realities: cost runaway, a larger security surface, alignment
drift, and verification burden.

## Brain / hands / session

The architectural pattern the major labs converge on decouples three concerns:

- **Brain** — the model and reasoning loop; stateless and replaceable.
- **Hands** — ephemeral, sandboxed execution environments.
- **Session** — an append-only event log of every thought, tool call, and
  observation.

Decoupling these is what lets the system survive component failure and swap models
without rewriting everything; coupling them means stale assumptions force wholesale
changes. The **session log — not the prompt — is what makes the system
recoverable and auditable.**

## Patterns for going long

- **Checkpoint-and-resume** at task-meaningful granularity (not every step, not only
  at the end).
- **Context resets over endless summarisation.** For very long jobs, repeated
  re-summarising loses fidelity; do a full reset with a **structured handoff file**
  instead. Treat the reset like onboarding a new engineer at shift change.
- **External state.** Keep progress in the filesystem outside the model's context —
  plan files (`prd.json`, feature lists), `progress.txt`, `CHANGELOG.md`. The
  **Ralph Loop** (Huntley, Carson) captures the idea: "the agent is amnesiac, but
  the filesystem isn't."
- **Generation separated from evaluation** — a planner/worker/judge pipeline, with
  **test ratchets** that block an agent from deleting failing tests to make things
  green. This is the [eval-driven](eval-driven-ai-development.md) discipline applied
  across a long run.
- **Completion criteria written before execution starts** — Osmani's single
  highest-leverage move; it counters the self-grading problem.
- **Memory governance** — curated long-term memory (e.g. "Memory Bank"-style),
  governed "like microservices" with identity and policy controls to prevent
  **memory drift** (an atypical shortcut hardening into broad practice).
- **Coordination** — role-specialised agents, **delegated approval** (human-in-the-
  loop with full execution state preserved, not stale serialized JSON), and fleet
  orchestration via identity/registry.

## What works vs what fails

| Works | Fails |
|---|---|
| Decoupled brain/hands/session surviving failures | Coupled designs needing wholesale change when assumptions go stale |
| External state enabling recovery without re-contextualising the model | Context rot degrading performance mid-run |
| Test ratchets preventing backsliding | Models declaring "done" at 30% (self-grading) |
| Session logs giving auditability | Memory drift; quality loss across repeated re-summaries; cost runaway without budgets/circuit-breakers |

## Two things the three meanings do not cover

[Bilgin Ibryam](https://generativeprogrammer.com/p/the-evolution-of-agentic-loops) (November
2026) sets out a six-stage evolution of agent loops — tool-calling, stateful, durable, ambient,
harness, persistent. **Four of the six are held elsewhere in these notes under other names**, and
his stage 3 and stage 6 are this note's *long-running execution* and *persistent agency*, so the
taxonomy is largely a restatement. Two stages supply something the three meanings above miss.

> **Provenance.** Ibryam's ninth source in these notes, and he already supplies the repo's
> [maturity model](agentic-sdlc-maturity-model.md) — a second staged taxonomy from one newsletter
> is carried for its gaps, not its frame. He discloses contributing to **Dapr Agents**, which
> appears in his own durable-execution section. 15+ frameworks cited with links; **no measurement
> of his own**.

**Ambient agents — the trigger question, which is absent from these notes entirely.** An ambient
agent is *activated by events or schedules rather than by user initiation*, and runs headless.

Every agent in this knowledge base is **invoked**: by a developer in a harness, by a PR opening,
by an alert firing, by CI. [Agentic code review](agentic-code-review.md) runs on a pull request;
[AI SRE](../../sre/ai-sre-and-the-incident-path.md) runs on a page;
[DoorDash's flag cleanup](../../case-studies/doordash-flag-cleanup-agents.md) runs on a schedule
someone set and watches. **A standing agent that activates on its own events is a different
operational proposition**, and the three walls above do not cover its distinctive problem: not
context, state or self-verification, but **who notices that it ran at all.**

That bears directly on two things already held.
[Agentic Autonomy Levels](agentic-autonomy-levels.md) bounds tools, permissions and budget for an
invoked run — an ambient agent needs the same contract plus a *trigger* budget, since nobody is
waiting for its output. And
[the AI gateway control plane](ai-gateway-control-plane.md) argues for per-action authorisation
rather than per-session trust; with no session and no human initiator, per-action is the only
unit left. The accountability problem in
[Accountability for Unread Code](accountability-for-unread-code.md) sharpens too: unread code at
least had an author who asked for it.

**Durable execution, with the mechanism this cluster never states.**
[The Agentic SDLC](agentic-sdlc.md) lists *"durable execution"* as a bullet and never explains
it. Ibryam's definition: record execution progress so a failed run **resumes rather than
restarts**, with an **idempotency key** preventing duplicate side effects when a step is retried.
Named implementations are ordinary workflow engines — Temporal, Restate, DBOS, Inngest, Dapr
Agents — which is the useful observation: **this is not an agent problem, it is the durable-workflow
problem with a model in one of the steps.**

**That is the third arrival at one requirement in these notes.**
[Cell-Based Architecture](../architecture/cell-based-architecture.md) needs a transaction
identifier that *"remains consistent across retries and reroutes"* before it can restart work in
another cell, so idempotency there is a **precondition for the failover strategy** rather than a
safety net. [Database Migration Strategies](../practices/database-migration-strategies.md) wants
backfills *"idempotent and resumable"* for the same reason. An agent step with side effects is the
same shape: **retry safety is what buys you the right to resume at all**, and the checkpoint-and-resume
pattern above silently assumes it.

Note the tension with Amex, which is worth holding rather than resolving: they deliberately
**restart rather than resume** across a boundary, because transferring partial state would breach
the isolation the architecture exists to maintain. Durable execution resumes *inside* one
workflow; cells restart *across* boundaries. Both need the identifier; they use it for opposite
moves.

**On persistent agents**, his stage 6 adds two smaller things to the *standing agents* idea held
from [Ultimate](../../reading/ultimate-self-extending-harness.md): a cycle name —
**Activate, Act, Adapt** — and **production examples** (Grok Bot, Meta Muse, Kiro Crew Bots).
The second matters more than it sounds, because the repo's only instance of a never-concluding
agent was one person's personal project with the author's own *"I don't really recommend it"*
attached.

## Distinctive vocabulary

**Context rot**, **brain/hands/session split**, the **Ralph (Wiggum) technique**
(amnesiac agent + external filesystem state), **test ratchet**, **memory drift**,
**delegated approval**, **ambient processing** (acting on event streams
unsupervised), **checkpoint-and-resume**.

## Relationship to other notes

- [Harness Engineering](harness-engineering.md) — the **anatomy** of the harness
  program (loop, tools, memory, patterns); this note is the **durability** layer
  built on top of it for long horizons.
- [Loop-Driven Development](loop-driven-development.md) — the agent loop these
  systems run; long-running agents are that loop sustained across sessions.
- [Backpressure Loops for Coding Agents](agent-backpressure-loops.md) — moving
  feedback into agent-actionable signals is how a long run self-corrects instead of
  drifting.
- [Eval-Driven Development](eval-driven-ai-development.md) — the planner/judge
  separation and test ratchets that keep a long run honest.
- [The AI-Native Engineering Stack](ai-native-engineering-stack.md) — where the
  agent runtime, sessions, and memory sit in the broader platform.

Tools named by the author (Claude Code, Claude Managed Agents, Google Agent
Platform, Cursor Composer) are described here neutrally as reference
implementations of the brain/hands/session pattern, not endorsements.
