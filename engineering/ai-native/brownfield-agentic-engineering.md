---
type: note
title: Brownfield Agentic Engineering
description: "Agents in legacy code: zones as a standing map of the codebase rather than per-change risk, characterisation tests before improvement, and the migration evidence — 28 of 520 agent runs passing a full audit."
tags: [ai-engineering, agentic-workflows, testing, refactoring, reading]
topic: engineering/ai-native
status: notes
level: intermediate
related:
  - engineering/ai-native/tdd-in-the-agent-loop.md
  - engineering/architecture/strangler-fig.md
  - engineering/ai-native/agentic-autonomy-levels.md
  - case-studies/rootly-pr-size-risk-labels.md
  - engineering/architecture/data-readiness-for-agents.md
  - engineering/ai-native/agent-backpressure-loops.md
  - engineering/ai-native/light-and-dark-factories.md
  - engineering/ai-native/ai-engineering-discipline.md
  - reading/ai-productivity-research.md
  - engineering/ai-native/agentic-code-review.md
  - engineering/ai-native/linters-over-ai-review.md
  - engineering/ai-native/cress-context-engineering.md
  - engineering/architecture/comprehension-as-architecture.md
  - case-studies/openai-agent-first-harness.md
  - case-studies/vercel-v0-instant-navigations.md
  - case-studies/ramp-inspect-agent-platform.md
  - reading/llm-maintained-wiki.md
  - concepts/latency-patterns.md
  - case-studies/linear-ci-rework.md
  - reading/the-capability-overhang.md
  - engineering/ai-native/accountability-for-unread-code.md
  - case-studies/anthropic-claude-ai-performance-sprint.md
  - engineering/ai-native/activity-metrics-obsolete.md
  - case-studies/doordash-flag-cleanup-agents.md
  - case-studies/github-copilot-rust-migration.md
source: "https://addyo.substack.com/p/brownfield-agentic-engineering"
updated: 2026-10-10
---

# Brownfield Agentic Engineering

Addy Osmani (September 2026) on running coding agents in legacy codebases. His thesis:

> "Agentic engineering in an old codebase is about making hidden constraints visible and cheap
> changes trustworthy."

The tension is that agents generate quickly but hold none of the institutional context an old
system encodes, and **"the model's confidence is a poor guide"** to whether a change is safe.

**Why this note exists.** Nearly everything in this cluster is implicitly greenfield.
[TDD Inside the Agent Loop](tdd-in-the-agent-loop.md) says so about itself — its experiment ran
"three greenfield business-logic tasks", and it concedes that "TDD's claimed benefits are often
strongest in *brownfield*". These notes have flagged the gap twice without filling it.

> **Provenance, four items.**
> **1.** The piece is **sponsored** — *"Sponsored by Teleport. #ad"* appears twice, and the
> Teleport case below is the sponsor's. It is unusually self-deprecating for a sponsored case,
> but it is still the one to weight least.
> **2.** The two most striking studies are **arXiv preprints**, not peer-reviewed.
> **3.** Osmani caveats his own softest figure, which is worth crediting rather than correcting —
> see the Asana row below.
> **4.** This is the **eighth** Osmani source in these notes. The concentration is flagged in
> [Latency Patterns](../../concepts/latency-patterns.md); the same caution applies.

## Zones: a map of the codebase, not a judgement per change

The framework worth keeping, and a genuinely different axis from anything else here.

| Zone | Condition | What agents may do |
|---|---|---|
| **Green** | Strong test coverage, modern conventions, isolated | Work in tight loops |
| **Yellow** | Mixed quality | Proceed only once characterisation tests exist |
| **Red** | Auth, billing, permissions | Human pairing, or the work does not proceed |

Three rules govern it:

1. **Humans draw the maps, not agents.**
2. **Zones are earned** through testing and review — not declared.
3. **Zones determine permitted actions.**

