---
type: case-study
title: Anthropic's claude.ai Performance Sprint
description: "An agent-driven two-week performance sprint gated on deterministic counts rather than wall-clock time — CPU instructions via Valgrind, React commits, style recalcs — with a ratchet that only lowers the ceiling."
tags: [performance, ai-engineering, ci-cd, testing, reading]
topic: case-studies
status: notes
level: intermediate
related:
  - case-studies/vercel-v0-instant-navigations.md
  - case-studies/github-huge-pr-rendering.md
  - case-studies/linear-ci-rework.md
  - case-studies/chatgpt-web-performance.md
  - case-studies/linear-performance-architecture.md
  - engineering/architecture/runtime-architecture-verification.md
  - concepts/latency-patterns.md
  - engineering/practices/feature-flags-and-branch-by-abstraction.md
  - case-studies/anthropic-ai-native-teams.md
  - case-studies/rootly-pr-size-risk-labels.md
  - engineering/ai-native/brownfield-agentic-engineering.md
  - case-studies/github-copilot-rust-migration.md
  - engineering/ai-native/agentic-verification.md
  - case-studies/anthropic-scion-source-control.md
source: "https://claude.dev/blog/how-we-made-claude-ai-faster/"
updated: 2026-10-18
---

# Anthropic's claude.ai Performance Sprint

Raymond Wang, Sam Attard and Issac G. (Anthropic, September 2026) report a two-week sprint in
August 2026 that made claude.ai and the desktop app **3.1× faster on the geometric mean of
thirteen measurements**, with an agent doing most of the work.

> **Provenance, stated plainly.** This is Anthropic reporting that an Anthropic model improved
> Anthropic's own product, self-measured against its own baseline. It is the most
> self-interested configuration a case study can have. The method below is specific enough to
> copy and check, which is why it is kept; the *magnitude* is not independent evidence about
> anything.

## What the agent did, precisely

The division of labour is worth getting right, because it is the detail most likely to be
garbled in retelling:

- **Claude Tag** — the Slack integration — ran *"an internal research model roughly comparable
  to Opus 5.5."* The tool and the model are separate things.
- The agent's remit: *"facilitate all things related to the performance of the claude.ai website
  and desktop app"* — monitoring deploys, building benchmarks, implementing solutions, proposing
  opportunities.
- The humans: *"setting goals, making tradeoffs, and approving every change."*

Everything ran from a single Slack channel with Claude in every thread.

