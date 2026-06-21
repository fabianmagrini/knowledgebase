---
title: CI Speed When Agents Write the Code
tags: [ci-cd, ai-engineering, testing, agentic-workflows]
topic: engineering/practices
status: notes
level: intermediate
related:
  - engineering/practices/ci-cd-ai-engineering.md
  - engineering/practices/agent-backpressure-loops.md
  - engineering/practices/long-running-agents.md
  - engineering/practices/loop-driven-development.md
  - engineering/practices/trunk-based-development.md
  - engineering/practices/change-absorption-capacity.md
  - concepts/devops-capability-model.md
source: ""
updated: 2026-06-21
---

# CI Speed When Agents Write the Code

A long-standing rule of delivery is that **CI must be fast** — keep it under ~10
minutes, as [trunk-based development](trunk-based-development.md) demands. The
usual justification is human: slow feedback forces the developer to **context
switch**. They push, the pipeline crawls, attention wanders to something else, the
flow state is lost, and reloading it when CI finally fails is expensive. The
pipeline's wall-clock time was really a proxy for *human idle and disruption cost*.

That premise is worth re-examining when **an AI agent writes most of the code and
supervises CI itself**. The cost that made fast CI sacred — the human losing
context while waiting — largely evaporates. CI speed doesn't stop mattering, but
*why* it matters changes.

## Why the context-switching cost drops

When the author and the CI-watcher is an agent rather than a person:

- **No flow state to break.** An agent doesn't lose its train of thought waiting
  ten minutes for a pipeline. Its context is the explicit state in its harness —
  it can hold the change, the diff, and the plan across an arbitrary wait without
  the degradation a human suffers. See [Long-Running Agents](long-running-agents.md).
- **Waiting isn't idle.** A human blocked on CI is one person doing nothing useful.
  An orchestrator can fan agents across many tasks, so time spent waiting on one
  pipeline overlaps with progress on others. Throughput decouples from any single
  pipeline's latency.
- **The human is already out of the inner loop.** The point of moving mechanical
  checks into [agent-actionable backpressure loops](agent-backpressure-loops.md) is
  that the agent — not a person — consumes CI's output and acts on it. If no human
  is watching the pipeline, no human is context-switching because of it.

So the classic argument "slow CI destroys developer productivity through context
switching" weakens at exactly the point where the developer is no longer the one
waiting.

## What this frees up

If the dominant cost of a slow pipeline was human disruption, removing that cost
makes a **slower, more thorough CI** newly affordable. You can spend pipeline
minutes you previously couldn't justify:

- Fuller integration and end-to-end suites instead of a thin fast subset.
- Mutation testing, fuzzing, broader static analysis, multi-version matrices.
- Heavier checks that give the agent a *richer, higher-signal* correction
  signal — the better the sensor, the better the agent self-corrects.

In other words, the optimisation can shift from "fastest pipeline that keeps a
human in flow" toward "most thorough pipeline the agent can act on," because the
constraint that capped thoroughness has moved.

## What still makes CI speed matter

This is a reframing, not a licence to let CI rot. Speed still matters — just for
different reasons, and as a different *kind* of constraint:

| Reason | Still binding? |
|---|---|
| **Human flow / context switching** | Largely **dissolved** when the agent waits, not the human |
| **Iteration throughput** | **Yes** — faster CI means more agent loop turns per hour; speed becomes a *throughput* lever, not a flow-protection one |
| **Lead time for changes** | **Yes** — [DORA](../../concepts/devops-capability-model.md) lead time still bounds delivery; now capped by agent + pipeline throughput, not human attention |
| **Cost** | **Shifts** — idle waiting is cheap if the agent sleeps/polls, but pipeline compute and agent supervision time still cost money at high fan-out |
| **The eventual human gate** | **Yes** — when a person finally reviews or approves, a slow path back to them re-introduces *their* context switch |
| **Signal quality** | **Yes** — flaky or slow CI still poisons the agent's feedback; a confused agent loops uselessly |

The sharpest version of the claim: **CI speed moves from a human-experience
constraint to a throughput-and-cost optimisation.** When humans waited, latency was
the enemy because it broke people. When agents wait, latency is a dial you trade
against thoroughness and spend — and you may rationally choose a slower, more
rigorous pipeline than you ever would have for a human in the loop.

## Caveats

- It assumes the agent genuinely closes the loop on CI output — reading failures and
  repairing them — not a human still triaging red builds. If a person is babysitting
  the pipeline, the old context-switch cost is fully back.
- Wall-clock cycle time still matters to the *business*; "the agent doesn't mind
  waiting" is not the same as "shipping slower is fine."
- It does not relax correctness. A slower pipeline is only worth it if the extra
  minutes buy stronger signal — see
  [Change Absorption Capacity (CATS)](change-absorption-capacity.md).

## Relationship to other notes

- [CI/CD as the Control Plane for AI-Assisted Engineering](ci-cd-ai-engineering.md)
  — the pipeline is the guardrail that makes agent-speed delivery safe; this note is
  the corollary about its *latency budget* once agents, not humans, wait on it.
- [Backpressure Loops for Coding Agents](agent-backpressure-loops.md) — the
  mechanism that takes the human out of the CI-watching loop in the first place.
- [Loop-Driven Development](loop-driven-development.md) — where CI speed reappears as
  loop-turn throughput rather than developer flow.
