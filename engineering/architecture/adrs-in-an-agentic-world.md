---
title: ADRs in an Agentic World
tags: [architecture, decision-making, ai-engineering, documentation, reading]
topic: engineering/architecture
status: notes
level: intermediate
related:
  - engineering/architecture/adr.md
  - engineering/architecture/agile-design-decisions.md
  - engineering/ai-native/agentic-sdlc.md
  - engineering/ai-native/ai-native-engineering-overview.md
source: "https://gshutler.com/2026/06/adrs-in-a-post-flip-world/"
updated: 2026-07-11
---

# ADRs in an Agentic World

Garry Shutler argues that agentic coding changes not what an
[ADR](adr.md) is, but **when and why** you write one. His starting point is what he
calls the **Pareto flip**: with agents doing the implementation, the classic 80/20
split inverts — thinking now accounts for most of the effort and implementation for
very little. In that world, the traditional *gatekeeping* role of the ADR falls away.

## ADRs as a purchase order

Historically an ADR functioned as a **purchase order**: reasoning committed to paper
*before* authorising expensive implementation work. It was a hedge — force the
argument up front so the team does not sink weeks into the wrong path. That discipline
made sense when building was the costly part.

When implementation becomes cheap, **the hedge goes with it**. There is less need to
pre-authorise a direction on paper, because building a candidate is now cheap enough
to be *part of how you decide* rather than a consequence of having decided.

## Write the ADR after exploring

The proposed inversion is to record the decision **after** exploration, anchored in
built evidence rather than argued in the abstract:

- Build a working **spike** for each candidate approach.
- Hold all candidates to the **same success criteria** before comparing.
- Write the ADR once exploration concludes, grounded in what the spikes revealed.

Shutler's claim is that this *increases* rigour rather than relaxing it: "an ADR
weighing three options used to mean three ideas; now it more frequently means three
spikes." Each option is a tested artifact, so the decision is "founded in reality
rather than rhetoric."

## Second-order effects

| Effect | What changes |
|---|---|
| **Wider scope** | Cheap spikes make it affordable to evaluate an interface *holistically* — including the code an integrator would have to write against each design, not just the internal implementation. This pushes toward **globally-best** rather than **locally-best** choices. |
| **Division of labour** | Agents can *draft* the ADR — translating explored context into documentation — while humans retain judgement over which decision, why, and which trade-offs are accepted. This mirrors the broader flip. |
| **ADRs as agent context** | The ADR is no longer only a record for future humans; it becomes durable context that future AI agents read to understand prior decisions. |

## Relationship to other notes

- [Architectural Decision Records (ADRs)](adr.md) — the artifact anatomy (structure,
  status lifecycle, when to write one). This note is the *economics*: how agentic
  coding shifts an ADR from a pre-authorisation gate to a post-exploration record.
- [Agile Design Decisions and Principles](agile-design-decisions.md) — cheap spikes
  effectively make more decisions **reversible** (two-way doors), because you can
  build and discard candidates; that reframes which decisions still warrant heavy
  up-front reasoning.
- [The Agentic SDLC](../ai-native/agentic-sdlc.md) — the wider cluster this belongs
  to: when code generation is cheap, leverage moves to intent, constraints, and
  judgement. Post-exploration ADRs are that principle applied to architectural
  decisions specifically.
