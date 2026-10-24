---
type: reading
title: Reactive Reducer Orchestration
description: "Brad Murry's position that the model should be removed from agent control flow entirely — agents write values into a typed context store, a deterministic microstep loop fires the edges — plus a thirteen-pattern orchestration taxonomy."
tags: [ai-engineering, agentic-workflows, architecture, reading]
topic: reading
status: notes
level: advanced
related:
  - reading/building-effective-agents.md
  - reading/multi-agent-coding-coordination.md
  - case-studies/cursor-agent-swarm-economics.md
  - engineering/ai-native/harness-engineering.md
  - engineering/ai-native/long-running-agents.md
  - engineering/architecture/runtime-architecture-verification.md
  - engineering/architecture/data-readiness-for-agents.md
  - engineering/ai-native/agentic-autonomy-levels.md
  - reading/ultimate-self-extending-harness.md
source: "https://bradmurry.com/software/reactive-reducer-patterns/"
updated: 2026-10-24
---

# Reactive Reducer Orchestration

Brad Murry (September 2026) argues that multi-agent orchestration goes wrong because models are
allowed to decide *control flow* — which agent runs next, when to hand off, when to stop — and
that this makes systems non-deterministic, unreplayable and expensive. His alternative:

> "The machine moves itself. Actors only ever contribute values."

*(The URL slug reads `reactive-reducer-patterns`, which suggests React state management. The
subject is multi-agent orchestration.)*

> **Provenance — read this before the ideas.** Three limits, all verified against the page
> rather than assumed:
>
> **1. No prior art is acknowledged anywhere.** There is no reference to state-machine
> literature, workflow engines (Temporal, AWS Step Functions, BPMN), the actor model, the
> blackboard architecture, or multi-agent systems research — *including under the pattern he
> names "Auction / Contract-Net"*. Pointers the note supplies below.
>
> **2. No benchmarks, measurements or production evidence.** Determinism, replayability and
> bounded token cost are **asserted design properties**, not measured outcomes.
>
> **3. A self-referential series** promoting the author's own framework and DSL, with the FSM
> YAML deferred across twelve companion articles. No executable code appears in this piece.
>
> Kept because the central architectural position is one these notes do not otherwise hold, and
> because it contradicts a note they do.

## The mechanism

| Element | How it works |
|---|---|
| **Typed context store** | All state lives in one schema'd object; writes are coerced to declared types |
| **Agents write, never transition** | An actor contributes a value to a named field. It cannot request a state change |
| **Guards are pure predicates** | Conditions evaluate over *context*, not over agent output — e.g. `size(votes.filter(...)) >= 2` |
| **Microstep loop** | Fire the first eligible guard-passing edge, repeat until the machine **parks** at a declared state |
| **Park record** | A journaled `(state, context)` tuple — the restart and recovery point |

Two consequences he draws out:

- **Handoffs are context writes, not messages.** The next state reads the full staged artifact
  rather than a paraphrase of it, which removes the lossy-summary failure that message-passing
  between agents invites.
- **A finished run is a sequence of `(state, context-write, edge-fired)` tuples**, so it replays
  exactly without reconstructing anything from model output.

The token claim, verbatim and unvalidated: *"token cost is bounded by the design (a `verdict`
enum, `maxIterations`, a retry budget read off the data itself) rather than by how well the
models behaved."* The reasoning is that agents interpolate from staged typed fields instead of a
growing transcript, so per-turn context stays roughly constant. Plausible as a design
consequence; no figures are offered. Read against
[Long-Running Agents](../engineering/ai-native/long-running-agents.md), which treats context rot
as the thing to manage rather than to design out.

## Why this generalises two positions already held

The reason to keep the note. The same move appears three times in these notes at different
layers, and nobody involved seems to have noticed the pattern:

| Note | Where the model is excluded |
|---|---|
| [Runtime Architecture Verification](../engineering/architecture/runtime-architecture-verification.md) | **Scoring.** "The agent does not compute the score … no model call anywhere in it", because a model-produced number cannot be reproduced or diffed, which disqualifies it as a gate |
| [Data Readiness for Agents](../engineering/architecture/data-readiness-for-agents.md) | **Gating.** "Retrieved text informs, it never gates" — prose supplies background, code decides |
| This note | **Control flow.** Actors contribute values; the machine decides what happens next |

The common principle is worth stating plainly: **let the model produce content, and keep
determinism wherever the output has to be reproduced, audited or compared.** Each source arrives
at it independently from a different problem, which is better evidence for the principle than
any one of them makes on its own.

## The disagreement with Cursor

Worth naming rather than smoothing, because these notes hold both.