**This is the instance the repo has been missing.**
[Vercel's Agent Loop for Instant Navigations](vercel-v0-instant-navigations.md) argues the shape
of this — turn a perceptual quality into a signal an agent can loop on — and
[Rendering Huge Pull Requests](github-huge-pr-rendering.md) builds an unattended autopilot but
**claims no agent driving it**. Here the agent demonstrably drove the work, with humans holding
goals and approval.

## The contribution is the metric, not the speedup

The reusable part. Wall-clock time proved **"noisy"** for CI gates, so the benchmarks were built
on **deterministic counts**:

| Measure | How |
|---|---|
| **CPU instruction counts** | Valgrind with `node --predictable` |
| React commits per interaction | — |
| V8 function-call counts | Precise coverage |
| Layout and style-recalc counts | — |
| DOM mutations | — |

This is the sharpest answer yet to a problem three notes here circle. Vercel's `instant()` gives
a **binary** assertion — content was visible without a network request, or it wasn't. GitHub's
rAF sampler is **statistical** — jank measured by sampling, so a regression is a distribution
shift. Instruction counts are **deterministic**: the same input yields the same number, every
run.

That property is exactly what
[Runtime Architecture Verification](../engineering/architecture/runtime-architecture-verification.md)
argues makes a measure usable as a *gate* rather than a suggestion — "pure functions,
reproducible, auditable — the same input always scores the same." That note makes the case for
keeping models out of scoring; this is the same requirement applied to performance, and it is why
a noisy metric cannot gate a build no matter how much it correlates with what users feel.

Their framing — measuring something makes it tractable — is the ordinary version of the point.
The specific version is better: **measuring it *deterministically* makes it gateable.**

## The ratchet

The mechanism most worth stealing, and the repo holds nothing like it.

Instruction counts could only **"ratchet down"**: the CI ceiling lowers whenever counts improve,
and never rises. Not a threshold someone chose — a **monotonic constraint**.

Two consequences. A performance budget set by hand goes stale and gets argued about; a ratchet
needs no maintenance and no negotiation, because the current best *is* the limit. And it is what
makes merging three thousand changes tractable — nobody re-litigates a budget per change, because
any change that worsens the count simply cannot land.

Worth noting what a ratchet cannot do: it locks in whatever the code does now, including
accidental wins, and it can block a legitimate change that trades instructions for something else
(a feature, clarity, a different resource). The article does not discuss the escape hatch, which
any real adoption would need.

## Reported figures

| Journey (p75) | Before → after |
|---|---|
| Fresh load of claude.ai | **3,085ms → 550ms** (5.6×) |
| Starting a Claude Code session | 837ms → 347ms (2.4×) |
| Loading a Cowork cloud session | 2,566ms → 728ms (3.5×) |
| **Overall** | **3.1× — geometric mean across thirteen measurements** |

Plus *"more than three thousand changes"* with *"not a single customer-facing incident or
rollback"*, via automated code review, feature flags, and staged rollout — employees, then 1%,
then everyone. That rollout ladder is
[progressive delivery](../engineering/practices/feature-flags-and-branch-by-abstraction.md) doing
the safety work rather than review doing it, which is the same division
[Rootly](rootly-pr-size-risk-labels.md) describes.

**How to read the headline.** A geometric mean across thirteen measurements is a more honest
construction than a single ratio — it resists one best case dominating — but the measurement set
is theirs, chosen to represent four journeys they identified as most of the activity, and the
baseline is their own unoptimised code. **A two-week sprint on a product that had not been
performance-tuned is the easiest available setting.** Nothing here speaks to agents working on a
mature, already-optimised system, which is the harder and more common case — the same limit
[Brownfield Agentic Engineering](../engineering/ai-native/brownfield-agentic-engineering.md)
raises about greenfield evidence generally.

## The optimisations

| Change | Note |
|---|---|
| Static composer baked into HTML | Render the input before any JavaScript runs |
| V8 code cache precompiled for the desktop shell | Parse/compile cost moved out of startup |
| Session prefetch on hover | Anticipation, from [Latency Patterns](../concepts/latency-patterns.md) |
| Sidebar re-renders reduced **90%** | — |
| Message-tree assembly: resolving message IDs **once instead of three times** | — |

The last is the most instructive precisely because it is unglamorous: redundant work done three
times, found once someone counted. Most of what the deterministic benchmarks surfaced looks like
this rather than like exotic optimisation — which is an argument for the *measurement* investment
over cleverness, and consistent with
[Linear's CI rework](linear-ci-rework.md) finding its wins in fixed overhead rather than
algorithms.

The static-composer move is the same instinct as
[ChatGPT's render-first](chatgpt-web-performance.md) streaming SSR — paint something usable before
verifying anything — reached independently for a logged-in product rather than an anonymous one.

## Relationship to other notes

- [Vercel's Agent Loop for Instant Navigations](vercel-v0-instant-navigations.md) — the argument
  this instantiates, and the comparison that matters: `instant()` is a binary oracle, instruction
  counts are a deterministic *continuous* one, so they support a ratchet where a pass/fail
  assertion cannot.
- [Rendering Huge Pull Requests (GitHub Copilot App)](github-huge-pr-rendering.md) — the
  unattended measurement loop without an agent claim; this is the version with one, and with a
  deterministic metric instead of a sampler.
- [Linear's CI Rework Under Agent Volume](linear-ci-rework.md) — the same lesson from the pipeline
  side: the wins were in fixed overhead, found by measuring rather than by insight.
- [Runtime Architecture Verification](../engineering/architecture/runtime-architecture-verification.md)
  — why reproducibility is the property that qualifies a measure as a gate.
- [ChatGPT's Web Performance Architecture](chatgpt-web-performance.md) and
  [Linear's Performance Architecture](linear-performance-architecture.md) — the other two
  client-performance case studies; both are architectural accounts, where this is a *method*
  account and the architecture is incidental.
- [Anthropic's AI-Native Team Structure](anthropic-ai-native-teams.md) — the other Anthropic
  self-report here, and worth reading beside it for the same provenance caution.
- [Feature Flags and Branch by Abstraction](../engineering/practices/feature-flags-and-branch-by-abstraction.md)
  — the machinery that made 3,000 changes survivable.
