---
type: note
title: Harness Design for Long-Running App Development
description: "Anthropic's measured comparison of solo agents against elaborate harnesses: the planner/generator/evaluator split, sprint contracts, context anxiety, and the finding that harness complexity should shrink as models improve."
tags: [ai-engineering, agentic-workflows, architecture, reading]
topic: engineering/ai-native
status: notes
level: intermediate
related:
  - engineering/ai-native/harness-engineering.md
  - engineering/ai-native/long-running-agents.md
  - engineering/ai-native/light-and-dark-factories.md
  - engineering/ai-native/agentic-autonomy-levels.md
  - engineering/ai-native/eval-driven-ai-development.md
  - reading/building-effective-agents.md
  - engineering/ai-native/ai-native-engineering-overview.md
  - case-studies/openai-agent-first-harness.md
source: "https://www.anthropic.com/engineering/harness-design-long-running-apps"
updated: 2026-07-26
---

# Harness Design for Long-Running App Development

An Anthropic engineering report on building the same applications with a solo agent and with
progressively elaborate harnesses, with time and cost recorded for each. Unlike most writing
in this area it is **experiment-backed rather than argued** — which is the main reason to
keep it.

Two limits on the evidence, both acknowledged in the post. The work is calibrated to
**Opus 4.6**, and it notes that newer models already reduce the need for some of the
machinery described — so the specific recommendations are a snapshot, not a standing
prescription. And the quality judgements are partly subjective (they concede Claude cannot
hear audio when assessing the audio workstation), so the **cost figures are firmer than the
quality claims**.

## The architecture

The organising idea is borrowed from generative adversarial networks: **separate the thing
that makes from the thing that judges**, because a model evaluating its own work over-praises
it.

| Role | Responsibility |
|---|---|
| **Planner** | Produces the spec |
| **Generator** | Implements against it |
| **Evaluator** | Verifies, with grading criteria supplied explicitly |

This is the **evaluator–optimizer** pattern from
[Building Effective Agents](../../reading/building-effective-agents.md) applied to whole-app
development rather than a single generation step. Supporting techniques:

- **Sprint contracts** — generator and evaluator agree the success criteria *before*
  implementation starts, rather than arguing about them afterwards
- **Explicit grading criteria** in the prompt (design quality, originality, craft,
  functionality) rather than "is this good?"
- **Few-shot calibration** of the evaluator using worked score breakdowns, so its judgements
  track the ones actually wanted
- **File-based handoffs** between agents, keeping the interface structured and inspectable
- **Playwright MCP** for automated interaction testing during evaluation

## What it cost

The headline numbers, for the retro game maker:

| Approach | Time | Cost |
|---|---|---|
| Solo agent | 20 min | **$9** |
| Full harness | 6 hr | **$200** |
| Simplified harness (audio workstation) | 3.8 hr | **$124.70** |

Roughly a **22× cost multiple** for the elaborate harness over the solo agent. The output was
better — the post documents specific bugs the evaluator caught and UI improvements across
iterations — but the report is unusually direct that this is a *trade*, not a free win. These
are the only quantified harness-overhead figures recorded in these notes.

## Context anxiety

A failure mode worth naming separately: as a model approaches what it perceives as its
context limit, it **concludes the work prematurely** — wrapping up rather than finishing.

This is distinct from **context rot**, which appears throughout these notes (see
[Long-Running Agents](long-running-agents.md)). Rot is output quality *degrading* as history
accumulates; anxiety is the model *stopping early*. Different symptom, different fix — rot
argues for keeping the window lean, anxiety argues for decomposition so no single run
approaches the limit.

The related technique: **context resets beat compaction**. Resetting to a clean slate carrying
forward only what is needed outperforms summarising in place, though the post notes newer
models narrow this gap.

## The finding that cuts the other way

The most useful conclusion is the one that argues against the harness:

> Harness complexity should **decrease** as models improve.

Components that were load-bearing for one model generation stop earning their cost for the
next, and the post's advice is to re-evaluate continuously and *remove* scaffolding rather
than accumulate it. Much of the machinery described exists to compensate for model
limitations, and compensations should retire when the limitation does.

This sits in genuine tension with
[Light and Dark Software Factories](light-and-dark-factories.md), which argues the harness
alone is insufficient and that architecture and type systems must add further external safety
nets. Both are credible: Osmani is arguing about *maintainability*, which models have no
incentive toward and which does not improve with capability; Anthropic is arguing about
*capability compensation*, which does. The reconciliation is that scaffolding propping up a
weak model should retire, while scaffolding encoding what the model does not care about
should not.

## Relationship to other notes

- [Harness Engineering](harness-engineering.md) — the anatomy of a harness; this is the
  measured question of how much of it to build.
- [Long-Running Agents](long-running-agents.md) — the durability problem this harness is
  built to solve, including the self-verification wall the generator/evaluator split
  addresses.
- [Building Effective Agents](../../reading/building-effective-agents.md) — the
  evaluator–optimizer pattern that this applies at application scale.
- [Agentic Autonomy Levels](agentic-autonomy-levels.md) — the cost data is a useful check on
  climbing the autonomy ladder for its own sake.
