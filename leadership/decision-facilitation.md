---
title: Facilitating Technical Decisions
tags: [leadership, communication, code-review]
topic: leadership
status: notes
related:
  - leadership/architecture-decision-forum.md
  - leadership/start-with-why.md
  - engineering/architecture/agile-design-decisions.md
  - leadership/protecting-mavericks.md
  - leadership/principal-engineer-influence.md
  - leadership/first-principles-thinking.md
source: "https://gist.github.com/fabianmagrini/10e09bb9cef680c07cad82e7bfbcb441"
updated: 2026-06-13
---

# Facilitating Technical Decisions

As engineers get more senior, the failure mode shifts from "can't explain it" to
**over-explaining** — teaching the room instead of driving alignment. The transformation is
from *proving a solution is correct* to *facilitating a quality decision*.

> **High signal / low noise:** only say things that change how people think, decide, or act.

Everything else — background, derivations, full justifications — belongs in pre-reads, deeper
sessions, or on-demand explanation, not the live discussion.

This is the personal-skill counterpart to the
[architecture decision forum](architecture-decision-forum.md): it operationalises the
facilitator role, and puts the [decision frameworks](../engineering/architecture/agile-design-decisions.md)
into words.

## The decision frame

Structure the conversation around the decision, not the explanation:

> **Decision:** What are we deciding?
> **Options:** What are the viable paths?
> **Trade-offs:** What do we gain / lose?
> **Recommendation:** What do you propose?
> **Open questions:** What still needs input?

## Reframe what you say

| Instead of… | Say |
|---|---|
| Explaining everything | "I'll focus on the decisions we need to align on — especially constraints and trade-offs." |
| Presenting a full solution | "The core tension here is between consistency and team autonomy." |
| Defending in depth | "This is a trade-off decision, not a perfect one." |

## Techniques

- **Lead with constraints, not solutions.** The constraints frame the whole conversation;
  the solution is a consequence of them.
- **Name the trade-off axis explicitly** (e.g. consistency vs. autonomy) so discussion
  stays on one dimension instead of sprawling.
- **Separate facts, assumptions, and opinions.** Label which is which — most disagreement is
  really disagreement about an assumption.
- **Quantify impact** where you can; a number ends a debate a paragraph can't.
- **Use silence** after a key point — let the room think rather than filling the gap.
- **Timebox aggressively:** ~5 min context, ~5 min options, 10–20 min discussion.
- **Detect circular detail** and stop mid-explanation — if you're re-justifying, you've
  already made the point.
- **Prune off-topic threads** actively, and **end early** when alignment is reached.

## Why it works

It accelerates shared understanding and raises execution quality: the group converges on a
decision they own, rather than passively receiving a lecture they may not act on. It pairs
with [start with the why](start-with-why.md) — lead with purpose and constraints, then
facilitate the choice.
