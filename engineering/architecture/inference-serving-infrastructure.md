---
type: note
title: Inference Serving Infrastructure
description: "The layer below the LLM application platform: prefix-cache-aware routing as the third independent arrival at route-the-work-to-the-state, a three-tier KV cache hierarchy, phase disaggregation, and a per-turn ephemeral sandbox that inverts Stripe's placement."
tags: [architecture, system-design, ai-engineering, performance, observability, reading]
topic: engineering/architecture
status: notes
level: advanced
related:
  - engineering/architecture/cell-based-architecture.md
  - case-studies/zalando-client-side-load-balancing.md
  - concepts/latency-patterns.md
  - engineering/architecture/llm-platform-engineering.md
  - case-studies/stripe-kai-agent-platform.md
  - engineering/ai-native/model-routing-and-ai-gateways.md
  - engineering/ai-native/team-topologies-agentic-platform.md
  - concepts/control-plane-data-plane.md
  - engineering/ai-native/ai-native-engineering-stack.md
  - engineering/security/governing-ai-in-the-cloud.md
  - engineering/architecture/agents-as-distributed-systems.md
  - engineering/architecture/caching-reference-data-apis.md
  - engineering/practices/performance-testing-strategy.md
  - engineering/ai-native/ai-gateway-control-plane.md
  - reading/courses.md
source: "https://cloud.google.com/blog/topics/developers-practitioners/the-open-ai-native-stack-on-kubernetes-from-open-models-to-distributed-inference-and-agents/"
updated: 2026-11-15
---

# Inference Serving Infrastructure

Abdelfettah Sghiouar and Allan Naim (Google Cloud, November 2026) describe a Kubernetes stack for
self-hosted inference: post-training, distributed serving, orchestration, and agent execution.

**This note is titled for the subject rather than the stack**, because the product list will date
and the routing and memory-hierarchy arguments will not. The components named — llm-d, OpenRL,
KubeRay, Agent Substrate, gVisor, vLLM, SGLang, Kueue, LeaderWorkerSet — are recorded where they
illustrate a mechanism, not as a recommended architecture.

> **Provenance.** Google Cloud promoting GKE, and roughly a third of the piece is that: GKE
> Inference Gateway, Managed Lustre, TorchTPU, TPU generations, a KubeCon presence. The
> open-source framing is nonetheless real — **llm-d is CNCF Sandbox**, co-founded with Red Hat,
> IBM Research, CoreWeave and NVIDIA, reportedly 500+ engineers across 25+ organisations — but
> the deployment path described runs through Google Cloud.
>
> **Every benchmark is the vendor's own, with no methodology**: KV cache hit rate 35% → 70%,
> TTFT down 70–85%, and a *Legal Agent Benchmark* moving 50% → 70% accuracy with post-training.
> That last one rests on a benchmark this note cannot verify exists independently. All figures
> below are **attributed, not relied on**.

**Where this sits, since the repo has drawn a boundary nearby.**
[Team Topologies for the Agentic Platform](../ai-native/team-topologies-agentic-platform.md)
files model hosting and fine-tuning as a complicated-subsystem that is *"optional unless doing
sovereign inference or custom optimisation"*, and [Courses](../../reading/courses.md) treats
model internals as background rather than practice. **This is on the practice side of that
line** — distributed-systems infrastructure, not model internals — but it is the first note here
aimed at teams actually running inference, and most readers of these notes will have it
encapsulated behind someone else's platform.
[LLM Platform Engineering](llm-platform-engineering.md) is the *application* serving layer above
it: hallucination flags, prompt registry, intent gates. This is the layer underneath.

## Prefix-cache-aware routing — and the third arrival at one idea

The problem named is **cache-blind load balancing**. Round-robin or least-connections scatters a
multi-turn conversation across pods, so each hop re-computes prefill against a cache that lives
somewhere else. The fix is a router — an *Endpoint Picker* — that evaluates **real-time KV cache
residency** and sends the request to the pod already holding the prefix:

