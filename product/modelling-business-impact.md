---
type: note
title: Modelling Software's Business Impact
description: "The value side of a repo full of activity metrics: NPV models over five categories, Pirate Metrics as the proxy layer, and the argument that once AI relieves the engineering constraint it moves to customer absorption capacity."
tags: [decision-making, leadership, observability, reading]
topic: product
status: notes
level: intermediate
related:
  - engineering/practices/change-absorption-capacity.md
  - product/prioritisation-as-a-symptom.md
  - product/explore-vs-exploit.md
  - leadership/mission-to-metrics.md
  - engineering/ai-native/activity-metrics-obsolete.md
  - leadership/revised-rules-engineering-leadership.md
  - concepts/theory-of-constraints.md
  - leadership/plan-is-not-a-strategy.md
  - engineering/architecture/comprehension-as-architecture.md
  - engineering/ai-native/apex-framework.md
  - concepts/devops-capability-model.md
source: "https://www.jamesshore.com/v2/blog/2026/modeling-softwares-business-impact"
updated: 2026-10-11
---

# Modelling Software's Business Impact

James Shore (September 2026) argues that software organisations measure the **cost** of
development carefully and model the **value** of it barely at all.

That asymmetry is visible in these notes. The cluster on measuring engineering activity is
dense — [From Mission to Metrics](../leadership/mission-to-metrics.md),
[The APEX Framework](../engineering/ai-native/apex-framework.md),
[Activity Metrics Under AI](../engineering/ai-native/activity-metrics-obsolete.md),
[DORA](../concepts/devops-capability-model.md) — and several of them end on "align to business
outcomes" without ever saying how that is done. This is the missing half.

**Provenance.** A practitioner essay recounting his own experience introducing the practice at
one company. No data, and — slightly ironically for a piece about measuring value — no outcome
figures for the models themselves.

## Why now: the constraint moves to the customer

> "Now, we can produce a lot more work, but that doesn't mean customers can **absorb** it."

This is a **third answer** to a question these notes keep asking. Once AI relieves the
engineering constraint, where does it go?

| Source | Where the constraint moves |
|---|---|
| [Revised Rules of Engineering Leadership](../leadership/revised-rules-engineering-leadership.md) | **Decision speed** — execution got cheap, choosing what to execute stayed hard |
| [Prioritisation as a Symptom](prioritisation-as-a-symptom.md) | Nowhere in particular — difficulty is an artefact of **coupling and slowness**, so fix those instead |
| [Theory of Constraints](../concepts/theory-of-constraints.md) | Wherever the next binding constraint happens to be |
| **Shore, here** | **Customer absorption capacity** |

None of the others names the customer. And the framing is a near-exact echo of
[Change Absorption Capacity](../engineering/practices/change-absorption-capacity.md), which
argues every *system* has a finite capacity to absorb change safely, and that exceeding it makes
delivery slower despite higher raw output.

**Shore's is the same shape pointed at the customer rather than the codebase** — and neither
author appears aware of the other. Read together they describe two independent ceilings on the
same pipeline: the system can only take so much change safely, and the customer can only take so
much change usefully. Shipping past either one converts output into waste, just with different
symptoms — incidents in the first case, ignored features in the second.

## The model

NPV forecasts over a five-year horizon, in five categories:

| Category | What it estimates |
|---|---|
| **New sales** | Customers gained × value per customer |
| **Upsell** | Upgrade adoption × revenue per upgrade |
| **Retention** | At-risk customers saved × their value |
| **Cost savings** | Operational efficiencies released |
| **Expenditures** | Development cost plus ongoing operational cost |

**Worth stating precisely:** he offers *guidance*, not formulas — "number of customers × value
per customer" is described as an approach rather than set out as an equation. Presenting these as
a calculation would overstate the piece. His term for the initiatives that warrant one is a
**product bet**, with spending released against Build-Measure-Learn milestones rather than
committed up front.

## The attribution problem, and the proxy answer

