---
type: note
title: Model Routing and AI Gateways
description: "Smart model routing directs each LLM request to the cheapest model that is good enough for the task, instead of sending everything to one expensive frontier model."
tags: [ai-engineering, agentic-workflows, reading]
topic: engineering/ai-native
status: notes
level: intermediate
related:
  - case-studies/cloudflare-ai-code-review.md
  - case-studies/portkey-product-engineer-company.md
  - engineering/ai-native/ai-native-engineering-stack.md
  - case-studies/microsoft-ai-core-competency.md
  - case-studies/zalando-client-side-load-balancing.md
source: "https://newsletter.pragmaticengineer.com/p/the-pulse-a-new-trend-smart-model"
updated: 2026-07-05
---

# Model Routing and AI Gateways

**Smart model routing** directs each LLM request to the cheapest model that is *good enough*
for the task, instead of sending everything to one expensive frontier model. Gergely Orosz
(*The Pulse*) frames it as an emerging trend driven mainly by **cost control**: token prices
vary roughly **10–20×** between budget and state-of-the-art models, so enterprises want to
shave spend without visibly degrading quality. This note captures the durable idea from that
news issue rather than the roundup around it.

## The problem

Using a single top-tier model for every request is simple but wasteful — many tasks (routine
edits, classification, boilerplate) don't need frontier reasoning, yet pay frontier prices. The
routing thesis is that **task difficulty is uneven**, so model selection should be too. Factory
AI's CEO Matan Grinberg is quoted claiming *open models are often sufficient* and handle roughly
**60% of coding tasks** cost-effectively — a vendor estimate, not an independent measurement.

## The product landscape

The article groups the tooling into two categories (vendor cost-savings figures are the
vendors' own claims, not verified here):

| Category | Examples | What they do |
|---|---|---|
| **Dedicated routers** | Factory Router (claims 20–25% savings), Not Diamond (claims ~30%; powers OpenRouter), Prism (Augment Code), Morph's Model Router, Weave Router | Score a request and pick the optimal model per task |
| **AI gateways with routing** | OpenRouter, LiteLLM, Kilo Gateway, Requestly.ai, Envoy AI Gateway | A proxy/interface layer in front of many providers, with routing as one feature |

The implication Orosz draws: routing will likely become a **standard capability** across
gateways as enterprise cost pressure intensifies, not a differentiated product.

## Why it matters beyond cost

- **Model-agnostic interface.** A gateway lets providers and models be swapped without touching
  application code — the same *harness independence* Satya Nadella describes in
  [Microsoft's AI strategy](../../case-studies/microsoft-ai-core-competency.md) ("own the
  harness, rent the model"), and the economic backdrop of *token capital* and consumption
  pricing that makes per-request efficiency worth optimising.
- **Resilience.** Once requests flow through a routing/gateway layer, failback chains and
  provider hot-swapping come almost for free — as seen in Cloudflare's per-tier circuit
  breakers and `Opus → older-Opus` failback below.

## Relationship to other notes

- **[Cloudflare's AI Code Review System](../../case-studies/cloudflare-ai-code-review.md)** — a
  concrete instance: **model tiering** matches model strength to job difficulty (top-tier for the
  hardest reasoning), keeps provider/model choice in one swappable config, and adds failback
  chains. Routing is the general pattern; Cloudflare's tiering is one production realisation.
- **[The Product Engineer Company (Portkey)](../../case-studies/portkey-product-engineer-company.md)**
  — Portkey *is* an AI gateway/observability platform, the product category described here.
- **[The AI-Native Engineering Stack](ai-native-engineering-stack.md)** — the routing/gateway
  layer sits between the application and the model providers in that stack.
- **[Microsoft's AI Strategy — Finding Core Competencies](../../case-studies/microsoft-ai-core-competency.md)**
  — harness independence and token-capital economics are the strategic case for a model-agnostic
  gateway.
