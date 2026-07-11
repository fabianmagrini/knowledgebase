---
type: case-study
title: Zalando's Client-Side Load Balancing
description: "moving ~1M req/s off a shared edge load balancer into the calling process: watch-based discovery, consistent hashing with hash parity, occupancy (Little's Law) as the load signal, N-ring fade-in, bounded-load walk, and the cache-locality-vs-zone-cost trade-offs"
tags: [architecture, system-design, performance, reading]
topic: case-studies
status: notes
level: intermediate
related:
  - case-studies/linear-performance-architecture.md
  - concepts/resilient-software-design.md
  - engineering/architecture/caching-reference-data-apis.md
  - engineering/ai-native/model-routing-and-ai-gateways.md
source: "https://engineering.zalando.com/posts/2026/06/client-side-load-balancing.html"
updated: 2026-07-05
---

# Zalando's Client-Side Load Balancing

Conor Gallagher (Senior Principal Engineer, Zalando) describes moving ~1 million requests/second
of internal traffic for the **Product Read API (PRAPI)** off a shared edge load balancer
(Skipper) and into the calling process. The metrics below are Zalando-reported.

## The problem: fan-out through shared infrastructure

Batch operations spawned up to **100 parallel calls**, each transiting the shared edge LB. That
fan-out multiplied every client's exposure to shared-infrastructure faults and made incidents
undiagnosable — teams couldn't tell Skipper latency from application latency. The fix was to make
each caller do its own routing, eliminating the shared hop and giving full visibility.

| | Server-side (shared) | Client-side (in-process) |
|---|---|---|
| Routing decision | Shared infrastructure | The calling process, locally |
| Fault blast radius | Every client competes; blame diffuse | Isolated per caller |
| Visibility | Shared-system logs hide faults | Caller owns telemetry (dest pod/node) |

## How they built it

- **Discovery — watch, don't poll.** A watch-based informer (`list + watch` on Kubernetes
  `EndpointSlice`) streams endpoint changes in real time, with a **2-second debounce** during
  scale events to prevent ring thrashing. Polling the K8s API had previously crashed control
  planes at this scale.
- **Consistent hashing with hash parity.** They replicated Skipper's exact algorithm —
  **xxHash64 on a virtual-node ring, 100 virtual nodes per endpoint** — and unit-tested that
  their ring was *identical* to Skipper's for any pod configuration ("hash parity"), so the
  cutover didn't move cache keys.
- **The right load signal: occupancy.** In-flight request count can't tell a pod serving a
  thousand 1 ms cache hits (occupancy ≈ 1.0) from one backed up on slow work. **Occupancy** —
  "seconds of work per second," from Little's Law, measured over a **150 ms sliding window** —
  captures real load. The combined signal penalises slow pods:

  ```
  effectiveLoad = max(inflight, occupancy) × min(podLatency / globalLatency, 5)
  ```

  The **5× "stuck-pod cap"** stops one slow pod from making every alternative look cheap.
- **N-ring fade-in.** When autoscaling adds pods, each scale event gets its own **independent
  fade curve** (a `^2.5` progression — slow start, rapid finish). Rings run in parallel via
  lock-free atomic references; newer rings gradually take traffic while older ones drain.
- **Bounded-load walk.** If a pod exceeds `loadPerLocalPod = (totalLoad × localWeight) /
  localPodCount`, the ring does a **capped walk (≤10 hops)** to a less-loaded pod — requests stay
  cache-local unless rerouting is genuinely necessary.
- **Retries and buffering.** A single fast, jittered retry against **exclude sets** (never retry
  the same pod), plus a **FIFO buffer** ahead of concurrency limits that queues already-admitted
  requests instead of rejecting them under spikes.

## Trade-offs the author names

- **Cache locality vs zone cost.** AZ-affinity cuts inter-AZ transfer cost but fragments the
  product cache across fewer local pods, raising DynamoDB misses.
- **Operational complexity.** In-process routing means owning watch connections, RBAC, staleness
  handling, and profiling — mitigated by a Skipper fallback, but "permanently ours."
- **Zone-aware routing paused.** Careful zone fade-in with latency-health factors proved fragile
  when composed with N-ring fade-in; paused pending clearer economic justification.

## Reported results

| Measure | Before → after |
|---|---|
| Skipper pods | 50+ → **8** (≈80% reduction) |
| Pod occupancy spread | 0.40–1.30 (imbalanced) → **0.60–0.90** (tight) |
| Median deployment time | 289 min → **128 min** |
| Peak traffic off shared infra | **~1M requests/second** |

Plus cost savings from fewer Skipper pods and tighter occupancy-based scaling (65% vs 50% CPU).

## Broader lessons

- **Consistent hashing and isolation pull in opposite directions** — you trade one benefit for
  the other.
- **Slow pipelines force larger batches**, which increase risk; fast pipelines enable safe
  incremental experiments (deploy time was itself a reliability lever).
- **Owning telemetry** (logging destination pod and node) revealed infrastructure faults that
  shared-system logs had hidden for years.

## Relationship to other notes

- **[Linear's Performance Architecture](linear-performance-architecture.md)** — the genre sibling:
  another single-company deep-dive where a hard performance property came from one architectural
  commitment defended over time (here, owning routing in-process).
- **[Resilient Software Design](../concepts/resilient-software-design.md)** — the retries,
  bounded-load walk, buffering, and Skipper fallback are resilience mechanisms (load shedding,
  graceful degradation) applied at the client.
- **[Caching Reference Data APIs](../engineering/architecture/caching-reference-data-apis.md)** —
  PRAPI serves cached product reference data, so the load-balancer's routing directly governs
  cache-hit locality; the AZ-affinity-vs-cache-fragmentation tension lives at that seam.
- **[Model Routing and AI Gateways](../engineering/ai-native/model-routing-and-ai-gateways.md)** —
  a cross-domain parallel: both distribute requests across backends from the client side, though
  here the backends are identical replicas chosen by *load* rather than models chosen by
  *cost/capability*.
