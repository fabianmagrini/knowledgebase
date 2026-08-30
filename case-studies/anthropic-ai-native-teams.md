---
type: case-study
title: Anthropic's AI-Native Team Structure
description: "Team shape held constant while concurrent projects went from 1–2 to 4–5 — and PMs reported as more critical, not less, which contradicts the no-PM product-engineer model."
tags: [ai-engineering, leadership, testing, reading]
topic: case-studies
status: notes
level: intermediate
related:
  - case-studies/portkey-product-engineer-company.md
  - leadership/revised-rules-engineering-leadership.md
  - engineering/ai-native/ai-augmented-engineering-team.md
  - case-studies/openai-agent-first-harness.md
  - engineering/ai-native/team-topologies-agentic-platform.md
  - engineering/practices/test-coverage-policy.md
  - engineering/ai-native/eval-driven-ai-development.md
  - leadership/senior-ic-role.md
  - engineering/ai-native/ci-speed-with-ai-agents.md
  - engineering/ai-native/agentic-autonomy-levels.md
  - case-studies/ramp-inspect-agent-platform.md
source: "https://newsletter.eng-leadership.com/p/how-anthropic-builds-ai-native-engineering"
updated: 2026-08-23
---

# Anthropic's AI-Native Team Structure

Gregor Ojstersek interviewing **Katelyn Lesse**, Head of Platform Engineering at Anthropic
(July 2026).

> **Read as self-description.** This is one interviewee's account of her own employer's
> practices, filtered through the newsletter's framing, partially paywalled, and citing the
> company's own product features as examples. The interviewee's own hedges are recorded below
> and are notable — she does not claim a solved problem.

## The structure did not change; the throughput did

| | |
|---|---|
| Team shape | **Two-pizza teams**: 5–8 engineers, a manager, a PM, a designer — unchanged |
| Concurrent projects per team | **1–2 previously, now 4–5** |
| Code authorship | Reported as essentially all AI-generated, with engineers owning architecture and system design |
| QA | No dedicated QA role |

**The leverage claim is specific and not otherwise recorded in these notes.** The common
framing is that AI makes individual engineers faster. This says the gain shows up as
**parallelism across projects** with team size held constant — a team of eight running four or
five workstreams rather than eight engineers each shipping more.

That is a different organisational consequence. Individual throughput scales the work a person
finishes; project parallelism scales how many *independent* things a team can hold — which is
bounded by coordination and attention rather than by typing speed.

## The disagreement about PMs

The interesting part, because these notes already hold the opposite position.

| | [Portkey](portkey-product-engineer-company.md) | Anthropic, as reported |
|---|---|---|
| Product managers | **None** — 24 engineers, 0 PMs; engineers own product end-to-end | **More critical than before** |
| Stated reasoning | Execution is cheap, so engineers can own the whole loop themselves | Execution is cheap, so *"whether teams build the right thing"* becomes the binding constraint |

**Both start from the same premise and design the opposite organisation.** Once implementation
stops being the bottleneck, the freed capacity can either be *absorbed* by engineers taking on
product judgement, or *matched* by adding more product decision-making alongside. Portkey took
the first route; Anthropic reports the second. The piece also cites OpenAI's reported **30:1
engineer-to-PM ratio**, giving three positions on one axis.

Neither source settles it, and the notes should hold both. What the disagreement suggests is
that the answer depends on something neither states explicitly — probably how much product
ambiguity the domain carries, and whether engineers have the customer contact to resolve it.

This is also [Revised Rules of Engineering Leadership](../leadership/revised-rules-engineering-leadership.md)
as an org chart: Larson argues execution got cheap, decision quality became the constraint, and
durable teams remain the unit. Preserving team shape while adding PM capacity is that thesis
implemented.

## Distributed technical leadership

Rather than one designated tech lead per team, the account describes **nearly all engineers
taking leadership as needed** — enabled by each engineer covering more ground.

Read against [The Senior IC Role](../leadership/senior-ic-role.md), which describes senior ICs
setting technical direction and leading initiatives, this suggests those responsibilities
spreading rather than concentrating. Whether that survives contact with a larger or less
experienced organisation is not addressed.

Engineers are described as **tech-agnostic** — the constraint is no longer familiarity with a
particular stack.

## Testing without a QA function

- **Weighted to unit tests**, following the traditional pyramid, explicitly to avoid CI
  becoming a bottleneck — consistent with
  [Test Coverage Policy](../engineering/practices/test-coverage-policy.md) and with
  [CI Speed When Agents Write the Code](../engineering/ai-native/ci-speed-with-ai-agents.md)
- **Model evaluations before release**, which is
  [eval-driven development](../engineering/ai-native/eval-driven-ai-development.md) as a
  release gate rather than a development practice

The **Outcomes** feature in Claude Managed Agents is cited as an example: agents assess whether
what they produced meets the stated success criteria and iterate. That is the measurable
stopping condition described in
[Agentic Autonomy Levels](../engineering/ai-native/agentic-autonomy-levels.md), productised.

A **prod ops** function is described as optimising systems and processes for decision-making
velocity — an operational role aimed at the constraint the rest of the structure assumes.

## The hedges, which are the interviewee's own

- *"They don't believe they have found a perfect formula"*
- This does **not** mean *"AI is building software on its own"* — engineers retain
  architectural and system-design ownership
- Continuous adjustment is described as the current state rather than an arrived-at model

Worth weighting those, because the headline figures — all code AI-generated, 4–5 concurrent
projects — invite a stronger reading than the interview supports.

## Relationship to other notes

- [The Product Engineer Company (Portkey)](portkey-product-engineer-company.md) — the direct
  counterpoint on PMs, from the same newsletter and the same premise.
- [Revised Rules of Engineering Leadership](../leadership/revised-rules-engineering-leadership.md)
  — durable teams plus decision quality as the scarce good; this is that argument as a
  reported org structure.
- [OpenAI's Agent-First Harness](openai-agent-first-harness.md) — the other lab's account,
  focused on the harness rather than the team shape; both report near-total AI authorship with
  humans holding architecture.
- [The AI-Augmented Engineering Team](../engineering/ai-native/ai-augmented-engineering-team.md)
  — the operating model in the abstract; this is one reported instance of team composition
  under it.
