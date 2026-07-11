---
type: overview
title: Engineering Leadership — Overview
description: "A map of the notes on senior-engineer leadership, communication, and decision governance — how to set direction and make good decisions with other people."
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
  - leadership/all-hands-meetings.md
  - leadership/managing-sideways.md
  - leadership/revised-rules-engineering-leadership.md
  - engineering/architecture/team-topologies.md
  - leadership/scaling-engineering-org.md
  - case-studies/portkey-product-engineer-company.md
  - leadership/senior-ic-role.md
  - leadership/engineering-manager-role.md
updated: 2026-06-27
---

# Engineering Leadership — Overview

A map of the notes on senior-engineer leadership, communication, and decision governance —
how to set direction and make good decisions with other people.

## Purpose & influence — setting direction

- [Start with the Why](start-with-why.md) — lead with purpose before approach or output.
- [A Plan Is Not a Strategy](plan-is-not-a-strategy.md) — strategy is an integrative set of
  choices (where to play / how to win), not a controllable list of initiatives.
- [The Senior IC Role](senior-ic-role.md) — what Staff/Principal/Architect ICs actually do
  (cross-team improvements, technical direction, leading initiatives, growing leaders) and why
  it is leadership through influence, not authority.
- [Principal Engineer Influence](principal-engineer-influence.md) — your words signal
  strategy; give feedback early and privately so forums validate rather than surprise.
- [Raising Problems Without Complaining](raising-problems-without-complaining.md) — managing up:
  raise blockers so they signal ownership, not a collaboration gap; "what's my move here?"
- [The New Leader's Credibility Problem](new-leader-credibility.md) — a new leader's diagnosis
  won't be believed; earn credibility by listening ("find the mystery") and a communication cascade.
- [Running an Effective All-Hands](all-hands-meetings.md) — the all-hands as the venue that
  counters information decay past ~50 people: a consistent three-act format, quarterly cadence,
  no live Q&A, and delegating the stage to direct reports.

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

- [The Engineering Manager Role](engineering-manager-role.md) — the management-track role
  definition: four pillars (people, technical, product, delivery leadership) and the manager's
  core job of removing obstacles; the sibling to [The Senior IC Role](senior-ic-role.md).
- [Protecting Mavericks](protecting-mavericks.md) — letting unconventional talent flourish
  without letting disruption damage the team.
- [Managed Disruption](managed-disruption.md) — introducing change into delivery safely and
  deliberately.
- [Managing Sideways](managing-sideways.md) — driving change across peer teams you don't control:
  why authority fails, the adoption-without-a-mandate play (recruit the first mover, let results
  recruit the next), and treating resistance as fear rather than flawed logic.
- [Team Topologies and Socio-Technical Architecture](../engineering/architecture/team-topologies.md) —
  shaping teams as a design material: Conway's Law, the four team types, and cognitive load as the
  binding constraint *(in architecture)*.
- [Scaling an Engineering Organisation (20/50/200)](scaling-engineering-org.md) — how structure
  changes as headcount grows: the coordination tax, ownership close to the work, when a platform
  team is worth it, on-call as the maturity diagnostic, and why AI magnifies ownership.
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
[AI-native engineering](../engineering/ai-native/ai-native-engineering-overview.md) operating model rests on these
practices — Intent Specs are *start with the why*; the governance forum is a *constraint
authority*; Principals become *orchestrators*.
