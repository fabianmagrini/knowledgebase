---
type: note
title: Cell-Based Architecture
description: "Bounding a failure domain at runtime: independently deployable cells with their own services and data, one router as the only thing allowed to cross a cell boundary, and restart-in-another-cell rather than resume — with deliberate service duplication accepted as the price of independence."
tags: [architecture, system-design, microservices, observability, reading]
topic: engineering/architecture
status: notes
level: intermediate
related:
  - concepts/resilient-software-design.md
  - concepts/control-plane-data-plane.md
  - reading/fintech-engineering-handbook.md
  - tools/dynamic-configuration-sidecar.md
  - engineering/architecture/composable-architecture.md
  - engineering/architecture/change-locality.md
  - engineering/architecture/over-engineering.md
  - case-studies/zalando-client-side-load-balancing.md
  - case-studies/netflix-service-topology.md
  - engineering/practices/database-migration-strategies.md
  - engineering/architecture/agents-as-distributed-systems.md
  - concepts/clean-code-and-solid.md
  - engineering/practices/software-design-principles.md
  - concepts/progressive-delivery.md
source: "https://americanexpress.io/cell-based-architecture-for-resilient-payment-systems/"
updated: 2026-11-02
---

# Cell-Based Architecture

Benjamin Cane, a Distinguished Engineer at American Express (June 2026), on the architecture of
their modernised core payments platform. A **cell** is:

> an independently deployable unit that can process payments on its own

with *"its own set of microservices, databases, and other components"*, such that *"a failure
stays within that cell instead of spreading across the platform."*

**This is the runtime partner to a term these notes use constantly in another sense.** "Blast
radius" appears in nine notes here and in every one of them it means *code review risk* — tier
the review by the scope of the change. This is blast radius as a **deployed property**: bound the
failure domain in the system itself rather than in the process that approves changes to it.
[Resilient Software Design](../../concepts/resilient-software-design.md) also defers *"circuit
breakers, bulkheads, timeouts, and the like"* to later posts in a series that was never captured.
A cell is a bulkhead at the coarsest available grain.

> **Provenance and shape.** Filed as a **pattern note rather than a case study**, deliberately:
> there are **no transaction volumes, no latency figures, no availability targets and no cell
> count** anywhere in the piece — unusual for an engineering post about a payments platform whose
> whole justification is availability. What it does have is design rules with reasons, which is
> what a pattern note holds. Amex writing about Amex, with the trade-offs stated but no outcomes.

## The boundary rule, stated absolutely

The sharpest thing in the piece, and the part that makes the pattern more than "microservices in
groups":

> Only the Global Transaction Router can communicate across cells.

Microservices are confined to *"pod-to-pod interactions within the cell's Kubernetes network"*,
and the router is the sole ingress *and* the sole path for reroutes: *"Transactions must enter a
cell through the Global Transaction Router; if a cell cannot process a transaction and that
transaction needs to be rerouted to another cell, it must also go through the Global Transaction
Router."*

**The cost he accepts rather than hides:**

> This enforcement occasionally results in duplicated services where shared implementations might
> otherwise seem simpler, but it preserves cell independence and improves latency.

**Deliberate duplication to preserve an isolation boundary** is the real trade, and it cuts
against the reuse instinct in [Clean Code and SOLID](../../concepts/clean-code-and-solid.md) and
[Software Design Principles](../practices/software-design-principles.md). A shared service
reachable from every cell *is* a cross-cell dependency however well-factored it looks, so the
choice is between one implementation and an intact failure domain. Worth noting the second
justification is latency, not purity — a local copy is also a faster copy.

The router is itself the obvious objection: everything crosses one component, which concentrates
the risk the cells distribute. The piece does not address what happens when the router degrades.

## Data locality, split by volatility

| Data | Treatment |
|---|---|
| **Static / semi-static** — *"currency rates and merchant category codes"* | *"Rather than relying on a fall-through read to a centralized system of record during transaction processing, we pre-populate this data in each cell ahead of time"* |
| **Dynamic** | *"We use deterministic routing to route transactions to the cell where the right data is already available"* — the router *"sends a transaction to the cell that already has the authoritative dynamic state"* |

Replication *"happens asynchronously outside the transaction path."* And cells *"never span
multiple regions — everything required to process transactions remains local within that
boundary."*

The move worth extracting: **where data cannot be replicated cheaply, route the work to the data
rather than fetching the data to the work.** Deterministic routing turns a consistency problem
into a placement problem — which is also why the router has to hold the routing state, and
therefore why it cannot be stateless.

## Restart, do not resume

The recovery decision that makes cross-cell failover tractable:

> We do not attempt to resume partially processed transactions across cells. Instead, we restart
> transaction processing in another cell with the original transaction data.

When something downstream fails, *"the orchestrator detects the failure, halts processing, and
sends the transaction back to the Global Transaction Router to be rerouted to another cell."*
Resuming would require transferring partial state across a boundary the architecture exists to
keep closed; restarting needs only the original input.

Two things make that safe, and both are necessary:

