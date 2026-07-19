---
type: case-study
title: Slack's Agentic E2E Testing Experiment
description: "Slack's measured experiment on where AI agents fit in the end-to-end testing stack: goal-based vs journey-based testing, three execution models (Playwright MCP / CLI / generated tests) compared across 200+ runs, and the cost, reliability, and token trade-offs that put agents at the apex of the pyramid rather than replacing deterministic tests"
tags: [testing, ai-engineering, agentic-workflows, reading]
topic: case-studies
status: notes
level: intermediate
related:
  - engineering/practices/test-coverage-policy.md
  - engineering/practices/visual-regression-testing.md
  - engineering/ai-native/agentic-code-review.md
  - engineering/ai-native/eval-driven-ai-development.md
source: "https://slack.engineering/agentic-testing-where-agents-fit-in-the-e2e-testing-stack/"
updated: 2026-07-19
---

# Slack's Agentic E2E Testing Experiment

A Slack engineering experiment measuring **where AI agents fit in the end-to-end
(E2E) testing stack**. The framing line is *"tests enforce journeys; agents verify
goals."* Deterministic E2E tests assert a *specific* UI path; an agent given a goal
can reach it by *any* path, so the two answer different questions. Slack's
conclusion is that agentic testing is a **new layer at the apex of the testing
pyramid**, complementing rather than replacing deterministic tests. All figures
below are Slack's self-reported experimental results (test workspaces,
non-production data, Claude Sonnet 4.5 and Opus 4.6 as the agent models).

## Goal-based vs journey-based testing

| | Journey-based (deterministic) | Goal-based (agentic) |
|---|---|---|
| Asserts | One specific UI path | The goal is achievable *by some* path |
| Resilience to UI change | Brittle — breaks on selector/layout change | Adaptive — finds another route |
| Cost / speed | Cheap, fast, CI-friendly | Expensive, slow, exploratory |
| Best for | Regression gating in CI | Exploration, flaky-workflow debugging, reproducing production bugs |

Only **~20% of runs followed identical action sequences** even when they reached the
correct outcome — the adaptability is real, but it also makes runs
non-deterministic, which is why agents sit *above* the deterministic layer rather
than inside CI regression gating.

## Three execution models compared

1. **Playwright MCP** — the agent drives the browser through Microsoft's Model
   Context Protocol: predefined browser actions with persistent DOM context.
2. **Playwright CLI** — the agent issues shell commands step-by-step (`claude -p`
   style execution).
3. **Generated tests** — the agent writes deterministic Playwright code from a
   natural-language description, which then runs like any normal test.

Inputs were tried as both natural language and structured YAML, across two
workflows: Thread Reply (~15–20 steps) and Search Discovery (~25–30 steps), over
**200+ automated executions**.

## The measured trade-offs

| Metric | Playwright MCP | Playwright CLI | Generated tests |
|---|---|---|---|
| Failure rate (simple) | 0% | ~12% | ~8% |
| Failure rate (complex) | ~12% | ~20% | ~48% |
| Avg runtime | 5–8 min | 9–11 min | ~3 min |
| Cost per run | $15–30 | $15–30 | Lower |
| Tokens (search flow) | ~3.5M | ~6M | ~7M |
| Agent turns | ~40 | ~85 | ~70 |

Reading the table: **MCP was the most reliable** (structured DOM context beats
blind shell steps), reliability **degraded sharply with complexity** for every
model — worst for generated tests on complex flows (~48%) — and **cost was high**
(10+ minutes, $15–30 a run).

## Why it costs so much — and the levers not yet pulled

The dominant cost driver is **token retransmission**: most tokens in a run are
*previously seen* DOM snapshots resent on each turn, not new reasoning. Slack notes
two obvious mitigations they had **not** implemented in these experiments — **prompt
caching** and **context compaction** — as the clearest path to making agentic
testing economical.

## Distinctive vocabulary

- **Action signature** — the ordered list of tool calls and UI actions a run
  produced, normalised so different runs can be compared for adaptability.
- **Goal-based vs journey-based testing** — the central distinction.
- **Playwright MCP** — structured browser interaction via the Model Context
  Protocol.

## Limitations Slack names

High and variable cost; reliability degrading with workflow complexity; slower than
deterministic tests; infrastructure-dependent (MCP more reliable than CLI); and
limited coverage of multi-window / cross-workspace scenarios. The recommendation is
therefore additive, not substitutive: keep deterministic tests for CI regression,
add agents for exploration and debugging.

## Relationship to other notes

- [Test Coverage Policy](../engineering/practices/test-coverage-policy.md) — the
  testing pyramid this sits atop; agentic testing is a new apex layer, not a
  replacement for the deterministic base that gates CI.
- [Visual Regression Testing](../engineering/practices/visual-regression-testing.md)
  — a sibling UI-testing technique that also "asks a different question" from a unit
  test; both are specialised layers complementing functional E2E.
- [Agentic Code Review](../engineering/ai-native/agentic-code-review.md) — the
  closest sibling: an agent performing a traditionally-human quality task in the
  SDLC, with the same cost/reliability engineering (model tiering, token discipline)
  determining whether it is viable.
- [Eval-Driven Development for AI Capabilities](../engineering/ai-native/eval-driven-ai-development.md)
  — the *inverse* discipline: that note is about testing the AI capability itself;
  this is about using AI to test the product.
