---
title: The DevOps Capability Model (Accelerate / DORA)
tags: [ci-cd, testing, culture, observability, reading]
topic: concepts
status: notes
level: intermediate
related:
  - concepts/continuous-delivery.md
  - engineering/practices/trunk-based-development.md
  - engineering/practices/ci-cd-ai-engineering.md
  - engineering/practices/engineering-playbook.md
  - engineering/practices/apex-framework.md
  - engineering/security/secure-sdlc.md
  - leadership/learning-organisation.md
  - engineering/architecture/team-topologies.md
source: "Forsgren, Humble & Kim — Accelerate: The Science of Lean Software and DevOps (2018); https://dora.dev"
updated: 2026-06-21
---

# The DevOps Capability Model (Accelerate / DORA)

The *Accelerate* research (Forsgren, Humble & Kim) is the empirical backbone behind most modern
claims about software delivery. Its finding: **24 capabilities**, grouped into **five categories**,
statistically drive software delivery performance — and delivery performance in turn predicts
organisational performance. The capabilities are *causes you can invest in*; the
[four delivery metrics](#the-four-delivery-metrics) are the *outcomes you measure*.

This note is the canonical reference the rest of the knowledge base points at when it says "DORA"
or "Accelerate" — see [Continuous Delivery](continuous-delivery.md) (the technical core),
[CI/CD as the Control Plane](../engineering/practices/ci-cd-ai-engineering.md), and
[The APEX Framework](../engineering/practices/apex-framework.md) (which folds DORA's AI-readiness
capabilities into its diagnostics).

## The four delivery metrics

Delivery performance is measured on four metrics — two for **throughput**, two for **stability** —
and high performers improve all four together rather than trading one for another.

| Facet | Metric | What it captures |
|---|---|---|
| Throughput | **Deployment frequency** | How often the team ships to production |
| Throughput | **Lead time for changes** | Commit → running in production |
| Stability | **Change failure rate** | % of deployments causing a degradation |
| Stability | **Time to restore service** (MTTR) | How fast service recovers from failure |

(Later DORA reports add a fifth, **reliability/operational performance**, as a guardrail.)

## The five categories and 24 capabilities

### 1. Continuous Delivery (8)

The technical core — expanded in [Continuous Delivery](continuous-delivery.md).

1. Version control for **all** production artifacts (code, config, infrastructure)
2. Deployment automation
3. Continuous integration
4. [Trunk-based development](../engineering/practices/trunk-based-development.md)
5. Test automation
6. Test data management
7. **Shift left on security** — security in design and the pipeline, not a late gate
   (see [Secure SDLC](../engineering/security/secure-sdlc.md))
8. Continuous delivery (the outcome the other seven enable)

### 2. Architecture (2)

9. **Loosely coupled architecture** — teams can test and deploy independently
10. **Empowered teams** — teams choose their own tools and make design decisions

### 3. Product and Process (4)

11. Gather and implement **customer feedback**
12. Make the **flow of work visible** through the value stream
13. **Work in small batches** — decompose work to enable fast feedback
14. Foster and enable **team experimentation**

### 4. Lean Management and Monitoring (5)

15. **Lightweight change-approval** processes (peer review over external boards)
16. **Monitor across application and infrastructure** to inform decisions
17. **Proactive notification** via system health checks
18. **WIP limits** to manage flow
19. **Visualise work** (dashboards, boards) to surface quality and flow

### 5. Cultural (5)

20. **Generative, Westrum culture** — performance-oriented, high-cooperation, safe to fail
21. **Support learning** — treat learning as an investment, not a cost
22. **Enable collaboration** across teams
23. Provide resources and tools that make **work meaningful**
24. **Transformational leadership** — vision, intellectual stimulation, supportive of teams

## Why all five categories matter

CD is the technical core, but **delivery performance is a whole-system property**. Loosely coupled
architecture and empowered teams remove deployment bottlenecks; small batches and visible flow
shorten lead time; lightweight approval and proactive monitoring keep the pipeline trustworthy; and
a [generative, learning-oriented culture](../leadership/learning-organisation.md) is what sustains
all of it. Investing only in the technical eight while ignoring architecture, process, and culture
is the common way capability programmes stall.

## Westrum's typology

The "generative culture" capability draws on Ron Westrum's typology of how organisations process
information:

| Type | Disposition | Failure response |
|---|---|---|
| **Pathological** | Power-oriented | Scapegoating; information hoarded |
| **Bureaucratic** | Rule-oriented | Justice; messengers tolerated |
| **Generative** | Performance-oriented | Inquiry; messengers trained, failure → learning |

Generative cultures correlate with high delivery performance because information flows to where it
is needed. This is the same psychological-safety thread as
[The Learning Organisation and AI Adoption](../leadership/learning-organisation.md).

## Relationship to other notes

- [Continuous Delivery](continuous-delivery.md) — the deep dive on the technical core (category 1);
  this note is the wider model that CD is one category of.
- [The APEX Framework](../engineering/practices/apex-framework.md) — uses DORA's AI-readiness
  capabilities as diagnostics; where this note describes the *capabilities*, APEX is a *scoreboard*
  for the AI era.
- [Engineering Playbook](../engineering/practices/engineering-playbook.md) and
  [CI/CD as the Control Plane](../engineering/practices/ci-cd-ai-engineering.md) — both track the
  four delivery metrics; this note is where the metrics and their drivers are defined.
