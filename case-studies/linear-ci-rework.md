---
type: case-study
title: Linear's CI Rework Under Agent Volume
description: "Absorbing a quadrupled test suite while PR wait fell from 6+ to just over 5 minutes: setup overhead as the cap on parallelism, a cache abandoned because rebuilding was faster, and ~87,000 runner-minutes saved per month."
tags: [ci-cd, testing, performance, ai-engineering, reading]
topic: case-studies
status: notes
level: intermediate
related:
  - engineering/ai-native/ci-speed-with-ai-agents.md
  - engineering/practices/change-absorption-capacity.md
  - engineering/ai-native/ci-cd-ai-engineering.md
  - concepts/latency-patterns.md
  - case-studies/linear-performance-architecture.md
  - engineering/practices/trunk-based-development.md
  - engineering/ai-native/brownfield-agentic-engineering.md
  - case-studies/chatgpt-web-performance.md
  - case-studies/github-huge-pr-rendering.md
  - case-studies/anthropic-claude-ai-performance-sprint.md
  - case-studies/anthropic-scion-source-control.md
source: "https://linear.app/now/ci-bottleneck-reworked"
updated: 2026-10-18
---

# Linear's CI Rework Under Agent Volume

Mufeez Amjad (Linear, September 2026) on rebuilding CI to keep up with agent-generated code.
Their framing of the problem:

> "Agents have made it exponentially faster to ship code, but validating those changes hasn't
> quite kept up at the same rate."

The scale of the pressure, and the result:

| | Reported |
|---|---|
| Test suite growth | *"our test suites almost **quadrupling** since the start of the year"* |
| Current rate | *"we're currently adding roughly **2,000 tests a week**"* |
| PR wait time | *"down from more than **6 minutes** to just over **5**"* |

**Read those together, because the headline understates the work.** A ~17% latency improvement
looks modest until you notice it was achieved while the suite roughly quadrupled. This is a team
running hard to stay approximately still — which makes it an unusually clean instance of
[Change Absorption Capacity](../engineering/practices/change-absorption-capacity.md): raising a
system's capacity to absorb agent-speed change, rather than getting faster in absolute terms.

**Provenance.** Company-authored and self-reported, with no counterfactual. Three things make it
more credible than the genre usually is: Linear does not sell CI tooling, the third-party runner
vendor is **not named** and carries no sponsorship disclosure, and the figures are granular
per-stage rather than one headline multiple — which is harder to cherry-pick.

## What they changed

| Category | Change | Reported effect |
|---|---|---|
| **Infrastructure** | Moved off GitHub Actions to third-party runners with faster CPUs and better cache infrastructure | **34%** speedup |
| | Switched to the `tsgo` TypeScript compiler | **−73%** |
| | Rewrote lint rules as AST analysis instead of type-checking | **−68%** API lint, **−55%** repository lint |
| **Critical path** | Minimised repository checkouts (sparse, blobless) | **94 → 20s** |
| | Resilient checkout with backoff retry | — |
| | Non-blocking cache writes moved off the critical path | **42s** per PR |
| | Change-detection job | **26 → 8s** median |
| **Setup** | Dependencies preinstalled into CI images | — |
| | Monorepo installs restricted to needed packages | **44–73 → 16–18s** |
| | `node_modules` caching **abandoned** in favour of rebuilding | **28 → 7.5s** |
| **Tests** | Large test files split for shard balance | — |
| | Optional module state sharing (Vitest isolation relaxed) | **17%** monthly; slowest shard **300–379 → 195s** |
| | Scaled **4 → 8 shards** while total setup time fell | — |
| | Batched seven independent checks into two jobs | **~87,000 runner-minutes/month, 11.8% of total CI usage** |

## The two findings worth taking elsewhere

**1. Setup overhead caps parallelism, so it has to come down first.** Their stated sequencing is
that aggressive sharding only becomes efficient once fixed per-shard costs are reduced — and the
evidence is that they went from **4 to 8 shards while total setup time fell**. Doubling shards
before cutting setup would have doubled the overhead instead: each new shard pays the full fixed
cost, so parallelism multiplies whatever you have not yet removed.

This is **setup reuse** from [Latency Patterns](../concepts/latency-patterns.md) — "parsing,
schema validation and connection establishment repeated per request are pure overhead" — with
the per-shard version of the same arithmetic, and it sits directly against that note's
**concurrency budget** row: fanning out is the fix until it is the cause.

**2. They removed a cache and got faster.** Dropping `node_modules` caching for plain rebuilding
took 28s to 7.5s. That is a direct counterexample to the caching reflex, and a concrete instance
of a trade [Latency Patterns](../concepts/latency-patterns.md) lists in the abstract: every
pattern has a cost, and here the restore-and-validate path was simply slower than redoing the
work. Worth remembering as a prompt — **measure the cache against rebuilding** rather than
assuming the cache wins.

A third, smaller one: moving **non-blocking cache writes off the critical path** for 42s per PR.
The work still happens; it just stops being something a PR waits on. That is the critical-path
discipline from [ChatGPT's Web Performance Architecture](chatgpt-web-performance.md) applied to a
pipeline instead of a page load.

## What this says about the repo's CI-speed argument

[CI Speed When Agents Write the Code](../engineering/ai-native/ci-speed-with-ai-agents.md) argues
that when agents wait rather than humans, the context-switching rationale dissolves and **"CI
speed moves from a human-experience constraint to a throughput-and-cost optimisation"** — with
the possibility that a team might rationally choose a *slower, more rigorous* pipeline.

That note carries no source. This is the first evidence bearing on it, and it supports the
reframing:

- Linear did not chase sub-minute CI for developer flow; the latency gain was modest.
- What they actually attacked was **fixed overhead and runner spend** — 87,000 runner-minutes a
  month is a cost result, not a flow result.
- The pressure driving all of it was **volume**: 2,000 tests a week, a quadrupled suite.

**The honest limit on that reading**, since it matters: the article never discusses the
trade-off. It does not consider a slower-but-more-thorough pipeline, and does not weigh cost
against developer experience. So it is *consistent with* the prediction rather than a test of it
— Linear never faced the choice the note poses, because absorbing the volume at roughly constant
latency was achievable. A team for whom it was not would be the real test.

## Relationship to other notes

- [CI Speed When Agents Write the Code](../engineering/ai-native/ci-speed-with-ai-agents.md) —
  the argument this is evidence for, and that note's first empirical grounding.
- [Change Absorption Capacity (CATS)](../engineering/practices/change-absorption-capacity.md) —
  the concept this instantiates: capacity raised to meet agent-speed change, measured as holding
  latency steady against a quadrupling suite.
- [CI/CD as the Control Plane](../engineering/ai-native/ci-cd-ai-engineering.md) — the pipeline as
  the guardrail that makes agent-speed delivery safe; this is what it costs to keep that guardrail
  usable at volume.
- [Latency Patterns](../concepts/latency-patterns.md) — setup reuse, concurrency budget and the
  caching trade, all three worked out in one pipeline with numbers attached.
- [Linear's Performance Architecture](linear-performance-architecture.md) — the same company's
  performance engineering one layer out, on the client. Both treat fixed startup cost as the thing
  to attack; that note does it for perceived page speed, this for pipeline latency.
- [Trunk-Based Development](../engineering/practices/trunk-based-development.md) — the source of
  the ~10-minute CI rule these numbers sit comfortably inside, even after the growth.
- [Brownfield Agentic Engineering](../engineering/ai-native/brownfield-agentic-engineering.md) —
  where the test volume comes from: generating tests that document existing behaviour is the
  recommended zero-risk starting work for agents, and this is the downstream bill.
