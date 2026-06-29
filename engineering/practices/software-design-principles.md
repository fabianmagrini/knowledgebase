---
title: Software Design Principles
tags: [system-design, refactoring, code-review]
topic: engineering/practices
status: draft
level: intermediate
related:
  - engineering/architecture/micro-frontend-principles.md
  - engineering/practices/quality-first-ai-coding.md
  - engineering/architecture/agile-design-decisions.md
  - engineering/practices/change-absorption-capacity.md
  - engineering/practices/code-review-policy.md
  - concepts/clean-code-and-solid.md
  - engineering/practices/naming-conventions.md
updated: 2026-06-19
---

# Software Design Principles

A prioritised set of code-level design principles. None of these are new — they
are the durable core of good software design — but their *weighting* changes when
AI generates a large share of the code. The theme below each principle is **why it
matters more, not less, in an AI-native workflow**: when machines produce code
quickly and everywhere, the principles that keep code reviewable, local, and
changeable are what keep the system healthy.

These are the **code-level analogue** of the boundary-level
[Microfrontend Architecture Principles](../architecture/micro-frontend-principles.md):
the same instincts — single responsibility, cohesion, loose coupling, clear
contracts — one altitude down, applied to modules and functions rather than to
deployable boundaries.

## The principles

1. **Single Responsibility.** A module should have one reason to change. Beyond
   the classic maintainability argument, single-purpose units **shrink the blast
   radius** of any one AI-generated change — a focused module is one an agent (or a
   reviewer) can reason about in isolation.

2. **High Cohesion.** Things that change together live together. Cohesive code
   gives an AI assistant a tight, relevant context window and stops a single edit
   from rippling across unrelated concerns.

3. **Loose Coupling.** Minimise what one unit must know about another. Loose
   coupling is what lets a generated change stay *local* instead of cascading; it
   is the code-level version of the independent-deployability argument for
   services and microfrontends.

4. **Clear Contracts.** Communicate through explicit, typed interfaces, not
   implementation details. Contracts are the seams an agent works against: a sharp
   interface tells the model exactly what is allowed and makes invalid usage fail
   fast, rather than leaking through shared internal state.

5. **Dependency Inversion at service boundaries.** Depend on abstractions, not
   concretions, where modules meet. Inverting dependencies at the boundary keeps
   the core independent of volatile details (frameworks, providers, transports)
   and makes the system testable and substitutable — and it gives AI a stable
   contract to code against on either side of the seam. Note the boundary: invert
   *at service seams*, not everywhere — an interface with a single implementation
   added "for SOLID" is just indirection.
   [Prefer simplicity until abstraction is justified](../../concepts/clean-code-and-solid.md).

6. **Readability over cleverness.** Optimise for the reader, not for the author's
   ingenuity. This rises in priority in an AI-native workflow for two reasons: a
   **human must review machine-generated output**, and clever code is a review
   tax; and the next *agent* to touch the code reads it as context, so obscure
   code degrades future generation too. Boring, obvious code is a feature.

7. **Refactor continuously.** Keep design debt low by improving structure as you
   go, not in big-bang cleanups. Continuous refactoring is how a codebase
   **absorbs high-volume AI-generated change** without decaying — the
   maintainability counterpart to
   [Change Absorption Capacity](change-absorption-capacity.md). Generation makes it
   cheap to *add*; refactoring is what keeps the result coherent.

## SOLID supports the architecture — it doesn't drive it

These principles (and SOLID more broadly) earn their keep *within* a boundary, but
they are not the organising force of a system. In modern React and microfrontend
architectures, the **boundary-level** principles —
[bounded contexts, explicit contracts, and team ownership](../architecture/micro-frontend-principles.md) —
have a bigger impact on maintainability than strict adherence to all five SOLID
principles. SOLID stays useful as a tool for shaping the code inside a module; it
should *serve* the architecture, not dictate it. When the two pull in different
directions at scale, the boundary wins — a clean bounded context with a sharp
contract survives imperfect internals, but flawless SOLID cannot rescue a system
whose boundaries and ownership are wrong.

## The through-line

The first five principles **localise change** — they ensure any single edit, human
or machine, stays small and well-bounded. The last two **keep the code legible and
malleable over time** so that a high rate of change does not compound into decay.
Together they are what let a team run AI for speed without trading away the ability
to understand and safely change its own system — the same "fast flow of change,
safely, with quality" goal that runs through the
[quality-first](quality-first-ai-coding.md) and
[code review](code-review-policy.md) notes.

## Relationship to other notes

- [Microfrontend Architecture Principles](../architecture/micro-frontend-principles.md) —
  the boundary-level sibling; SRP, cohesion, coupling, and contracts restated at
  the scale of deployable units and teams.
- [Quality-First AI Coding](quality-first-ai-coding.md) — the practice of slowing
  down to let these principles hold even when generation is fast.
- [Agile Design Decisions and Principles](../architecture/agile-design-decisions.md) —
  emergent design and reversibility; these principles are what make emergent design
  safe to evolve.
- [Change Absorption Capacity](change-absorption-capacity.md) — the system property
  that continuous refactoring and low coupling protect.
- [Code Review Policy](code-review-policy.md) — readability and clear contracts are
  what make review tractable at AI-era code volumes.
