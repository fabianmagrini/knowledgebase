---
type: note
title: Light and Dark Software Factories
description: "Addy Osmani's lights-out manufacturing analogy for agent pipelines: which loops run unattended, why lit factories put judgement upstream at design rather than at the diff, and why the harness alone is not enough."
tags: [ai-engineering, agentic-workflows, architecture, reading]
topic: engineering/ai-native
status: notes
level: intermediate
related:
  - engineering/ai-native/ai-factory.md
  - engineering/ai-native/harness-engineering.md
  - engineering/ai-native/own-the-outer-loop.md
  - engineering/ai-native/agentic-autonomy-levels.md
  - engineering/ai-native/agent-backpressure-loops.md
  - engineering/ai-native/agentic-code-review.md
  - engineering/ai-native/loop-driven-development.md
  - engineering/ai-native/long-running-agents.md
  - engineering/ai-native/ai-native-engineering-overview.md
source: "https://addyosmani.com/blog/software-factories/ (also published at https://addyo.substack.com/p/software-factories-light-and-dark)"
updated: 2026-07-26
---

# Light and Dark Software Factories

Addy Osmani borrows **lights-out manufacturing** — factories where robots work in the dark
because no human is present, as FANUC has run since 2001 and Xiaomi demonstrated in 2024 — as
the axis for deciding which agent loops run unattended.

| | Definition |
|---|---|
| **Dark** | Code ships without human review, "verified only by other machines" |
| **Lit** | Human judgement stays embedded in the pipeline — "the lights stay on wherever a wrong call is expensive" |

The essay is synthesis and argument, not research: there are no studies, no metrics, and no
comparison of lit against dark outcomes across organisations. Its one piece of empirical
grounding is a single reported experiment (below). Bob Bemer is credited with coining
"software factories" in 1968 (*The economics of program production*).

## Where the lights go

The load-bearing move is *placement*, not amount. A lit factory does not mean a human
reading every diff at the end — it means judgement applied **upstream, at design and
architecture, before generation begins**, plus explicit gates at the points where a wrong
call is expensive. Dark and lit pipelines have the same structure; they differ in where the
human sits in it.

This is a meaningfully different answer from "review the output more carefully", and it is
the main reason to keep this note distinct from
[Agentic Code Review](agentic-code-review.md).

## The three-layer stack

The essay makes explicit a hierarchy this knowledge base has held only as separate notes:

| Layer | What it is |
|---|---|
| **Loop** | One agent repeating gather → act → check until done — see [Loop-Driven Development](loop-driven-development.md) |
| **Harness** | The environment constraining that loop: sandbox, tools, memory, completion gates — see [Harness Engineering](harness-engineering.md) |
| **Factory** | Many harnessed loops feeding a queue, reviewed before production — see [The AI Factory](ai-factory.md) |

The full closed loop as drawn: intent/signals → queue → harness (build) → automated checks →
review gate → deployment → monitoring → feedback.

Working at this level is what Osmani calls **loop engineering** — designing the system the
agent runs inside, rather than steering it turn by turn through prompts. The term names the
shift in where an engineer's effort goes once the factory framing is taken seriously: from
composing individual instructions to specifying the loop, its constraints, and its gates.

## When a loop earns the dark

Osmani's conditions for running unattended:

- Checks are **cheap** and run often
- Verification rests on **green-or-red oracles** — type gates, property tests — not judgement
- Results are immediate and do not drift
- The loop is **short**. Dex Horthy's rule is cited: 3–10 steps is sustainable; beyond ~20
  steps, context accumulation causes drift

Anything failing these stays lit. The governing principle — *"you can only hand a loop as
much autonomy as you can cheaply and reliably verify, and not one inch more"* — is a sharper
statement of the **calibrated autonomy** already recorded in
[Agentic Autonomy Levels](agentic-autonomy-levels.md).

## The harness is not enough

The essay's strongest claim, and the one that pushes against
[Harness Engineering](harness-engineering.md): a well-built harness still cannot make a model
care about long-term maintainability, because the model has no incentive to. The architecture
and the type system have to act as external safety nets, which makes **the codebase itself a
verification substrate**:

- Strong typing and explicit method signatures, so errors surface at compile time
- Test seams that let behaviour be pinned and observed
- Legible layout and short call stacks
- Well-defined component boundaries that bound blast radius
- Dependency injection, so components are swappable

The practical implication is that codebases differ in how much darkness they can safely
support, and that difference is a design choice made before any agent runs.

## Graphs over freeform loops

A distinction not otherwise covered in these notes: structured workflows — finite state
machines, directed graphs with conditional edges — outperform open-ended agent loops. They
constrain wandering and, more usefully, produce **legible failure points**: when a graph
breaks you know which node broke. Jerry Liu (LlamaIndex) is cited for hybrid workflow-graph
approaches and David Khourshid for the state-machine and actor framing.

## The reported failure

Dex Horthy (HumanLayer, author of *12-factor-agents*) is cited from the talk *Harness
Engineering is Not Enough: Why Software Factories Fail*, reporting a four-month experiment
running a fully automated factory. It ended in "painstaking manual debugging" — the failure
mode being not a dramatic outage but **comprehension debt** compounding quietly over months:
the widening gap between how much code exists and how much anyone still understands.

This is one team's reported experience, presented in a conference talk.

## What this restates

Much of the essay consolidates arguments already held here, several from Osmani's own
earlier pieces. Recorded as pointers rather than repeated:

- **Verification, not generation, is the constraint** → [Agentic Code Review](agentic-code-review.md)
- **Comprehension debt** → [Agentic Code Review](agentic-code-review.md), [Loop-Driven Development](loop-driven-development.md)
- **Agents own the inner loop, humans the outer** → [Own the Outer Loop](own-the-outer-loop.md)
- **Back pressure between generation and verification capacity** → [Backpressure Loops for Coding Agents](agent-backpressure-loops.md)
- **Autonomy as a safety property to be calibrated** → [Agentic Autonomy Levels](agentic-autonomy-levels.md)

## Relationship to other notes

- [The AI Factory](ai-factory.md) — what a factory *is*; this note is about how much of it
  you dare run unattended.
- [Harness Engineering](harness-engineering.md) — the layer this note argues is necessary but
  insufficient on its own.
- [Agentic Autonomy Levels](agentic-autonomy-levels.md) — the graduated scale; light/dark is
  the same judgement reduced to a binary per loop.
