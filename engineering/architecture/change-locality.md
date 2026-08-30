---
type: note
title: Change Locality and Boundary Drift
description: "The understanding needed to make a change should be proportional to its scope — and boundaries drawn correctly go stale, with excess cognitive load as the diagnostic that they have."
tags: [architecture, system-design, decision-making, reading]
topic: engineering/architecture
status: notes
level: intermediate
related:
  - engineering/architecture/team-topologies.md
  - engineering/architecture/ddd-strategic-design.md
  - engineering/architecture/bounded-context-canvas.md
  - engineering/architecture/over-engineering.md
  - engineering/architecture/comprehension-as-architecture.md
  - engineering/architecture/reversibility-decays.md
  - engineering/architecture/architectural-change-cases.md
  - engineering/architecture/overview.md
  - engineering/architecture/adr.md
  - engineering/architecture/enforced-architecture-rules.md
  - engineering/architecture/runtime-architecture-verification.md
source: "https://www.infoq.com/articles/evolutionary-architecture-change-locality/"
updated: 2026-08-23
---

# Change Locality and Boundary Drift

Michael Fischer, Nicholas Lawrence and Monica Karekar (InfoQ, August 2026) argue that a system
can only evolve coherently while teams can make local business changes without needing global
context. Their principle:

> The understanding required to make a change should be **proportional to the scope** of the
> change.

Experience report from an InfoQ Certified Architect Program cohort; no data or measured cases.

## The test for locality

A capability has locality when the team responsible can answer three questions **independently**:

1. **What can change here?**
2. **What contract protects neighbouring work?**
3. **What evidence proves the change is safe?**

Needing another team to answer any of the three is the signal. Their worked example: an
e-commerce address-change feature scoped to checkout, where discovery surfaced dependencies on
warehouse cutoff timing, fraud rules, delivery-partner instructions, support scripts and refund
policy — **none owned by checkout**.

## Boundary drift

The contribution these notes did not already hold is **temporal**.
[Team Topologies](team-topologies.md) and [DDD strategic design](ddd-strategic-design.md) both
treat boundaries as things to draw well. This treats them as things that **go stale**:

> Boundaries are provisional hypotheses about which decisions should change together.

A hypothesis is right until conditions change. The named drift patterns — product scope
expanding, team reorganisation, a platform absorbing capabilities, an outsourced capability
becoming core — all move the *decision path* while leaving the *structural boundary* where it
was. Nothing breaks at the moment of drift, which is why it accumulates.

Their second worked case: a retail bank's account-opening team owned the application form and
welcome communications, then loan underwriting, debit-card fulfilment and evolving compliance
rules arrived. The boundary never moved; the decisions did.

The authors stress that drift is **sociotechnical** — it shows up across technology, teams,
process and people, so it cannot be diagnosed from the architecture diagram alone.

## Cognitive load, inverted

[Team Topologies](team-topologies.md) uses cognitive load as a **design input**: size a team's
domain to what it can hold. This uses it as a **diagnostic output**: a team carrying business,
technical, operational and organisational context *beyond its scope* is evidence that its
boundary has drifted away from its responsibility.

Same concept, opposite direction — and the inverted version is the more actionable one, because
excess load is observable in a team that already exists, whereas the design-time version
requires predicting load before the work is done.

Other signals they list: delivery friction, incident recovery depending on outside teams,
support escalation patterns, review queue depth, and dependence on named experts.

## Restoring locality

| Practice | The point |
|---|---|
| **Redistribute repeated mechanics** | Move *toil* to platforms while **policy ownership stays with domain teams** |
| **Expose essential policy** | Make governing decisions visible via contracts, tests, dashboards, events or [decision records](adr.md) |
| **Rehearse exception paths** | Test whether a redesign actually keeps changes local under realistic conditions, rather than assuming it |

The first is the sharpest distinction: **offload the toil, not the judgement.** A platform that
absorbs the mechanics of a capability while the owning team keeps the policy preserves locality;
a platform that absorbs the policy has just relocated the boundary, which is one of the drift
patterns.

## When locality is the wrong goal

The caveats are load-bearing:

- **Not all boundary problems are drift.** Some changes are genuinely cross-cutting and no
  boundary would have contained them.
- **Consistency and risk control can outweigh local autonomy.** Fraud, refunds, compliance and
  safety may warrant broad agreement despite the locality cost.
- **Low cognitive load is not automatically good.** If it has been achieved by hiding essential
  complexity rather than removing accidental complexity, the load has moved, not gone.

## A pattern across three notes

*This connection is the note's own reading.*

Three independent sources recorded here describe the same underlying failure — **an
architectural property assessed once and never re-checked**:

| Note | What silently stops being true |
|---|---|
| [Reversibility Decays](reversibility-decays.md) | A two-way door stops being one as dependencies accumulate |
| [Comprehension as an Architectural Characteristic](comprehension-as-architecture.md) | The shared model thins out with no alarm |
| This note | A boundary drawn correctly stops matching the decision path |

None of the three fails loudly, and all three are usually discovered during an incident or a
migration — the moments when the assumption is finally tested. The general lesson is that some
architectural properties are **claims with a shelf life**, and the practice they need is
re-checking rather than better initial judgement.
[Architectural Change Cases](architectural-change-cases.md) is the closest existing habit: it
speculates forward about how decisions might have to change, and these three notes are the
argument for revisiting those cases rather than filing them.

## Relationship to other notes

- [Team Topologies](team-topologies.md) — boundaries and cognitive load at design time; this is
  the same pair examined for decay, with load as a symptom rather than a budget.
- [Domain-Driven Design: Strategic Design](ddd-strategic-design.md) and the
  [Bounded Context Canvas](bounded-context-canvas.md) — how to draw the boundary; this is how to
  tell it no longer fits.
- [Over-Engineering Is Solving the Wrong Problem](over-engineering.md) — its
  three-people/five-microservices case is the adjacent failure: boundaries that never matched
  the domain, rather than ones that stopped matching.
