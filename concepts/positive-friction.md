---
type: note
title: Positive Friction
description: "A name for something these notes arrived at three times without one: an incidental cost that was also carrying a benefit, so removing the cost removes the benefit — and the harder category, because an unchosen constraint cannot be defended."
tags: [decision-making, culture, refactoring, ai-engineering, reading]
topic: concepts
status: notes
level: intermediate
related:
  - engineering/architecture/design-docs.md
  - engineering/ai-native/tdd-in-the-agent-loop.md
  - engineering/ai-native/trust-factory.md
  - leadership/designing-with-constraints.md
  - concepts/constraints-as-a-lens.md
  - concepts/theory-of-constraints.md
  - reading/offloading-thinking-to-ai.md
  - engineering/ai-native/substitution-myth-in-code-review.md
  - case-studies/tano-eleven-x-pr-throughput.md
  - engineering/ai-native/linters-over-ai-review.md
  - engineering/practices/change-absorption-capacity.md
  - product/four-abstraction-levels-of-refinement.md
  - product/predictability-vs-outcomes.md
  - product/modelling-business-impact.md
  - leadership/decision-facilitation.md
  - engineering/architecture/change-locality.md
  - engineering/architecture/reversibility-decays.md
  - case-studies/linear-ci-rework.md
  - leadership/revised-rules-engineering-leadership.md
source: "https://cutlefish.substack.com/p/tbm-450-the-loss-of-positive-friction"
updated: 2026-11-21
---

# Positive Friction

John Cutler (*The Beautiful Mess*, November 2026) names something these notes have arrived at
three separate times without a word for it:

> The bottleneck was both a bottleneck **AND** an enabling constraint. The thing that was
> annoying, challenging, glacial, and vibe-crushing was also the thing that forced us to pay
> attention (even if we hated it).

Or compressed: *"A constraint can be 'enabling' and 'limiting' at the same time."*

## The three arrivals it names

| Note | The same observation, unnamed |
|---|---|
| [Writing an Effective Design Doc](../engineering/architecture/design-docs.md) | The Amazon memo as **proof-of-work** — the thinking it forced *"was a property of writing being expensive"*, and cheap generation voids the certificate while leaving the ritual intact |
| [TDD Inside the Agent Loop](../engineering/ai-native/tdd-in-the-agent-loop.md) | *"**The forcing function collapses.** For a human, writing the test first constrains a design that does not exist yet — the friction **is** the value"* |
| [The Trust Factory](../engineering/ai-native/trust-factory.md) | Beck's **single-player development**: solo human-plus-genie work *"removes the person-to-person interactions (pairing, review, planning) where trust is actually built"* |

Each says a cost was quietly carrying a benefit, and the benefit departs with the cost. Having
the general term is worth something because it makes the question askable *before* the removal
rather than diagnosable afterwards: **what is this friction currently forcing, and what forces
it once the friction is gone?**

## The distinction from deliberate constraints

[Designing with Constraints](../leadership/designing-with-constraints.md) already holds that
*"constraints enable rather than restrict creativity"* — but those are constraints somebody
**chose**: one page maximum, one defining constraint, a separable core. Cutler's are
**incidental** — a slow approval, a revision cycle, a remote pairing session nobody enjoyed.

That difference is the whole problem, and it runs in the hard direction:

| | Chosen constraint | Positive friction |
|---|---|---|
| Visibility | Named, documented, defensible | Invisible until removed |
| Who argues for it | Whoever imposed it | Nobody |
| On a proposal to remove it | "That constraint is doing X" | "Finally" |

**You can defend a constraint you chose; you cannot defend one you never knew you had.** Which
is why the losses in the three notes above were all discovered retrospectively.

## What was actually being bought: time

His three examples are specific about the lost function rather than vaguely nostalgic:

- the *"dumb"* project ROI pro forma *"at least forced us to wait a couple of days or weeks for a
  better alternative to emerge"*
- the pairing session was *"a critical way to extend the hivemind of the team"*
- six rounds of revision on a doc *"meant that the team had a couple of days to reflect before
  pressing send"*

**Two of the three bought delay, not rigour**, and that is sharper than the usual slow-is-good
claim. If the mechanism was *elapsed time for a better idea to surface*, then replacing the
process with a faster, higher-quality version does not restore the function — a better pro forma
produced in an hour buys nothing the slow one bought. The replacement has to supply **waiting**,
which no quality improvement does.

His contractor anecdote is the same mechanism in miniature: being *"forced to look at the plans
for a bit, consider the cost, and walk impatiently around the house thinking about how we live
has inspired objectively better decisions."*

## The diagnostic

The questions he says friction used to force are usable as a test:

- *"Is this worth it?"*
- *"Is that actually what they meant?"*
- *"Is this design workable in the long run?"*

For any process being removed, ask which of these it was forcing. **If the answer is none, the
friction was waste and should go.** That gives the concept a falsifiable edge, which it badly
needs — see the objection below.

