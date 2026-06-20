---
title: Long-Running Agents
tags: [ai-engineering, agentic-workflows, architecture, reading]
topic: engineering/practices
status: notes
level: intermediate
related:
  - engineering/practices/harness-engineering.md
  - engineering/practices/loop-driven-development.md
  - engineering/practices/agent-backpressure-loops.md
  - engineering/practices/eval-driven-ai-development.md
  - engineering/practices/ai-native-engineering-stack.md
  - engineering/practices/ai-native-engineering-overview.md
source: "https://addyo.substack.com/p/long-running-agents"
updated: 2026-06-20
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
