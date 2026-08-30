---
type: note
title: Landing the Plane
description: "James Stanier argues the end of a project needs more leadership attention than the start — why work stalls at 90%, how late scope arrives disguised as good ideas, and what formal closure involves."
tags: [leadership, decision-making, reading]
topic: leadership
status: notes
level: intermediate
related:
  - product/prioritisation-as-a-symptom.md
  - concepts/optimal-stopping.md
  - leadership/managed-disruption.md
  - engineering/practices/release-confidence.md
  - leadership/engineering-manager-role.md
  - leadership/magical-thinking.md
  - leadership/engineering-leadership-overview.md
source: "https://www.theengineeringmanager.com/growth/landing-the-plane/"
updated: 2026-08-30
---

# Landing the Plane

James Stanier (The Engineering Manager, August 2026) takes the aviation cliché seriously as a
management claim: takeoff is exciting and largely procedural, **landing is where the accidents
happen**, and the two need different skills. Applied to delivery, the argument is that the end
of a project deserves *more* leadership presence than the start, and usually gets less.

**Provenance.** This is a practitioner essay, not research. It carries no original evidence,
and the psychological scaffolding it borrows is of uneven strength — the ninety-ninety rule is
an aphorism, and the Zeigarnik effect and peak-end rule both have contested replication
records. The mechanisms are best read as *illustrative vocabulary for a familiar experience*
rather than as load-bearing findings; the operational advice stands on its own without them.
The page also carries newsletter and book promotion.

## Why the last stretch is genuinely harder

Two causes, and it is worth keeping them separate because they have different remedies.

**Structural.** What remains at the end is the residue: edge cases, integrations with systems
you don't control, and decisions nobody anticipated. It is the least estimable work in the
project, and it arrives at the moment estimates are being scrutinised most closely. Tom
Cargill's ninety-ninety rule — "the first 90% of the work takes 90% of the time, and the
remaining 10% takes the other 90%" — is the joke version of this.

**Psychological.** Novelty pays out early; completion is unglamorous. Stanier reaches for Seth
Godin's *Dip* for the shape of it, and for **completion bias** — research by Diwas KC and
colleagues that "when workload rises, people gravitate towards easier tasks to maintain a sense
of progress." The observable behaviour is the useful part: under end-of-project pressure a team
clears a queue of small tickets while the one hard blocker sits untouched, and the burndown
looks healthy throughout.

The goal-gradient effect (Kivetz, Urminsky and Zheng) supplies the caveat that matters most for
management: effort accelerates near a goal **only when the finish line is visible and stable**.
A finish line that keeps moving doesn't merely delay the work, it removes the mechanism that
was carrying it.

## The quiet death

The failure mode Stanier names, and the one the repo has no other word for: a project that is
never cancelled and never finished. It fades at 90–95%, having consumed nearly its full cost
and delivered nothing. No decision is taken, so there is no post-mortem, no reallocation, and
no learning — and the next initiative starts against a background belief that things here don't
land.

That is a sharper framing than "the project was late." A cancelled project at 40% returns
budget and a lesson. A quiet death at 95% returns neither, which makes it the more expensive
outcome despite looking like the more diligent one.

## Noble obstacles

The vocabulary worth borrowing, via Jon Acuff: **noble obstacles** are late additions that
arrive disguised as diligence. Dark mode. One more refactor before we ship. A performance pass.
An extra config option a stakeholder mentioned.

Each is defensible in isolation, which is exactly what makes the category hard to police —
refusing any single one looks like carelessness, and the person proposing it is usually acting
in good faith. Naming the class lets the conversation happen once, at the level of *we are in
the descent and are not taking new scope*, instead of relitigating each item on its individual
merits. The stock reply Stanier offers: **"That's great for v2."**

## Flying the descent

| Practice | What it is doing |
|---|---|
| Raise check-in cadence — weekly to twice-weekly or daily | Surfacing the avoided blocker before it becomes the schedule |
| One prioritised backlog, all new requests deferred to v2 | Keeping the finish line stationary |
| Brief daily stakeholder updates | Buying the scope protection by removing the anxiety that drives requests |
| Explicit scope trades rather than silent absorption | Making the cost of an addition visible to the person asking |
| Checklists over heroics | The aviation borrowing that actually transfers — a landing shouldn't depend on who is on shift |

The through-line is that the leader gets *closer* during the descent, not further away. Late-
stage projects are often the ones a manager steps back from, on the reasoning that the work is
understood and the team has it — which is the moment the two failure modes above are least
likely to be reported upward.

## Closure as a practice

Peak-end reasoning is the weakest evidence in the piece, but the prescriptions it motivates are
sensible on ordinary grounds:

- **Retrospect while it is fresh** — the specific insights decay within days of shipping.
- **Mark the landing explicitly** — written acknowledgement, individual recognition, time back.
  A project that ends by everyone drifting onto the next thing reads as *that didn't matter*.
- **Plan for the energy dip** — the team is depleted precisely when the next initiative is
  most tempting to start. Stacking it immediately borrows against the next landing.

For prevention, Stanier suggests auditing current projects for anything stuck near done,
writing a pre-mortem before entering the final stretch, and keeping a reusable landing
checklist.

## Relationship to other notes

- [Prioritisation as a Symptom](../product/prioritisation-as-a-symptom.md) — the complement.
  That note is about choosing what to start; this one is about the discipline of not
  re-choosing once you have.
- [Optimal Stopping and the 37% Rule](../concepts/optimal-stopping.md) — "done enough" is a
  stopping problem. Optimal stopping formalises when to stop *searching*; this is the softer
  organisational version, where the cost of continuing is mostly unbooked.
- [Managed Disruption](managed-disruption.md) — the counterweight, and a real tension. Managed
  disruption is about absorbing change into delivery safely; this argues for a phase where
  change is deliberately refused. Both are right at different points in a project's life, and
  the skill is knowing which phase you are in.
- [Release Confidence as a System Property](../engineering/practices/release-confidence.md) —
  the mechanical counterpart. That note is about the deployment being safe; this is about the
  project reaching a deployment at all.
- [The Engineering Manager Role](engineering-manager-role.md) — already holds obstacle removal
  as the core job. The descent is where the obstacles are least visible from outside the team.
- [Magical Thinking in Engineering Leadership](magical-thinking.md) — a related failure mode.
  Where magical thinking substitutes rhetoric for operational work, the quiet death substitutes
  no decision at all; both leave the leader without evidence against their own approach.
