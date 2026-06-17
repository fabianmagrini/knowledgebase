---
title: Thinking in Constraints
tags: [architecture, system-design, decision-making]
topic: engineering/architecture
status: draft
level: intermediate
related:
  - engineering/architecture/adr.md
  - engineering/architecture/agile-design-decisions.md
  - engineering/architecture/architectural-change-cases.md
  - leadership/designing-with-constraints.md
  - leadership/first-principles-thinking.md
  - concepts/theory-of-constraints.md
updated: 2026-06-17
---

# Thinking in Constraints

Solution architecture is the discipline of choosing a structure that satisfies a
set of forces no one of which can be fully optimised. Those forces are
**constraints** — the boundary conditions that bound the solution space before any
option is chosen. A solution architect's first job is not to pick a design; it is
to **surface, classify, and challenge the constraints**, because once they are
clear the design largely falls out of them.

Constraints are usually experienced as restrictions. The more useful stance is
that they are an architect's primary input: they collapse an infinite space of
possible designs into a tractable one, make trade-offs explicit, and let
decisions be made *by the constraint* rather than by endless debate.

## A taxonomy of architectural constraints

Constraints arrive from many directions; naming the category helps you find the
ones you have missed.

- **Business** — budget, time-to-market, total cost of ownership, build-vs-buy,
  strategic bets, vendor relationships.
- **Regulatory & compliance** — data residency, privacy (e.g. GDPR), sector rules
  (PCI-DSS, HIPAA), auditability and retention. Often the hardest of hard limits.
- **Technical** — the existing stack, legacy systems that must be integrated,
  platform and language choices, interoperability and protocol requirements.
- **Operational** — availability and SLA targets, scalability envelope, disaster
  recovery, observability, supportability with the on-call team you actually have.
- **Organisational** — team topology and skills, governance, and **Conway's Law**:
  the system will tend to mirror the communication structure that builds it, so
  team boundaries are an architectural constraint whether acknowledged or not.
- **Quality attributes (NFRs) as constraints** — performance, security,
  reliability, and the rest are not features to maximise but budgets to meet; a
  latency target or a security posture *constrains* the legal designs.

## Distinctions worth keeping straight

- **Hard vs soft.** Hard constraints are immovable (a regulatory deadline, a
  physical latency floor). Soft constraints are negotiable preferences. Treating a
  soft constraint as hard over-constrains the design and forecloses good options;
  treating a hard one as soft produces an architecture that cannot ship.
- **Constraint vs requirement.** A requirement says what the system must *do*; a
  constraint bounds *how* it may do it. "Process payments" is a requirement;
  "cardholder data must never touch our servers" is a constraint.
- **Constraint vs assumption.** An assumption is a constraint you have not yet
  validated. Unvalidated assumptions are where architectures fail quietly —
  promote them to explicit constraints or test them.

## Working with constraints in practice

1. **Surface them early and widely.** Most damaging constraints are discovered
   late. Interview stakeholders across business, security, operations, and the
   teams who will build and run the system.
2. **Classify and record them.** Capture the binding constraints as the *context*
   of an [Architecture Decision Record](adr.md) — the decision only makes sense
   against the constraints that forced it.
3. **Challenge them.** Ask "is this real, or inherited?" This is
   [first-principles thinking](../../leadership/first-principles-thinking.md):
   strip away constraints that are merely habit so the genuine limits stand out.
4. **Let constraints drive trade-offs.** You cannot maximise every quality
   attribute; the binding constraints tell you which to favour. A strict data-
   residency constraint may force regional partitioning; a hard latency budget
   may force data locality and rule out a chatty service mesh; team topology may
   dictate service boundaries (Conway again).
5. **Revisit when they move.** Constraints are not permanent. An
   [architectural change case](architectural-change-cases.md) is exactly the tool
   for anticipating which constraints might shift and what that would cost.

## Anti-patterns

- **Ivory-tower design** — choosing a structure before the constraints are known,
  then forcing reality to fit it.
- **Inventing constraints** — gold-plating with self-imposed limits that no
  stakeholder actually requires.
- **Stale constraints** — designing against yesterday's limits (a data-centre
  capacity cap, a since-retired system) long after they ceased to bind.
- **Over-constraining** — hardening every preference until no feasible design
  remains.

## How this relates to the other "constraint" notes

This note is one of three lenses on constraints in this knowledge base, and they
are deliberately different:

- **[Designing with Constraints](../../leadership/designing-with-constraints.md)** —
  constraints as *creative filters for what deserves to be built* (product
  identity, the one-page test). That note imposes constraints to sharpen a
  product; this one *surfaces and reconciles* the constraints a solution must
  live within.
- **[Theory of Constraints](../../concepts/theory-of-constraints.md)** —
  constraint as the single *bottleneck that limits throughput* in a flow. Same
  word, different sense: there it is the thing to relieve; here it is the boundary
  to design within.
- **[First-Principles Thinking](../../leadership/first-principles-thinking.md)** —
  the move that tells the two apart in practice: which constraints are real
  (keep), and which are inherited assumptions (discard)?
