---
title: Resilient Software Design
tags: [architecture, system-design, microservices, reading]
topic: concepts
status: notes
level: intermediate
related:
  - engineering/architecture/composable-architecture.md
  - engineering/practices/performance-testing-strategy.md
  - engineering/practices/release-confidence.md
  - engineering/practices/change-absorption-capacity.md
  - concepts/progressive-delivery.md
  - engineering/practices/gitops.md
  - engineering/practices/database-migration-strategies.md
  - tools/containers/postgresql-ha-kubernetes.md
  - tools/containers/dynamic-configuration-sidecar.md
  - sre/incident-swarming.md
  - engineering/architecture/caching-reference-data-apis.md
  - case-studies/zalando-client-side-load-balancing.md
source:
  - "https://www.ufried.com/blog/why_resilient_software_design_1/"
  - "https://www.ufried.com/blog/why_resilient_software_design_2/"
updated: 2026-06-20
---

# Resilient Software Design

Uwe Friedrichsen defines resilience as **"keeping up correct operation in the face
of unexpected (external) adverse events — or at least recovering from them in a
timely manner, while offering a gracefully degraded service."** His argument across
this series is that resilience has shifted from optional to **mandatory**, and that
developers can no longer delegate availability entirely to operations. These two
posts make the *case* for resilient design; the concrete patterns (circuit
breakers, bulkheads, timeouts, and the like) come later in the series.

## Why resilience became mandatory

Traditionally, developers ignored resilience: high-availability infrastructure —
clustering, replication, load balancing — kept systems up, and developers only had
to avoid bugs and respect infrastructure constraints. Three shifts broke that
arrangement:

1. **An explosion of distributed peers** — from monolithic mainframes through
   client/server, web, and SOA to mobile and IoT, systems went from dozens of nodes
   to potentially tens of thousands, many of them *outside organisational control*
   and on unreliable networks.
2. **Faster update propagation** — change cycles collapsed from weeks to seconds.
3. **"Never down" availability** — 24/7 expectations erased maintenance windows.

Modern infrastructure (container schedulers, service meshes, API gateways) can
create a **false sense of security**, tempting developers back to the old
assumption that availability is someone else's problem. The complexity, Friedrichsen
argues, is irreversible.

## Distribution creates novel failure modes

Once a system is distributed, it exhibits failure modes that simply do not exist
inside a single process — *"Everything fails, all the time"* (Werner Vogels):

| Failure mode | What happens |
|---|---|
| **Crash** | A process stops; in-flight data may be lost |
| **Omission** | Brittle/flaky communication; messages are dropped |
| **Timing** | A response exceeds its SLA — and can exhaust thread pools catastrophically |
| **Response** | A *wrong* response arrives (common with replication, caches, eventual consistency) |
| **Byzantine** | A node behaves erratically and unpredictably |

At the application level these surface as lost, incomplete, duplicate, distorted,
delayed, or out-of-order messages, and as partial, out-of-sync local views of
global state.

## Two problems that become very hard

Distribution turns two otherwise-simple problems into hard or impossible ones:

- **Event ordering** — establishing causal relationships across process boundaries
  (e.g. concurrent stock updates producing conflicting inventory views).
- **Consensus** — the **FLP impossibility** result (Fischer, Lynch, Paterson, 1985)
  proves that distributed consensus cannot be guaranteed if even one process may
  fail.

As Leslie Lamport put it: *"A distributed system is one in which the failure of a
computer you didn't even know existed can render your own computer unusable."*

## The takeaway

Because failure is normal and partial, **resilience is a first-class design
concern** — built into how services time out, isolate, degrade, and recover — not a
property that infrastructure supplies for free. Designing for failure means
assuming messages will be lost, duplicated, delayed, or reordered, and choosing
explicitly between guarantees such as *at-most-once* and *at-least-once* delivery
(and making operations idempotent accordingly).

## Relationship to other notes

- [Composable Architecture](../engineering/architecture/composable-architecture.md) —
  packaged business capabilities and BFFs are exactly the distributed peers that
  make resilience necessary; this note is the *why* behind designing them to fail
  gracefully.
- [Performance Testing Strategy](../engineering/practices/performance-testing-strategy.md) —
  reliability and availability under load are where these failure modes show up and
  get measured.
- [Release Confidence as a System Property](../engineering/practices/release-confidence.md) —
  a sibling "system property" framing; resilience and release confidence are both
  emergent properties you design and verify for, not features you add.
- [Change Absorption Capacity](../engineering/practices/change-absorption-capacity.md) —
  the capacity to absorb adverse change safely; resilience is its run-time,
  failure-facing counterpart.
