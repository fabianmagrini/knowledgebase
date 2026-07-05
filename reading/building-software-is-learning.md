---
title: Building Software Is Learning
tags: [ai-engineering, reading]
topic: reading
status: notes
level: intermediate
related:
  - reading/what-is-software-engineering-ai.md
  - engineering/ai-native/loop-driven-development.md
  - engineering/architecture/agile-design-decisions.md
  - engineering/ai-native/spec-driven-development.md
source: "https://registerspill.thorstenball.com/p/building-software-is-learning"
updated: 2026-07-05
---

# Building Software Is Learning

Thorsten Ball (originally an internal Amp-team message) argues that building *new* software is
fundamentally an **iterative learning process**, not the linear execution of a predetermined
spec. When there's no spec and you're building something new, misalignment between the builder
and the requester is **inevitable** — not a failure to be engineered away. The learning can't be
avoided, only *accelerated*, so the real question is:

> "How can I get feedback as soon as possible?" — not "How do I build this perfectly?"

## Feedback-compression toolkit

Ball's techniques all shorten the loop between a first attempt and reality correcting it:

| Technique | What it buys |
|---|---|
| **1-hour prototypes** | A rough, throwaway version that exposes wrong assumptions fast |
| **30-minute written specs** | Just enough written intent to check alignment before building |
| **Daily incremental shipping** | Real usage as the feedback source, not a distant big-bang release |
| **Scope reduction** | Concentrate effort on the *unknowns*; skip features that teach you nothing |
| **Fake demos and videos** | Provoke reactions without building the real thing |
| **README-driven API design** | Write the interface's docs first to feel whether it makes sense |

The unifying reframe: **"done" means "ready for feedback," not "perfect."** And feedback is meant
in the widest sense — CI systems, colleagues, users, and your own observation all count.

## Distinctive framing

- *"Getting your ass whooped by reality"* — the moment confident assumptions meet actual use.
- *"The `...`"* — the gap between a confident commitment and the humbled discovery that follows.

The point of naming these is to normalise them: the humbling is the *learning*, and shipping
sooner just moves it earlier and makes it cheaper.

## Implications for AI agents

Ball's frame suggests agents should ship testable increments over monolithic implementations,
treat architectural decisions as **hypotheses requiring validation**, engage stakeholders
frequently rather than delivering fully-formed solutions, and recognise "done" as ready-for-feedback.
Frequency is the lever: *"as soon as possible, as often as possible, ship things"* that generate
useful feedback.

## Relationship to other notes

- **[What Is Software Engineering? (Adapting to AI)](what-is-software-engineering-ai.md)** — the
  sibling essay. Colin Breck frames engineering as "discovery and learning" (Farley's *optimising
  for learning* pillar) as one of three; Ball makes that single idea the whole thesis and supplies
  the concrete feedback-compression toolkit.
- **[Loop-Driven Development](../engineering/ai-native/loop-driven-development.md)** — the same
  "shorten the feedback loop" instinct as an engineering practice; this note is the essay behind
  the why.
- **[Agile Design Decisions](../engineering/architecture/agile-design-decisions.md)** — the
  Walking Skeleton, YAGNI, and emergent-design moves are "ship to learn" applied to architecture.
- **[Spec-Driven Development](../engineering/ai-native/spec-driven-development.md)** — a useful
  contrast: a written spec is *one* of Ball's feedback tools (the 30-minute outline, README-first),
  not a substitute for the learning that only real feedback provides.
