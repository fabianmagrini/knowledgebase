---
title: "Domain-Driven Design: Strategic Design"
tags: [architecture, system-design, microservices, reading]
topic: engineering/architecture
status: notes
level: intermediate
related:
  - engineering/architecture/bounded-context-canvas.md
  - engineering/architecture/composable-architecture.md
  - engineering/architecture/micro-frontend-principles.md
  - engineering/architecture/thinking-in-constraints.md
  - engineering/architecture/event-storming.md
  - engineering/architecture/team-topologies.md
source: "https://medium.com/@lambrych/domain-driven-design-ddd-strategic-design-explained-55e10b7ecc0f"
updated: 2026-06-20
---

# Domain-Driven Design: Strategic Design

**Strategic design** is the half of Domain-Driven Design (after Eric Evans) that
works in the **problem space** — high-level domain analysis, abstracted from code,
concerned with business priorities and conceptual boundaries. **Tactical design**
is the move toward the **solution space**: code-level patterns and model
implementation. The **bounded context** is the vehicle that carries a model from
one to the other. The distinctive claim of DDD is that good boundaries are a
**socio-technical** problem — the work of teams collaborating with domain experts,
not just a technical decomposition.

## Subdomains: where to invest

A domain is partitioned into **subdomains**, each a distinct area of knowledge with
a business goal and a level of strategic importance. The type decides how much
custom effort it deserves:

| Subdomain type | What it is | Build strategy |
|---|---|---|
| **Core domain** | The single primary competitive advantage — "your business" | Invest heavily; build in-house; cannot be commoditised |
| **Supporting** | Important but non-differentiating | Custom but lightweight; can be outsourced |
| **Generic** | Common to any organisation (e.g. payroll) | Buy off-the-shelf; do not build |

The governing question to ask constantly is **"what is the core?"** — it keeps the
model from bloating and directs effort where it actually differentiates the
business. (This is the same core/supporting/generic axis the
[Bounded Context Canvas](bounded-context-canvas.md) records under *strategic
classification*.)

## Bounded context and ubiquitous language

A **bounded context** is the linguistic and semantic boundary around a specific
model — the scope within which a **ubiquitous language** (the shared vocabulary of
team and domain experts, expressed directly in the model) is consistent and valid.
The same word can mean different things in different contexts; the boundary is what
makes each meaning unambiguous. Without deliberate boundaries the model degrades
into a **big ball of mud** — one large, highly interconnected model with no rational
segmentation. Strategic design is the act of *taming* that with bounded contexts.

> Subdomains live in the **problem space** (the business as it is); bounded contexts
> live in the **solution space** (the models you choose to build). They often align
> one-to-one, but need not.

## Context mapping

Once there are several bounded contexts, **context mapping** describes how they
relate and communicate — and, crucially, treats **team collaboration as a
first-class design concern**. Each relationship pattern is as much an organisational
choice as a technical one:

| Pattern | Relationship |
|---|---|
| **Partnership** | Two teams integrate closely and succeed or fail together, as one combined system |
| **Shared kernel** | Teams share a subset of the model, with the cost of tight coordination on it |
| **Customer–supplier** | Upstream/downstream with a clear dependency direction; supplier accommodates the customer |
| **Conformist** | Downstream team simply adopts the upstream model as canonical |
| **Anticorruption layer (ACL)** | A translation layer isolates a context from another's model, preventing coupling |
| **Open host service (OHS)** | A context exposes a defined service/protocol for many consumers |
| **Published language** | A well-documented shared language/protocol for integration (often paired with OHS) |
| **Separate ways** | No integration — the contexts deliberately do not share a model |

**Domain events** are the asynchronous glue: a context emits an event, and others
subscribe and react, sharing information without direct coupling.

## Why it matters

Strategic design decides the boundaries everything else inherits — service and
team topologies, where to invest, and how teams depend on one another. Because the
context-map patterns *are* team relationships, an architecture that ignores them
ends up fighting the organisation. This is the same insight as Conway's Law in
[Thinking in Constraints](thinking-in-constraints.md): team boundaries are an
architectural constraint, and the context map is where you make them explicit.

## Relationship to other notes

- [Bounded Context Canvas](bounded-context-canvas.md) — the **tool** that designs
  *one* bounded context in detail; this note is the **theory** of the wider
  strategic landscape it sits in.
- [Composable Architecture](composable-architecture.md) — packaged business
  capabilities and BFFs are bounded contexts realised as deployable backend units.
- [Microfrontend Architecture Principles](micro-frontend-principles.md) — its first
  principle, *bounded contexts*, is strategic design applied at the frontend layer.
- [Thinking in Constraints](thinking-in-constraints.md) — Conway's Law and team
  topology as the organisational constraints that context mapping makes visible.
