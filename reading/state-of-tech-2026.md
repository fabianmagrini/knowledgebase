---
type: reading
title: The State of the Tech Industry in 2026
description: "A signpost: most of this survey is already held in depth here. Kept for four things — GitHub's agent/human PR crossover in August 2026, compute capacity as a binding constraint, 5–10 parallel agents against the repo's ~3, and Uber's token economics."
tags: [ai-engineering, agentic-workflows, observability, reading]
topic: reading
status: notes
level: beginner
related:
  - reading/ai-productivity-research.md
  - engineering/ai-native/review-replacement.md
  - engineering/ai-native/dark-factories-examined.md
  - engineering/ai-native/agile-in-the-age-of-ai.md
  - engineering/ai-native/model-routing-and-ai-gateways.md
  - engineering/ai-native/brownfield-agentic-engineering.md
  - case-studies/anthropic-ai-native-teams.md
  - reading/what-is-software-engineering-ai.md
  - engineering/ai-native/accountability-for-unread-code.md
  - engineering/ai-native/substitution-myth-in-code-review.md
  - leadership/revised-rules-engineering-leadership.md
  - reading/the-capability-overhang.md
  - reading/multi-agent-coding-coordination.md
  - case-studies/ramp-inspect-agent-platform.md
  - case-studies/rootly-pr-size-risk-labels.md
  - case-studies/cursor-agent-swarm-economics.md
  - reading/agentic-ai-architecture-emag.md
source: "https://newsletter.pragmaticengineer.com/p/the-state-of-the-tech-industry-in"
updated: 2026-10-11
---

# The State of the Tech Industry in 2026

Gergely Orosz (October 2026) surveys the industry on the back of interviews with engineers at
OpenAI, Anthropic, Uber, Linear and Ramp, plus unnamed sources. ~5,000 words; the main text is
readable and only the presentation slides are paywalled.

**This is a signpost, not a standalone argument.** Most of the survey is already held here in
more depth — the shape it shares with
[Five Studies on AI Productivity](ai-productivity-research.md) and
[Agentic AI Architecture](agentic-ai-architecture-emag.md). What follows is the four things the
repo did not have, and pointers for the rest.

## Already held, in more depth