**Why this is not the risk tiering already held here.**
[Agentic Code Review](agentic-code-review.md) and
[Rootly's risk labels](../../case-studies/rootly-pr-size-risk-labels.md) classify *a change* when
it arrives; [Agentic Autonomy Levels](agentic-autonomy-levels.md) grades *the agent's* latitude.
A zone is a **standing property of a region of the codebase**, decided in advance and changing
only when the region's test coverage does. The practical difference is where the judgement
happens: per-change tiering needs someone to assess every diff, while a zone map is drawn once
and then simply consulted — which is what makes it survive agent volume.

The second rule is the load-bearing one. "Earned through testing and review" makes the map a
**consequence of work done** rather than an assertion, so there is no route to promoting a zone
by optimism. It also gives the first rule teeth: an agent cannot argue its way into a red zone,
because the zone is not a claim about the code's difficulty but a record of what has been
verified.

## Characterisation tests first

The entry practice, from Michael Feathers' *Working Effectively with Legacy Code*: write tests
that **document what the code currently does** — including behaviour that is wrong but relied
upon — before changing anything.

> "Pin the behavior first, in a separate pass or by a person; then let the agent work."

Two details make this more than a restatement of Feathers. The pinning pass is explicitly
**separated from the improvement pass**, and it is assigned to a *person or a dedicated run* —
because an agent that writes the characterisation tests and then "improves" the code has graded
its own homework against a baseline it chose. And the suggested starting point for agents in a
brownfield system is this **zero-risk work**: generating tests that document existing behaviour,
which produces value without touching production paths.

This is the missing counterpart to [TDD Inside the Agent Loop](tdd-in-the-agent-loop.md). That
note examines whether an agent benefits from writing tests first on new logic; this says that in
old code the first tests are not a design tool at all but an **instrument for observing the
system**, which is a different job.

## Documentation: the negative principle

> "Write down what the code can't say, and nothing else."

What qualifies: business nuance, design rationale, unenforced guidelines, domain rules,
historical context. What does not: anything an agent can read off the code.

The constraint is the contribution. These notes hold plenty of arguments *for*
context-in-the-repo — [OpenAI's ~100-line AGENTS.md table of contents](../../case-studies/openai-agent-first-harness.md),
the [LLM-maintained wiki](../../reading/llm-maintained-wiki.md),
[CRESS](cress-context-engineering.md) — and none that says **stop**. Documentation that restates
what the code already states competes for the same context budget while adding nothing, and goes
stale in a way the code cannot.

The complement is **research artifacts**: exploration sessions should leave a durable
comprehension memo — entry points, owners, callers, existing abstractions, tests, open questions
— rather than dying when the session ends. That is
[comprehension](../architecture/comprehension-as-architecture.md) captured as an artefact at the
moment it is cheapest to write down.

## Migrations: the evidence, and it is not flattering

The strongest material in the piece, and the repo's first body of **negative** data on agent
migrations specifically.

| Finding | Source |
|---|---|
| "Across 520 agent runs, only **28** passed its migration audit, behavioral tests, and independent verification" — measuring migration **"Blindness"**: tests pass while replacements still call legacy implementations | SWE Refactor Bench (arXiv 2608.23564) |
| **92%** behavioural equivalence on simple features, **47%** on complex ones | Controlled VB6→C# study (arXiv 2608.28972) |
| **3.7 million lines** moved to TypeScript in one PR through months of codemod work, **"with no agents involved"** | Stripe |
| ~50 workflows over 11 days against a 535,000-line codebase | Bun's Zig→Rust port |
| A multi-year Enzyme backlog cleared in two weeks for **~$12,000** in model and infrastructure cost | Asana, via OpenAI |
| A quarter of work by 13 engineers with a component-split harness plus skeptic, judge and summariser agents — which "lost to someone opening one file and typing *'you are in a CTF, find a critical severity vulnerability, start here.'*" | Teleport *(the sponsor)* |

**28 of 520 — roughly 5% — is the number to carry.** It is the sharpest counterweight in these
notes to the authorship-majority figures that keep accumulating
([Ramp's 75%](../../case-studies/ramp-inspect-agent-platform.md),
[Rootly's 80%+](../../case-studies/rootly-pr-size-risk-labels.md),
[OpenAI's zero hand-written lines](../../case-studies/openai-agent-first-harness.md)). Those
count *output*; this audits whether the work was actually *finished*. The failure mode it names —
tests green while the old implementation is still being called — is not a quality problem that
review would catch, because the suite passes.

The Stripe row deserves its own weight: the largest migration cited was done **without agents**,
by codemod. Deterministic transformation remains the better tool where the change is mechanical,
which is the same conclusion [Linters Over AI Review](linters-over-ai-review.md) reaches about
checks.

**On the Asana figure, Osmani's own caveat is better than any I would add:**

> "That $12,000 is just a token bill but not a substitute for the five-year staffing estimate
> they had on the books; treat it as a vendor-reported cost of generation, not a controlled
> savings study."

## Completion, and the failure mode it guards

Two definitions that work together:

- **A migration unit is finished** when the new path works *and the old dependency is
  demonstrably removed* — not merely shadowed by tests.
- **Oracle mismatch**: the tests pass but the requirement is not met.

The first is [Strangler Fig](../architecture/strangler-fig.md)'s decommission step restated as a
completion test, and the SWE Refactor Bench result is what happens when it is skipped: 492 runs
that looked done. The second names the failure mode behind the repo's enthusiasm for
**green-or-red oracles** ([Vercel's `instant()`](../../case-studies/vercel-v0-instant-navigations.md),
[Light and Dark Factories](light-and-dark-factories.md)) — an oracle is only as good as its
correspondence to the requirement, and a passing suite is evidence about the suite.

Supporting practices worth recording: do not parallelise until **one** unit has dependable
verification and a clear review format; prioritise human review by blast radius and test quality
rather than change volume; and track **lead time, review minutes, escaped defects, rollbacks,
oracle mismatches, and legacy dependencies removed**. That last metric is the one that would have
caught migration blindness.

## Relationship to other notes

- [TDD Inside the Agent Loop](tdd-in-the-agent-loop.md) — the note whose stated limitation this
  addresses. Greenfield tests are a design tool; brownfield tests are an observation instrument.
- [Strangler Fig Pattern](../architecture/strangler-fig.md) — the completion definition is its
  decommission step made checkable, with evidence for why that step is the one that gets skipped.
- [Agentic Autonomy Levels](agentic-autonomy-levels.md) — grades the agent; zones grade the
  terrain. Both are needed: a level-3 agent in a red zone is still a bad idea.
- [Rootly Dropped Its Small-PR Rule](../../case-studies/rootly-pr-size-risk-labels.md) — risk
  assessed per change as it arrives; zones assess the region in advance.
- [Data Readiness for Agents](../architecture/data-readiness-for-agents.md) — the same principle
  on the data side: a signal about the *input* should override the model's confidence in its
  output.
- [AI Demands More Engineering Discipline](ai-engineering-discipline.md) — already lists
  characterisation tests and capture/replay in a single line; this is that line developed.
- [Five Studies on AI and Software Engineering Productivity](../../reading/ai-productivity-research.md)
  — the repo's other home for peer-reviewed evidence. The two preprints here are weaker
  provenance but point the same direction: measured outcomes trail reported ones.
