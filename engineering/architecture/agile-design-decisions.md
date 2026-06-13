---
title: Agile Design Decisions and Principles
tags: [architecture, system-design, code-review, refactoring]
topic: engineering/architecture
status: notes
related:
  - engineering/architecture/adr.md
  - engineering/architecture/c4-model.md
  - engineering/architecture/composable-architecture.md
  - engineering/practices/start-with-why.md
  - engineering/practices/federated-pr-review.md
  - engineering/practices/code-review-policy.md
  - engineering/practices/architecture-decision-forum.md
source: "https://gist.github.com/fabianmagrini/76071cbc06aa1a5eafd19a7fb5ea2457"
updated: 2026-06-13
---

# Agile Design Decisions and Principles

> Agile doesn't mean "no design" — it means *continuous* design.

The shift is from Big Design Up Front (BDUF) to emergent, iterative design: a minimal
end-to-end skeleton that grows by evolution, with decisions delegated to teams inside
explicit guardrails.

| Traditional | Agile equivalent |
|---|---|
| Complete system blueprints | Walking Skeleton + evolutionary growth |
| Design review boards | Distributed decision-making with guardrails |
| Future-proofing | YAGNI (You Ain't Gonna Need It) |
| Permanent architecture | Easily replaceable components |

## Decision frameworks

Two axes that compose: *how reversible* is the decision × *how wide* is its blast radius.
Together they answer "who decides, and how carefully."

### Reversibility — one-way vs. two-way doors

- **Type 1 — One-Way Doors (irreversible).** Consequential and nearly impossible to
  reverse without significant cost, data loss, or time. E.g. primary language, cloud
  provider, database paradigm (SQL vs. graph), a public API once released. **Slow down** —
  these are not made in a stand-up; use ADRs, POCs, and guild consultation.
- **Type 2 — Two-Way Doors (reversible).** If wrong, you can back out cheaply. E.g. a
  utility library, naming conventions, UI tweaks, internal class structure. **Decide
  immediately and move on** — delegate to the team.

> It is better to make a wrong Type 2 decision quickly than a right decision slowly.

### Scope — blast radius

| Tier | Affects | Decision-maker |
|---|---|---|
| **A — Local** | Internals of one service/module | The development squad |
| **B — Boundary** | How System A talks to System B | Solution designer facilitates producer + consumer teams |
| **C — Global / cross-cutting** | The entire ecosystem | Architecture guild / principal architect sets **guardrails** |

Teams have autonomy *between* the guardrails but cannot cross them.

### Delegation Poker

A Management 3.0 practice with 7 levels (Tell → Sell → Consult → Agree → Advise → Inquire →
Delegate). It creates explicit agreements about decision authority — removing ambiguity
about who decides what, preventing both micromanagement and anarchy.

## Emergent architecture

Start with a **Walking Skeleton** (minimal end-to-end implementation) and let structure
evolve from actual needs rather than speculation. This is only safe with the supporting
discipline:

- TDD for safe refactoring
- CI/CD for rapid, low-risk deployment
- Code review discipline
- A balance of intentional skeleton and emergent "flesh"

### The architectural runway

Solution designers work one sprint ahead (Sprint N+1), building infrastructure and
"Enabler" stories so delivery teams are never blocked — just-enough structure, just in time.

## Technical debt as a tool

Martin Fowler's quadrant distinguishes good debt from mess:

| | Reckless | Prudent |
|---|---|---|
| **Deliberate** | "We don't have time for tests." (bad debt) | "Hard-code this, refactor in January." (good debt) |
| **Inadvertent** | "What is layering?" (competence gap) | "We should have used a graph DB." (learning) |

Prudent/deliberate debt is a conscious trade-off for time-to-market — and is documented in
an [ADR](adr.md). Repayment strategies:

- **Boy Scout Rule** — leave code better than you found it.
- **The Tax** — allocate 15–20% of every sprint to technical enablers.
- **Debt ceilings** — metrics (coverage thresholds, performance limits) that trigger a
  mandatory stop.

## Start with the "Why"

Understanding the problem before the solution prevents "solutioneering" and unlocks team
autonomy via Commander's Intent. Tools: the **5 Whys** to find root causes, and spotting the
**XY Problem** (asking about an attempted solution rather than the real need). See
[Start with the Why](../practices/start-with-why.md).

## The simplicity paradox

> Simplicity is not the absence of complexity — it's the thoughtful *organization* and
> *hiding* of it.

> Anyone can add complexity. Only those who deeply understand the problem can take
> complexity away.

True simplicity is an outcome, not a starting point: it requires mastering the complexity
first, demands painful trade-offs and saying "no," and emerges through iteration rather than
appearing in version 1.
