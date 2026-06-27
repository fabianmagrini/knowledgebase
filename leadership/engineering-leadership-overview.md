---
title: Engineering Leadership — Overview
tags: [meta, leadership, communication]
topic: leadership
status: complete
related:
  - leadership/start-with-why.md
  - leadership/plan-is-not-a-strategy.md
  - leadership/decision-facilitation.md
  - leadership/principal-engineer-influence.md
  - leadership/raising-problems-without-complaining.md
  - leadership/protecting-mavericks.md
  - leadership/managed-disruption.md
  - leadership/architecture-decision-forum.md
  - leadership/first-principles-thinking.md
  - leadership/designing-with-constraints.md
  - leadership/learning-organisation.md
  - engineering/architecture/agile-design-decisions.md
  - sre/incident-swarming.md
  - leadership/new-leader-credibility.md
  - leadership/revised-rules-engineering-leadership.md
  - engineering/architecture/team-topologies.md
  - case-studies/portkey-product-engineer-company.md
updated: 2026-06-27
---

# Engineering Leadership — Overview

A map of the notes on senior-engineer leadership, communication, and decision governance —
how to set direction and make good decisions with other people.

## Purpose & influence — setting direction

- [Start with the Why](start-with-why.md) — lead with purpose before approach or output.
- [A Plan Is Not a Strategy](plan-is-not-a-strategy.md) — strategy is an integrative set of
  choices (where to play / how to win), not a controllable list of initiatives.
- [Principal Engineer Influence](principal-engineer-influence.md) — your words signal
  strategy; give feedback early and privately so forums validate rather than surprise.
- [Raising Problems Without Complaining](raising-problems-without-complaining.md) — managing up:
  raise blockers so they signal ownership, not a collaboration gap; "what's my move here?"
- [The New Leader's Credibility Problem](new-leader-credibility.md) — a new leader's diagnosis
  won't be believed; earn credibility by listening ("find the mystery") and a communication cascade.

## Running the decision — facilitation

- [Facilitating Technical Decisions](decision-facilitation.md) — high signal / low noise;
  the decision frame; facilitate rather than lecture.
- [Architecture Decision Forum](architecture-decision-forum.md) — the advisory body that
  governs high-blast-radius decisions without becoming a gatekeeper.
- [Agile Design Decisions and Principles](../engineering/architecture/agile-design-decisions.md) — the
  decision frameworks (reversibility, blast radius, delegation) the forum and facilitation
  put into practice.
- [First-Principles Thinking](first-principles-thinking.md) — framing the problem before deciding:
  strip inherited assumptions, separate hard from soft limits, reason forward from what holds.
- [Designing with Constraints](designing-with-constraints.md) — the complement: impose deliberate
  constraints (one-pager, separable core tech, one defining constraint) to collapse decision space.

## People & change

- [Protecting Mavericks](protecting-mavericks.md) — letting unconventional talent flourish
  without letting disruption damage the team.
- [Managed Disruption](managed-disruption.md) — introducing change into delivery safely and
  deliberately.
- [Team Topologies and Socio-Technical Architecture](../engineering/architecture/team-topologies.md) —
  shaping teams as a design material: Conway's Law, the four team types, and cognitive load as the
  binding constraint *(in architecture)*.
- [The Learning Organisation and AI Adoption](learning-organisation.md) — the cultural
  prerequisites (psychological safety, slack, intelligent failure) that let teams absorb new
  technology faster than it changes.
- [Revised Rules of Engineering Leadership](revised-rules-engineering-leadership.md) — how
  leadership shifts when AI makes execution cheap: durable teams and fast, good decisions become
  the scarce goods (bridges to the AI-native cluster).
- [The Product Engineer Company (Portkey)](../case-studies/portkey-product-engineer-company.md) —
  a case study of the no-PM, end-to-end-ownership operating model: barbell teams, disciplined
  scope, and AI in reliability-critical work *(in case studies)*.

## The through-line

Leadership here is **advisory, not authoritarian**: set direction through purpose and clear
signals, facilitate decisions the group owns, govern only the choices whose blast radius
demands it, and protect the people who drive change. Much of the
[AI-native engineering](../engineering/practices/ai-native-engineering-overview.md) operating model rests on these
practices — Intent Specs are *start with the why*; the governance forum is a *constraint
authority*; Principals become *orchestrators*.
