---
title: Architecture — Overview
tags: [meta, architecture, system-design]
topic: engineering/architecture
status: complete
related:
  - engineering/architecture/c4-model.md
  - engineering/architecture/composable-architecture.md
  - engineering/architecture/micro-frontend-canvas.md
  - engineering/architecture/agile-design-decisions.md
  - engineering/architecture/adr.md
  - engineering/architecture/architectural-change-cases.md
  - engineering/architecture/design-systems-ai-control-plane.md
  - leadership/architecture-decision-forum.md
  - engineering/architecture/strangler-fig.md
  - engineering/architecture/thinking-in-constraints.md
  - engineering/architecture/generative-ui.md
  - engineering/architecture/micro-frontend-principles.md
  - engineering/architecture/bounded-context-canvas.md
  - engineering/architecture/ddd-strategic-design.md
  - engineering/architecture/event-storming.md
  - engineering/architecture/team-topologies.md
updated: 2026-06-20
---

# Architecture — Overview

A map of the architecture notes — how to *describe*, *shape*, *decide*, and *constrain*
systems.

## Describing systems

- [C4 Model](c4-model.md) — four-level diagramming (context → container → component → code).

## Shaping systems

- [Composable Architecture](composable-architecture.md) — packaged business capabilities,
  API gateway/BFF, journey APIs, GraphQL federation.
- [The Micro-Frontend Canvas](micro-frontend-canvas.md) — a single-page tool for deciding and
  validating micro-frontend boundaries (capability, ownership, communication) before coding.
- [Domain-Driven Design: Strategic Design](ddd-strategic-design.md) — the problem-space theory:
  subdomains (core/supporting/generic), bounded contexts, ubiquitous language, and the eight
  context-mapping patterns.
- [Event Storming](event-storming.md) — the collaborative discovery workshop that feeds DDD:
  map domain events on a wall, and the clusters reveal candidate bounded contexts.
- [Team Topologies and Socio-Technical Architecture](team-topologies.md) — the organisational
  mirror of the architecture: Conway's Law, the four team types, interaction modes, and aligning
  team boundaries to bounded contexts (the inverse Conway manoeuvre).
- [Bounded Context Canvas](bounded-context-canvas.md) — the DDD domain/service-layer sibling: a
  single-page canvas for designing one bounded context (purpose, language, communication, decisions).
- [Microfrontend Architecture Principles](micro-frontend-principles.md) — the principles a good
  boundary must satisfy at scale (bounded contexts, autonomy, contracts, independent deploy).
- [Strangler Fig Pattern](strangler-fig.md) — modernise legacy incrementally behind a
  facade, without a big-bang rewrite.
- [Design Systems as the AI Control Plane](design-systems-ai-control-plane.md) — the design
  system as constraint layer and platform for AI-generated UI.
- [Generative UI](generative-ui.md) — producing UI with AI at build time (generated code) and
  run time (LLM-assembled interfaces from a whitelisted component registry).

## Deciding & recording

- [Agile Design Decisions and Principles](agile-design-decisions.md) — continuous design;
  reversibility (one-way / two-way doors) and blast-radius frameworks; emergent
  architecture; technical debt as a tool.
- [Architectural Decision Records (ADRs)](adr.md) — lightweight, version-controlled records
  of significant decisions.
- [Architectural Change Cases](architectural-change-cases.md) — extend ADRs forward in time:
  structured speculation about how decisions might have to change, with cost and reversibility.
- [Architecture Decision Forum](../../leadership/architecture-decision-forum.md) — the advisory
  body where cross-cutting decisions are made and logged as ADRs *(in practices)*.

## Constraining systems

- [Thinking in Constraints](thinking-in-constraints.md) — surface, classify, and
  challenge the boundary conditions (business, regulatory, technical, operational,
  organisational, NFRs) that bound the solution space before any design is chosen.

## The through-line

Describe with C4, shape with composable + design-system primitives, decide with the
reversibility/blast-radius frameworks within explicit constraints, and record in ADRs
ratified through the decision forum. The decision-making side connects to the
[engineering leadership overview](../../leadership/engineering-leadership-overview.md); the
AI-era constraints connect to the
[AI-native engineering overview](../practices/ai-native-engineering-overview.md).
