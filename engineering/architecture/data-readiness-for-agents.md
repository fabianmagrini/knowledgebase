---
type: note
title: Data Readiness for Agents
description: "Human scepticism was invisible labour in every data pipeline; agents supply none of it. Data contracts with freshness SLAs, three context models, 'retrieved text informs, it never gates', and quality signals rather than model confidence as the routing gate."
tags: [architecture, ai-engineering, governance, reading]
topic: engineering/architecture
status: notes
level: intermediate
related:
  - engineering/practices/api-contract-functional-testing.md
  - engineering/ai-native/agentic-autonomy-levels.md
  - engineering/architecture/reversibility-decays.md
  - engineering/ai-native/cress-context-engineering.md
  - engineering/security/agent-skill-security.md
  - engineering/ai-native/ai-gateway-control-plane.md
  - engineering/architecture/runtime-architecture-verification.md
  - case-studies/oracle-ai-agent-memory.md
source: "https://martinfowler.com/articles/making-data-ready-for-agentic-ai.html"
updated: 2026-08-30
---

# Data Readiness for Agents

Pramod Sadalage and Prem Chandrasekaran (Thoughtworks, August 2026) argue that data
architectures built for human analysts fail autonomous agents, and the reason is a single
asymmetry:

> "A human hesitates at data that looks wrong; an agent acts on it anyway."

The framing worth keeping is that **human scepticism was invisible labour inside every data
pipeline**. Analysts noticed stale values, knew the fiscal calendar differed from the
Gregorian one, and paused when a number looked implausible. None of that was ever written
down, because it did not need to be. Remove the human and that work does not disappear — it
becomes a gap, and it has to be reconstructed explicitly in the architecture.

This is the repo's first note on data as a platform concern. The
[AI-native cluster](../ai-native/ai-native-engineering-overview.md) is almost entirely about
generating *code*; this is about the data the resulting agents act on.

## The five attributes, in dependency order

Their layering, with the argument that readiness is **capped by your weakest foundational
layer** — you cannot buy context on top of untrusted data.

| Layer | Attribute | What it requires |
|---|---|---|
| 1 | **Trusted** | Data contracts, schema as code, freshness SLAs, quarantine of violations |
| 2 | **Traceable & governed** | Lineage capturing *why*, staged autonomy, just-in-time credentials |
| 3 | **Contextual** | Domain, semantic and capability models |
| 4 | **Operational** | Retrieval → real-time query → write-back, exposed as capabilities |

## Contracts and the freshness subtlety

Schema enforced as code (they point to the Open Data Contract Standard), checked in CI, with a
**quarantine pattern** routing violations to a dead-letter queue *before* anything reaches an
agent. Agents read from the Gold tier only — Silver carries validation, Bronze is raw.

The detail worth extracting is how freshness is defined: **keyed to successful refresh timing,
not to content changing**. A table that legitimately did not change is fresh; a table whose
refresh silently failed is stale and looks identical from the content side. Content-based
staleness checks conflate the two, and the failure mode is exactly the one the article is
about — an agent confidently reasoning over a pipeline that stopped running on Tuesday.

Data contracts are the same instrument as
[API contracts](../practices/api-contract-functional-testing.md) pointed at a different
boundary: a machine-checkable agreement between producer and consumer, enforced in CI rather
than negotiated after an incident.

## The three context models — and the rule under them

| Model | What it holds |
|---|---|
| **Domain model** | Entities and their relationships |
| **Semantic model** | Metrics as code — business definitions version-controlled like software |
| **Capability model** | Which operations are permitted, with preconditions |

The semantic model resolves natural language into **constrained SQL** rather than letting a
model compose queries freely, which is where a plausible-looking wrong answer usually enters.

The load-bearing principle, and the most portable line in the piece:

> **"Retrieved text informs, it never gates."**

Business rules get extracted into code. Retrieved prose can supply background, but must never
be the thing that decides whether an action proceeds — because a rule interpreted from text at
action time is a rule an agent can reason its way around, and because whoever can influence the
retrieved corpus can then influence the decision. This is the
[gate versus rule](../ai-native/agent-backpressure-loops.md) distinction applied to context.

## Quality signals as the gate, not model confidence

The inversion worth recording. **Confidence-threshold routing keyed to data-quality signals**:
any contract or SLA breach forces human involvement, *overriding* the model's own certainty.
A model's confidence is a statement about its output; a contract breach is a fact about its
input, and the second should win.

The authors are honest that the composite version is unsolved — start with **hard gates** (any
breach escalates) rather than attempting weighted confidence scores until there is evidence to
support the weights.