```yaml
spec:
  scheduling:
    strategy: PrefixCacheAware
    fallback: LeastQueueDepth
  observability:
    kvCacheSyncInterval: "50ms"
```

Reported effect: hit rate **35% → 70%**, time-to-first-token down **70–85%** on multi-turn agent
workloads.

**This is the third independent arrival at the same principle in these notes, at three different
layers**, which is the reason to keep this note:

| Layer | The same move |
|---|---|
| **Payments** | [Cell-Based Architecture](cell-based-architecture.md) — deterministic routing to *"the cell that already has the authoritative dynamic state"*, which that note generalises as **route the work to the data rather than fetching the data to the work** |
| **Edge load balancing** | [Zalando](../../case-studies/zalando-client-side-load-balancing.md) — consistent hashing with **hash parity**, so a load-balancer cutover *"didn't move cache keys"* |
| **Inference** | prefix-cache-aware routing: the scheduler treats KV cache residency as the placement constraint |

Three teams, three domains, one conclusion: **once the expensive thing is state that is already
somewhere, routing stops being a load-distribution problem and becomes a placement problem.**

**And the caveat the piece does not make is already held here.** Zalando's note states it
directly: *"consistent hashing and isolation pull in opposite directions — you trade one benefit
for the other"*, with an explicit AZ-affinity-versus-cache-fragmentation tension. Cache-affinity
routing **concentrates load on whichever pod holds the hot prefix**, which is why the manifest
above needs a `fallback: LeastQueueDepth` at all. The fallback is the admission; the piece does
not discuss when it fires or what it costs.

It is also a good illustration that
[the nineteen latency patterns](../../concepts/latency-patterns.md) compose rather than
partition. That grid lists **Caching**, **Colocation** and **Partitioning** as three separate
Locality entries; prefix-cache-aware routing is all three at once — cache the prefill, colocate
the request with it, partition the conversation space across pods.

## The KV cache as a memory hierarchy

Three tiers, when the cache outgrows accelerator memory:

| Tier | Medium |
|---|---|
| 1 | **HBM** — accelerator memory |
| 2 | **CPU RAM** |
| 3 | **NVMe SSD / network storage** |

Ordinary systems thinking — the same shape as any cache hierarchy — applied to inference state,
which is the part that is new. And they concede the ceiling: even with three tiers, long-context
interactions still degrade. Worth holding beside
[Caching Reference Data APIs](caching-reference-data-apis.md), which is the same discipline for
slow-moving data; the difference is that KV cache is **per-conversation and write-heavy**, so
none of the long-TTL/ETag machinery there applies.

## Phase disaggregation

**EPD disaggregation** splits **Encoding, Prefill and Decode** onto separately scheduled
hardware via LeaderWorkerSet, rather than running all three on one accelerator.

The underlying observation generalises: **different phases of a single request have different
hardware profiles**, so co-locating them means sizing for the most demanding phase and wasting
the accelerator during the others. Prefill is compute-bound, decode is memory-bandwidth-bound,
and paying for one shape while running the other is the inefficiency being removed. That is the
same reasoning as the **fan-out amplification** warning in
[Performance Testing Strategy](../practices/performance-testing-strategy.md) read in reverse:
the aggregation tier is the choke point because one request becomes many, and here one request
becomes three *phases* with different costs.

## Accelerator time-slicing and delta-weight sync

For the reinforcement-learning case, the stated problem is accelerators sitting **idle during
rollout generation** — training waits on inference, so expensive hardware does nothing. Two
mechanisms:

- **Cooperative time-slicing** — training and inference share the same accelerators rather than
  holding separate pools
- **Delta-weight synchronisation** — only parameter *deltas* cross the network to rollout
  workers, not full weights

Both are classic utilisation plays, and the second is the more portable idea: **synchronise the
difference, not the state**. Dynamic Resource Allocation handles bin-packing across heterogeneous
fleets, which they admit *"requires profiling and configuration tuning"* — the usual honest
caveat on any bin-packer.

