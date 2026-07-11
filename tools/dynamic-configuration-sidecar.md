---
title: Dynamic Configuration Sidecar (Airbnb Sitar)
tags: [architecture, system-design, microservices, reading]
topic: tools
status: notes
level: intermediate
related:
  - concepts/resilient-software-design.md
  - tools/postgresql-ha-kubernetes.md
  - engineering/architecture/composable-architecture.md
  - engineering/architecture/thinking-in-constraints.md
  - engineering/architecture/caching-reference-data-apis.md
source: "https://medium.com/airbnb-engineering/sitar-agent-building-a-reliable-dynamic-configuration-sidecar-at-scale-b7e00c152068"
updated: 2026-06-20
---

# Dynamic Configuration Sidecar (Airbnb Sitar)

Airbnb's **Sitar-agent** delivers configuration changes to tens of thousands of
service pods within tens of seconds — **without redeploys** — and keeps serving
config even when the central configuration service is down. It is a concrete
instance of [resilient software design](../concepts/resilient-software-design.md):
the whole architecture is shaped by the rule that *the application must keep reading
config through a control-plane outage*.

> **"Agent" here is not an AI agent.** Sitar-agent is a traditional sidecar daemon
> process — included in this knowledge base as a distributed-systems case study, not
> an agentic-AI one.

## The sidecar pattern

Sitar-agent runs as an isolated **Kubernetes sidecar container** beside each
subscribed service pod. Airbnb deliberately rejected folding the logic into the
main container despite the cost saving, to get:

- **Multi-language support** for free (Java, Python, Go, TypeScript, Ruby) — one
  agent, no per-language reimplementation.
- **Fault isolation** and independent logging.
- Operational clarity.

## Delivery lifecycle

1. **Create/update** — developers commit changes via Git or a web UI to the central
   **Sitar Service**, with versioning and ACLs.
2. **Snapshot** — a service periodically packages all config groups and uploads a
   snapshot to **AWS S3**.
3. **Pod startup (dual bootstrap)** — the agent **preloads the latest S3 snapshot**
   (fast, and resilient to a Sitar Service outage), then **syncs recent changes**
   from Sitar Service; it signals readiness only after the sync succeeds.
4. **Periodic polling** — the agent polls Sitar Service roughly every 10 seconds
   (with jitter) for changes.
5. **Application read** — the main container reads from local disk via a client
   library with an in-memory cache.

## Key trade-offs

- **Pull, not push.** Airbnb kept a pull-based agent-polls-server model despite the
  overhead, for simplicity and stateless operation. Server-side **10-second TTL
  caching** and **change tokens** (tracking the last-scanned DB row) keep the cost
  down. They accept "a few seconds" of propagation delay because *"dynamic config is
  not a real-time signalling mechanism"*.
- **Local datastore: Sparkey → SQLite.** Sparkey (write-once, read-many) became a
  bottleneck — full re-indexing on every write, whole-file locking, limited language
  bindings. Evaluated against RocksDB:

  | Criterion | SQLite (chosen) | RocksDB |
  |---|---|---|
  | Read performance | 2–3× slower, but "sufficient for Sitar's workload" | Best raw throughput |
  | Concurrency | Native **WAL mode**, concurrent read/write | Manual tuning |
  | Operations | Single file, minimal tuning | Compaction, block cache, column families |
  | Multi-language bindings | Official, all Airbnb languages | Immature, inconsistent |

  SQLite won on **operational practicality and multi-language support**, not raw
  speed — a deliberate choice to favour the binding constraint (polyglot, low-ops)
  over peak performance.

## Reliability mechanisms

- **S3 snapshot preload** decouples pod startup from Sitar Service availability.
- **Local on-disk cache** means the application reads config locally even when the
  service is unreachable.
- **Graceful degradation** — the guiding principle: *"a slightly stale value is
  tolerable, but an unreadable config is not."*
- **Change tokens** give incremental sync, reducing database load.
- **Safe migration** — the Sparkey→SQLite cutover used **shadow reads** (run both in
  parallel and compare) behind a **feature-flag-gated** rollout starting with
  non-critical services.

## Scale (Airbnb's reported figures)

Tens of thousands of pods across polyglot services; config changes "several times
each minute" org-wide; propagation to all subscribers within "tens of seconds";
10-second polling with jitter. Treat as the team's reported numbers.

## Relationship to other notes

- [Resilient Software Design](../concepts/resilient-software-design.md) — the
  theory this illustrates: decoupling from a dependency (the control plane), local
  caching, and graceful degradation are textbook resilience patterns.
- [Highly Available PostgreSQL on Kubernetes](postgresql-ha-kubernetes.md) — a
  sibling Kubernetes infra case study; both choose explicit, visible degradation
  over silent failure.
- [Composable Architecture](../engineering/architecture/composable-architecture.md) —
  the distributed-services context in which per-pod sidecars and control planes sit.
- [Thinking in Constraints](../engineering/architecture/thinking-in-constraints.md) —
  the pull-vs-push and SQLite-vs-RocksDB decisions are binding constraints
  (multi-language, low-ops) driving the design over raw performance.
