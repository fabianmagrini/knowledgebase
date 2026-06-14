---
title: Designing with Constraints
tags: [leadership, reading]
topic: leadership
status: notes
level: intermediate
related:
  - leadership/first-principles-thinking.md
  - leadership/start-with-why.md
  - engineering/architecture/agile-design-decisions.md
source: "https://jordanlord.co.uk/blog/3-constraints/"
updated: 2026-06-14
---

# Designing with Constraints

The argument is that constraints enable rather than restrict creativity: by collapsing the
decision space they force clearer thinking and better solutions. Products tend to fail when they
are too complex or lack a distinct identity, so the author proposes three constraints to apply as
filters *before* building anything — deciding what deserves to exist.

## The three constraints

1. **One page maximum.** The idea must fit on a single page that captures the north star. If it
   needs more than a page, it is too complex — do not build it. The one-pager becomes the shared
   reference: anything not on it is not worth fighting over.

2. **Separable core technology.** Develop reusable intellectual property that is distinct from the
   product itself, so the core survives product pivots and compounds in value over time. Cited
   examples: Linux → Git, HashiCorp → HCL, Google → Kubernetes.

3. **One defining constraint.** Choose a single visible, central constraint that shapes the
   product's identity and permeates the user experience. The design then "falls out" of a
   well-chosen constraint. Cited examples: Minecraft's block-based structure, IKEA's flat-pack
   methodology.

## The rule

Reject any idea that fails any one of the three. Used this way, constraints reduce feature creep
and decision fatigue — the decision is made by the constraint, not by debate.

## Relationship to other notes

- [First-Principles Thinking](first-principles-thinking.md) — a complementary move: that note
  *strips inherited* constraints to find what actually holds; this one *imposes deliberate*
  constraints to enable design. Hard vs. soft limits there, chosen limits here.
- [Start with the Why](start-with-why.md) — the one-page north star is a purpose-first artifact:
  lead with the why before the what.
- [Agile Design Decisions and Principles](../engineering/architecture/agile-design-decisions.md) —
  the same instinct that good design emerges from clear constraints rather than up-front
  completeness.