| Orosz's claim | Where it lives here |
|---|---|
| "Theater of code reviews" — engineers rubber-stamping volumes they cannot read | The repo's densest cluster: [Dark Factories Examined](../engineering/ai-native/dark-factories-examined.md) (+31.3% unreviewed merges, +242% incidents), [Accountability for Unread Code](../engineering/ai-native/accountability-for-unread-code.md) (the moral crumple zone), [The Substitution Myth](../engineering/ai-native/substitution-myth-in-code-review.md), [Replacing Code Review](../engineering/ai-native/review-replacement.md) |
| Two-pizza teams persist despite AI | [Anthropic's AI-Native Team Structure](../case-studies/anthropic-ai-native-teams.md) — shape held constant, concurrent projects 1–2 → 4–5 |
| Migrations collapsing from years to weeks | [Brownfield Agentic Engineering](../engineering/ai-native/brownfield-agentic-engineering.md) already carries the Bun 11-day port and Asana's two-week Enzyme backlog |
| Domain expertise becoming the differentiator | [Revised Rules](../leadership/revised-rules-engineering-leadership.md) (durable teams with domain context), [The Capability Overhang](the-capability-overhang.md) (deep and wide knowledge) |
| Planning and testing still essential | [Agile in the Age of AI](../engineering/ai-native/agile-in-the-age-of-ai.md) |

## 1. The GitHub crossover

The single most consequential datapoint, and **shared exclusively with the author**, so not
published elsewhere:

> "There were more agent-authored PRs in August 2026 on GitHub than human-authored ones."

With a **ninefold increase in agent-authored PRs over eight months**, and the projection of *"3x
as many fully AI-generated PRs, per month (probably 75M+), than human generated ones at the end
of 2023 (25M in December 2023)."*

This extends a series the repo already holds. [Replacing Code
Review](../engineering/ai-native/review-replacement.md) carries GitHub's earlier figure —
"the number of PRs opened has increased fivefold" over three years, with the acceleration
concentrated recently. **This supplies the crossover date**, which is the thing that makes the
trend legible rather than merely steep.

Worth keeping the comparison honest: these are *authorship* counts, the same measure the repo has
repeatedly flagged as saying nothing about value
([Ramp's 75%](../case-studies/ramp-inspect-agent-platform.md),
[Rootly's 80%](../case-studies/rootly-pr-size-risk-labels.md)). A crossover in volume is a real
fact about the platform and not a claim about output quality — and
[Cursor's thrash finding](../case-studies/cursor-agent-swarm-economics.md), where 68,000 commits
was worse than 971, is the standing reason to hold those apart.

Linear's own data points the same way: **agent-created issues have exceeded human-created ones
since July 2026**, with AI-only PR reviews trending upward.

## 2. Compute capacity as a binding constraint

**The repo had nothing on this**, across 200-plus notes about agent-driven engineering.

- GPU and memory shortages described as "common knowledge"
- CPU shortages trending — *"nearly impossible to get CPUs on spot instances"*
- Regions reportedly at capacity, with advance reservations needed months ahead

That is a material omission in this collection. Every note here reasons about what agents *can*
do and what they cost per token; none asks whether the capacity exists to run them. It bears
directly on [Ramp's platform](../case-studies/ramp-inspect-agent-platform.md), whose entire
buy-versus-build argument is that cloud sandboxes remove the parallel-session ceiling a laptop
imposes — a ceiling that returns, differently shaped, if the region is full.

The related signal: **"agentic infra"** named as an emerging specialisation. If capacity is the
constraint, someone owns it.

## 3. Parallel agents: 5–10, against the repo's ~3

A direct tension worth stating rather than averaging. Three named engineers report
independently:

| | |
|---|---|
| Boris Cherny | "5-10 Claudes on Claude Web, in parallel" |
| Peter Mattis | "5-10 agent sessions concurrently" |
| Dima Zaytsev | "5-10 (literally) worktrees locally" |

[Agile in the Age of AI](../engineering/ai-native/agile-in-the-age-of-ai.md) records roughly
**three** as the comfortable ceiling, on the argument that human cognitive load — not tooling —
binds how many agents one person can direct. The repo has leaned on that figure, including in
[Multi-Agent Coding](multi-agent-coding-coordination.md).

**Two readings, and the note should not pretend to know which.** Either the ceiling moved
(better tooling, better isolation, more practice), or these three are unusually practised
operators at companies that build the tools, which is a selected sample by construction. Note
that all three are at firms building agent products. The honest position is that the ~3 figure
should no longer be quoted as settled, and that 5–10 is not yet evidence of a general ceiling
either.

## 4. Uber's token economics

> "Uber's per-token costs are down 50%+" — via open models and smart routing

With token usage rising while total cost stayed flat since May. That is
[Model Routing and AI Gateways](../engineering/ai-native/model-routing-and-ai-gateways.md)'
thesis — route each request to the cheapest adequate model — with a production number attached,
and it is the first figure here showing the *cost curve* rather than a point cost.

## Two claims to hold at arm's length

**The reliability claim is an impression, not a measurement.** Verbatim, from Mario Zechner on a
podcast:

> "Everything is broken. It sure feels like software has become a brittle mess, with 98% uptime
> becoming the norm instead of the exception, including for big services."

**"It sure feels like"** is doing the work, and Zechner himself notes the trend predates agents.
98% uptime is roughly seven days of downtime a year; as an industry-wide norm that would be
extraordinary, and nothing here measures it. Recorded as a practitioner impression because stated
flatly it would become the most alarming reliability claim in these notes on the thinnest
evidence available. The repo's actual measured signal on this is the Faros **+242% incident rise**
in [Dark Factories Examined](../engineering/ai-native/dark-factories-examined.md) — narrower,
but counted.

**The Fowler quote contradicts a note the repo holds.**

> "Nothing has hit with the magnitude of AI. This is a whole size difference from anything that
> we've faced before … For AI there's no argument about how important it is."

[What Is Software Engineering? (Adapting to AI)](what-is-software-engineering-ai.md) holds the
opposite from Colin Breck via Dave Farley: **AI changes tempo, not principles.** Both are
assertions by senior figures with no evidence attached, and the newer one should not quietly win
on recency. Worth holding as an open disagreement — and noting that it is partly a question about
*what* is being measured for magnitude: the rate of practice change (Fowler's reading) or the
durability of the underlying discipline (Farley's).

## Relationship to other notes

- [Five Studies on AI and Software Engineering Productivity](ai-productivity-research.md) — the
  other data signpost here, and the stronger one: peer-reviewed studies rather than interviews.
  Read this for *scale* indicators and that one for *effect* estimates.
- [Replacing Code Review With Upstream Verification](../engineering/ai-native/review-replacement.md)
  — holds the earlier GitHub PR-volume figure that this one extends with a crossover date.
- [Agile in the Age of AI](../engineering/ai-native/agile-in-the-age-of-ai.md) — the ~3 parallel
  agents figure this unsettles.
- [Model Routing and AI Gateways](../engineering/ai-native/model-routing-and-ai-gateways.md) —
  the Uber cost figures as production evidence for its argument.
- [Ramp's Inspect Agent Platform](../case-studies/ramp-inspect-agent-platform.md) — the
  parallel-session ceiling argument, now with a capacity constraint sitting behind it.
- [What Is Software Engineering? (Adapting to AI)](what-is-software-engineering-ai.md) — the
  Fowler/Farley disagreement about whether this shift is different in kind.
