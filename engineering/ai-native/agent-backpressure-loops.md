---
title: Backpressure Loops for Coding Agents
tags: [ai-engineering, ci-cd, testing, reading, agentic-workflows]
topic: engineering/ai-native
status: notes
level: intermediate
related:
  - engineering/ai-native/own-the-outer-loop.md
  - engineering/ai-native/quality-first-ai-coding.md
  - engineering/ai-native/ci-cd-ai-engineering.md
  - engineering/ai-native/harness-engineering.md
  - engineering/ai-native/eval-driven-ai-development.md
  - engineering/ai-native/modern-engineering-values.md
  - engineering/ai-native/loop-driven-development.md
  - concepts/theory-of-constraints.md
  - languages/go-agentic-language.md
  - engineering/ai-native/agentic-code-review.md
  - engineering/ai-native/long-running-agents.md
  - engineering/ai-native/ci-speed-with-ai-agents.md
  - engineering/ai-native/agentic-autonomy-levels.md
source: "https://generativeprogrammer.com/p/stop-babysitting-your-coding-agent"
updated: 2026-06-20
---

# Backpressure Loops for Coding Agents

Coding agents generate output faster than humans can validate it. When the only feedback is
human review, every mistake becomes review work — the agent produces code, a human spots the
failure, explains it, the agent retries. That is **babysitting**, not review, and it does not
scale. The proposal is to move inexpensive correctness checks out of the human loop and into
machine-readable loops the agent can act on itself, so humans are left to focus on intent,
design, and architectural trade-offs.

Marc Brooker is cited for the underlying framing: agents are feedback loops around imperfect
models, so the leverage is in *where* the feedback closes — in an agent loop a machine can detect
and repair, rather than in a human loop.

## The backpressure loop pattern

| | |
|---|---|
| **Intent** | Move inexpensive correctness checks from human review into the agent's workflow. |
| **Problem** | Agents produce code faster than humans can validate. |
| **Solution** | Expose machine-readable **feedback sensors** the agent can run and interpret immediately. |
| **Result** | Agents fix mechanical failures autonomously; humans handle intent and design. |

**Feedback sensors** include type checkers, tests, linters, builds, browser/screenshot checks,
logs and traces, structural rules, and evals.

## Backpressure vs. gates

- **Backpressure (good):** signals the agent encounters *during* coding that trigger
  self-correction — type failures, failing tests, lint warnings, build errors, screenshot
  mismatches.
- **Gates (insufficient alone):** CI failures *after* the agent finishes. A green build proves
  only that the code compiles and existing tests pass — not that product requirements survived or
  that generated tests assert anything meaningful.

This is the in-loop complement to
[CI/CD as the control plane](ci-cd-ai-engineering.md): the pipeline gate is necessary but late;
backpressure closes the loop earlier.

## Concrete practices

**Start with boring checks.** Put explicit commands in project documentation (`AGENTS.md` or
equivalent) so the agent runs them as a matter of course:

- run typecheck after TypeScript changes;
- run the linter;
- run affected tests;
- fix failures before requesting review.

**Make feedback context-efficient.** Success should be compressed; failure should be actionable.
Dumping hundreds of lines of passing output wastes tokens and clarity. A useful shape:

```
✓ typecheck
✓ lint
✗ auth tests
FAIL auth/session.test.ts
Expected redirect to /login for expired session.
Received 200 from /dashboard.
```

Generic errors ("the code is wrong") do not guide correction; specific expected-vs-actual detail
lets the agent reason about a fix. Moss Banay's term **wasted human backpressure** names the
attention spent on mistakes the agent should have caught itself (missing imports, broken builds,
visual errors).

## Layered feedback architecture

Not every check belongs in the same loop (the layering draws on Birgitta Böckeler's distinction
between sensors for live sessions and those for pipelines/monitoring):

| Layer | When | Examples |
|---|---|---|
| **Inner loop** | Fast, per-session | Typecheck, lint, focused tests, build, screenshots |
| **Before PR** | On completion | Full and integration test suites, structural rules, security checks |
| **Scheduled / explicit** | Periodic | Mutation testing, fuzzing, semantic evals, architecture drift review |

The trade-off is **speed vs. comprehensiveness**: fast sensors aid iterative flow, slow ones
bottleneck it. Layering keeps expensive checks out of the rapid self-correction loop. A related
research framing, **Effective Feedback Compute**, holds that feedback is only useful when it is
informative, valid, non-redundant, and retained for later decisions.

## Anti-patterns

- Relying solely on human review for mechanical errors.
- Running every possible check in the inner loop.
- Dumping large volumes of passing output into the agent's context.
- Using unstructured, non-actionable error messages.

## The scaling rule

> When you correct the same agent mistake twice, turn it into backpressure.

Instrument the system so that category of error is caught automatically from then on — via a
test, type, linter rule, build check, browser assertion, error message, or script. The emerging
skill is less about asking agents to try harder and more about **designing feedback loops that
make poor output hard to accept**, shifting the human role from continuous validator to architect
of the validation system.

## Relationship to other notes

- [Quality-First AI Coding](quality-first-ai-coding.md) — the human-orchestrated counterpart
  (multi-model review). This note moves the cheap, mechanical feedback *out* of the human loop;
  that note keeps the judgement-heavy review *in* it.
- [CI/CD as the Control Plane for AI-Assisted Engineering](ci-cd-ai-engineering.md) — the gate
  layer; backpressure is the earlier, in-session feedback that precedes it.
- [Harness Engineering](harness-engineering.md) — feedback sensors are wired into the harness's
  core loop; this note is the feedback pattern, that note is the machinery.
- [Eval-Driven Development for AI Capabilities](eval-driven-ai-development.md) — evals are one of
  the sensors, especially in the scheduled layer.
