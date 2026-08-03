---
type: case-study
title: Slack AI's Path to Multi-Cloud
description: "Four phases from SageMaker to AWS+GCP: the capacity economics behind provisioned vs on-demand throughput, the spillover pattern, an intelligent routing layer with per-feature backup models, and the operational price of provider agnosticism."
tags: [ai-engineering, architecture, observability, reading]
topic: case-studies
status: notes
level: intermediate
related:
  - engineering/ai-native/model-routing-and-ai-gateways.md
  - engineering/ai-native/ai-gateway-control-plane.md
  - case-studies/cloudflare-ai-code-review.md
  - case-studies/microsoft-ai-core-competency.md
  - concepts/resilient-software-design.md
  - case-studies/slack-agentic-e2e-testing.md
  - engineering/practices/feature-flags-and-branch-by-abstraction.md
source: "https://slack.engineering/slack-ai-the-path-to-multi-cloud/"
updated: 2026-08-03
---

# Slack AI's Path to Multi-Cloud

Shaurya Kethireddy (Slack, May 2026) on how Slack AI's serving infrastructure moved from a
single managed service to orchestrating models across AWS and Google Cloud. An engineering
experience report with named technologies, specific figures and a candid trade-off list; the
metrics are Slack's own.

## The four phases, and what forced each

The useful structure is that every phase is a response to a problem the previous one created.

| Phase | What it was | What forced the move on |
|---|---|---|
| **SageMaker** | Self-managed model serving inside a zero-knowledge VPC | Scaling latency, GPU scarcity, over-provisioning, and lag before new models were available |
| **Bedrock** | Fully managed serving; **Model Units** and Provisioned Throughput as the capacity abstraction | Paying for provisioned capacity that sat idle outside peak hours |
| **Bedrock Hybrid** | Provisioned Throughput for latency-sensitive traffic, On-Demand for bursty traffic, joined by a **spillover pattern** | Single-provider outage risk; wanting models only available elsewhere |
| **Multi-cloud** | AWS plus Google Cloud Vertex AI, with routing between them | — |

**The capacity economics are the part least covered elsewhere in these notes.** Provisioned
throughput buys predictable latency at the cost of paying for a fixed ceiling; on-demand
absorbs bursts but with variable latency. Spillover runs the steady, latency-sensitive
baseline on provisioned capacity and lets overflow spill to on-demand. Notes such as
[Model Routing and AI Gateways](../engineering/ai-native/model-routing-and-ai-gateways.md)
treat "a gateway" as an abstraction; this is the operational reality inside it.

## The intelligent routing layer

What sits between features and providers:

- **Metric-driven model selection** — routing decided from real-time telemetry rather than static config
- **Automated circuit breakers** — unhealthy provider or model paths are cut out without human intervention (see [Resilient Software Design](../concepts/resilient-software-design.md))
- **A designated backup model for every feature**, with continuous health monitoring
- **An API normalisation layer** translating each provider's differing signals into a common vocabulary

That last item is the concrete price of provider agnosticism. "Swap providers without touching
application code" is cheap to say; the normalisation layer is where the cost lands, and it has
to be maintained against every provider's independent evolution.

Migrations were run behind **feature flags with A/B testing** and gradual rollout — reported as
zero customer-facing incidents across the transitions. This is
[branch by abstraction](../engineering/practices/feature-flags-and-branch-by-abstraction.md)
applied to model providers: the abstraction layer is what makes the swap survivable.

## Reported results

Self-reported, and specific:

| | |
|---|---|
| Quality improvement on reasoning tasks | **~10%** |
| Latency reduction, high-velocity low-token workloads | **~67%** |
| Customer-facing incidents during migrations | **zero** |

The latency figure comes from matching workloads to better-suited models, not from removing
infrastructure — worth separating from the added hop that any centralised routing layer
introduces.

## Routing is not only a cost play

Worth recording as a corrective. [Model Routing and AI Gateways](../engineering/ai-native/model-routing-and-ai-gateways.md)
frames routing as driven mainly by **cost** — Orosz's 10–20× spread between budget and frontier
token prices. Slack's stated drivers are different:

- **Infrastructure redundancy** — removing the single point of failure
- **Model-to-feature matching** — different models are better at different jobs
- **Access to vendor-exclusive innovations**
- **Dynamic orchestration** from live telemetry

Cost barely features. Read together, the two notes say routing earns its place on reliability
and capability grounds even where the token-price arbitrage is uninteresting.

## What it cost them

The trade-off list is candid, and is the argument against copying this at smaller scale:

- **Operational complexity rose significantly** — API friction, unified monitoring across
  providers, and cost attribution that no longer maps cleanly to one bill
- **Provider-agnostic expertise is required**, and **on-call knowledge gaps emerged** — an
  underrated cost, since the people carrying the pager now need working models of two
  providers' failure behaviour
- **Cross-functional alignment** with Security, Legal and Compliance became a prerequisite
  rather than a formality

## Stated lessons

1. Cross-functional alignment (legal, compliance, security) is essential to scaling AI
2. **Abstraction layers matter more than specific model choices**
3. Treat the architecture as continuously evolving, not a destination
4. Provider agnosticism is what makes resilience real
5. **Redefine "failure" to include performance degradation, not just uptime** — *soft failures*

The second and fifth transfer furthest. The abstraction-layer point is the same conclusion
Satya Nadella reaches from strategy in
[Microsoft's AI Strategy](microsoft-ai-core-competency.md) — *own the harness, rent the model*
— arrived at here from operations. And redefining failure to include degradation is what makes
the circuit breakers meaningful: a provider that is up but slow is a failure this system has to
detect and route around.

## Relationship to other notes

- [Model Routing and AI Gateways](../engineering/ai-native/model-routing-and-ai-gateways.md) —
  the trend and product landscape; this is one organisation implementing it end to end, and a
  corrective to that note's cost-first framing.
- [The AI Gateway as a Governance Control Plane](../engineering/ai-native/ai-gateway-control-plane.md) —
  the same seam justified on governance grounds. Slack's layer is built for reliability and
  routing; that note's version adds identity, action policy and audit to the same position in
  the architecture.
- [Cloudflare's AI Code Review System](cloudflare-ai-code-review.md) — model tiering and
  failback *within* a provider; this is the same reasoning extended across providers.