Note what the three map onto. *Is this worth it* is
[Modelling Business Impact](../product/modelling-business-impact.md) and
[Predictability vs Outcomes](../product/predictability-vs-outcomes.md). *Is that actually what
they meant* is level 1 in
[The Four Abstraction Levels of Refinement](../product/four-abstraction-levels-of-refinement.md)
and the confirmation questions in
[Facilitating Technical Decisions](../leadership/decision-facilitation.md). *Is this design
workable in the long run* is [change locality](../engineering/architecture/change-locality.md)
and [reversibility decay](../engineering/architecture/reversibility-decays.md). **The questions
are all held here; what was not held is that a process could be the thing asking them.**

## Single-player gravity

His sharpest observation, and an escalation of Beck rather than a restatement:

> As people turn inwards into their own little AI-assisted universe, their own 'team' of agents,
> and their own workflows, there is even LESS patience… It is **too easy** to work in
> single-player mode. And multiplayer mode seems archaic in comparison. Almost quaint. A reminder
> of all that messy friction.

[The Trust Factory](../engineering/ai-native/trust-factory.md) says single-player development
*erodes* trust. Cutler adds that it becomes **preferred** — so the erosion is self-reinforcing
rather than a one-time cost. Collaborative practice does not merely get skipped; it starts to
feel like an imposition, which is a much harder thing to reverse than a lapsed habit.

The evidence for this in these notes is a first-person account.
[Tano](../case-studies/tano-eleven-x-pr-throughput.md) reports exactly the loss, from someone who
chose the trade: *"Code reviews used to be one of my favourite things at PostHog. I had a feed of
every PR coming in and I read them all… Having no time to read all PRs means missing context
across the business."* Reading every PR was friction. It was also how one engineer held a model
of the whole business, and nothing replaced it. The same mechanism underlies
[The Substitution Myth in Code Review](../engineering/ai-native/substitution-myth-in-code-review.md):
review's non-detection functions were never anyone's stated purpose for reviewing, so they were
not defended when review was optimised away.

## The objection, which the piece does not answer

**He never concedes that most friction is genuinely waste**, and the omission matters: without
that concession, "positive friction" is available as a defence of any status quo, which is
precisely how the term will be misused. *"We shouldn't automate this, the slowness makes us
think"* is an argument that can be made about anything.

These notes hold a strong counterweight, and it should be read alongside:

- [Linters Over AI Review](../engineering/ai-native/linters-over-ai-review.md) — **27 seconds**
  pre-commit against PR-time feedback; the latency *was* the problem, and removing it is the win
- [Linear's CI Rework](../case-studies/linear-ci-rework.md) — setup overhead as a pure cap on
  parallelism, with nothing redeeming about it
- [Revised Rules of Engineering Leadership](../leadership/revised-rules-engineering-leadership.md)
  — AI-tool adoption moving **25% → 100% by removing friction**
- [Change Absorption Capacity](../engineering/practices/change-absorption-capacity.md) — the
  problem is usually too little absorption capacity, not too much speed

The defensible version is narrower than the title suggests: **friction is not valuable, but some
friction is load-bearing, and the load is invisible from outside.** The test above is what
separates the two, and it is the only thing standing between this concept and nostalgia.

**He also offers no practices** — the piece names the problem and stops. The actionable material
has to come from the instances: **study hall** (enforced reading, in `design-docs`, which
survives cheap generation because it forces *consumption* rather than production), **a human
writing the test first** then handing it to an agent (`tdd-in-the-agent-loop`, which preserves
the forcing function precisely because the constraint comes from someone who has not seen the
implementation), and **deliberate occasional friction** — doing the thinking manually on purpose,
from [Offloading Thinking to AI](../reading/offloading-thinking-to-ai.md).

> **Provenance.** A short newsletter post with **no data and no named cases** — a contractor
> anecdote and some customer calls carrying the whole argument. Filed for the vocabulary and the
> diagnostic, not the evidence.

## Relationship to other notes

- [Writing an Effective Design Doc](../engineering/architecture/design-docs.md),
  [TDD Inside the Agent Loop](../engineering/ai-native/tdd-in-the-agent-loop.md) and
  [The Trust Factory](../engineering/ai-native/trust-factory.md) — the three instances this names.
- [Designing with Constraints](../leadership/designing-with-constraints.md) — chosen constraints
  that enable; this is the incidental kind, which nobody is positioned to defend.
- [Constraints as a Lens](constraints-as-a-lens.md) and
  [Theory of Constraints](theory-of-constraints.md) — the bottleneck as the thing to relieve;
  Cutler's addition is that the bottleneck may also be doing work you have not accounted for,
  which is a real caveat to "elevate the constraint".
- [Offloading Thinking to AI](../reading/offloading-thinking-to-ai.md) — deliberate occasional
  friction as the individual-scale practice, and the convenience trap as the same mechanism
  applied to thinking rather than to process.
- [Tano](../case-studies/tano-eleven-x-pr-throughput.md) — the loss reported first-hand by
  someone who chose it.
- [Linters Over AI Review](../engineering/ai-native/linters-over-ai-review.md) — the
  counterweight: friction that was simply cost.
