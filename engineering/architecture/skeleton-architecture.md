---
type: note
title: Skeleton Architecture
description: "structural guardrails for AI-generated code: a human-designed immutable skeleton (base classes, contracts, security context) that constrains AI-generated tissue, enforced by the Template Method pattern, schema-first contracts, and compile-time topology checks"
tags: [architecture, ai-engineering, system-design, agentic-workflows, reading]
topic: engineering/architecture
status: notes
level: intermediate
related:
  - engineering/architecture/design-systems-ai-control-plane.md
  - engineering/architecture/generative-ui.md
  - engineering/architecture/thinking-in-constraints.md
  - engineering/ai-native/cress-context-engineering.md
  - engineering/ai-native/agentic-sdlc.md
source: "https://www.infoq.com/articles/skeleton-architecture/"
updated: 2026-07-19
---

# Skeleton Architecture

Patrick Farry (InfoQ, reviewed by Thomas Betts) argues that reliable AI-assisted
code generation needs **structural guardrails in the code itself**, not just better
prompts. The proposal is to split a system into an immutable **skeleton** — the
abstractions, contracts, and cross-cutting concerns humans design — and flexible
**tissue** — the concrete implementations AI generates *within* the skeleton's
constraints. Where [Design Systems as the AI Control Plane](design-systems-ai-control-plane.md)
applies this idea to UI, skeleton architecture is the general-code equivalent for
backend and business logic.

## Skeleton vs tissue

| Layer | Who writes it | What it is |
|---|---|---|
| **Skeleton** | Architects (human) | Abstract base classes, interfaces, security context, schemas — immutable, controls execution flow |
| **Tissue** | AI | Concrete implementations, business logic, feature code — fills the gaps the skeleton leaves open |

The mechanism Farry highlights is the **Template Method pattern**: the base class
locks a `final run()` method that handles cross-cutting concerns (auth, logging,
scheduling, resource lifecycle) and calls a protected `_execute()` that the AI
implements. The AI can only fill the one hole left for it; it cannot override the
workflow around it.

## Why AI specifically needs this

The article frames AI as a *high-speed stochastic engine optimising for completion*
— not a learner that understands system invariants. Left unconstrained it
optimises locally and produces architectural drift. Three limitations motivate the
constraint layer:

- **Context constraint** — minimising the information scope the model must hold at
  once. Farry cites the *"Lost in the Middle"* finding (Liu et al.) that LLM
  accuracy degrades as context lengthens; a skeleton isolates dependencies so the
  model reasons over less. This is the *Small* property from
  [CRESS context engineering](../ai-native/cress-context-engineering.md) enforced
  structurally.
- **Blank-page problem** — a skeleton turns open-ended generation into
  *fill-in-the-blanks*, replacing an unbounded prompt with a bounded gap.
- **Hallucinated cross-cutting logic** — templates prevent the model from inventing
  its own security or scheduling logic; those live in the skeleton.

## Hard guardrails

The distinctive claim is that guardrails must be **physically difficult for AI to
bypass**, not advisory. Prose conventions are invisible to an agent (the same point
`design-systems-ai-control-plane.md` makes about codifying design rules). Concrete
mechanisms:

- **Schema-first contracts** — JSON Schema + OpenAPI/AsyncAPI as the inviolable
  source of truth for interfaces.
- **Fail-fast validators** — a contract violation calls `sys.exit(1)`; the crash
  forces human intervention rather than letting bad output through.
- **Compile-time topology enforcement** — tools like **ArchUnit** assert
  architectural rules ("no AI-written module imports the database directly").
- **Read-only skeleton repository** — base classes live in a separate,
  permission-restricted repo the AI cannot modify.
- **Framework-level safety nets** — e.g. weak-reference / memory monitoring to catch
  AI-generated leaks, and test harnesses that isolate the functional core (tissue)
  from side effects (skeleton) so AI-generated tests are reliable.

## Why other patterns fall short alone

Farry positions skeleton architecture against two existing decompositions, arguing
each is necessary but insufficient for AI generation:

| Pattern | Strength | Gap for AI |
|---|---|---|
| **Atomic design** (atoms → molecules → organisms) | Clean micro-components | Shifts integration burden back to humans |
| **Vertical slice architecture** | Excellent feature locality | Duplication and **governance drift** — inconsistent security postures across slices |

The skeleton supplies the shared, enforced backbone those patterns lack when a
stochastic engine is filling in the parts.

## The skill shift

The pattern reframes the engineer's role. Rather than translating syntax, engineers
own **systems modelling, contracts, and nonfunctional requirements**, and act as a
**director** monitoring AI output with "extreme vigilance". Farry contrasts the
domain judgement senior engineers accumulate — "scar tissue" from experience — with
a model that has completion skill but no such judgement. This is the
[agentic-SDLC](../ai-native/agentic-sdlc.md) through-line: when generation is cheap,
leverage moves to intent, constraints, and judgement.

## Relationship to other notes

- [Design Systems as the AI Control Plane](design-systems-ai-control-plane.md) — the
  *UI-specific* version of the same idea (codified primitives as the constraint
  layer); skeleton architecture is the general-code sibling for backend/business
  logic.
- [Generative UI](generative-ui.md) — its whitelisted component registry is a
  sibling *hard guardrail*: a constrained set of approved building blocks AI must
  compose from.
- [Thinking in Constraints](thinking-in-constraints.md) — skeleton architecture is
  constraints made executable; the skeleton *is* the binding constraint the design
  is built around.
- [CRESS Principles for Context Engineering](../ai-native/cress-context-engineering.md)
  — the *Small* and *Specific* context properties this operationalises structurally
  rather than through prompt wording.
- [The Agentic SDLC](../ai-native/agentic-sdlc.md) — the wider shift the director
  role and constraint-first design belong to.
