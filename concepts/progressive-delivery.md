---
type: note
title: Progressive Delivery
description: "extending continuous delivery with gradual, measured exposure (canary, blue-green, ring, flag rollout) gated on telemetry"
tags: [ci-cd, observability, testing]
topic: concepts
status: notes
level: intermediate
related:
  - concepts/continuous-delivery.md
  - concepts/ci-cd-continuous-deployment.md
  - engineering/practices/feature-flags-and-branch-by-abstraction.md
  - engineering/practices/release-confidence.md
  - concepts/resilient-software-design.md
  - concepts/devops-capability-model.md
  - engineering/practices/gitops.md
  - engineering/practices/rollback-and-roll-forward.md
  - leadership/managed-disruption.md
source: "James Governor / RedMonk — Progressive Delivery (2018); Adam Zimman, Heidi Waterhouse, James Governor — Progressive Delivery (LaunchDarkly, 2019)"
updated: 2026-06-21
---

# Progressive Delivery

Progressive delivery extends [continuous delivery](continuous-delivery.md) with
**gradual, controlled exposure**: a change reaches users a slice at a time, each
expansion gated by observed behaviour rather than a single all-or-nothing release.
Coined by James Governor (RedMonk) in 2018, it is sometimes summarised as
"continuous delivery with fine-grained control over the blast radius."

Where [continuous deployment](ci-cd-continuous-deployment.md) answers *how code
gets to production* (automatically, on every passing build), progressive delivery
answers *how a feature reaches users once the code is there* (incrementally, under
measurement). The two compose: deploy continuously, then release progressively.

## The two pillars (Governor)

Progressive delivery rests on two ideas:

1. **Release progression** — expose the change to an expanding population (1% →
   10% → 50% → 100%, or internal → beta → everyone), promoting only when signals
   stay healthy. The opposite of a big-bang cutover.
2. **Delegation** — the people who own the feature (product, the owning team)
   control its rollout, not a central release/ops gatekeeper. Release becomes a
   product decision made through configuration, not a deployment ticket.

## The control loop

Progressive delivery is a feedback loop, not a one-shot action:

```text
deploy (dark) → expose to a small cohort → observe SLIs / telemetry
      → automated analysis vs. a baseline → promote  (widen the cohort)
                                          → or roll back (contract instantly)
```

This makes it **load-bearing on observability**: without trustworthy signals —
error rate, latency, business metrics — there is nothing to gate promotion on. The
ability to contract instantly is what makes widening low-drama, the same property
as [release confidence](../engineering/practices/release-confidence.md).

## Techniques

Progressive delivery is an umbrella over several rollout strategies, usually
combined with [feature flags](../engineering/practices/feature-flags-and-branch-by-abstraction.md):

| Technique | How exposure grows | Best for |
|---|---|---|
| **Canary** | Route a small % of traffic to the new version, watch, then widen | Catching regressions on real traffic with minimal blast radius |
| **Blue-green** | Run two full environments; switch traffic, keep the old as instant rollback | Fast cutover and rollback when running two stacks is affordable |
| **Rolling** | Replace instances in batches | Infrastructure-level updates with no extra environment |
| **Feature-flag % rollout** | Flip a flag for an expanding cohort, independent of deploy | Per-feature, per-user control; A/B and targeting |
| **Ring deployment** | Concentric rings (internal → early adopters → general) | Org-wide rollouts with progressively wider, riskier audiences |

Canary and feature-flag rollout are the most distinctly "progressive" — both vary
exposure continuously and can be **automated against guardrail metrics**. Blue-green
and rolling are primarily deployment mechanics that progressive delivery builds on.

## Why it matters

In the [DORA](devops-capability-model.md) frame, progressive delivery improves the
**stability** metrics — change failure rate and time to restore — *without*
sacrificing the **throughput** metrics. A bad change is caught at 1% of traffic and
rolled back in seconds, so failures rarely become incidents and recovery is near
instant. It is one of the cleanest ways to keep shipping fast while shrinking the
cost of being wrong — a core tool for
[managed disruption](../leadership/managed-disruption.md), where every change stays
small and reversible.

## Tooling

The control loop is increasingly automated. Kubernetes-native controllers like
**Argo Rollouts** and **Flagger** automate canary analysis and promotion/rollback
against metrics; flag platforms like **LaunchDarkly**, **Unleash**, and
**Split** own targeting and percentage rollout. The pattern predates the tools,
though — the loop matters more than any vendor.

## Relationship to other notes

- [Continuous Delivery](continuous-delivery.md) and
  [Continuous Deployment](ci-cd-continuous-deployment.md) — progressive delivery is
  the layer on top that controls *exposure*; CD gets the artifact to production,
  progressive delivery governs who sees it.
- [Feature Flags and Branch by Abstraction](../engineering/practices/feature-flags-and-branch-by-abstraction.md)
  — flags are the primary mechanism that makes progressive rollout possible; this
  note is the strategy, that note is the technique.
- [Resilient Software Design](resilient-software-design.md) — gradual rollout and
  instant rollback are designing for failure at the release layer.
