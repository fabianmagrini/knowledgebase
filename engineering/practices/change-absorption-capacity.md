---
title: Change Absorption Capacity (CATS)
tags: [ai-engineering, refactoring, observability, testing, api-design, reading]
topic: engineering/practices
status: notes
level: intermediate
related:
  - engineering/practices/ci-cd-ai-engineering.md
  - engineering/practices/api-contract-functional-testing.md
  - engineering/practices/ai-native-engineering-overview.md
  - engineering/practices/eval-driven-ai-development.md
  - engineering/practices/test-coverage-policy.md
  - engineering/practices/ai-dlc-methodology.md
  - engineering/practices/harness-engineering.md
  - leadership/learning-organisation.md
  - engineering/practices/release-confidence.md
  - engineering/practices/quality-first-ai-coding.md
  - engineering/architecture/architectural-change-cases.md
  - engineering/practices/agile-in-the-age-of-ai.md
  - engineering/practices/modern-engineering-values.md
  - engineering/practices/loop-driven-development.md
  - engineering/practices/ci-speed-with-ai-agents.md
  - concepts/theory-of-constraints.md
  - engineering/practices/software-design-principles.md
  - concepts/resilient-software-design.md
  - engineering/practices/agentic-code-review.md
  - engineering/practices/ai-engineering-discipline.md
  - engineering/practices/apex-framework.md
source: "https://stackoverflow.blog/2026/05/12/you-shipped-it-fast-but-did-you-ship-it-right/"
updated: 2026-06-20
---

# Change Absorption Capacity (CATS)

AI tools have made code *production* cheap, but most delivery systems haven't evolved to
*absorb* that code safely. The gap between how fast code arrives and how safely a system can
take it on is where production incidents live. If incoming change velocity exceeds a system's
capacity to absorb it, delivery paradoxically slows — gains from faster generation are eaten
by debugging and rework.

## The illusion of correctness

AI-generated code looks sound under review: syntactically clean, tests passing. But it carries
hidden assumptions about boundary conditions, concurrency, domain rules, and security context
that don't surface until production. Happy-path review and happy-path tests don't catch them.
The faster code is generated, the more of this latent risk accumulates per unit time.

## Change absorption capacity

Every system has a finite capacity to safely absorb new changes. Treat it as a real,
bounded resource:

- When change velocity stays under capacity, speed **compounds** — each change is cheaper.
- When velocity exceeds capacity, **fragility accumulates** — each change is more expensive,
  and effective delivery speed drops even as raw output rises.

**Refactoring is not cleanup — it's the mechanism that raises absorption capacity.** Bundle
continuous refactoring with feature work rather than deferring it; that's what lets a system
take agent-speed change safely at scale.

## The CATS framework

Four foundational practices that raise absorption capacity:

| | Practice | What it means | Replaces |
|---|---|---|---|
| **C** | **Contracts** | Versioned API specs, event/data schemas, explicit ownership | Implicit conventions |
| **A** | **Automated verification** | Domain-invariant tests, schema validation in CI, security checks | Happy-path coverage only |
| **T** | **Telemetry** | Logs, metrics, traces of real runtime behaviour; drift detection, canary thresholds | Guessing from code |
| **S** | **Simplification** | Continuously reduce coupling, clarify ownership; measure whether change gets cheaper | One-off "cleanup" |

These map directly onto existing notes here: contracts and automated verification are the
subject of [API Spec, Contract, and Functional Testing](api-contract-functional-testing.md);
the pipeline that enforces them is [CI/CD as the Control Plane](ci-cd-ai-engineering.md);
verifying the agents themselves (not just their output) is
[Eval-Driven Development](eval-driven-ai-development.md).

## A two-week starting plan

**Week 1 — establish boundaries and verification**
- Identify the most brittle boundaries in the system.
- Write contracts for them: field meanings, ownership, versioning.
- Add schema validation to CI.
- Write one critical **invariant test** that protects a domain rule.

**Week 2 — observe and simplify**
- Add drift-detection dashboards.
- Remove one high-risk coupling point.
- Establish rollback procedures: feature flags and canary thresholds.

**Smallest first step:** pick one unstable boundary, document its contract, and add one
invariant test protecting its domain rules.

## Measure change cost, not code cleanliness

The goal is whether modifications get progressively cheaper, not whether code looks tidy.
Useful signals:

- **PR size trends**
- **Incidents per change**
- **Coordination overhead** (how many people/teams a change must involve)
- Whether changes to a given area become **cheaper or more expensive** over time

> Fast *with* CATS: speed compounds. Fast *without* it: fragility compounds.

This is the quality counterpart to the rest of the
[AI-Native Engineering](ai-native-engineering-overview.md) notes — when generation is cheap,
leverage moves to the boundaries, contracts, and feedback loops that let a system safely keep up.
