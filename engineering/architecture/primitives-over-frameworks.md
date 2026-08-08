---
type: note
title: Primitives Over Opinionated Frameworks
description: "Which dependencies to keep when implementation labour gets cheap: retain unopinionated primitives, drop the opinion layer, own the thin layer between — and the cases where that is the wrong call."
tags: [architecture, system-design, ai-engineering, decision-making, reading]
topic: engineering/architecture
status: notes
level: intermediate
related:
  - engineering/ai-native/modern-engineering-values.md
  - engineering/architecture/over-engineering.md
  - case-studies/microsoft-ai-core-competency.md
  - engineering/architecture/agile-design-decisions.md
  - engineering/architecture/composable-architecture.md
  - languages-and-frameworks/react-state-management.md
  - engineering/architecture/overview.md
  - case-studies/stripe-kai-agent-platform.md
source: "https://www.robinwieruch.de/agentic-coding-bet-on-primitives/"
updated: 2026-08-08
---

# Primitives Over Opinionated Frameworks

Robin Wieruch (July 2026) argues that agentic coding changes which dependencies are worth
having. The underlying reversal — that agents make custom solutions economically viable where
libraries once saved scarce labour — is already recorded as *own your stack* in
[Modern Engineering Values](../ai-native/modern-engineering-values.md). What this adds is the
distinction that makes it actionable.

Experience-based, drawn from one freelance project. No data, and the crossover point below is
asserted rather than located.

## The distinction: primitives vs opinions

"Own your stack" sounds like build-versus-buy. The actual claim is narrower and more useful —
it is about *which layer* to depend on:

| | Examples | What you get |
|---|---|---|
| **Primitives** — unopinionated | DOM, SVG, SQL, HTTP, `d3-scale`, `date-fns`, `zod` | A computed capability, with implementation decisions left to you |
| **Opinion layer** — opinionated | Recharts, ORMs, component libraries | A capability *plus* a bundle of decisions someone else made |

The recommendation is to keep the primitives, drop the opinion layer, and own the thin custom
layer between them. That is not "write it yourself" — the dependency count barely changes. It
is a claim about **where in the stack someone else's judgement is worth accepting.**

## Why the ladder was built, and why it wobbles

The historical mechanism matters more than the conclusion. Twenty years of climbing the
abstraction ladder — jQuery to React to meta-frameworks — happened because **human
implementation labour was the scarcest resource**. A library trades flexibility for labour
saved, and when labour is expensive that is straightforwardly a good trade.

Agentic coding collapses implementation cost, so the trade is repriced. The pendulum swings
from **renting opinions** to **owning a layer**. Note the shape of the argument: it is
conditional on a cost curve and there is a **crossover point**, so this is not a claim that
libraries were always wrong — it is a claim that the input that justified them has changed.

## A library is someone else's constraints

*This connection is the note's own reading, not Wieruch's.*
[Over-Engineering Is Solving the Wrong Problem](over-engineering.md) argues that enough
constraints leave exactly one solution, and that the solution is right *because* it is the
only one that fits.

An opinionated library is a set of constraint choices made for a different problem. Adopting
one means inheriting constraints that were never yours — which is a decent explanation for the
familiar experience of library-shaped code that nearly, but not quite, fits: you are running
someone else's optimum. When implementation was expensive, accepting a near-fit was rational.
When it is cheap, satisfying your own constraints exactly becomes affordable.

## When to keep the opinion layer

The caveats are load-bearing and qualify the flat version of this claim elsewhere in these
notes:

- **Accessibility-critical components** — modals, date pickers, comboboxes — still warrant
  mature libraries. These encode years of keyboard, focus-management and screen-reader edge
  cases that are easy to generate plausibly and get subtly wrong. This is the most important
  caveat and the one most likely to be skipped.
- **Without established agentic workflows**, the traditional maths still favours libraries —
  the crossover has not happened for you yet.
- **Commodity UI** — an internal dashboard does not need a bespoke chart layer.
- **Comprehension, not just authorship.** Owning a layer requires the competence to
  *understand* it, which is a higher bar than generating it with an agent. The maintenance
  obligation is real and permanent.

`modern-engineering-values.md` already flags that its stance suits "small, autonomous, expert
teams rather than as a universal prescription". These caveats are the specific form of that
warning.

## Practices

- **Spike competing approaches in a time-box** rather than deciding from first principles
- The worked example: custom chart components from **D3 scales plus React SVG rendering**,
  driven by the product's own design tokens — primitives underneath, thin owned layer on top
- **Document the patterns** and put agentic review over the custom layer, so the owned code
  stays coherent as it grows

## Relationship to other notes

- [Modern Engineering Values](../ai-native/modern-engineering-values.md) — *own your stack* as
  one of eight values; this is that value examined on its own, with the layer distinction and
  the exceptions it needs.
- [Over-Engineering Is Solving the Wrong Problem](over-engineering.md) — the constraints
  argument this note applies to dependency choice.
- [Microsoft's AI Strategy](../../case-studies/microsoft-ai-core-competency.md) — *own the
  harness, rent the model* is the same rent/own split one layer up: keep the orchestration you
  control, rent the commodity underneath.
- [Agile Design Decisions](agile-design-decisions.md) — adopting an opinionated framework is
  closer to a one-way door than adding a primitive, which is a useful way to size the decision.
