---
title: The Micro-Frontend Canvas
tags: [architecture, system-design, reading]
topic: engineering/architecture
status: notes
level: intermediate
related:
  - engineering/architecture/composable-architecture.md
  - engineering/architecture/architectural-change-cases.md
  - engineering/architecture/agile-design-decisions.md
  - engineering/architecture/design-systems-ai-control-plane.md
  - engineering/practices/engineering-playbook.md
  - engineering/architecture/generative-ui.md
source: "https://lucamezzalira.medium.com/the-micro-frontend-canvas-a-practical-tool-for-better-boundaries-99da1a7b858d"
updated: 2026-06-19
---

# The Micro-Frontend Canvas

Luca Mezzalira argues that most micro-frontend failures come not from technical inadequacy but
from **skipped design phases**: teams jump to implementation without deciding boundaries,
ownership, and communication, producing systems that look independent but stay tangled
underneath. The canvas forces those decisions before they become costly code. As he puts it,
"the architecture was just doing its job: surfacing a misalignment nobody designed away."

## The canvas

A structured, single-page artifact capturing the key decisions for **one** micro-frontend (one
canvas per micro-frontend). It is used in two modes:

- **Planning mode** — establish alignment before coding to prevent costly rework.
- **Assessment mode** — audit a struggling existing system against the same questions.

A useful side effect: it **depersonalises critique** by directing discussion at the design rather
than at individuals.

### The seven sections

| Section | What it decides |
|---|---|
| **Business capability** | Which business subdomain this represents — not merely which UI it renders |
| **Boundaries validation** | Whether the boundary is appropriately sized and genuinely independent |
| **Dependencies** | What it requires — in particular whether a corresponding backend boundary exists |
| **Communication methodology** | Inter-micro-frontend patterns, contracts, testing, and ownership |
| **Governance and observability** | Production ownership, performance standards, shared-dependency management |
| **Quality guardrails** | The standards that are actually enforced |
| **Challenges and risks** | Likely problems, named while the design can still absorb them |

These are not narrowly technical questions — they are decisions about ownership, alignment, and
trade-offs.

### Example: the checkout boundary

Checkout owns the cart, payment, and order-confirmation flow, and needs product price and
availability. The boundaries-validation decision: checkout calls **its own backend-for-frontend**,
which aggregates pricing, rather than importing from the catalog micro-frontend. That avoids the
most common hidden dependency in e-commerce — checkout silently importing formatting helpers from
catalog — before the coupling is embedded.

## When micro-frontends are justified

Only three situations genuinely justify them:

1. **Scaling teams** — a monolithic frontend has become a deployment bottleneck.
2. **Business-capability alignment** — boundaries follow business domains (checkout, profiles,
   dashboards), not code abstractions.
3. **Risk isolation** — a failure affects one module, not the whole system.

If none apply, "a well-structured monolith or a modular monolith is very likely the better
choice."

## How to run it

- Hold a brief boundary-identification session with cross-functional stakeholders.
- Complete the canvas **asynchronously** rather than in a long workshop (one large financial
  organisation found the async-first approach better).
- Treat it as a **living document** — revisit when friction emerges, business direction shifts, or
  new features stress existing boundaries. Boundaries are situational, not eternal; correctness is
  relative to a moment in time.

## Grounding and the AI angle

The canvas aligns with **Domain-Driven Design** (business capabilities, bounded contexts),
**Team Topologies** (socio-technical alignment of team structure and architecture), and systems
thinking (architecture surfaces organisational misalignment).

In the 2026 framing, a filled-in canvas is "exactly the input modern development now runs on":
precise boundary decisions feed AI coding assistants and stop them defaulting to patterns that
dissolve boundaries — cross-imports, shared global stores, fat contracts. Mezzalira references
complementary **boundary-protection skills** that keep AI-generated code aligned with the designed
boundaries. The canvas is released under Creative Commons for non-commercial use.

## Anti-patterns

- Jumping to implementation without a design phase.
- Apparent independence that hides real dependencies.
- Undefined ownership of the composite application.
- "Shared" resources that are not actually shared consistently across teams.
- Assuming tooling solves what is really an organisational problem.

The canvas gives shared language and structure, but it does **not** replace judgement about
trade-offs in a specific political and technical context — that remains the harder problem.

## Relationship to other notes

- [Composable Architecture](composable-architecture.md) — the paradigm (PBCs, BFF) the canvas
  designs within; the checkout/BFF decision is composable thinking applied to a boundary.
- [Architectural Change Cases](architectural-change-cases.md) — a sibling structured design
  artifact; both force decisions before they become code, and both are living documents.
- [Agile Design Decisions and Principles](agile-design-decisions.md) — the reversibility and
  blast-radius lens behind "boundaries are situational, not eternal".
- [Design Systems as the AI Control Plane](design-systems-ai-control-plane.md) — the canvas's
  boundary-protection skills are the micro-frontend analogue of the design system as a constraint
  layer for AI-generated code.
- [Modern Web Engineering Playbook](../practices/engineering-playbook.md) — the broader web
  engineering context in which micro-frontends and BFFs sit.
