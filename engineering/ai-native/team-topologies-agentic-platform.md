---
type: note
title: Team Topologies for the Agentic Platform
description: "Olivier Wulveryck applies Skelton & Pais's Team Topologies to an organisation built around an agentic platform — the \"agentic factory\" where AI agents plan, code, test, and ship."
tags: [ai-engineering, agentic-workflows, leadership, architecture, reading]
topic: engineering/ai-native
status: notes
level: intermediate
related:
  - engineering/architecture/team-topologies.md
  - engineering/ai-native/ai-augmented-engineering-team.md
  - engineering/ai-native/agentic-sdlc-maturity-model.md
  - engineering/architecture/design-systems-ai-control-plane.md
  - engineering/security/governing-ai-in-the-cloud.md
  - leadership/scaling-engineering-org.md
source: "https://blog.owulveryck.info/2026/06/24/who-does-what-team-topologies-for-the-agentic-platform.html"
updated: 2026-07-05
---

# Team Topologies for the Agentic Platform

Olivier Wulveryck applies Skelton & Pais's [Team Topologies](../architecture/team-topologies.md)
to an organisation built around an **agentic platform** — the "agentic factory" where AI agents
plan, code, test, and ship. His framing: the platform determines *what* systemic capabilities are
needed; Team Topologies answers *who* provides them and *how* teams interact. The four team types
and three interaction modes still hold, but their composition and boundaries shift.

## Cognitive load becomes an anticipation burden

Traditional development spreads complexity across roles and time. An agent generates output
instantly, so all the anticipated decisions compress into a single prompt window. The author
reframes cognitive load as two new burdens on one person:

- **Anticipation burden** — everything the human must foresee *before* launching the agent.
- **Cognitive throughput** — sustaining a high-velocity flow of decisions.

A mature platform *absorbs* the anticipation burden by being **queryable by agents**, narrowing
human judgement to the "contested, structural decisions." This is the same bottleneck shift as in
the [AI-augmented engineering team](ai-augmented-engineering-team.md) — from typing to intent and
constraint — viewed through an organisational-structure lens.

## The four team types, re-mapped

| Team type | Adapted role | Key shift |
|---|---|---|
| **Stream-aligned** | Drive production through an AI orchestrator; supply *dynamic context*, specs, and guardrails | **Becomes non-technical** — domain experts and PMs, not engineers; the platform absorbs operations and incident management |
| **Platform** | Provide *systemic context*, deterministic guardrails, agentic tooling (MCP servers, CI/CD), execution engines | Strict self-service; treated as a living product with its own backlog and PO |
| **Enabling** | Environment provisioning, agent training, manual shift-left enforcement | A **permanent** structural role (you can't fully upskill non-technical teams); shrinks to on-demand consultancy as the platform matures |
| **Complicated-subsystem** | Deep AI infrastructure — model hosting, RAG optimisation, fine-tuning, red-teaming, evaluation | Optional unless doing sovereign inference or custom optimisation; encapsulated entirely behind the platform |

The **non-technical stream-aligned team** is the article's central inversion of standard Team
Topologies, and it only works once platform maturity is high enough (below).

### Dynamic vs systemic context

- **Dynamic context** — business-specific specifications, product guardrails, and domain knowledge,
  owned by the **stream-aligned** team.
- **Systemic context** — global business knowledge, architectural patterns, organisational
  guardrails, and shared capabilities, owned by the **platform**.

Every capability has one accountable owner and multiple contributors; concerns are split along
this dynamic/systemic seam.

## Deterministic guardrails and platform maturity

The inversion depends on the platform meeting hard criteria — until then, **enabling teams bridge
the gap by manual enforcement**:

- **Hardcoded (deterministic) guardrails** — deterministic enforcement of security, compliance, and
  brand, *not* a stochastic agreement with an LLM.
- **Measurable reliability** against internal SLAs.
- **High self-service index** — zero platform intervention for the common path.
- **Agent-readable documentation** with examples.
- **Decision traceability and audit trails.**

The deterministic-vs-stochastic distinction is the platform-team counterpart to the
[design system as an AI control plane](../architecture/design-systems-ai-control-plane.md): a hard
constraint layer that makes agent output safe at scale.

## Interaction modes evolve along two maturity axes

| Mode | When | Who |
|---|---|---|
| **Facilitating** | Early, hands-on | Enabling team coaches stream-aligned teams on safe platform use |
| **X-as-a-Service** | Target state | Platform delivers capabilities via self-service |
| **Collaboration** | Integrating deep capability | Complicated-subsystem team integrates with the platform, evolving toward X-as-a-Service |

The evolution is driven by two parallel axes — **team maturity** (mastering context packaging and
orchestrator operation) and **platform maturity** (expanding guardrails, docs, deterministic
controls). As platform self-service grows, the enabling team's presence shrinks. This mirrors the
[Agentic SDLC Maturity Model](agentic-sdlc-maturity-model.md): the curve is about how much entropy
the organisation can absorb and how deeply governance is encoded.

## Governance patterns

- **Rule of Three** — borrowing Fowler's refactoring heuristic: once a guardrail is duplicated
  across three teams, it graduates into a platform capability.
- **The Bottleneck Paradox** — platform success can recreate cognitive overload, this time on the
  *platform PO*, unless automation handles detection and prioritisation of graduation candidates.
- **Application governance** — portfolio oversight (active/abandoned apps, usage metrics,
  deprecation) to prevent *industrialised shadow IT*. The author connects this to **computational
  governance** from the Data Mesh world, applied to agentic application portfolios.

### Target-state example

A marketing team generates landing pages by supplying campaign intent; the platform injects brand
guidelines and accessibility rules; deterministic guardrails verify compliance — all without
marketing understanding the CI/CD pipeline. The enabling team, heavily present early on, is reduced
to occasional edge-case support.

## Relationship to other notes

- **[Team Topologies and Socio-Technical Architecture](../architecture/team-topologies.md)** —
  supplies the underlying model (four team types, three interaction modes, cognitive load, Conway's
  Law). This note is a specific *application* of that theory to the agentic platform, not a
  restatement.
- **[The AI-Augmented Engineering Team](ai-augmented-engineering-team.md)** — the sibling operating
  model. That note covers role recomposition, Intent Specs, and the delivery loop; this one covers
  the *organisational structure* (non-technical stream-aligned teams, guardrail graduation, the
  bottleneck paradox) via Team Topologies.
- **[Agentic SDLC Maturity Model](agentic-sdlc-maturity-model.md)** — the maturity curve the
  interaction-mode evolution rides on.
- **[Design Systems as the AI Control Plane](../architecture/design-systems-ai-control-plane.md)** —
  the deterministic-guardrail / constraint-layer idea, seen from the platform-team side.
