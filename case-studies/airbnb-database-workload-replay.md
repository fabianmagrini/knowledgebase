---
type: case-study
title: Airbnb's Database Workload Capture and Replay
description: "Differential testing at the database layer, from before anyone called it that: recorded production queries replayed against two MySQL versions with results diffed — and the finding that making the oracle deterministic removes a behaviour from the test's scope."
tags: [testing, system-design, performance, observability, ci-cd, reading]
topic: case-studies
status: notes
level: advanced
related:
  - engineering/ai-native/agentic-verification.md
  - engineering/practices/performance-testing-strategy.md
  - engineering/practices/database-migration-strategies.md
  - engineering/practices/release-confidence.md
  - case-studies/github-copilot-rust-migration.md
  - engineering/ai-native/brownfield-agentic-engineering.md
  - concepts/control-plane-data-plane.md
  - tools/dynamic-configuration-sidecar.md
  - case-studies/netflix-service-topology.md
source: "https://airbnb.tech/infrastructure/beyond-synthetic-testing-capturing-and-replaying-real-database-workloads-at-airbnb/; https://medium.com/airbnb-engineering/beyond-synthetic-testing-capturing-and-replaying-real-database-workloads-at-airbnb-cea7ee9b1ab2"
updated: 2026-10-25
---

# Airbnb's Database Workload Capture and Replay

Zuofei Wang and Erluo Li (post authored with Zheng Liu) on a system that records production
MySQL traffic and replays it against candidate databases — to validate version upgrades, verify
engine migrations, and size clusters.

> **Retrieval and provenance.** The Medium copy returns **403**; this is read from Airbnb's own
> canonical version at `airbnb.tech`, which is also the more durable domain. Airbnb writing about
> Airbnb's own infrastructure — self-interested, but low-stakes: nothing is being sold, and the
> headline figures are **failure findings rather than success metrics**, which is the credible
> direction for self-reporting. The article carries **no publication date**, which is unusual
> enough to note.

The scale it operates at: *"a fleet of hundreds of clusters supporting thousands of use cases at
millions of queries per second (QPS)."*

## Differential testing, from before the term arrived here

[Agentic Verification](../engineering/ai-native/agentic-verification.md) named this category
recently, with two instances — agents doing exhaustive old-versus-new comparisons across the
Copilot Rust port, and Carlini's C compiler checked against GCC. **This is a third, and the
first with nothing to do with AI**: ordinary database infrastructure practice, which is worth
recording because it establishes the technique as engineering rather than an artefact of the
agent era.

Two replay modes, and the second is the differential one:

| Mode | What it does |
|---|---|
| **Replay only** | *"Queries are replayed to a single target database at a configurable speed… query results are ignored"* — load and latency testing |
| **Replay and compare** | *"The same queries are run against two target databases at once, and their results are compared"* |

MySQL 5.7 is the oracle for 8.0. The architecture behind it is three stages:

- **Log Mover** — a **ProxySQL sidecar** tailing local query logs to cloud storage.
- **Log Processor** — an offline job parsing the binary logs, grouping by backend cluster,
  reassembling transactions in order, bucketing into five-minute windows, and rewriting
  `INSERT`s.
- **Log Replayer** — an API server as control plane, a task scheduler, and distributed workers
  issuing the queries.

