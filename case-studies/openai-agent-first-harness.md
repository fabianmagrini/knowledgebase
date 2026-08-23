---
type: case-study
title: OpenAI's Agent-First Harness
description: "Five months shipping an internal product with zero manually-written code: agent legibility as the organising principle, the repository as system of record, mechanically-enforced architecture, and remediation-hint linters."
tags: [ai-engineering, agentic-workflows, architecture, reading]
topic: case-studies
status: notes
level: intermediate
related:
  - engineering/ai-native/harness-design-experiments.md
  - engineering/ai-native/harness-engineering.md
  - engineering/ai-native/agent-backpressure-loops.md
  - engineering/ai-native/agentic-autonomy-levels.md
  - engineering/ai-native/light-and-dark-factories.md
  - engineering/ai-native/ai-factory.md
  - reading/factory-engineers.md
  - tools/claude-code-steering-mechanisms.md
  - case-studies/rootly-pr-size-risk-labels.md
  - engineering/practices/code-review-policy.md
  - engineering/ai-native/dark-factories-examined.md
  - engineering/architecture/enforced-architecture-rules.md
  - case-studies/anthropic-ai-native-teams.md
source: "https://openai.com/index/harness-engineering/"
updated: 2026-07-26
---

# OpenAI's Agent-First Harness

An OpenAI team reports building and shipping an internal beta over five months with **zero
manually-written lines of code** — application logic, tests, CI configuration, documentation,
observability and internal tooling all agent-generated. Their framing:

> Humans steer. Agents execute.

The engineering job, on this account, stops being implementation and becomes designing
environments, specifying intent, and building the feedback loops that let agents work
reliably.

| | Reported |
|---|---|
| Duration | 5 months |
| Code | ~1,000,000 lines |
| Merged PRs | ~1,500 |
| Team | 3 → 7 engineers |
| Throughput | ~3.5 PRs per engineer per day |
| Claimed speed-up | ~10× versus writing it by hand |

All figures are **self-reported and unaudited**, and the ~10× is an estimate against a
counterfactual that was never run. They do come from a product shipped to hundreds of internal
users and external alpha testers rather than a benchmark exercise. *(Recorded from a
third-party copy of the article; openai.com blocks automated retrieval.)*

## Agent legibility is the organising principle

The idea most of the rest follows from: **anything not accessible in the repository does not
exist to the agent.** Systems get optimised for agent reasoning rather than human comfort.

- **The repository is the system of record.** Versioned artefacts — markdown, code, schemas —
  in preference to knowledge living in chat, tickets, or an external wiki. If a decision isn't
  committed, the agent cannot act on it.
- **Progressive disclosure.** `AGENTS.md` is a **~100-line table of contents**, not a manual:
  a small entry point that teaches the agent where to look next, backed by an indexed `docs/`
  directory of design docs, execution plans, product specs and references.
- **A doc-gardening agent** runs recurring scans for stale documentation.

That `AGENTS.md` treatment is a concrete answer to the failure named in
[Claude Code Steering Mechanisms](../tools/claude-code-steering-mechanisms.md) — the
"gravitational pull toward `CLAUDE.md`" that turns one file into a mixed control plane. The
fix here is the same one that note argues for: make the entry point an index and push detail
to where it loads on demand.

## Constraints enforced mechanically

Autonomy is granted locally and bounded structurally rather than by review attention.

- **Layered domain architecture** with fixed dependency directions —
  Types → Config → Repo → Service → Runtime → UI. Architecture the agent cannot drift out of.
- **Golden principles** — opinionated mechanical rules maintained continuously by
  garbage-collection processes rather than by convention.
- **Custom linters with remediation hints** — error messages that carry the fix, not just the
  complaint.

That last technique is the sharpest thing in the piece. It is exactly what
[Backpressure Loops for Coding Agents](../engineering/ai-native/agent-backpressure-loops.md)
argues for — moving mechanical feedback out of human review and into a loop the agent can act
on itself — implemented at the level of the error message. A lint failure that states the
remedy closes the loop without a human in it.

Supporting infrastructure in the same spirit: Chrome DevTools Protocol integration so the
agent can validate UI behaviour and reproduce bugs directly, and a local ephemeral
observability stack exposing logs, metrics and traces by query so the agent can investigate
rather than guess.

## Throughput changes the review calculus

Two practices follow from the volume:

- **The Ralph Wiggum Loop** (their term) — the agent iterates on its own changes until every
  reviewer is satisfied, before a human is involved.
- **Minimal blocking merge gates**, on the reasoning that at high throughput *corrections are
  cheap and waiting is expensive*.

The second is a live disagreement with other notes here.
[Rootly](rootly-pr-size-risk-labels.md) also relaxed a merge-time rule, but replaced it with
risk labels and feature-flag gates rather than fewer gates outright; the
[Code Review Policy](../engineering/practices/code-review-policy.md) holds the opposite
default, with scrutiny tiered up by risk. Worth reading as a claim that only holds under
their conditions — mechanically-enforced architecture, remediation-hint linters, and an agent
that has already self-reviewed — rather than as portable advice to drop merge gates.

## The tension with Anthropic's finding

Set beside [Harness Design for Long-Running App Development](../engineering/ai-native/harness-design-experiments.md),
these are two lab engineering teams reporting real work and reaching opposite conclusions
about how much harness to build. Anthropic's is that **harness complexity should shrink as
models improve**, since much of it compensates for limitations that later generations do not
have. OpenAI's is an elaborate, heavily-invested harness treated as the durable work product.

They are not straightforwardly reconcilable, and the honest reading is that the question is
open. One partial resolution: Anthropic measured harnesses that compensate for *capability*,
while much of OpenAI's harness encodes *context and constraint* — where the code lives, what
depends on what, what the house style is — which no model improvement supplies.

## What the authors say they don't know

Unusually explicit, and worth recording:

- How architectural coherence holds up over **years** of fully agent-generated code
- Where human judgement adds the most leverage
- How the approach scales as models get more capable
- Whether any of it generalises beyond their particular repository structure and tooling

## Relationship to other notes

- [Harness Design for Long-Running App Development](../engineering/ai-native/harness-design-experiments.md) —
  the other lab's experiment, reaching a different conclusion (above).
- [Harness Engineering](../engineering/ai-native/harness-engineering.md) — the component
  anatomy; this is one built out in production.
- [Factory Engineers, Not Product Engineers](../reading/factory-engineers.md) — the same claim
  that the factory, not the product, is the engineer's work product. This is that position
  with numbers attached.
- [Agentic Autonomy Levels](../engineering/ai-native/agentic-autonomy-levels.md) — their
  progressive autonomy levels, from supervised PRs to end-to-end features, are that ladder
  climbed in one organisation.
