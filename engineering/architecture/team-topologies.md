---
title: Team Topologies and Socio-Technical Architecture
tags: [architecture, system-design, leadership, culture]
topic: engineering/architecture
status: notes
level: intermediate
related:
  - engineering/architecture/ddd-strategic-design.md
  - engineering/architecture/event-storming.md
  - engineering/architecture/bounded-context-canvas.md
  - engineering/architecture/micro-frontend-principles.md
  - engineering/architecture/composable-architecture.md
  - concepts/devops-capability-model.md
  - engineering/practices/team-topologies-agentic-platform.md
  - leadership/engineering-leadership-overview.md
  - leadership/learning-organisation.md
  - reading/what-is-software-engineering-ai.md
source: "Skelton & Pais — Team Topologies (2019); Conway (1968)"
updated: 2026-06-21
---

# Team Topologies and Socio-Technical Architecture

A system's architecture and the organisation that builds it are two views of the same thing.
**Socio-technical architecture** treats team structure as a first-class design material:
boundaries, communication paths, and cognitive load are architectural decisions, not HR ones.
*Team Topologies* (Matthew Skelton & Manuel Pais) is the best-known model for designing them
deliberately.

## Conway's Law and the inverse manoeuvre

> "Organizations… are constrained to produce designs which are copies of the communication
> structures of these organizations." — Melvin Conway, 1968

Because teams ship their communication structure, you get the architecture your org chart implies
whether you intend to or not. The **inverse Conway manoeuvre** turns this into a tool: deliberately
shape teams to match the architecture you *want*. This is why team boundaries should track
[bounded contexts](ddd-strategic-design.md) — a context owned by two teams fractures; a team owning
two contexts blurs them. It is also the organisational case for
[loosely coupled architecture and empowered teams](../../concepts/devops-capability-model.md) —
two of the Accelerate capabilities.

## The four fundamental team types

Team Topologies reduces the zoo of team labels to four:

| Team type | Purpose |
|---|---|
| **Stream-aligned** | The default. Owns a fast flow of work for one product/service/journey, end to end. Most teams should be this. |
| **Platform** | Provides internal self-service capabilities (golden paths) that reduce stream-aligned teams' cognitive load. |
| **Enabling** | Specialists who coach stream-aligned teams to adopt a missing capability, then step back. Temporary by design. |
| **Complicated-subsystem** | Owns a part needing rare, deep expertise (e.g. a pricing engine, video codec) so other teams don't have to. |

## The three interaction modes

How teams interact is also designed, not left to chance:

- **Collaboration** — two teams work closely for a defined period to discover something new.
  High bandwidth, but expensive; meant to be temporary.
- **X-as-a-Service** — one team consumes another's capability through a clean interface, with
  minimal collaboration. The steady state for platform consumption.
- **Facilitating** — an enabling team helps another remove an obstacle. The mode that moves a
  team from collaboration to X-as-a-Service.

A common pattern: teams **collaborate** to define a boundary, then settle into **X-as-a-Service**
once the interface stabilises.

## Cognitive load and fracture planes

The binding constraint is **team cognitive load**: a team can only own as much domain as it can
hold in its head. When a team's load is too high, quality and flow degrade — the same ceiling on
[sustainable pace](../practices/agile-in-the-age-of-ai.md) that applies to individuals. The remedy
is to split along **fracture planes** — natural seams (bounded context, regulatory boundary, change
cadence, risk profile) where a system divides cleanly. Bounded contexts and good
[micro-frontend/micro-service boundaries](micro-frontend-principles.md) are fracture planes.

## Relationship to other notes

- [DDD Strategic Design](ddd-strategic-design.md) and [Bounded Context Canvas](bounded-context-canvas.md)
  — supply the *technical* boundaries; team topologies aligns *team* boundaries to them. They are the
  two halves of the inverse Conway manoeuvre.
- [Microfrontend Architecture Principles](micro-frontend-principles.md) — team autonomy and
  independent deployability are Conway's Law applied at the frontend boundary.
- [The DevOps Capability Model](../../concepts/devops-capability-model.md) — "loosely coupled
  architecture" and "empowered teams" are the capabilities team topologies operationalises.
- [Engineering Leadership — Overview](../../leadership/engineering-leadership-overview.md) and
  [The Learning Organisation](../../leadership/learning-organisation.md) — the leadership and
  cultural side of shaping teams *(in leadership)*.
