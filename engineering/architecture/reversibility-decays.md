---
type: note
title: Reversibility Decays
description: "Two-way doors lock behind you: the cost of exiting a decision only ever rises as dependencies accumulate, so optionality is something maintained rather than a property assessed once."
tags: [architecture, decision-making, system-design, reading]
topic: engineering/architecture
status: notes
level: intermediate
related:
  - engineering/architecture/agile-design-decisions.md
  - engineering/architecture/adrs-in-an-agentic-world.md
  - engineering/architecture/architectural-change-cases.md
  - engineering/architecture/adr.md
  - engineering/practices/feature-flags-and-branch-by-abstraction.md
  - engineering/ai-native/modern-engineering-values.md
  - engineering/architecture/primitives-over-frameworks.md
  - engineering/architecture/overview.md
  - engineering/architecture/design-docs.md
  - concepts/optimal-stopping.md
  - engineering/architecture/change-locality.md
  - engineering/architecture/data-readiness-for-agents.md
source: "https://fffej.substack.com/p/two-way-doors-sometimes-lock-behind"
updated: 2026-08-08
---

# Reversibility Decays

The one-way / two-way door framing is load-bearing across these notes — it appears in
[Agile Design Decisions](agile-design-decisions.md), [Design Docs](design-docs.md),
[Optimal Stopping](../../concepts/optimal-stopping.md) and elsewhere as the test for how much
rigour a decision deserves. Jeff (July 2026) supplies the correction none of them carry:

> Two-way doors sometimes lock behind you.

A decision classified as reversible at the moment it was made does not stay reversible.
Dependencies accumulate around it, and the classification silently expires.

Experience-based argument, no data.

## The strike price only moves one way

The sharpest analogy in the piece. A financial option has a **fixed strike price** — the cost
of exercising it is known when you buy it. A technical option does not:

> The cost to exit a technical decision can only move in one direction.

Adopt a feature-flag provider and the exit cost on day one is a small integration. A year
later, product teams gate releases on it, data science reads its assignment logs, release
automation drives it, and analytics joins against it. Nothing about that was decided; it
accumulated. The thing became **load-bearing** without anyone choosing to make it so.

Other instances given: cloud lock-in through managed services and proprietary runtimes, CI/CD
servers via specialised testing features, and observability stacks through the dashboards and
alerts configured against them. In each, the artefact that locks you in is not the thing you
adopted — it is the configuration and integration built on top of it.

## Optionality is maintained, not held

The reframe that follows:

> Optionality isn't a point in time decision, it's something that must be maintained.

Treating reversibility as a *property assessed at decision time* is the error. It is a
**running cost**, and one that is paid in attention rather than money — which is why it is
usually not paid at all. The term for the accumulated shortfall is **reversibility debt**.

This refines the *option value* item in
[Modern Engineering Values](../ai-native/modern-engineering-values.md), which prescribes
preserving future flexibility and maximising the ability to adapt. This note is the missing
half: option value is not preserved by intending to preserve it.

It also generalises a discipline
[Feature Flags and Branch by Abstraction](../practices/feature-flags-and-branch-by-abstraction.md)
already applies narrowly. That note treats each release toggle as debt from the moment it
ships, with a removal ticket and an expiry date. The same logic applies to any adopted
dependency: the exit stays cheap only while something actively keeps it cheap.

## The tension with cheap regeneration

*This synthesis is the note's own, not the author's.*

[ADRs in an Agentic World](adrs-in-an-agentic-world.md) argues that cheap spikes "effectively
make more decisions **reversible** (two-way doors), because you can build and discard
candidates." Read against this piece, that claim needs narrowing — and the way it narrows is
useful:

**Reversibility has two costs.** *Rebuilding* the thing, and *un-wiring* everything that came
to depend on it. Agents collapse the first and do nothing for the second.

You can regenerate a feature-flag client in an afternoon. You cannot un-wire four teams from
it. So cheap generation genuinely does widen the set of reversible decisions — but only for
decisions whose exit cost is dominated by construction, and those are precisely the decisions
that were never the risky ones. For anything that becomes an integration point, cheap
regeneration is irrelevant to the cost that matters.

The corollary for [Primitives Over Opinionated Frameworks](primitives-over-frameworks.md):
an opinionated framework is not merely closer to a one-way door at adoption — it *travels*
toward one faster, because it invites more surface to be built against it.

## What to do about it

- **Record the assumptions that make it reversible** in the ADR, not just the decision. A
  reversibility claim without its conditions cannot be re-checked later.
- **Attach a rough exit cost, and revisit it.** This is what
  [Architectural Change Cases](architectural-change-cases.md) already asks for — cost and
  reversibility, speculated forward. The addition here is that those estimates **go stale**,
  so re-costing is part of the practice rather than a one-off exercise.
- **Test the exit before committing.** Prove the migration path exists while it is still
  cheap to prove.
- **Let low-value options expire deliberately.** Maintaining optionality has a real cost, and
  the author is explicit that it does not always justify itself. Choosing to lock a door is
  legitimate; discovering it locked is not.

That last point is what keeps this from being an argument for permanent hedging. The claim is
not that every door should stay open — it is that **which doors are still open should be a
known fact rather than an assumption inherited from a decision record nobody has re-read.**

## Relationship to other notes

- [Agile Design Decisions](agile-design-decisions.md) — the reversibility framework this
  qualifies. Its one-way/two-way test remains the right question; this note says the answer
  has a shelf life.
- [Architectural Change Cases](architectural-change-cases.md) — forward speculation about how
  decisions might have to change; reversibility decay is why those cases need revisiting
  rather than filing.
- [ADRs in an Agentic World](adrs-in-an-agentic-world.md) — the cheap-regeneration claim this
  narrows, split into construction cost and integration cost.
- [Feature Flags and Branch by Abstraction](../practices/feature-flags-and-branch-by-abstraction.md)
  — flag debt is reversibility debt in its most familiar form, with the maintenance discipline
  already worked out.
