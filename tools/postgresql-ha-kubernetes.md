---
title: Highly Available PostgreSQL on Kubernetes
tags: [system-design, performance, observability, reading]
topic: tools
status: notes
level: intermediate
related:
  - concepts/resilient-software-design.md
  - engineering/practices/performance-testing-strategy.md
  - engineering/practices/database-migration-strategies.md
  - engineering/architecture/thinking-in-constraints.md
  - tools/dynamic-configuration-sidecar.md
source: "https://www.datadoghq.com/blog/engineering/postgresql-ha-kubernetes/"
updated: 2026-06-20
---

# Highly Available PostgreSQL on Kubernetes

A Datadog engineering case study of making Kubernetes-hosted PostgreSQL fail over
safely. It is a concrete instance of
[resilient software design](../concepts/resilient-software-design.md): the
trade-off it works through — consistency vs availability vs latency under a network
fault — is exactly the kind of design constraint that distributed systems force.

## The problem they hit

During a **gameday** simulating a zonal failure, Datadog found their clusters could
not fail over safely when network latency spiked. Their setup used **asynchronous
streaming replication** (the leader commits without waiting for standbys), so when
the network degraded, replication lag grew past Patroni's `maximum_lag_on_failover`
threshold and **every standby became ineligible for promotion**. That left an
unacceptable choice: wait for latency to subside, or promote a lagging node and risk
**data loss**.

Baseline architecture:

- **Leader pool** — one writer + two standbys (not serving traffic, failover-eligible).
- **Read-replica pool** — many async read-only replicas, excluded from failover.
- **Coordination** — Patroni (HA manager) + ZooKeeper (distributed config store);
  ephemeral znodes maintain a single leader and prevent **split-brain**.

## The fix: hybrid synchronous replication

Datadog moved to a two-tier replication strategy:

- **Leader-pool standbys → synchronous** (`synchronous_commit: remote_apply`): the
  leader waits for a standby to write, flush, and replay the WAL before
  acknowledging the client. No acknowledged write can be lost on failover.
- **Read replicas → stay asynchronous**, to avoid paying latency on nodes that can
  never be promoted anyway.

Key Patroni settings:

| Setting | Effect |
|---|---|
| `synchronous_mode: true` | Enables synchronous replication management |
| `synchronous_node_count: 1` | One standby must acknowledge each commit |
| `synchronous_mode_strict: true` | Blocks writes if **no** healthy sync standby exists — fail closed rather than silently lose durability |

## Performance trade-offs (Datadog's pgbench measurements)

Benchmarked with TPC-B workloads; treat as **their measured figures**, not general
constants. Synchronous replication costs latency and throughput:

| `synchronous_commit` | Latency increase | Throughput reduction |
|---|---|---|
| `remote_apply` | 53% | 34% |
| `on` | 46% | 31% |
| `remote_write` | 38% | 27% |

Despite the benchmark cost, Datadog report **no significant impact on
application-level write latency or throughput** under sustained production load
after a gradual rollout — the synthetic worst case did not translate to the real
workload.

## Failure scenarios they validated

1. **A sync standby is lost** — Patroni reassigns the sync role to another eligible
   replica via `synchronous_standby_names`.
2. **All sync standbys lost, non-strict** — Patroni clears
   `synchronous_standby_names`, falling back to async to **preserve write
   availability** (trading durability).
3. **All sync standbys lost, strict** — Patroni sets it to `*` (any replica may
   acknowledge); writes **block** until one responds — durability over availability.
4. **Leader crashes mid-commit** — a promoted standby may diverge; the old leader
   uses **`pg_rewind`** to discard unreplicated local changes and rejoin.
5. **ZooKeeper unavailable** — with **failsafe mode** on, Patroni checks REST
   connectivity to all members and demotes to read-only if any are unreachable;
   with it off, the leader keeps writing until its TTL lock expires.

## Operating it

- **Gradual rollout** across datacentres and workload tiers, with bake-in periods
  and monitoring.
- **Tunable without downtime** — `synchronous_commit` can be changed via
  `patronictl edit-config`, enabling fast fallback if performance suffers.
- **Failures become visible** — synchronous replication surfaces write blocking
  explicitly, where asynchronous replication loses data silently; explicit failure
  is more recoverable.
- **Manual-failover guardrails** — `patronictl failover` / `switchover` reject
  async nodes unless forced.
- **Monitoring signals** — track `SyncRep` / `WalSenderWaitForReply` wait events in
  `pg_stat_activity` (prolonged waits = replica/network trouble), and alert when
  `patroni_sync_standby` is empty for sustained periods (loss of failover safety).
- **Why not DRBD?** Block-level replication was rejected as too large an
  architectural shift; database-level replication gave better visibility,
  flexibility, and operational confidence.

## Relationship to other notes

- [Resilient Software Design](../concepts/resilient-software-design.md) — the
  theory this makes concrete: failure modes (omission/timing), consensus (ZooKeeper
  leader election), and graceful degradation (strict vs non-strict fallback) in a
  real system.
- [Performance Testing Strategy](../engineering/practices/performance-testing-strategy.md) —
  the pgbench/TPC-B benchmarking that quantified the durability/latency trade-off
  before rollout.
- [Thinking in Constraints](../engineering/architecture/thinking-in-constraints.md) —
  consistency vs availability vs latency is a binding design constraint; strict mode
  chooses durability, non-strict chooses availability.
