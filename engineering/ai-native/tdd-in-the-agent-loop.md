---
type: note
title: TDD Inside the Agent Loop
description: "An experiment finding TDD inside autonomous agent loops produced worse solutions at 3–8× the tokens — because the discipline's forcing function and its psychology both depend on a human doing it."
tags: [ai-engineering, testing, agentic-workflows, reading]
topic: engineering/ai-native
status: notes
level: intermediate
related:
  - engineering/ai-native/scaling-ai-adoption.md
  - engineering/ai-native/loop-driven-development.md
  - engineering/practices/test-coverage-policy.md
  - engineering/ai-native/eval-driven-ai-development.md
  - engineering/ai-native/agentic-code-review.md
  - engineering/ai-native/dark-factories-examined.md
  - engineering/ai-native/harness-design-experiments.md
  - engineering/ai-native/ai-native-engineering-overview.md
  - engineering/ai-native/agent-backpressure-loops.md
  - engineering/ai-native/light-and-dark-factories.md
source: "https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html"
updated: 2026-08-23
---

# TDD Inside the Agent Loop

Birgitta Böckeler (Thoughtworks, on Martin Fowler's *Exploring Gen AI*, August 2026) ran an
experiment on whether test-driven development retains its value when an **agent** runs the
red-green-refactor cycle autonomously. Her finding: it did not, and it cost **3–8× more
tokens**.

This is an experiment rather than an argument, which is why it is worth recording — but it is
an exploratory one, and the author explicitly declines to draw firm conclusions from it. The
caveats below are hers and they are substantial.

## The setup

| | |
|---|---|
| Tasks | Three greenfield business-logic tasks (small, medium, large) with idiosyncratic requirements |
| Generation | Sonnet 4.6 |
| Evaluation | Opus 4.8, blind, across design / code / test dimensions |
| Design | 5 batches, two TDD and two non-TDD runs each, plus test-first variants |
| Regression check | Mutation testing |
| Adherence | Judged by transcript analysis |

## What it found

**Non-TDD solutions ranked #1 or #2** on the small and medium tasks; TDD solutions came
**#3–4**. Mutation scores showed no meaningful difference between them, so the TDD runs were
not even buying better regression sensitivity. Only when the prompt emphasised up-front design
did a TDD solution rank first — and its paired TDD run ranked last.

Token multipliers: **8.5×** on small tasks, **2.96×** medium, **4.89×** large. *(Cache hits
were not tracked, so these reflect context re-reads rather than pure compute.)*

## Why it does not transfer

Two mechanisms, and they are the durable content:

**TDD's benefits are substantially psychological.** Kent Beck's rationale is about *managing
fear* and experiencing progress incrementally. An agent has no fear to manage and no sense of
progress to sustain, so the half of the discipline that motivates a human simply has no
counterpart.

**The forcing function collapses.** For a human, writing the test first constrains a design
that does not exist yet — the friction *is* the value. An agent plans the implementation and
writes the test in the same breath, so nothing is being forced. The observed consequence:
non-TDD runs built a complete architecture before coding, while TDD runs locked the design into
"whatever shape the first test happened to decide."

Böckeler also cites Ivett Ördög's hypothesis: agents internalise **completed functions** from
training data rather than step-by-step processes, so incremental TDD works against the grain of
what the model has learned to produce.

## The correction this implies

[Scaling AI Adoption in the SDLC](scaling-ai-adoption.md) prescribes:

> **TDD as standard.** AI is excellent at writing code to pass a test. Tests written *first*
> form a boundary that keeps AI output honest.

This experiment is a direct test of that claim and does not support it — at least for
autonomous loops on greenfield business logic. That note now carries a pointer here.

Worth being precise about the scope, because the prescription is not simply wrong:

- The claim that **agents are good at writing code to pass a test** is not contested. What is
  contested is that making the agent *author the test first* improves the result.
- **Tests as a gate remain valuable.** The finding is about *sequencing within the agent's
  loop*, not about whether tests should exist or block. Everything in
  [Backpressure Loops](agent-backpressure-loops.md) and the CI gates elsewhere in these notes
  stands.
- A **human** writing the test first, then handing it to an agent, is a different arrangement
  from the one tested here — the forcing function is preserved because the design constraint is
  applied by someone who has not yet seen the implementation.

## What to do instead

Her alternatives are more useful than the negative result, and share a shape: **measure the
outcome rather than mandate the process.**

- **Mutation testing as a regression sensor** — check whether the tests actually detect
  changes, rather than prescribing how they were written
- **Trigger refactoring** through static analysis, modularity reviews and team rituals, since
  the red-green-refactor rhythm is not supplying it
- **Approved Scenarios** (Ördög) as a confidence-building alternative
- **Structural metrics** — files touched per change, tokens per change

That move — from process discipline to outcome measurement — is the same one
[Agentic Code Review](agentic-code-review.md) makes for review, and it fits the
green-or-red-oracle logic in [Light and Dark Software Factories](light-and-dark-factories.md):
what an agent loop needs is a signal it can be judged against, not a ritual it can perform.

## Caveats, all the author's own

- **Small sample**, three tasks, one domain: greenfield business logic
- **Quality judgement was largely Opus's discretion**, which makes the ranking a model's
  opinion rather than a measurement
- **No TDD run achieved perfect adherence** — so part of what was measured may be
  imperfectly-executed TDD
- **Mutation-score analysis was incomplete**
- **Agent prompts are volatile across model versions**, so the result is tied to a moment

Greenfield is the important one. TDD's claimed benefits are often strongest in *brownfield*
work — characterising existing behaviour before changing it — which this design does not test
at all.

## Relationship to other notes

- [Scaling AI Adoption in the SDLC](scaling-ai-adoption.md) — its TDD-as-standard prescription
  is what this contests, in the narrow case of agent-authored tests inside an autonomous loop.
- [Loop-Driven Development](loop-driven-development.md) — that note generalises TDD's loop to
  larger units and says it differs "in scale and scope, not principle". This is evidence that
  something *does* change with scale: the forcing function does not survive the generalisation,
  even if the loop shape does.
- [Eval-Driven Development](eval-driven-ai-development.md) — evals as the outcome measure that
  replaces process discipline; mutation testing plays the same role for regression sensitivity.
- [Harness Design for Long-Running App Development](harness-design-experiments.md) — the other
  measured source here, and a similar conclusion from the other direction: scaffolding that
  compensates for a model's limitations should be justified by results, not assumed.