**Capture moved to the proxy, from the clients.** Their previous system had each language
binding — Java, Python, Ruby — running its own query logger into Kafka, with *"ambiguous
ownership"* and too little transactional context to reassemble a faithful replay. The fix is one
capture point at the wire protocol instead of N in the application, which is the same reasoning
as [Airbnb's own config sidecar](../tools/dynamic-configuration-sidecar.md): put the
cross-cutting concern beside the process rather than inside every polyglot client.

Timing is preserved rather than approximated — workers wait on a synchronised start signal, then
space queries *"according to their original timestamps and the chosen speed factor"* (1×, 2×, 3×,
or a target QPS). That is what makes the same rig serve capacity planning: concurrency and
pacing are reproduced, not modelled.

## The best detail: determinism has a price

To make replay comparable, the Log Processor rewrites every `INSERT` to pin the captured
`last_insert_id`, so anything downstream depending on it behaves identically across engines.
Then they say what it costs:

> by pinning last_insert_id, we no longer exercise the target's native auto-increment generation

**Making the oracle deterministic removed a behaviour from the test's scope.** `agentic-verification`
already advises *"normalise outputs before comparing"* so incidental differences do not drown the
real ones — but it does not say that normalisation is itself a narrowing. Every transformation
applied to make a differential comparison tractable removes something from what is being
compared, and the removed thing is invisible precisely because the comparison now passes.

That generalises well past databases, and it is the sharpest contribution of the piece to the
oracle thread running through these notes.

## What replay actually caught

The regression with numbers:

> the latency for one query pattern went from 0.03 to 2.6 seconds, reading 273 MB per join
> instead of 5 MB, which we traced to an upstream change in how MySQL 8.0.20+ reads rows while
> sorting

And the same rig as a capacity instrument:

> On one large cluster, replaying 80% more write traffic pushed average commit latency up by
> almost 500% from about 6 ms to 34 ms

The other findings were behavioural rather than performance: metadata-locking changes in 8.0,
the consequences of query-cache removal, and a changed `innodb_autoinc_lock_mode` default
breaking code that assumed sequential IDs.

### The finding where the bug was in neither database

> queries whose row order was never fully determined, either with no ORDER BY or an ORDER BY
> without a unique tiebreaker, which quietly return different rows on a new engine once a LIMIT
> is applied

This is **latent under-specification in the application**, not a defect in either engine. The
queries were always ambiguous; one engine's incidental ordering happened to be stable, so nothing
ever failed. Running two side by side is what made the ambiguity observable.

Worth holding as a general property of differential testing: it finds places where the *old*
system's behaviour was never actually specified, only relied upon. A test suite cannot find
those, because the suite was written against the same incidental behaviour.

## Where it sits against the repo's testing notes

[Performance Testing Strategy](../engineering/practices/performance-testing-strategy.md) opens
with almost this article's thesis — *"flat load tests against isolated endpoints don't reveal how
a distributed system behaves under real use"* — and answers it by prescribing realistic traffic
**shapes**: ramp-up, steady state, spike, soak, with a modelled read/write split. Airbnb's answer
is to stop modelling the shape and **replay the recorded one**, with the speed factor as the only
synthetic parameter. Their framing of what synthetic misses is narrow and concrete: *"Synthetic
benchmarks such as sysbench don't capture the full spectrum of production queries."*

The two are complementary rather than competing — shapes are what you use before you have a
capture pipeline, or for traffic that has never existed — but the difference is worth naming,
because replay removes the step where someone guesses the mix.

It is also the rig that would catch the failure
[Brownfield Agentic Engineering](../engineering/ai-native/brownfield-agentic-engineering.md)
reports: **28 of 520** agent migration runs passing audit, with tests green while replacements
still called legacy implementations. A capture-and-compare harness does not care whether the
tests pass; it asks whether both paths answer the same way on recorded input.

## What the piece does not cover

- **No false-positive accounting.** The practical question for anyone building this is how much
  diff noise "replay and compare" produced and how it was triaged. Nothing. That is exactly the
  *"incorrect test oracles"* failure mode named in
  [the Copilot migration](github-copilot-rust-migration.md) — the check itself being wrong is a
  distinct failure from the code being wrong.
- **No comparison against existing tooling.** Percona's `pt-upgrade` and MySQL's own log replay
  facilities do a version of this; why they were insufficient is the missing section for a reader
  deciding whether to build or adopt.
- **No cost or storage figures** for capturing at millions of QPS, and nothing on retention.
- **Nothing on the replay target's lifecycle.** Replaying 80% more *write* traffic implies a
  disposable target, but provisioning, seeding and teardown go undescribed.
- **A constraint that bounds who can copy it**, stated but not explored: *"Captured traffic is
  never replayed against lower environments"*, with logs encrypted in transit and at rest under
  least privilege. The rig only works where production-grade data handling is already available,
  which is a real barrier and is presented only as a security note.
- **No publication date.**

## Relationship to other notes

- [Agentic Verification](../engineering/ai-native/agentic-verification.md) — the third instance
  of differential testing and the first non-AI one, plus the qualification that note is missing:
  normalisation narrows the comparison.
- [Performance Testing Strategy](../engineering/practices/performance-testing-strategy.md) —
  modelled traffic shapes versus replaying the recorded one; replay removes the guess about the
  mix.
- [Database Migration Strategies](../engineering/practices/database-migration-strategies.md) —
  the stateful-change problem this de-risks, with an engine upgrade as the worked case.
- [Brownfield Agentic Engineering](../engineering/ai-native/brownfield-agentic-engineering.md) —
  migration blindness is a missing differential test; this is a production harness for the
  comparison that would expose it.
- [Migrating the Copilot Runtime to Rust](github-copilot-rust-migration.md) — old-versus-new
  comparison at the application layer, and the source of the "incorrect test oracles" risk this
  piece leaves unaddressed.
- [Release Confidence as a System Property](../engineering/practices/release-confidence.md) —
  confidence built upstream of the deployment moment; a replay rig is one of the strongest
  upstream instruments available.
- [Control Plane and Data Plane](../concepts/control-plane-data-plane.md) — the replayer's own
  split: API server as control plane, workers issuing queries as data plane.
- [Dynamic Configuration Sidecar](../tools/dynamic-configuration-sidecar.md) — Airbnb's other
  sidecar, and the same reasoning for moving a cross-cutting concern out of polyglot clients.
