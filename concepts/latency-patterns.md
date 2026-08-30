---
type: note
title: Latency Patterns
description: "A taxonomy of latency techniques in four categories — locality, work reduction, concurrent execution, anticipation — plus the argument that AI applications lose most of their time outside the model call."
tags: [architecture, system-design, performance, reading]
topic: concepts
status: notes
level: intermediate
related:
  - concepts/resilient-software-design.md
  - engineering/practices/performance-testing-strategy.md
  - engineering/architecture/caching-reference-data-apis.md
  - case-studies/zalando-client-side-load-balancing.md
  - case-studies/chatgpt-web-performance.md
  - engineering/ai-native/model-routing-and-ai-gateways.md
source: "https://generativeprogrammer.com/p/latency-patterns-for-faster-ai-applications"
updated: 2026-08-30
---

# Latency Patterns

Bilgin Ibryam (August 2026) catalogues nineteen latency techniques and groups them into four
categories. The grouping is the useful part — it is close to exhaustive over the ways latency
can be attacked, which makes it a checklist for *where you have not looked* rather than a list
of tricks.

| Category | The move |
|---|---|
| **Locality** | Move things closer together |
| **Work reduction** | Do less |
| **Concurrent execution** | Overlap whatever work remains |
| **Anticipation** | Do it before you are asked |

**Provenance, and it matters here.** These are established distributed-systems patterns, not
new ones — hedged requests and tail latency come from Dean and Barroso's *The Tail at Scale*
(2013), and caching, replication, partitioning, prefetching, precomputation and prewarming are
older still. The contribution is the taxonomy and the re-application, and the AI framing should
not make decades-old techniques read as discoveries. The piece offers **no benchmarks** — every
example is illustrative. Its cited grounding is where the substance actually lives: Pekka
Enberg's *Latency: Reduce Delay in Software Systems*, Dean and Barroso, Marc Brooker on serial,
parallel and quorum latencies, and Brendan Gregg's *Systems Performance*.

## The nineteen

| Locality | Work reduction | Concurrent execution | Anticipation |
|---|---|---|---|
| **Colocation** — place interacting components near each other | **Algorithmic work reduction** — indexes, better data structures | **Synchronisation avoidance** — remove lock contention | **Predictive prefetching** — fetch likely future reads early |
| **Replication** — readable copies in several places | **Selective data processing** — carry only the fields needed | **Independent concurrency** — run tasks with no data dependency together | **Optimistic update** — show the likely result before completion |
| **Partitioning** — divide so related data stays together | **Setup reuse** — retain parsed schemas and validated state | **Progressive response** — stream partial results as they finish | **Speculative execution** — run the probable branch before it is confirmed |
| **Caching** — shortcuts for repeated reads or computation | **Request coalescing** — combine predictable calls into one | **Concurrency budget** — cap fan-out to prevent overload | **Precomputation** — maintain aggregates as source data changes |
| | **Runtime tuning** — allocation, GC, scheduling overhead | **Hedged requests** — send equivalent copies, take the first answer | **Prewarming** — initialise capacity before requests arrive |

Two in that grid are the ones most often missing from a team's vocabulary. **Concurrency budget**
is the counterweight to independent concurrency — fanning out is the fix until it is the cause,
and the budget is what stops parallelism turning into self-inflicted overload. **Setup reuse**
is the quiet one: parsing, schema validation and connection establishment repeated per request
are pure overhead that no amount of downstream optimisation recovers.

## The AI-specific claim

The one genuinely AI-shaped argument, and it holds: teams optimise the model call and leave the
rest of the critical path unexamined. **Non-model latency** — retrieval, tool calls, schema
validation, serialisation, network hops between orchestrator and services — often dominates, and
none of it is visible in a benchmark of tokens per second.

The metric he proposes is **time to first useful result**, not full completion. That is the
quantity a user experiences, and it is what makes *progressive response* structurally more
valuable in AI applications than elsewhere: streaming a partial answer changes perceived latency
without changing total latency at all.

## Every pattern is a trade

The discipline is the part worth carrying over, more than any individual pattern. Each entry
comes with its cost:

| Pattern | What it costs |
|---|---|
| Colocation | Reduces scheduling flexibility and makes failover harder |
| Replication | Synchronous delays writes; asynchronous introduces lag |
| Request coalescing | "One slow operation [can] hold back all the others" |
| Hedged requests | "Spends extra capacity and can worsen overload" |
| Prewarming | "Consume[s] capacity even when no request uses them" |

Note the shape: several of these **make the tail worse while improving the average**. Hedging is
the clearest case — it is a tail-latency technique that becomes a tail-latency *cause* once
capacity is tight, which is precisely when tail latency is being investigated.

The closing test is the most portable line in the piece. Before applying a pattern, check
whether it **"will amplify the tail or trade away quality, freshness, privacy, cost, or
correctness."** Freshness and correctness are the two that latency work tends to spend without
noticing: caching, precomputation, optimistic update and speculative execution all buy speed
with staleness or with a guess that may be wrong.

## A note on this source

This is the seventh note here drawn from Ibryam's newsletter, alongside
[Backpressure Loops](../engineering/ai-native/agent-backpressure-loops.md),
[Skill Engineering Disciplines](../engineering/ai-native/skill-engineering-disciplines.md),
[Loop-Driven Development](../engineering/ai-native/loop-driven-development.md),
[Securing AI Agent Skills](../engineering/security/agent-skill-security.md),
[Claude Code Steering Mechanisms](../tools/claude-code-steering-mechanisms.md) and part of the
[Agentic SDLC Maturity Model](../engineering/ai-native/agentic-sdlc-maturity-model.md). The
arguments hold up individually, but a knowledge base where one newsletter supplies seven notes
is tracking a writer as much as a field. Worth weighting future sources accordingly.

## Relationship to other notes

- [Resilient Software Design](resilient-software-design.md) — the sibling frame in this folder:
  that one is designing for failure, this is designing for latency. They overlap where
  degradation is the answer to both, and they conflict where a resilience measure (retries,
  quorums, synchronous replication) is itself a latency cost.
- [Performance Testing Strategy](../engineering/practices/performance-testing-strategy.md) — the
  measurement counterpart. That note argues flat load tests against isolated endpoints hide how
  a distributed system behaves; this supplies the vocabulary for what to do once the critical
  path is visible.
- [Zalando's Client-Side Load Balancing](../case-studies/zalando-client-side-load-balancing.md)
  — several of these patterns in production at ~1M req/s, with the tail-latency and
  occupancy/Little's Law mechanics worked out rather than named.
- [Caching Reference Data in APIs](../engineering/architecture/caching-reference-data-apis.md) —
  one cell of the grid, treated in depth.
- [ChatGPT's Web Performance Architecture](../case-studies/chatgpt-web-performance.md) — the
  client-side instance: streaming, deferred imports and render-first are progressive response
  and work reduction applied to the browser's critical path.
- [Model Routing and AI Gateways](../engineering/ai-native/model-routing-and-ai-gateways.md) —
  the AI cluster's existing performance-adjacent note, which optimises *cost* by routing to the
  cheapest adequate model. This is the latency axis of the same request path, and the two
  trade against each other.