## A per-turn ephemeral sandbox — which inverts Stripe's placement

Agent security in a multi-tenant cluster: **gVisor** provides a user-space kernel intercepting
system calls, with **sub-millisecond spin-up** for an ephemeral sandbox **per agent turn**.

**This is the opposite architectural choice from the one these notes already hold, and both are in
production.** [Stripe's Kai platform](../../case-studies/stripe-kai-agent-platform.md) makes its
sharpest decision in the other direction — *"the sandbox is a tool, not the environment"*: agents
run **outside** the sandbox and call into it for isolated work.

| Placement | Consequence |
|---|---|
| **Stripe** — sandbox as a callable tool | The agent's own execution is unconstrained; isolation applies only to what it explicitly delegates |
| **Here** — sandbox as the per-turn environment | Everything the agent does is confined; the cost is a spin-up on every turn, which is why sub-millisecond matters |

Neither is wrong, and the choice follows from what you are defending against. Stripe is bounding
*user-supplied analytics code*; this is bounding **model-generated code in a multi-tenant
cluster**, where the threat is a tenant's agent reaching another tenant. The piece is also honest
that spin-up overhead is *minimised rather than eliminated* — a real cost multiplied by turn
count, and a long agent run is many turns.

## What the piece does not cover

- **No cost quantification.** *"A fraction of serving cost"* is claimed and never measured, which
  they effectively concede. For a stack whose entire argument is utilisation, that is the missing
  number — and [cost attribution as infrastructure](llm-platform-engineering.md) is the thing it
  would need.
- **No methodology for any benchmark**, including the accuracy claim resting on a Legal Agent
  Benchmark that cannot be independently checked here.
- **No cache-affinity load-skew analysis**, despite shipping a fallback strategy that exists
  precisely because of it.
- **No comparison against hosted inference.** The decision a reader faces is self-host versus
  API, and the piece assumes the answer — which is the question
  [Model Routing and AI Gateways](../ai-native/model-routing-and-ai-gateways.md) and
  [the gateway control plane](../ai-native/ai-gateway-control-plane.md) actually address.
- **Framework fragmentation acknowledged but not resolved** — they concede parallel Slurm, Ray
  and Kubernetes clusters remain costly, which is an argument *against* the consolidation story
  the piece is making.

## Relationship to other notes

- [Cell-Based Architecture](cell-based-architecture.md) and
  [Zalando's Client-Side Load Balancing](../../case-studies/zalando-client-side-load-balancing.md)
  — the same route-to-the-state principle at the payments and edge layers; Zalando also supplies
  the load-skew caveat this piece omits.
- [Latency Patterns for AI Applications](../../concepts/latency-patterns.md) — Caching,
  Colocation and Partitioning composing into one mechanism, and TTFT as the metric that matters.
- [LLM Platform Engineering](llm-platform-engineering.md) — the application serving layer above
  this one, and the home of the cost-attribution argument this piece needs.
- [Stripe's Kai Agent Platform](../../case-studies/stripe-kai-agent-platform.md) — the opposite
  sandbox placement, in production, defending against a different threat.
- [Model Routing and AI Gateways](../ai-native/model-routing-and-ai-gateways.md) — routing by
  cost and capability at the API boundary; this is routing by cache residency inside a serving
  cluster.
- [Team Topologies for the Agentic Platform](../ai-native/team-topologies-agentic-platform.md) —
  why most teams will have all of this encapsulated behind a platform rather than operating it.
- [Control Plane and Data Plane](../../concepts/control-plane-data-plane.md) — the serving stack
  is a control plane (scheduler, endpoint picker, quota) over a data plane (model replicas), with
  the 50ms cache-sync interval as the reconciliation loop.
- [Governing AI in the Cloud](../security/governing-ai-in-the-cloud.md) — self-hosted models
  inside Kubernetes as a governance surface, which is the compliance case driving this
  architecture.
