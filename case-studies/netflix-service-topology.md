---
type: case-study
title: Netflix's Service Topology at Scale
description: "how Netflix builds a real-time service dependency graph from millions of flow records/sec: three physical layers, a three-stage aggregation pipeline whose load-bearing step resolves network intermediaries into true application edges, consistent-hashing load distribution against 100x hot nodes, and immutable-snapshot time travel"
tags: [architecture, system-design, microservices, observability, reading]
topic: case-studies
status: notes
level: intermediate
related:
  - case-studies/zalando-client-side-load-balancing.md
  - concepts/resilient-software-design.md
  - tools/dynamic-configuration-sidecar.md
source: "https://netflixtechblog.com/building-service-topology-at-scale-architecture-challenges-and-lessons-learned-f4b792f3f0d8"
updated: 2026-07-19
---

# Netflix's Service Topology at Scale

A Netflix engineering case study of a real-time **service topology** system — a
live map of which microservice depends on which — built to process *millions of
flow records per second* across regions so engineers can reason about dependencies
and blast radius **during** an incident rather than waiting for hours-old batch
data. All metrics below are Netflix's own reported figures.

## The core problem: hops are not edges

Network flow logs record individual **network hops**, not application-level service
relationships. Load balancers, NAT gateways, and other intermediaries sit between
services, so a raw flow shows `Source → Intermediary` and `Intermediary →
Destination` — never the true `Source → Destination` dependency. Reconstructing the
real application edge from those fragments is the problem the system exists to
solve.

## Three physical layers

Topology is assembled from three independently-optimised data sources, each with
storage suited to its shape:

| Layer | Data | Storage |
|---|---|---|
| **Network** | eBPF flow logs | Graph database |
| **IPC** | Application-level RPC metrics | Separate graph database |
| **Tracing** | Distributed traces | Columnar (Parquet) |

## The three-stage aggregation pipeline

The network layer is built by a pipeline that redistributes load at multiple points
rather than aggregating in one place. Stages are connected by **Server-Sent Events
(SSE)**, not gRPC — a deliberate choice (see lessons).

1. **FlowLog Ingestion (Stage 1)** — consumes multi-region Kafka, applies 5-minute
   windowing, does initial aggregation.
2. **Intermediate GraphEntity (Stage 2)** — the **load-bearing step**: joins
   incoming flows (`Source → Intermediary`) with outgoing flows (`Intermediary →
   Destination`) to synthesise the direct application edge, then redistributes
   records keyed by intermediary ID. Without this, the topology would show
   infrastructure instead of real service dependencies.
3. **GraphEntity Ingestion (Stage 3)** — final aggregation, enrichment from external
   KV stores, and persistence to the graph database.

## Load distribution and time travel

- **Consistent hashing with dynamic discovery.** Aggregators are spread across
  instances via consistent hashing, with membership discovered from the service
  registry so the cluster **rebalances automatically during auto-scaling** without
  manual coordination — the same registry-driven rebalancing idea as
  [Airbnb's config sidecar](../tools/dynamic-configuration-sidecar.md).
- **Time travel without full event sourcing.** Immutable 5-minute aggregator
  snapshots (keyed by `entity_id + timestamp`) plus property-level mutation tracking
  let engineers query historical topology at any point in time, avoiding the cost of
  full event sourcing.

## Scale challenges and how they were solved

Netflix frames these as a *cascade* — fixing one bottleneck exposes the next.

| Challenge | Symptom | Fix |
|---|---|---|
| **Kafka lag** | Pipeline minutes behind | More partitions, tuned fetch parameters, larger socket buffers |
| **Hot nodes** | Some instances took ~100x more traffic (power-law skew) | Graduated redistribution across the three stages spreads load at multiple points |
| **Memory / GC** | More CPU in GC than business logic | Switched from immutable to **mutable aggregators on the hotpath** — a deliberate deviation from Scala idiom — cutting heap allocation >50% and GC pauses from hundreds to tens of ms |
| **Reactive streams** | Stalled pipelines, opaque backpressure | Team education, simpler stream patterns, monitoring at async boundaries |
| **Serialisation** | Erratic errors | Standardised on JSON throughout for debuggability |

## Distinctive vocabulary

**Service topology** (live dependency graph); **intermediary resolution**
(reconstructing true edges from hop fragments); **data amplification** (volume
multiplying during shuffle when many sources route to one owner); **hot node**
(power-law traffic concentration); **backpressure**; **async boundary** (the
`.async` operator in Pekko Streams — a thread boundary buying parallelism at the
cost of complexity).

## Lessons (as framed by the authors)

- **Scale is qualitative.** "What works at 100 req/s fails at 100,000 req/s" — the
  design, not just the tuning, has to change.
- **Break conventions deliberately, on evidence.** Abandoning immutability on the
  hotpath was justified by measurement, not preference.
- **Bottlenecks cascade.** Fix Kafka lag → find hot nodes → find GC pressure;
  optimisation is continuous iteration through the current weakest point.
- **Distribution beats concentration.** Multi-stage redistribution stops power-law
  traffic from overwhelming a single owner.
- **Measure technology fit.** gRPC proved wrong for streaming aggregation; SSE won
  despite being the less fashionable choice.
- **Powerful abstractions need investment.** Reactive streams demanded real team
  education before they paid off — don't assume framework fluency.

## Relationship to other notes

- [Zalando's Client-Side Load Balancing](zalando-client-side-load-balancing.md) —
  the closest sibling: another distributed-systems-at-scale case study where
  **consistent hashing** and **load imbalance** are the central concerns. Zalando
  distributes *request* load across service instances; Netflix distributes
  *aggregation* load across pipeline instances, but both fight the same skew.
- [Resilient Software Design](../concepts/resilient-software-design.md) — the theory
  behind the pipeline's **backpressure** and graceful degradation under load.
- [Dynamic Configuration Sidecar (Airbnb Sitar)](../tools/dynamic-configuration-sidecar.md)
  — a sibling infrastructure system that also uses **service-registry discovery** to
  rebalance automatically as the fleet scales.
