---
type: case-study
title: Stripe's Kai Agent Platform
description: "Skills at scale in production: 1,000+ skills from 100+ teams, quality degrading past ~150, dynamic tool gating as the mitigation, and the sandbox exposed as a tool rather than as the execution environment."
tags: [ai-engineering, agentic-workflows, architecture, reading]
topic: case-studies
status: notes
level: intermediate
related:
  - engineering/ai-native/skill-engineering-disciplines.md
  - engineering/ai-native/harness-engineering.md
  - engineering/ai-native/cress-context-engineering.md
  - tools/claude-code-steering-mechanisms.md
  - engineering/ai-native/team-topologies-agentic-platform.md
  - engineering/ai-native/long-running-agents.md
  - engineering/architecture/primitives-over-frameworks.md
  - case-studies/microsoft-ai-core-competency.md
source: "https://www.langchain.com/blog/how-stripe-built-their-knowledge-ai-platform-on-deep-agents"
updated: 2026-08-08
---

# Stripe's Kai Agent Platform

**Kai** is a session-based conversational agent available to every Stripe employee, connecting
internal data warehouses, Slack and Google Suite to synthesise data, draft documents and
produce artifacts. Built on LangChain's Deep Agents framework.

> **Read the provenance.** This is published by LangChain about its own framework. The
> architecture is described in terms of what Deep Agents enables; alternatives Stripe weighed
> or rejected do not appear, and "one engineer built it in a week" is vendor-favourable
> framing. The figures are Stripe-supplied but vendor-selected. The technical detail is
> substantial and specific — it is simply not disinterested.

Kept here for the **skills-at-scale** material, which is the first account in these notes of
an organisation running an agent skills library large enough to break.

## Skills at scale, and where they break

| | |
|---|---|
| Skills in the library | **1,000+**, contributed by **100+ teams** |
| Internal MCP tools available | **500+** |
| Where quality degrades | past roughly **150 skills** combined with the system prompt |

That degradation threshold is the useful number. [Skill Engineering
Disciplines](../engineering/ai-native/skill-engineering-disciplines.md) treats skills as a
discipline in the abstract; this is what happens when the library outgrows the context it has
to fit in.

The mitigations:

- **Dynamic tool loading.** The model selects from available skills, and only then are the
  corresponding tools loaded via an `allowedTools` list. Tools are **gated rather than
  front-loaded** — 500+ tools are available but never all present at once. This is the
  [CRESS](../engineering/ai-native/cress-context-engineering.md) *Small* principle enforced
  structurally rather than by discipline, and the same progressive-disclosure move
  [Claude Code Steering Mechanisms](../tools/claude-code-steering-mechanisms.md) argues for
  against the gravitational pull toward one large instruction file.
- **Pinned foundational skills** that persist regardless of model-driven selection, so policy
  behaviour stays consistent no matter what the model chooses to load.

**Federated ownership** is the organisational half: individual teams maintain their own
skills rather than a platform team curating all 1,000. That is the
[agentic platform team](../engineering/ai-native/team-topologies-agentic-platform.md) pattern —
the platform supplies the mechanism, domain teams supply the content.

## The four layers

| Layer | Responsibility |
|---|---|
| **Deep Agents base** | LLM interaction primitives, request management, agent execution, middleware composition |
| **Stripe harness** | Security, infrastructure, internal service integration |
| **Configuration** | Custom agent instances with specialised skill sets |
| **UI** | The user-facing product |

The stated rationale:

> The Deep Agents layer solves all the non-Stripey problems, so that we can focus on solving
> the Stripey agent problems.

Three middleware components carry most of the behaviour:

- **Filesystem** — a virtual, S3-backed filesystem letting agents read, write and reference
  files across conversation turns via a *sync in / sync out* pattern
- **Sandbox** — isolated execution for Python analytics and file processing
- **Summarisation** — context management across multi-turn sessions, with a tunable threshold
  trading performance against cost. The context-accumulation problem
  [Long-Running Agents](../engineering/ai-native/long-running-agents.md) describes, met with an
  explicit knob.

## The sandbox is a tool, not the environment

The sharpest decision. Agents run **outside** the sandbox and call into it as a tool, rather
than executing inside it. LLM-generated code therefore never runs in the agent's own context,
and the blast radius of generated code is bounded by an interface rather than by trust.

It is worth separating this from the more common framing of sandboxing as *where the agent
lives*. Here the agent is the untrusted-code *caller*, not its neighbour.

## A counter-instance worth recording

[Primitives Over Opinionated Frameworks](../engineering/architecture/primitives-over-frameworks.md)
argues that once implementation labour is cheap, teams should keep unopinionated primitives and
drop the opinion layer. Stripe did the opposite at the agent-infrastructure layer: they adopted
an opinionated framework precisely so they would not have to build it, and report an unusually
fast path to production.

The two are reconcilable, and the reconciliation is the interesting part. Deep Agents is not
Stripe's product — it is commodity infrastructure underneath it, and the layer Stripe *does*
own is the "Stripey" one. That is the same split as
[Microsoft's *own the harness, rent the model*](microsoft-ai-core-competency.md), moved one
notch up the stack: **rent the generic agent runtime, own the organisation-specific layer.**

The general lesson is that "own it" and "rent it" are answered per layer, not per system, and
the question is always which layer encodes something only you know.

## Adoption, as reported

296 → 5,000+ users in roughly four weeks; **83% of Stripe** using it weekly across 60,000+
sessions; marketing at 95% and go-to-market teams at 87%. Notably, adoption was
engineering-driven despite the product being aimed at non-engineers.

The stated design lesson behind that:

> The whole promise of this product is you don't need to tune knobs.

— opinionated defaults and minimal configuration, on the argument that purpose-built tools for
non-technical users beat developer tools adapted downward. Plausible, though it is exactly the
conclusion a vendor selling agent infrastructure would reach.

Stripe also rebuilt internal service scaffolding for **Python** despite a decade of Ruby and
Java, justified retrospectively by Kai's speed to production — a real cost that the framing
converts into a success story.

## Relationship to other notes

- [Skill Engineering Disciplines](../engineering/ai-native/skill-engineering-disciplines.md) —
  the discipline in the abstract; this is the production instance, including the scale ceiling
  that note has no reason to anticipate.
- [Harness Engineering](../engineering/ai-native/harness-engineering.md) — the four-layer split
  is a worked example of deciding which parts of a harness to build versus adopt.
- [CRESS Principles](../engineering/ai-native/cress-context-engineering.md) — `allowedTools`
  gating is context minimalism implemented as a mechanism rather than a habit.