[Cursor's Agent Swarm Economics](../case-studies/cursor-agent-swarm-economics.md) puts a
**frontier planner in control flow**: a strong model does the decomposition, delegation and
design coherence, while cheap workers execute. That division *is* the cost argument — "few
moments in a large task genuinely require frontier intelligence, such as the original
decomposition, the design decisions, and certain trade-offs."

Murry's position deletes exactly that role. Control flow is declared in advance as edges and
guards; no model chooses the next step.

They cannot both be right about where the leverage sits, and the honest reading is that they are
solving different problems. Cursor's task is **open-ended** — implement a 835-page specification
from scratch, where the decomposition is itself the hard intellectual work and cannot be declared
up front. Murry's patterns are **bounded workflows** — review, voting, critique loops, planner/
executor — where the shape *is* known in advance and the model's job is to fill in values. The
useful question a reader is left with is which of those two a given task actually is, because the
answer determines whether a planner is leverage or a liability.

## The thirteen patterns, honestly accounted

Grouped by orchestration problem: **flow** (sequential pipeline, parallel fan-out/fan-in),
**authority** (supervisor/router, hierarchical manager/worker), **delegation** (peer
handoff/swarm, auction/contract-net, dynamic team formation), **reasoning** (debate/consensus,
quorum/voting, generator/critic/refiner), **planning** (planner/executor), **coordination**
(blackboard/shared-state, event-driven/publish-subscribe).

**Five of the thirteen are already held**, from
[Building Effective Agents](building-effective-agents.md):

| Murry | Anthropic's name |
|---|---|
| Sequential Pipeline | Prompt chaining |
| Parallel Fan-Out/Fan-In | Parallelisation |
| Supervisor/Router | Routing |
| Hierarchical Manager/Worker | Orchestrator–workers |
| Generator/Critic/Refiner | Evaluator–optimizer |

The eight that are not held — peer handoff, auction/contract-net, dynamic team formation,
debate/consensus, quorum/voting, planner/executor, blackboard, event-driven — are the taxonomy's
contribution to these notes.

**The prior art the article omits**, since several of these are decades old and presenting them
as newly enumerated would misrepresent the field:

- **Blackboard architecture** — 1970s–80s AI; the Hearsay-II speech-understanding system is the
  canonical instance.
- **Contract-net protocol** — Davis and Smith, 1980. The name is used without the citation.
- **Event-driven/publish–subscribe** and **FSM-driven orchestration** — standard distributed-
  systems and workflow-engine territory (Temporal, Step Functions, BPMN), not agent-specific.

What is plausibly new is not the patterns but the claim that **all thirteen reduce to one
substrate** — a typed context plus declared edges — which is the thesis the series exists to
argue.

## Three idioms worth keeping

Concrete, and transferable beyond his DSL:

| Idiom | What it solves |
|---|---|
| **"Many contributors, one field"** | Several agents write into one `map` keyed by author — votes, bids, critiques — rather than separate scalar fields. Collapses join logic, attribution and cardinality into a single mechanism |
| **"Accumulate what you keep; consume what re-arms"** | Destroy scalar *triggers* to re-enable a loop while preserving *records* in lists and maps. Prevents a stale judgement being silently reused on the next pass |
| **"When nothing is destroyed, every test becomes a comparison"** | Write `size(drafts) > size(verdicts)` rather than `has(verdict)`, so freshness and retry budgets become comparisons across both sides of the loop |

The third is the one with reach. A presence check (`has(x)`) cannot distinguish "produced this
round" from "left over from last round"; a comparison can. That is the same class of error as the
freshness subtlety in
[Data Readiness for Agents](../engineering/architecture/data-readiness-for-agents.md) — a table
whose refresh silently failed looks identical to one that legitimately did not change — and the
fix has the same shape: measure the thing that advances, not the thing that exists.

## Relationship to other notes

- [Building Effective Agents](building-effective-agents.md) — the five overlapping patterns, from
  a source with a model deciding routing. The contrast is the point: Anthropic's routing pattern
  *is* a model in control flow.
- [Cursor's Agent Swarm Economics](../case-studies/cursor-agent-swarm-economics.md) — the direct
  disagreement, and the bounded-versus-open-ended reading that reconciles it.
- [Multi-Agent Coding Without Worktree Chaos](multi-agent-coding-coordination.md) — the closest
  sibling in shape: one practitioner's own orchestration approach and toolchain. Wells coordinates
  through file reservations and a coordinator agent; this coordinates through a shared typed store
  and no coordinator at all.
- [Harness Engineering](../engineering/ai-native/harness-engineering.md) — the component anatomy
  this is one opinionated instance of, with the control loop pushed out of the model.
- [Runtime Architecture Verification](../engineering/architecture/runtime-architecture-verification.md)
  and [Data Readiness for Agents](../engineering/architecture/data-readiness-for-agents.md) — the
  same model-exclusion principle at the scoring and gating layers.
- [Agentic Autonomy Levels](../engineering/ai-native/agentic-autonomy-levels.md) — its
  orchestration axis assumes an orchestrator *agent*; this replaces it with a state machine, which
  is arguably a different kind of autonomy rather than a different level of it.
