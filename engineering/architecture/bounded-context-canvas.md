---
title: Bounded Context Canvas
tags: [architecture, system-design, microservices, reading]
topic: engineering/architecture
status: notes
level: intermediate
related:
  - engineering/architecture/micro-frontend-canvas.md
  - engineering/architecture/micro-frontend-principles.md
  - engineering/architecture/composable-architecture.md
  - engineering/architecture/architectural-change-cases.md
  - engineering/architecture/ddd-strategic-design.md
source: "https://github.com/ddd-crew/bounded-context-canvas"
updated: 2026-06-20
---

# Bounded Context Canvas

The Bounded Context Canvas, from the [DDD Crew](https://github.com/ddd-crew/bounded-context-canvas),
is a collaborative single-page tool for designing **one bounded context** in
Domain-Driven Design. It forces a team to make explicit the choices that usually
stay fuzzy — a context's name, purpose, responsibilities, interfaces, and language
— so the design can be challenged and aligned on before it is embedded in code.
It is inspired by Strategyzer's Business Model Canvas, and licensed CC-BY-4.0.

A **bounded context** is the core DDD unit of boundary: the scope within which a
particular domain model and its **ubiquitous language** are consistent and valid.
The canvas is the artifact for designing that scope deliberately.

## The canvas sections

| Section | What it captures |
|---|---|
| **Name** | The context's identity — how it will be framed and referred to |
| **Purpose** | Why and what of the context, in business language |
| **Strategic classification** | Importance (core / supporting / generic), business role (revenue, engagement, compliance…), and evolution stage (genesis → custom → product → commodity, per Wardley Maps) |
| **Domain roles** | Behavioural archetype — how the context functions (e.g. analysis vs execution), referencing Brandolini and Wirfs-Brock |
| **Inbound communication** | Messages received from collaborators — commands, queries, events — and the relationship type with each |
| **Outbound communication** | Messages this context initiates toward other collaborators |
| **Ubiquitous language** | The key domain terms and definitions specific to this context |
| **Business decisions** | The core rules and policies the context enforces |
| **Assumptions** | Design assumptions made with incomplete information, made explicit |
| **Verification metrics** | Measurable signals of boundary fitness, from CI/CD, project tools, or production telemetry |
| **Open questions** | Unresolved uncertainties, with the team's confidence level |

## How to run it

- Complete the sections **in order** for a structured first pass, or work
  **outside-in** (start from communication) or **inside-out** (start from business
  rules), depending on what the team knows.
- Treat it as collaborative and iterative — the value is in making design elements
  **visible for critique** rather than in filling boxes.
- An **alternative format** uses *use-case swimlanes* — organising communication as
  `message in → decision(s) made → message(s) out` — which lines up with flow-based
  modelling such as EventStorming and Domain Message Flow Modelling.

## Grounding

The canvas draws on Eric Evans' DDD (bounded context, ubiquitous language), Martin
Fowler's *Bounded Context*, Wardley Maps (evolution classification), and the DDD
Crew's Core Domain Charts (strategic importance). Contributors include Kenny
Baas-Schwegler, Kim Lindhard, Michael Plöd, and Maxime Sanglan-Charlier. Editable
templates exist for Miro, draw.io, Excalidraw, and Lucidchart, plus a
version-controllable HTML form.

## Relationship to other notes

- [The Micro-Frontend Canvas](micro-frontend-canvas.md) — the **UI-layer sibling**.
  Both are single-page canvases for designing one boundary before coding; this one
  works at the **domain / service** layer, the micro-frontend canvas at the
  **frontend** layer. The micro-frontend canvas asks whether a *corresponding
  backend boundary* exists — the Bounded Context Canvas is the tool for designing
  that boundary.
- [Microfrontend Architecture Principles](micro-frontend-principles.md) — its first
  principle, *bounded contexts*, is the concept this canvas operationalises at the
  domain level.
- [Composable Architecture](composable-architecture.md) — packaged business
  capabilities and backend-for-frontends are composed from well-drawn bounded
  contexts; the canvas is how you draw one.
- [Architectural Change Cases](architectural-change-cases.md) — a fellow structured,
  living design artifact; both surface decisions early and are revisited as the
  system evolves. The canvas's *assumptions* and *open questions* are where future
  change cases often originate.
