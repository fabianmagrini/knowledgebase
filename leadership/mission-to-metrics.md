---
type: note
title: From Mission to Metrics
description: "Annie Zhou's four-layer cascade — mission, strategy, goals, metrics — as the written artefact that lets a growing organisation distribute decisions without losing alignment."
tags: [leadership, decision-making, governance, reading]
topic: leadership
status: notes
level: intermediate
related:
  - leadership/plan-is-not-a-strategy.md
  - leadership/start-with-why.md
  - leadership/first-principles-thinking.md
  - leadership/engineering-leadership-overview.md
  - product/explore-vs-exploit.md
  - product/prioritisation-as-a-symptom.md
source: "https://www.anniez.xyz/p/mission-to-metrics"
updated: 2026-07-26
---

# From Mission to Metrics

Annie Zhou argues that organisations scale by writing down the chain from why they exist to
what they measure. The problem it solves is specific: growth breaks the informal coordination
that worked when everyone could talk to everyone. The usual responses — more meetings, more
coordinators — treat the symptom. The absent thing is a **shared framework people can read**,
so that anyone can see how their work connects upward without leadership re-aligning them
constantly.

Drawn from the author's experience at Block and Facebook, with Facebook's 2018 MSI pivot as a
documented public example (below). It is offered as practice rather than as something
validated across organisations.

## The four layers

| Layer | Horizon | Answers |
|---|---|---|
| **Mission** | Timeless | Why the organisation exists |
| **Strategy** | Evergreen | How it intends to accomplish that |
| **Goals** | Time-bound | The specific outcomes that would show the strategy is working |
| **Metrics** | Measured | The numbers tracking progress toward those outcomes |

This picks up exactly where [A Plan Is Not a Strategy](plan-is-not-a-strategy.md) stops.
Roger Martin defines what a strategy must be — an integrative set of choices about where to
play and how to win — and leaves it there. The cascade is the machinery for getting that
choice down to something a team can act on and measure.

## Two properties that make it work

**Recursive.** Each team runs the same four layers at its own level, with its goals derived
from the layer above. This is what actually distributes decision-making: a team that can see
the chain can decide locally without asking, because it knows what it is optimising for and
why.

**Exhaustive without overlap.** Across a level, the coverage must be complete and
non-duplicating. Gaps mean work nobody owns; overlaps mean teams colliding over the same
outcome. This is the property most likely to erode quietly as an organisation reorganises.

## Three kinds of metric

| Type | Purpose | Example |
|---|---|---|
| **Target** | The number being deliberately moved | Revenue, retention |
| **Guardrail** | A counter-metric that catches collateral damage | Uptime paired against delivery velocity |
| **Diagnostic** | Explains *why* a target moved | Funnel conversion, cohort breakdowns |

The guardrail category is the one most often missing. A target metric with no counter-metric
is an invitation to move it by damaging something unmeasured.

**Anchor on an apex metric** — the single lagging indicator the business ultimately depends
on. Zhou's example is Facebook's ads and product organisations operating under one apex
metric, revenue.

> Note on terminology: this "apex metric" is unrelated to
> [The APEX Framework](../engineering/ai-native/apex-framework.md), LinearB's model for
> measuring AI engineering impact. Same word, different concepts.

**Pair lagging with leading.** Lagging indicators are what you are judged on; leading
indicators are what predicts them. The discipline is to **write down the hypothesis**
connecting the two — *we believe moving this leading indicator will move that lagging one* —
and then test it against reality rather than assuming it.

## Metrics as a pressure test

The most useful inversion in the piece: when a metric comes out fuzzy, the instinct is to
tweak the number, but the fault is usually higher up. An aspiration like "grow the business"
cannot produce a sharp metric because it is not yet a strategy. **Metrics failing to
crystallise is diagnostic information about the layers above them.**

The corresponding audit: walk each metric backward through goals and strategy to mission. If
it does not trace, remove it.

## How it fails

Mostly variants of **Goodhart's law** — once a measure becomes a target, it stops being a
good measure:

- The number becomes the goal rather than a proxy for the goal
- The proxy drifts away from the outcome it once stood for
- Local optimisation improves one team's metric at the expense of the global one
- **Vanity metrics** — features shipped, tickets closed — presented as outcomes
- Metrics outliving the reasoning that produced them, still tracked after the strategy moved
- New initiatives judged against the benchmarks of mature products

The cited public case is Facebook's 2018 shift to **Meaningful Social Interactions (MSI)**,
intended to favour genuine engagement over passive consumption, which is widely reported to
have amplified divisive content instead — the metric was moved successfully while the
outcome it stood for went the other way.

## Relationship to other notes

- [A Plan Is Not a Strategy](plan-is-not-a-strategy.md) — the layer above: what makes
  something a strategy rather than a list of initiatives. This note is how that choice
  reaches the ground.
- [Start with the Why](start-with-why.md) — the mission layer, and why the top of the cascade
  has to be genuinely held rather than stated.
- [First-Principles Thinking](first-principles-thinking.md) — the reasoning that produces a
  strategy worth cascading in the first place.
- [Exploring vs Exploiting in Product Discovery](../product/explore-vs-exploit.md) — the
  failure mode of judging new initiatives against mature-product benchmarks is the
  exploration/exploitation distinction showing up as a measurement problem.
