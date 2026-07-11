---
type: case-study
title: The Product Engineer Company (Portkey)
description: "Portkey's product-engineer operating model (24 engineers, 0 PMs, 1 designer): end-to-end ownership, the barbell structure, disciplined scope, and how AI factors into reliability-critical infrastructure work"
tags: [leadership, culture, ai-engineering, reading]
topic: case-studies
status: notes
level: intermediate
related:
  - engineering/ai-native/ai-augmented-engineering-team.md
  - leadership/revised-rules-engineering-leadership.md
  - engineering/ai-native/modern-engineering-values.md
  - product/explore-vs-exploit.md
  - engineering/ai-native/model-routing-and-ai-gateways.md
  - leadership/engineering-leadership-overview.md
  - reading/factory-engineers.md
source: "https://newsletter.eng-leadership.com/p/the-product-engineer-company-how"
updated: 2026-06-27
---

# The Product Engineer Company (Portkey)

A case study of Portkey — an AI gateway/observability platform — running a
**product engineer** operating model: **24 engineers, 0 product managers, 1
designer**, where every engineer owns end-to-end decision-making rather than
receiving specs from a separate PM layer. It is the concrete, single-company
instantiation of the operating model sketched abstractly in
[The AI-Augmented Engineering Team](../engineering/ai-native/ai-augmented-engineering-team.md).

The account is from Portkey's head of GTM/CS (via Gregor Ojstersek's newsletter),
so it is one company's self-description, not a generalisable prescription.

## The product engineer

A product engineer combines engineering depth with product thinking: building
features, debugging customer issues, writing docs, and joining product
discussions across the whole lifecycle — not just coding. The claimed enabler is
the product itself: **infrastructure-heavy "plumbing for AI"** where sound
decisions require deep technical knowledge that *can't be abstracted away to a
non-technical PM*. The model is presented as fitting this domain, not as universal.

| | Traditional | Portkey |
|---|---|---|
| Roles | Engineers build, PMs decide, designers specify | Engineers decide and own end-to-end |
| Composition | Layered PM / eng / design | 24 eng · 0 PM · 1 designer |
| Accountability | Split across roles | One owner from conception to support |

## Org-design principles

- **Barbell structure** — two complementary archetypes: *deep specialists* focused
  on reliability and infrastructure stability, and *fast-moving builders* who
  prototype and ship visible features. (The structural cousin of the
  [team-topologies](../engineering/architecture/team-topologies.md) fracture-plane
  idea, applied to individual archetypes.)
- **Disciplined scope** — "every feature has to justify its place." They *rejected*
  building AI-evaluation tools despite customer demand, to stay on production-traffic
  infrastructure rather than fragmenting — "staying in their lane". This is an
  [exploit-over-explore](../product/explore-vs-exploit.md) stance made explicit.
- **Strategic direction over detailed roadmaps** — thematic evolution
  (AI gateway → MCP gateway → agent gateway) instead of a fixed annual roadmap, to
  stay flexible in a fast-moving market. Echoes the
  [plan-is-not-a-strategy](../leadership/plan-is-not-a-strategy.md) distinction.

## The AI factor

- **~40% of code is AI-generated** — deliberately *lower* than typical product
  teams, because reliability-critical infrastructure makes mistakes costly. AI
  handles repetitive work; judgement for reliability stays human.
- Daily tooling: **Claude Code and Cursor**, plus two custom **Claude Agent SDK**
  agents — one for customer task tracking, one ("Dagger") monitoring 1,600+ LLM
  prices across 80+ providers.
- **Documentation as infrastructure** — docs live as markdown in the GitHub repo
  rather than a separate tool, so agents can read the context. The same
  context-in-the-repo principle in
  [Modern Engineering Values](../engineering/ai-native/modern-engineering-values.md).

## Hiring for end-to-end ownership

- **Realistic technical interviews** — candidates may use AI tools in technical
  rounds (it reflects real work); AI use in *behavioural* rounds is treated as a
  red flag.
- **Hiring rigour** — five-to-six rounds including an on-site "super day" of
  practical problem-solving, on the basis that end-to-end ownership demands
  seniority and judgement.

## Reading

The model's viability is tied to its preconditions: a technical domain where
product decisions *are* engineering decisions, senior engineers who can own
end-to-end, and disciplined scope. It corroborates the
[revised rules of engineering leadership](../leadership/revised-rules-engineering-leadership.md)
— durable teams making fast, good decisions when execution is cheap — but as a
single data point from one infrastructure company, not proof the no-PM model
generalises to product areas where domain depth *can* be abstracted.

## Relationship to other notes

- [The AI-Augmented Engineering Team](../engineering/ai-native/ai-augmented-engineering-team.md)
  — the operating-model *framework*; this note is one company's lived *instance*.
- [Revised Rules of Engineering Leadership](../leadership/revised-rules-engineering-leadership.md)
  — durable teams + fast decisions when execution is cheap.
- [Modern Engineering Values](../engineering/ai-native/modern-engineering-values.md)
  — end-to-end ownership and context-in-the-repo as values.
- [Exploring vs Exploiting in Product Discovery](../product/explore-vs-exploit.md)
  — "staying in their lane" as a deliberate exploit posture.