- **A point of no return.** *"Once a transaction has been sent to an external system (e.g., card
  issuer), we consider that a point of no return, and we don't allow transactions to be rerouted
  after that point."*
- **Idempotency.** *"Each transaction carries a unique transaction identifier that remains
  consistent across retries and reroutes. Downstream systems use these identifiers to detect and
  suppress duplicate requests."*

**This is what the fintech handbook's first principle buys you.**
[Fintech Engineering Handbook](../../reading/fintech-engineering-handbook.md) states *"no
invented data"* — idempotency, deduplication and reconciliation as the practices that uphold it,
with *"the same instruction applied twice must not move money twice."* That note has the
principle; this shows the architecture it enables. Without a consistent transaction identifier
you cannot restart work in a different cell at all, so idempotency is not a safety net here but
**a precondition for the failover strategy**. The same property appears in
[Database Migration Strategies](../practices/database-migration-strategies.md) as *"idempotent
and resumable"* for backfills — same requirement, different operation.

## Edge minimalism: observability must not be in the critical path

Two mechanisms, both inverting a common default:

> If our logging infrastructure becomes unavailable, we don't want that to impact the ability to
> process transactions. We do this by using an asynchronous logger configured with a **buffer
> truncation policy**, so if the buffer is full, we drop logs instead of blocking transaction
> processing.

> We maintain an **in-memory configuration that is updated asynchronously**, so if the
> configuration service becomes unavailable, we can continue running with the last known
> configuration.

**This is static stability applied inside the transaction path.**
[Control Plane and Data Plane](../../concepts/control-plane-data-plane.md) defines static
stability as the property that keeps one plane failing from breaking the other; here logging and
configuration are control-plane concerns explicitly denied the ability to stop the data plane.
The deliberate choice is *"accepting degraded non-critical functionality (logging, metrics) to
preserve transaction processing"* — losing observability precisely when you would most want it,
which is the right call for payments and worth naming as a trade rather than a win.

Set against [Airbnb's Sitar sidecar](../../tools/dynamic-configuration-sidecar.md), which reaches
the same conclusion — local cache, survive control-plane outages, graceful degradation — as a
**platform service** rather than in-process. Same principle, two placements: a sidecar makes it
uniform across polyglot services, in-memory config makes it one fewer process in the path.

## What the piece does not cover

- **No cell sizing, count or placement guidance.** For a pattern whose entire value is bounding a
  failure domain, **the size of that domain is the central design question** — how large a cell
  should be, how many to run, how to place them across zones — and none of it is addressed.
- **No per-cell deployment story**, despite *"independently deployable"* being in the definition.
  Whether cells are released independently, and whether that is used for progressive rollout
  ([progressive delivery](../../concepts/progressive-delivery.md) would make a cell a natural
  rollout unit), goes unmentioned.
- **No numbers at all** — no volumes, latency, availability, or cell counts.
- **No incident evidence.** Nothing on a cell failure actually being contained in production,
  which is the single observation that would validate the design.
- **Nothing on the router's own failure.** The one component permitted to cross every boundary is
  the one whose degradation is not discussed.
- **No threshold for adoption.** He concedes the pattern *"often increases management overhead
  and architectural complexity"* and concludes the benefits outweigh it *"for mission-critical
  systems like payments"* — which assumes the threshold rather than locating it.
  [Over-Engineering Is Solving the Wrong Problem](over-engineering.md) holds that structure must
  be justified by constraints; payments is a genuine constraint, so the pattern is well-founded
  *here*, and a reader is given no way to judge whether it is founded for them.

## Relationship to other notes

- [Resilient Software Design](../../concepts/resilient-software-design.md) — the bulkhead that
  note defers to a later post and never reaches, at the coarsest grain. Its failure-mode taxonomy
  (crash, omission, timing, response) is what a cell boundary is built to contain.
- [Fintech Engineering Handbook](../../reading/fintech-engineering-handbook.md) — "no invented
  data" as a principle; restart-don't-resume is the architecture that principle makes possible.
- [Control Plane and Data Plane](../../concepts/control-plane-data-plane.md) — static stability,
  applied here by denying logging and config the ability to block a transaction.
- [Dynamic Configuration Sidecar](../../tools/dynamic-configuration-sidecar.md) — the same
  degradation argument solved as a platform service rather than in-process.
- [Zalando's Client-Side Load Balancing](../../case-studies/zalando-client-side-load-balancing.md)
  — fault isolation per caller rather than per cell: *"every client competes; blame diffuse"*
  against *"isolated per caller"*. Same instinct at a different boundary.
- [Netflix's Service Topology at Scale](../../case-studies/netflix-service-topology.md) —
  computing blast radius *during* an incident; cells bound it in advance.
- [Change Locality and Boundary Drift](change-locality.md) — a cell is a locality claim about
  *failure* rather than about change, and it decays the same way: a cell is only independent
  until someone adds a shared dependency.
- [Composable Architecture](composable-architecture.md) — fault isolation as a claimed property
  of component boundaries; this is what enforcing it actually costs.
