---
title: Architectural Change Cases
tags: [architecture, system-design, reading]
topic: engineering/architecture
status: notes
level: intermediate
related:
  - engineering/architecture/adr.md
  - engineering/architecture/agile-design-decisions.md
  - engineering/architecture/strangler-fig.md
  - engineering/architecture/composable-architecture.md
  - engineering/practices/change-absorption-capacity.md
  - engineering/architecture/micro-frontend-canvas.md
source: "https://www.infoq.com/articles/architectural-change-cases/"
updated: 2026-06-14
---

# Architectural Change Cases

Architectures decay as business needs, technologies, and operating environments shift. An
**architectural change case** is a tool for anticipating that pressure: it identifies a potential
change to a solution's assumptions that may significantly affect the architecture. Where an ADR
*documents a decision*, a change case *articulates a possibility* — contingency planning without
prescribing a solution up front. The stance is that architecture is inherently unfinished, not
because the plan is incomplete but because external conditions keep shifting.

## Why structure the speculation

- **Change is inevitable.** Treating future change as trivially reversible invites costly
  retrofitting later.
- **Speculation needs structure.** Change cases turn endless "what-ifs" into a bounded set of
  realistic scenarios with estimated cost and reversibility.
- **Validate empirically.** Naming a change case is not enough; small experiments reveal its
  magnitude and cost without building whole alternatives.
- **Surface hidden assumptions.** Change cases expose fragility in decisions made under MVP time
  pressure or when adopting a major dependency.

## Anatomy of a change case

| Component | Content |
|---|---|
| Trigger | A potential shift in a quality attribute requirement (QAR) or business assumption |
| Likelihood | A probability estimate |
| Affected decisions | Which decisions would need revision if the assumption proves invalid |
| Cost | A forecast using **t-shirt sizing** (S, M, L, XL) |
| Options | Alternative resolutions |

### When to write one

- Introducing a major dependency.
- Adopting AI-generated code.
- Hardcoding business rules.
- Optimising for rapid MVP delivery.
- Coupling to an external platform.
- Knowingly accepting a scalability or maintainability trade-off.

## Five classes of change case

| Class | Example trigger |
|---|---|
| External interface change | A third-party API evolves, forcing synchronised modifications |
| Subsystem replacement | Vendor failure or an open-source project being cancelled |
| Infrastructure shift | Datacentre migration, cloud adoption, latency changes |
| Business-model transformation | A failed MVP or market invalidation |
| Security vulnerability | A new weakness emerging from external factors |

## Identifying and validating

- **Identification:** pre-mortem reviews (imagine the architecture has failed; work backwards)
  and Chaos Monkey-style fault injection.
- **Validation:** run architectural experiments to get empirical data without building complete
  alternatives, and use **fitness functions** to baseline QARs and measure improvement. Extrapolate
  the measured effort across the larger implementation to size the change.

The trade-off is speculation cost vs. future flexibility: invest in modularity and decoupling
where a change case is plausible, but avoid over-engineering for unlikely scenarios — let
experiments calibrate how much effort is warranted.

## AI-specific mitigations

- Maintain repositories of **AI context artifacts** — requirements, specifications, code samples,
  acceptance tests — so generation can be reproduced.
- Define **reproducibility change cases** for different AI versions or providers.
- Anticipate external-system interface evolution as a first-class change case.

## Positioning

The article places change cases alongside established practice:

- **ADRs** — change cases extend ADR thinking by examining evolution over time rather than a
  single decision.
- **ATAM** (Architecture Tradeoff Analysis Method) — assesses *current* QAR alignment; change
  cases assess *future* evolution.
- **Continuous / Evolutionary Architecture** and **fitness functions** — the broader school that
  treats change pressure as inevitable and measurable.
- **Minimum Viable Architecture (MVA)** — should incorporate change-case success criteria, not
  only the immediate business solution.

> Example: an insurance company's vacation-rental MVP wrote change cases for 50% higher adoption
> (scalability failure), expansion to RV/boat cover (exceeding the parent underwriter's capacity),
> and multi-state regulatory shifts. These revealed that the assumed reuse of the parent's
> underwriting system was invalid, pointing to an independent system instead.

## Relationship to other notes

- [Architectural Decision Records (ADRs)](adr.md) — change cases extend ADRs forward in time:
  the ADR captures the decision, the change case captures how it might have to change.
- [Agile Design Decisions and Principles](agile-design-decisions.md) — the reversibility and
  blast-radius lens applied to *speculative future* changes rather than the present decision.
- [Strangler Fig Pattern](strangler-fig.md) — a concrete resolution a subsystem-replacement or
  business-model change case might call for.
- [Composable Architecture](composable-architecture.md) — the modularity and decoupling that make
  many change cases cheap to resolve.
- [Change Absorption Capacity (CATS)](../practices/change-absorption-capacity.md) — the
  reproducibility change cases for AI-generated code are one facet of keeping a system able to
  absorb AI-driven change.
