---
type: note
title: Comprehension as an Architectural Characteristic
description: "Treating shared understanding as a quality attribute that decays silently — Naur's theory-building as the grounding, and concrete fitness functions (truck factor, DOA, onboarding time) for measuring it."
tags: [architecture, ai-engineering, decision-making, documentation, reading]
topic: engineering/architecture
status: notes
level: intermediate
related:
  - engineering/ai-native/agentic-code-review.md
  - engineering/ai-native/light-and-dark-factories.md
  - reading/ai-productivity-research.md
  - engineering/architecture/architectural-change-cases.md
  - engineering/architecture/adr.md
  - engineering/ai-native/ai-gateway-control-plane.md
  - engineering/ai-native/dark-factories-examined.md
  - engineering/architecture/team-topologies.md
  - engineering/architecture/overview.md
  - engineering/ai-native/tdd-in-the-agent-loop.md
source: "https://www.infoq.com/articles/system-comprehension-evolutionary-architecture/"
updated: 2026-08-23
---

# Comprehension as an Architectural Characteristic

Jacobus Meintjes, Narayana Rengaswamy, Paul Katsande and Sureshbabu Bikki (InfoQ, August 2026)
argue that **human comprehension** — the shared mental model of why a system is built as it is
— should be treated as an architectural characteristic alongside performance and availability.

Its distinguishing property is the reason it gets neglected: **it decays silently.** Latency
regressions page someone; a shared model quietly thinning out produces no signal at all until a
production incident or a migration exposes it.

An experience report grounded in cognitive science and organisational practice rather than
quantitative study.

## Naur: the program is the theory

The grounding is Peter Naur's *Programming as Theory Building* (1985), which is not otherwise
recorded in these notes despite several of them relying on the idea.

Naur's claim is that a program is not fundamentally the source text — it is the **theory** the
developers hold about what the system does and why. The code is a residue of that theory. On
that reading, losing comprehension is not losing documentation, it is **losing the system**:
the artefact remains, but the thing that made it modifiable has gone.

That is why comprehension debt appears across these notes as an observed problem —
[Agentic Code Review](../ai-native/agentic-code-review.md),
[Light and Dark Software Factories](../ai-native/light-and-dark-factories.md) — and why it
behaves differently from technical debt. Technical debt is in the artefact and can be paid down
by working on it. Theory lives in people and leaves with them.

## Three erosion forces

1. **Decentralised decision-making** — good for autonomy, fragmenting for the global picture
2. **Team churn** — the theory holders leave
3. **GenAI** — removes the comprehension that *used to be a by-product of implementation*

The third is the new one, and it is the sharpest framing in the piece. Understanding was never
a deliverable; it accumulated as a side effect of doing the work. Remove the work and the side
effect disappears, without anything in the process noticing.

Margaret-Anne Storey's distinction is used to separate the liabilities: **cognitive debt** (lost
shared understanding, in people) versus **intent debt** (missing rationale, in artefacts). That
taxonomy is already in these notes from the peer-reviewed side — see
[Five Studies on AI Productivity](../../reading/ai-productivity-research.md) — and this is it
operationalised.

## Fitness functions for comprehension

The concrete contribution, and worth noting against the record: an
[earlier paper in the same InfoQ series](../ai-native/ai-gateway-control-plane.md) framed itself
through evolutionary architecture while supplying **no** fitness functions. This one delivers
them.

| Indicator | What to measure |
|---|---|
| **Knowledge distribution** | Degree of Authorship (DOA); truck factor via `git-truck` |
| **Onboarding friction** | Time-to-productivity for new engineers |
| **Code review dynamics** | PR size, human-reviewer requirement, distribution of who reviews what |
| **Documented intent** | ADRs required for changes at domain boundaries — see [ADRs](adr.md) |
| **Domain leakage** | Architectural constraint violations caught automatically |

**Their caveat matters as much as the list.** Metrics about people change behaviour once
enforced, so these are **investigation triggers, not gates** — a truck factor of one is a
prompt to ask why, not a build failure. And automation can measure structure but never intent
comprehension: only a human can confirm someone's understanding matches the design intent.

## The comprehension checkpoint

The practical reframe: code review stops being purely a quality gate and becomes a check that
reviewers **hold the theory** — and it works better *before* generation than after.

That is the same "judgement upstream" move
[Light and Dark Software Factories](../ai-native/light-and-dark-factories.md) argues for,
reached from a different direction. That note puts judgement upstream because a wrong call is
expensive to unwind; this puts it upstream because comprehension formed after the fact is not
really comprehension.

The associated practices:

- **Pre-generation design review** in preference to post-generation code review
- **Manual PR descriptions as comprehension probes** — their strongest specific claim:
  > The value lies entirely in producing the commit message / PR description **manually**,
  > instead of having an agent generate it automatically.
- **Engineer rotation across modules**, distributing theory rather than concentrating it
- **Lightweight ADRs at domain boundaries**, capturing rationale where it is load-bearing
- **Explicit behavioural contracts** — idempotency, retry-safety — documented beyond the API
  schema, since those are the properties a reader cannot infer from the signature

The PR-description point deserves emphasis because it inverts an obvious efficiency. Having an
agent write the description is faster and produces a better-formatted artefact; the argument is
that the artefact was never the point. Writing it is a **forcing function that verifies you
understood what you shipped** — structurally the same mechanism
[TDD Inside the Agent Loop](../ai-native/tdd-in-the-agent-loop.md) finds collapsing when an
agent performs the ritual instead of a human.

## Relationship to other notes

- [Agentic Code Review](../ai-native/agentic-code-review.md) — carries comprehension debt as a
  failure mode; this supplies the theory underneath it and something to measure.
- [Dark Factories Examined](../ai-native/dark-factories-examined.md) — the Faros finding that
  review collapsed while agents opened under 1% of PRs is comprehension erosion caught in
  telemetry, and exactly what these indicators would surface earlier.
- [Architectural Change Cases](architectural-change-cases.md) — evolving a system safely
  presumes someone understands it; comprehension is the precondition that note assumes.
- [Team Topologies](team-topologies.md) — cognitive load as the constraint on team boundaries;
  this is the same concern measured after the fact rather than designed for up front.