> "Who gets the credit for the success? Obviously, everybody contributed. But how much?"

A feature ships alongside marketing, sales motion and partnerships, so revenue cannot be
attributed to it cleanly. His answer is to measure **intermediate** outcomes instead, via
**Pirate Metrics** (AARRR): Acquisition, Activation, Retention, Referral, Revenue. A feature can
plausibly be shown to move activation or retention even when its contribution to revenue is
unrecoverable.

That is the same move as a proxy anywhere else — it trades directness for measurability — and it
carries the familiar risk. The proxies are closer to the work and therefore more gameable, which
is why the governance point below matters more than the arithmetic.

## What the model is actually for

The best reframe in the piece, and the reason it survives being wrong:

> "The model will force some of those hidden assumptions to the surface, where they can be
> dissected and discussed."

The artefact's value is not forecast accuracy. It is that **someone has to state what they are
assuming** in order to produce it — how many customers, at what value, over what period. An
initiative proposed without a model carries all of that implicitly, where it cannot be argued
with. That case holds even when every number turns out wrong, which is a considerably more
defensible claim than predicting revenue.

He pairs it with a governance rule:

> "use this as **a tool for decision-making** rather than a way of assessing people's
> performance"

**This is the third independent arrival at that rule in these notes**, from a third domain:

- [Comprehension as an Architectural Characteristic](../engineering/architecture/comprehension-as-architecture.md)
  — metrics about people change behaviour once enforced, so they are "investigation triggers, not
  gates"
- [Activity Metrics Under AI](../engineering/ai-native/activity-metrics-obsolete.md) — never
  report per individual; team-level minimum, because the dashboard becomes a leaderboard
- **Shore** — a value model used to assess people stops being usable for deciding

Architecture, engineering metrics and product finance, reaching the same conclusion separately.
That convergence is better evidence for the rule than any one of them, and it suggests the
failure mode is a property of **measurement under organisational pressure** rather than of any
particular metric.

## Getting it adopted

The part most writing on this omits, and the reason attempts fail. Shore's route: work with the
VP of Product to introduce the idea to leadership, secure **CEO and CFO sponsorship**, then rely
on peer relationships for day-to-day cooperation — improving the models iteratively through
cross-functional critique.

Two details worth keeping. **Finance is an ally, not an obstacle** — he reports finance teams
strengthening the critiques without damaging relationships, which is the opposite of the usual
expectation. And after delivery the model becomes an **accountability artefact**: the team is
answerable for delivered value rather than for schedule adherence, which is a different and
harder standard than the one most delivery organisations actually use.

## Relationship to other notes

- [Change Absorption Capacity (CATS)](../engineering/practices/change-absorption-capacity.md) —
  the pairing worth reading together: two ceilings on one pipeline, the system's and the
  customer's, arrived at independently.
- [Prioritisation as a Symptom](prioritisation-as-a-symptom.md) — the sharpest disagreement
  here. That note argues effort spent improving prioritisation is misallocated because estimates
  cannot be checked and the counterfactual is never run; this argues for building the estimates
  anyway, on the grounds that the *value* is the assumption-surfacing rather than the number.
  Both can hold if you read Shore as defending the artefact and not the forecast.
- [Exploring vs Exploiting](explore-vs-exploit.md) — a model is how a draw on the **Idea Fund**
  would be justified, and how an exploration that paid off would be recognised afterwards.
- [From Mission to Metrics](../leadership/mission-to-metrics.md) — the target/guardrail/diagnostic
  split and Goodhart; this supplies the business-value layer those metrics are meant to serve.
- [Activity Metrics Under AI](../engineering/ai-native/activity-metrics-obsolete.md) — the
  activity side of the same ledger. Its "rework per AI spend" is a cost-efficiency ratio; this is
  the value side it would need to be divided into.
- [Revised Rules of Engineering Leadership](../leadership/revised-rules-engineering-leadership.md)
  and [Theory of Constraints](../concepts/theory-of-constraints.md) — the competing answers to
  where the constraint went.
