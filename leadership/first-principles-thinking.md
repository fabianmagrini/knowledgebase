---
title: First-Principles Thinking
tags: [leadership, reading, decision-making]
topic: leadership
status: notes
level: intermediate
related:
  - leadership/decision-facilitation.md
  - leadership/start-with-why.md
  - leadership/engineering-leadership-overview.md
  - engineering/architecture/agile-design-decisions.md
  - leadership/designing-with-constraints.md
  - leadership/raising-problems-without-complaining.md
  - engineering/architecture/thinking-in-constraints.md
  - concepts/constraints-as-a-lens.md
source: "https://www.philmckinney.com/how-to-improve-your-first-principles-thinking-skills/"
updated: 2026-06-17
---

# First-Principles Thinking

First-principles thinking is the practice of breaking a problem down to its fundamental truths
and building a solution up from what actually holds. The contrast is **reasoning by analogy** —
deciding from precedent, competition, and convention. Analogy works until the underlying
conditions change and nobody notices; the argument is that the most expensive assumption is not
one you have not yet thought of, but one you stopped questioning years ago.

## The cost of inherited assumptions

The author (Phil McKinney, a former HP CTO) illustrates with an HP example: the company
benchmarked innovation using "R&D as a percentage of revenue". The metric was inherited from
decades earlier and never re-examined, yet it measured accounting categories rather than
innovation output. Treated as bedrock when it was really "a choice nobody remembered making", it
is described as draining the innovation pipeline over a decade.

The trap is that **experience becomes a blind spot**: the more familiar a constraint, the more it
feels like a fact rather than a choice. This is called **derivative thinking** — following
inherited constraints — and its cost is measured in years, not quarters.

## The three-skill framework

### 1. Strip the assumptions

1. Write the problem in its original framing and language.
2. Underline words that imply constraints — "must", "can't", "always", "never".
3. Classify each constraint: **physically true** vs. **inherited**.
4. Set the inherited ones aside and restate the actual problem.
5. Treat the survivors as the real design constraints for brainstorming.

### 2. Test what remains and build up

1. Push on each surviving constraint; separate *expensive or unfamiliar* from *impossible*.
2. Distinguish **hard limits** (physically immutable — physics, unit economics, human behaviour
   at scale) from **soft limits** (negotiable — merely costly, unfamiliar, or uncomfortable).
3. State each hard limit plainly, one sentence each.
4. **Reason forward** from the hard limits rather than backward from convention. Forward reasoning
   yields unexpected solutions; backward reasoning yields modified versions of existing answers.

### 3. When to use it

Run the process if any of these is "yes":

- Has the environment changed significantly?
- Do all the candidate solutions feel like variations of the same thing?
- Is the current approach inherited rather than deliberately chosen?
- Would a bad assumption here cost more than an afternoon to discover?

## Practice: the assumption-reversal exercise

A partner-based technique:

1. Each person brings one real, high-stakes problem.
2. Partners analyse *each other's* problem — an outside view sees the assumptions more clearly.
3. List every assumption without evaluating; prioritise quantity.
4. Reverse each assumption ("requires budget" → "what if it required no budget?").
5. Discuss what the reversals reveal; usually one exposes a constraint that is actually negotiable.

## Anti-patterns

- Skipping assumption-stripping, then spending months optimising a solution to the wrong problem.
- Treating every constraint as granite (immutable).
- Relying on past experience after the environment has changed significantly.
- Anchoring to the shape of existing answers instead of reasoning from constraints.

## Relationship to other notes

- [Facilitating Technical Decisions](decision-facilitation.md) — first-principles thinking is a
  way to frame the *problem* before a group decides; it pairs with the decision frame there.
- [Start with the Why](start-with-why.md) — both push past inherited "how" toward the underlying
  purpose and the truths that actually hold.
- [Agile Design Decisions and Principles](../engineering/architecture/agile-design-decisions.md) —
  the reversibility / blast-radius / delegation frameworks are themselves a way to separate hard
  limits from soft ones when deciding how much rigour a decision needs.
