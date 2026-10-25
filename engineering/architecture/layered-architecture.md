---
type: note
title: Layered Architecture
description: "The five-layer separation (domain, application, infrastructure, interface, repository) with dependencies flowing inward — and the horizontal-to-vertical shift that keeps it from producing God-modules as a system grows."
tags: [architecture, system-design, refactoring, reading]
topic: engineering/architecture
status: notes
level: intermediate
related:
  - concepts/clean-code-and-solid.md
  - engineering/architecture/enforced-architecture-rules.md
  - engineering/architecture/skeleton-architecture.md
  - engineering/architecture/change-locality.md
  - engineering/architecture/ddd-strategic-design.md
  - engineering/architecture/composable-architecture.md
  - engineering/architecture/over-engineering.md
  - engineering/practices/software-design-principles.md
  - engineering/architecture/comprehension-as-architecture.md
  - engineering/architecture/agile-design-decisions.md
  - engineering/architecture/llm-platform-engineering.md
  - engineering/architecture/functional-core-imperative-shell.md
source: "https://mikehuls.com/layered-architecture-for-building-readable-robust-and-extensible-apps/"
updated: 2026-10-26
---

# Layered Architecture

Mike Huls (January 2026) starts from a symptom rather than a principle:

> "Adding a feature means performing open-heart surgery on the application, modifying existing
> business logic rather than extending the system."

The claim is that this is **structural rather than qualitative** — not code that needs tidying,
but a system with no place to put a new thing. Layering gives it one.

**The pattern is long-established** and these notes should say so: this is the family that
includes Cockburn's ports and adapters, Palermo's onion architecture and Martin's Clean
Architecture. Huls acknowledges drawing on DDD, SOLID and onion/hexagonal thinking but cites no
sources. What the piece contributes is a **concrete articulation with a worked example** (Python
— Pydantic and dataclasses — though nothing in the structure is Python-specific) and the
vertical-slicing caveat below. Filed here because these notes repeatedly reference layer rules
and dependency direction without ever defining the layers.

## The five layers

| Layer | What belongs in it |
|---|---|
| **Domain** | Business constraints and data shapes, as strict models. Concerned with *meaning, not orchestration* |
| **Application** | "The heart of the system" — orchestrates workflows, coordinates domain models and repositories, and handles application-level failures independently of infrastructure |
| **Infrastructure** | Tools the application layer calls: logging, crypto, HTTP clients, email senders. **No business logic** |
| **Interface** | The gateway for everything external — HTTP APIs, CLIs, queue consumers. Validate input, call the application layer, format the response |
| **Repository** | Persistence abstracted away — databases, SQL, schemas — so application logic stays database-agnostic |

The organising constraint is that **dependencies flow inward**, which keeps business logic
independent of frameworks. The interface layer knows about the application layer; the domain
knows about neither.

Two terms from the worked example worth keeping, because they name the shape of a correct
implementation:

- **Composition root** — a single place (`main.py` in his example) where concrete dependencies
  are assembled and injected. Everything else receives what it needs rather than constructing it.
- **Thin adapter** — what an endpoint becomes once the logic moves inward. His framing of the
  before state is the useful half: the endpoint had been **"a God-function"**, and the refactor
  turns it into a thin adapter that translates and delegates.

## The horizontal-to-vertical shift

The part that makes this more than a restatement, and the reason to keep the note.

> "Horizontal layering improves structure; vertical slicing by domain improves scalability. The
> rules are not about restriction or purity but act as guard rails to preserve architectural
> intent over time and keep the system understandable as it grows."

Layers alone are a *horizontal* cut. Applied to a growing system they produce the failure they
were meant to prevent: one `services/` directory accumulating every workflow in the product, one
`repositories/` holding every table. The fix is to slice **vertically by domain first** and layer
*within* each slice.

Three rules hold that together:

| | Rule |
|---|---|
| 1 | Domains do not import each other's internals |
| 2 | Shared concepts go in a `shared` domain |
| 3 | Dependencies flow inward **inside each slice** |

His justification for having rules at all is the sentence worth carrying: *"without some basic
rules the architecture collapses quietly."* The quiet part is the problem — nothing fails when a
boundary is crossed once, so the decay produces no signal until a change that should have been
local is not. That is the same silent-failure shape as
[Comprehension as an Architectural Characteristic](comprehension-as-architecture.md), and the
reason [Enforced Architecture Rules](enforced-architecture-rules.md) argues for making the
crossing fail a build rather than a review.

## What the piece does not address

Recorded because it bounds the advice: **there is no discussion of when this is too much
structure.** Five layers plus vertical slices is a substantial amount of ceremony, and the
article offers no guidance on the size or stage at which it starts paying for itself — the
problem statement assumes a system already painful to change. Read against
[Over-Engineering Is Solving the Wrong Problem](over-engineering.md), which argues that
structure should be justified by constraints rather than adopted on principle, and
[Agile Design Decisions](agile-design-decisions.md)'s emergent-design position: add structure
when it pays for itself. A small application given all five layers on day one has bought the
cost without the condition that makes it worthwhile.

## Relationship to other notes

- [Clean Code and SOLID](../../concepts/clean-code-and-solid.md) — that note distinguishes Clean
  Code from Clean Architecture ("system boundaries, dependency direction, domain isolation,
  framework independence") in a comparison table and points forward without a destination. This
  is the destination: the architecture half, set out concretely.
- [Enforced Architecture Rules for Agents and Humans](enforced-architecture-rules.md) — the
  mechanical counterpart, and the pairing worth reading together. Tune's package/layer/role tiers
  are *how you stop* the three rules above being violated; this is *what they encode*. Neither
  note is complete without the other: rules without a pattern enforce nothing in particular, and
  a pattern without enforcement collapses quietly.
- [Skeleton Architecture](skeleton-architecture.md) — the same dependency-direction discipline
  aimed specifically at constraining generated code, via base classes and compile-time topology
  checks rather than directory conventions.
- [Domain-Driven Design: Strategic Design](ddd-strategic-design.md) — where the vertical slices
  come from. Rule 1 (domains do not import each other's internals) is a bounded-context boundary
  expressed as an import constraint, and rule 2's `shared` domain is close to DDD's shared kernel.
- [Change Locality and Boundary Drift](change-locality.md) — the property vertical slicing buys:
  understanding needed for a change proportional to its scope. God-modules are that property lost.
- [Composable Architecture](composable-architecture.md) — layering within a service; that note
  handles composition *between* services (gateways, BFFs, packaged business capabilities).
- [Software Design Principles](../practices/software-design-principles.md) — the code-level
  analogue. Dependency inversion at service boundaries is this pattern's central rule applied one
  altitude down.
