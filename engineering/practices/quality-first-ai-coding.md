---
title: Quality-First AI Coding
tags: [ai-engineering, code-review, reading]
topic: engineering/practices
status: notes
level: intermediate
related:
  - engineering/practices/code-review-policy.md
  - engineering/practices/change-absorption-capacity.md
  - engineering/practices/harness-engineering.md
  - engineering/practices/federated-pr-review.md
  - engineering/practices/agent-backpressure-loops.md
  - engineering/practices/modern-engineering-values.md
  - engineering/practices/prompt-engineering-for-programmers.md
  - engineering/practices/software-design-principles.md
  - concepts/clean-code-and-solid.md
source: "https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/"
updated: 2026-06-19
---

# Quality-First AI Coding

A counter-position to the idea that AI's value in coding is raw speed. The argument is that
LLMs can be used to produce *higher-quality* code at a measured pace — "writing better code more
slowly" — rather than emitting large volumes of barely-passable output. AI is treated as a force
multiplier for careful engineering, not a replacement for thought.

## The stance: quality over velocity

The author (Nolan Lawson) contrasts two ways of using AI for coding:

- **The "slop cannon"** — generate barely-passable code in large PRs and merge with little
  review. Optimises for velocity at the cost of quality.
- **Methodical, quality-focused use** — use AI to deepen understanding and improve the code,
  accepting that raw output may not increase.

Under this view the bottleneck is not *finding* issues — LLMs are good at surfacing bugs when
orchestrated well — but *validating and prioritising* them.

## Multi-model bug review

The central technique: use several different models (e.g. Claude, Codex, and others) as
independent sub-agents to review a PR, then synthesise their findings.

- **Run models in parallel** and have each report issues ranked by severity
  (critical / high / medium / low).
- **Synthesise across models** to suppress false positives — the claim is that the more
  different models review a PR, the less likely a hallucinated or bogus bug survives.
- **Fix critical/high iteratively** with agents; **deprioritise low-ROI** fixes.
- **Abandon the PR** when review reveals a fundamentally flawed approach, rather than patching.
- **Clear context between sweeps** so earlier conclusions don't bias later ones.

## Supporting techniques

- Ask for **Markdown documentation with Mermaid diagrams** to make the change legible.
- Use comprehension-focused skills (the author cites Matt Pocock's `/grill-me`) to interrogate a
  PR until it is genuinely understood before merging.
- Treat **pre-existing bugs surfaced during review** as worthwhile "side-quests" — debt
  remediation as a positive by-product rather than a delay.

## Anti-patterns

- Merging unvetted multi-hundred-line PRs.
- Accepting LLM output without understanding it.
- Treating velocity as the primary success metric.
- Ignoring pre-existing bugs the review surfaces.

## Trade-offs

The approach **burns substantial tokens and time** and does not necessarily increase raw code
output. The claimed returns are improved codebase health, deeper architectural understanding,
discovery of subtle failure modes, and the educational value of seeing hidden complexity. The
underlying principles are familiar pre-AI ones — **KISS** and **DRY** — applied with AI as the
reviewer rather than the author.

> Referenced: Anthropic's *Mythos* research project (on LLM agents' bug-finding capability) and
> Matt Pocock's `/grill-me` skill.

## Relationship to other notes

- [Change Absorption Capacity (CATS)](change-absorption-capacity.md) — the system-level
  counterpart of the same "velocity is not the goal" stance; this note is the hands-on,
  individual-workflow version.
- [Code Review Policy](code-review-policy.md) and
  [Federated PR Review](federated-pr-review.md) — the organisational policy and multi-team
  governance around review; this note is a practitioner technique that runs inside those.
- [Harness Engineering](harness-engineering.md) — multi-model review is an
  [advisor-pattern](harness-engineering.md) harness (sub-agents reviewing, a coordinator
  synthesising); this note is the workflow, that note is the machinery.
