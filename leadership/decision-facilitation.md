---
type: note
title: Facilitating Technical Decisions
description: "As engineers get more senior, the failure mode shifts from \"can't explain it\" to over-explaining — teaching the room instead of driving alignment; plus the listener's side, where simulating the implementation while listening generates a question every thirty seconds."
tags: [leadership, communication, decision-making]
topic: leadership
status: notes
related:
  - leadership/architecture-decision-forum.md
  - leadership/start-with-why.md
  - engineering/architecture/agile-design-decisions.md
  - leadership/protecting-mavericks.md
  - leadership/principal-engineer-influence.md
  - leadership/principal-engineer-consensus.md
  - leadership/first-principles-thinking.md
  - leadership/raising-problems-without-complaining.md
  - sre/incident-swarming.md
  - sre/self-blame-in-incident-reviews.md
  - sre/cognitive-diversity-in-incident-reviews.md
  - leadership/arguing-to-win.md
  - leadership/new-leader-credibility.md
  - leadership/revised-rules-engineering-leadership.md
  - leadership/senior-ic-role.md
  - engineering/architecture/event-storming.md
  - leadership/engineering-manager-role.md
  - reading/how-i-use-llms-2026.md
  - leadership/learning-organisation.md
  - reading/multi-agent-coding-coordination.md
  - engineering/ai-native/substitution-myth-in-code-review.md
source: "https://gist.github.com/fabianmagrini/10e09bb9cef680c07cad82e7bfbcb441; https://www.seangoedecke.com/you-should-all-be-asking-way-more-questions/"
updated: 2026-10-25
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

## The other side of the table

Everything above is the **speaker's** craft. The listener's side has its own, and
[Sean Goedecke](https://www.seangoedecke.com/you-should-all-be-asking-way-more-questions/)
(September 2026) argues it is mostly **asking far more questions than feels polite** — at a rate
he puts at *"on average one question every thirty seconds."*

**Why interrupt rather than save them up**, which is the argument that earns the practice,
because interrupting is socially expensive:

> A small misunderstanding early on balloons into a big misunderstanding later, because all the
> things you misinterpret based on the first misunderstanding will become misunderstandings in
> their own right, and so on. That's why you can't just wait until someone's finished talking
> and ask all your questions at once.

**Where the questions come from.** The technique that makes this more than willingness is
simulating the implementation while listening — *"visualizing the specific lines of code that
would need to be written in order to implement it."* At minimum:

- how data flows between services — what kind, and how it travels over the wire
- how services communicate, *"e.g. how will they auth?"*
- what data needs to be persisted, and where it will live

Hold those three against a plan as it is described and the gaps announce themselves. Much of the
question-asking advice elsewhere — *"ask clarifying questions rather than declaring problems"* in
[Principal Engineer Influence](principal-engineer-influence.md), Wells's *"surface hidden
questions"* in [Multi-Agent Coding Coordination](../reading/multi-agent-coding-coordination.md) —
says to do it without saying how the questions are generated. This is the how.

Two supporting details: his preferred form is **confirmation rather than enquiry** — *"so when
you say X, you mean Y?"*, or *"this X is the thing you mentioned earlier when you were saying
Z?"* — which makes a misunderstanding cheap to correct. And his diagnosis of why people do not
do it is **skin in the game**: *"When you're in a position where you are the one responsible for
success or failure — where you are going to have to go away after the conversation and take a
bunch of concrete actions — you will find yourself wanting to ask many questions."* Note that
these notes already hold that phrase from **John Allspaw** in
[The Substitution Myth in Code Review](../engineering/ai-native/substitution-myth-in-code-review.md),
where it is better sourced and concerns review accountability; this is a different application of
the same idea.

### The apparent contradiction, and what resolves it

**High signal / low noise** above and one question every thirty seconds look like opposite
advice. They are not, and the distinction is worth stating: the noise being cut is the
*speaker's* unrequested background, derivations and re-justification. The listener's questions
are the highest-signal utterances in the room, because each one is evidence about whether
alignment is actually happening. Timeboxing aggressively and pruning threads is compatible with
being interrupted constantly — what is not compatible is a speaker who treats interruption as
disruption.

**The absence that decides whether any of this is usable.** Goedecke acknowledges the social cost
only as *"I'm sure this is frustrating to some people"*, and says nothing about **who can afford
to do it**. A staff engineer questioning every thirty seconds is received very differently from a
graduate doing the same thing, and the piece does not address the asymmetry. The condition is in
[The Learning Organisation](learning-organisation.md) — psychological safety, where *"people feel
secure asking questions, admitting confusion"* — which makes this advice for the room to enable
rather than only for the individual to adopt. His support throughout is anecdotal: one story
about a neighbouring team's *"complex event-driven system that was very elegant but made it
completely impossible to silo customer data in a single datacenter"*, against a flagship
single-location guarantee, so it was abandoned. A good illustration of a design error that
questioning would have caught, and a single case.

## Why it works

It accelerates shared understanding and raises execution quality: the group converges on a
decision they own, rather than passively receiving a lecture they may not act on. It pairs
with [start with the why](start-with-why.md) — lead with purpose and constraints, then
facilitate the choice.
