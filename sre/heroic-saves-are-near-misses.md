---
type: note
title: Heroic Saves Are Near Misses
description: "why a save that only worked because of luck, timing, or one specific person carries the same information as an outage — and why recognition systems quietly select for heroics over preparedness"
tags: [leadership, culture, reading]
topic: sre
status: notes
level: intermediate
related:
  - sre/self-blame-in-incident-reviews.md
  - sre/incident-swarming.md
  - leadership/learning-organisation.md
  - leadership/landing-the-plane.md
  - leadership/coach-and-judge.md
source: "https://greatcircle.com/blog/2026/07/21/heroic-saves-are-near-misses/"
updated: 2026-08-30
---

# Heroic Saves Are Near Misses

Brent Chapman borrows the **near miss** from aviation and other safety-critical fields and
applies it to incident response. A near miss and an accident share the same underlying
vulnerability; only the outcome differs. The claim that follows is the whole argument: a
dramatic save is a near miss, because it worked "because of luck, timing, or the presence of
one specific person" — none of which are properties of the system.

The operational consequence: **a save should trigger the same investigation an outage would.**
Where an outage prompts a review as a matter of course, a save prompts a thank-you and nothing
else, so the identical latent weakness goes unexamined in one case and examined in the other.

**Provenance.** An essay from a consultant who has led incident management at Google and Slack.
No data; the argument rests on the aviation analogy and on experience. The page promotes his
consulting practice and a forthcoming book, *Incident Management for DevOps and SRE*. This is
also his third piece in these notes — see the caveat at the end.

## The caveat, which the argument needs

Chapman is not arguing against gratitude, and the note would misrepresent him without this:

> "When someone saves the day at 3 a.m., thank them." … "Heroes are still welcome, and still
> admired."

The individual's "skill, expertise, and dedication are worth appreciating." What he is arguing
about is where **sustained** recognition points — the promotion case, not the Slack message.

## The perverse incentive

The mechanism is an asymmetry in visibility, and it works without anyone intending it.

| | Visibility | Effect on recognition |
|---|---|---|
| **The heroic save** | Dramatic, timestamped, witnessed by everyone on the call | Rewarded readily; it makes a legible story |
| **Preparedness work** — runbooks, training, coordination, monitoring | Produces the absence of an event | "Largely invisible in performance reviews" |

An organisation that rewards only what it can see therefore **selects for heroics over
preparedness** while believing it values both. Chapman's remedy is stated at the level of what
to notice: "Recognize the work that makes heroic saves unnecessary: the runbooks, the training,
the well-coordinated responses."

The compounding problem is that the hero becomes a single point of failure — the bottleneck and
the knowledge store — and leadership stays unaware of the structural weakness for as long as the
heroes keep delivering. Success is exactly what suppresses the signal.

## "Heroic" as a stage, not a compliment

Chapman uses **Heroic** as the name of the earliest stage in an incident-management maturity
model: response quality is a property of *specific talented individuals rather than of the
company*. The reframe is useful — it makes "we have great incident responders" a diagnosis
rather than a boast.

Recorded accurately: he names only this first stage and refers to "the rest of the maturity
model" without setting out the others, so there is no model here to capture. The single label is
the takeaway.

His prescription is correspondingly general — "investigate why the heroics were necessary, and
invest in the answers." No questions, checklist, or process are offered. The practical gap is
that a review triggered by a *success* has no natural convening moment the way an outage does,
and the piece does not say what creates one.

## Relationship to other notes

- [Self-Blame in Post-Incident Reviews](self-blame-in-incident-reviews.md) — the sibling from
  the same author, which already carries this argument in one sentence as an analogy. The pair
  is symmetrical: heroism concentrates the *saving* in one person, self-blame concentrates the
  *fault* in one person, and both leave the system unexamined. That note is about facilitating
  the conversation; this one is about what the organisation rewards.
- [Swarming in Incident Response](incident-swarming.md) — the structural alternative, and the
  same author's positive case. A swarm distributes response across whoever holds relevant
  context; a hero is what a company has instead of one.
- [The Learning Organisation and AI Adoption](../leadership/learning-organisation.md) — states
  the general principle via Edmondson: investigate the system, not the individual. This applies
  it to an unusual case — a *success*, where nothing appears to need investigating.
- [Landing the Plane](../leadership/landing-the-plane.md) — already prescribes checklists over
  heroics, on the grounds that a landing shouldn't depend on who is on shift. Both borrow from
  aviation; this note supplies why the borrowing is more than a metaphor, since the near miss is
  a real reporting category in that field.
- [Coach and Judge](../leadership/coach-and-judge.md) — the recognition system as a management
  instrument. Both notes turn on the gap between what a manager says is valued and what their
  behaviour actually rewards.

## A note on this cluster

This is the third Chapman piece filed here, making him the source of three of the four notes in
`sre/`. The arguments hold up individually, but the folder now largely reflects one consultant's
view of incident practice. A future source that disagrees with him — or simply comes from an
operator rather than an adviser — would do more for this cluster than a fourth agreement.
