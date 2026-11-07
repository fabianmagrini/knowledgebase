---
type: note
title: TDD Inside the Agent Loop
description: "Böckeler's experiment finding agent-run TDD ranked below non-TDD at 3-8x the tokens, the two mechanisms for why it does not transfer — and the methodology side, where Example Mapping before any prompt is the one component that survives the critique, plus a three-level pause-point ladder."
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
  - engineering/architecture/comprehension-as-architecture.md
  - engineering/ai-native/review-replacement.md
  - engineering/ai-native/brownfield-agentic-engineering.md
  - engineering/ai-native/agentic-verification.md
  - engineering/ai-native/spec-driven-development.md
  - product/four-abstraction-levels-of-refinement.md
  - engineering/ai-native/agentic-autonomy-levels.md
  - case-studies/meta-forum-ai-native-build.md
  - engineering/ai-native/accountability-for-unread-code.md
  - case-studies/cursor-agent-swarm-economics.md
source: "https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html; https://www.codecentric.de/en/knowledge-hub/blog/exact-coding-with-ai"
updated: 2026-11-07
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

## The methodology side, and the one part of it that survives this

[EXACT Coding](https://www.codecentric.de/en/knowledge-hub/blog/exact-coding-with-ai) (Marco
Emrich and Ferdinand Ade, codecentric, April 2026) is the prescriptive counterpart to the
experiment above: **Ex**ample-guided, **A**I-**C**ollaborative, **T**est-driven Coding, as a
seven-step workflow whose steps 4–7 are the red-green-refactor cycle run by an agent.

> **It is a method, not a finding.** There is **no evidence of any kind** in the piece — no
> measurement, no experiment, no case data — and it comes with a Leanpub book and full-day
> workshops attached. Its central claim, *"quality can still be ensured even with high AI
> usage — the question is less 'less AI' and more about what guardrails you set"*, is asserted
> rather than shown, and the specific guardrail it prescribes is the one the experiment above
> tested and ranked **#3–4 against non-TDD's #1–2** at **3–8× the tokens**. Carried for two
> components, not for the loop.

**Example Mapping is the component that answers this note's own diagnosis.** EXACT's step 2 is a
*"short workshop with story, rules, examples, and open questions"*, held **"before the first line
of code or the first prompt is written"**, converted in step 3 into an organised test list.

That is exactly the arrangement flagged above as preserving the forcing function: a **human
authoring the examples before an implementation exists**. The collapse described earlier happens
because the agent plans the implementation and writes the test in the same breath; examples
agreed in a workshop cannot be reverse-engineered from code that has not been written. Example
Mapping is a pre-existing BDD practice — not an invention here — and naming it closes the gap
this note left open, which was *what to do instead of asking the agent to write the test first*.
It belongs with [spec-driven development](spec-driven-development.md)'s formality spectrum and the
problem-before-solution sequencing in
[The Four Abstraction Levels of Refinement](../../product/four-abstraction-levels-of-refinement.md),
whose level 1 is the same artefact under another name.

**The autonomy levels are a pause-point ladder these notes did not hold:**

| Level | Where the human interrupts |
|---|---|
| **A** | *"The agent works through the test list largely on its own; review at the end"* |
| **B** | *"Pause after every complete Red–Green–Refactor cycle"* |
| **C** | *"Pause after every phase (Red, Green, Refactor)"* |

[Agentic Autonomy Levels](agentic-autonomy-levels.md) is a multi-axis model of *what an agent is
permitted to do*; this is the finer and more immediate question of **where a human breaks into a
loop already running** — the *"watch the run, step in when it drifts"* verb from
[Meta's Forum](../../case-studies/meta-forum-ai-native-build.md) given three concrete positions.
Worth having as a dial even where the loop being paused is not red-green-refactor.

**"Verification debt"** is a compact name for something these notes measure in three places:
*"The generated code looks convincing, reviews become superficial — until things go wrong in
production."* That is the **"neither"** column in
[Accountability for Unread Code](accountability-for-unread-code.md) — neither read nor checked —
with [Faros's +31.3% unreviewed merges and +242% incidents](dark-factories-examined.md) as its
measurement and the 14%-of-570 review study as the mechanism.

One incidental idea worth more than the methodology: their exercise domain is a card game,
*"Overlords: The Card Game"*, chosen because it *"rarely appears in the training data of LLMs,
[so] you can observe live how the AI solves real logic problems rather than just reciting from
memory."* That is sound instinct about **evaluation contamination** applied to teaching material
— the same reason [Cursor's swarm benchmark](../../case-studies/cursor-agent-swarm-economics.md)
withheld the SQLite source and tests from the agents it measured.

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