They also propose **reversibility classes** as a better predictor for autonomy escalation than
transaction size: cleanly reversible actions earn autonomy faster than irreversible ones,
regardless of value. That sits directly on
[Reversibility Decays](reversibility-decays.md) — if the cost of exiting a decision only rises
over time, an autonomy level granted on today's reversibility is a claim with a shelf life.
The staged progression itself (shadow → supervised → guardrailed → autonomous) is the same
ground as [Agentic Autonomy Levels](../ai-native/agentic-autonomy-levels.md), which treats it
in more depth.

## Access design: capabilities, not wrappers

For the operational layer: design **5–10 well-described business capabilities**, not 50 thin
API wrappers. Naive one-to-one API-to-MCP conversion is on Thoughtworks' Radar at **HOLD**.

The reasoning generalises beyond MCP. An interface auto-derived from an existing API surface
inherits decisions made for a different consumer — pagination shapes, CRUD granularity, field
names meaningful only to the team that built them — and pushes the work of composing them into
the agent, which is the least reliable place for it. Start read-only: **MCP Resources before
Tools**, with write access earned.

## The security frame

**The lethal trifecta** (Simon Willison): agent access to private data + exposure to untrusted
content + the ability to communicate externally. Any two are manageable; all three together
constitute the exposure. Worth holding beside
[Securing AI Agent Skills](../security/agent-skill-security.md), which treats the supply-chain
half of the same problem.

**Regulatory grounding**, which these notes otherwise lack entirely: EU AI Act Articles 12 and
19 require automatic logging sufficient to reconstruct a system's operation over its lifetime,
retention of at least six months, and demonstrable reasoning chains, with penalties up to €15M
or 3% of global turnover. The authors characterise these as regulatory teeth rather than
hypothetical risk. This is what makes **agentic lineage** — audit trails capturing not what an
agent queried but *why* — a compliance artefact rather than a nice-to-have.

## Numbers to attribute rather than believe

- **"Accuracy jumps from ~20% to >92% with a semantic layer"** cites an **AtScale** benchmark.
  AtScale sells a semantic layer, so this is a vendor benchmarking the value of its own product
  category. The direction is plausible and the magnitude is not independent.
- The **87% of leaders believe their data is AI-ready / 43% cite data readiness as their biggest
  barrier** paradox comes from self-reported surveys (Precisely/Drexel LeBow; KPMG). It is a
  nice rhetorical closing — an organisation "sure of itself and wrong" — but it is opinion data,
  and the two figures may simply come from different respondents.

## What the authors concede

Carrying these keeps the framework honest:

- **Confidence-threshold scoring is unsolved.** Hard gates first; weighted composites only when
  evidence supports the weights.
- **The "Adaptive Gold" tier — agents curating datasets — is extrapolation.** Agents curating
  catalogues exist; applying it to the datasets themselves is forward-looking, not mainstream.
- **Knowledge graphs are supplementary,** not foundational: GraphRAG and Graphiti add
  relationship-traversal depth beyond fixed joins at the cost of separate infrastructure.
- **Ownership is the part no tool solves.** Data as a product with named owners, published SLAs
  and versioned lifecycles is "the operating model that keeps it honest".

## Relationship to other notes

- [API Spec, Contract, and Functional Testing](../practices/api-contract-functional-testing.md)
  — the same instrument at a different boundary. Data contracts are to pipelines what consumer
  contracts are to services.
- [Agentic Autonomy Levels](../ai-native/agentic-autonomy-levels.md) — holds the staged-autonomy
  progression in more depth. The addition here is that the *data* layer supplies a gating signal
  independent of the agent's own confidence.
- [Reversibility Decays](reversibility-decays.md) — reversibility classes as an autonomy
  predictor, with the caution that reversibility is maintained rather than assessed once.
- [CRESS Principles for Context Engineering](../ai-native/cress-context-engineering.md) — context
  quality for code generation; this is context quality for data access, and "retrieved text
  informs, it never gates" is a constraint CRESS does not impose.
- [Securing AI Agent Skills](../security/agent-skill-security.md) — the supply-chain half of
  agent security; the lethal trifecta is the data-access half.
- [The AI Gateway as a Governance Control Plane](../ai-native/ai-gateway-control-plane.md) — the
  same governance concerns concentrated at the model-call seam rather than the data seam.
- [Runtime Architecture Verification](runtime-architecture-verification.md) — the sibling
  argument about observing what a system actually does; agentic lineage is that idea applied to
  data access, with the EU AI Act as the forcing function.
- [Oracle AI Agent Memory](../../case-studies/oracle-ai-agent-memory.md) — a vendor
  implementation of governed, provenance-carrying agent memory: "memory with receipts" is one
  product's answer to the traceability layer described here.
