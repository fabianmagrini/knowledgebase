---
title: Loop-Driven Development
tags: [ai-engineering, testing, ci-cd, reading]
topic: engineering/practices
status: notes
level: intermediate
related:
  - engineering/practices/agent-backpressure-loops.md
  - engineering/practices/harness-engineering.md
  - engineering/practices/eval-driven-ai-development.md
  - engineering/practices/agentic-sdlc.md
  - engineering/practices/test-coverage-policy.md
source: "https://generativeprogrammer.com/p/from-test-driven-to-loop-driven-development"
updated: 2026-06-14
---

# Loop-Driven Development

Software engineering has always run as a feedback loop. Test-driven development made that loop
explicit at the unit level (write a failing test → make it pass → refactor). The argument here is
that AI agents extend the same loop to larger work units — tasks, pull requests, migrations —
giving **loop-driven development**. It differs from TDD in *scale and scope*, not principle: the
engineer's job becomes designing the loop around the agent rather than writing the code inside it.

## The five-component loop

A loop wraps a unit of work with:

| Component | Role |
|---|---|
| **Trigger** | What starts the loop — a human, a schedule, or an event |
| **Goal** | The desired end state |
| **Harness** | The agent's environment (tools, sandbox, context) |
| **Verifier** | The check that decides whether to continue or stop |
| **State** | Persistent memory across iterations |

## The engineering leverage stack

The article frames five additive eras: each layer keeps the capabilities of the ones below and
adds a new control surface. The leverage point migrates *upward* over time.

| Era | Period | Adds | Limitation it exposes |
|---|---|---|---|
| **Autocomplete** | 2021–2022 | Accept/reject inline suggestions | Narrow scope |
| **Prompt engineering** | 2022–2023 | Reason–act–observe cycles (ReAct), tools, goals | Drift and convergence |
| **Context engineering** | 2024–2025 | Repo context, files, tests, logs, conventions | Context without correctness |
| **Harness engineering** | 2025–2026 | Sandbox, verifier, CI, evals, review gates | (the checkable environment) |
| **Loop engineering** | now | Orchestration: worktrees, skills/playbooks, MCP, durable memory | Needs escalation safeguards |

The harness layer is the subject of [Harness Engineering](harness-engineering.md); loop
engineering wraps harnesses with recurring, decision-based orchestration.

> "The point of a harness is not to make the model magically correct. The point is to make the
> work observable, constrained, and checkable."

## The verifier principle

The verifier is what separates a loop from vague iteration: without it you have *repeated
prompting*; with it the loop converges toward the goal. Verifiers can be **deterministic** (tests,
builds, linters) or **probabilistic** (reviewer models). The principle: separate maker from
checker, and run deterministic checks before probabilistic ones. Real-time feedback that makes the
agent self-correct before a human is involved is [backpressure](agent-backpressure-loops.md) — one
form of in-loop verification.

## Why judgement intensifies

- **Safety scales with autonomy.** The more autonomy the loop has, the stronger the checks must
  be. Expanded delegation demands expanded guardrails.
- **Control-point migration.** Engineers trade fine-grained code authorship for system-level
  decisions — choosing goals, designing context, setting permissions, defining checks, assessing
  acceptable risk.
- **Skills as infrastructure.** Reliable loops need durable playbooks and scoped skills, so
  conventions are not rediscovered on every run.

## Anti-patterns

- **Unverified loops** — without a verifier, a loop wastes hours, mutates the repository, and
  produces plausible but problematic work.
- Treating expanded autonomy as a reason to *relax* constraints rather than strengthen them.

## References

The piece credits Martin Fowler (TDD), the ReAct paper, AutoGPT, and Addy Osmani's "loop
engineering" framing.

## Relationship to other notes

- [Harness Engineering](harness-engineering.md) — era 4 of the stack: the environment a single
  agent run executes in. This note wraps harnesses in a recurring control loop.
- [Backpressure Loops for Coding Agents](agent-backpressure-loops.md) — by the same author;
  backpressure is the in-loop verification/feedback component of the loop.
- [Eval-Driven Development](eval-driven-ai-development.md) — evals are probabilistic verifiers.
- [The Agentic SDLC](agentic-sdlc.md) — the lifecycle-level cybernetic loop; this is the
  practitioner-tooling articulation of the same idea.
- [Test Coverage Policy](test-coverage-policy.md) — the TDD lineage the loop generalises from.
