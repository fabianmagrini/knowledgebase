---
title: Self-Blame in Post-Incident Reviews
tags: [leadership, culture, communication, reading]
topic: sre
status: notes
level: intermediate
related:
  - sre/incident-swarming.md
  - leadership/learning-organisation.md
  - leadership/decision-facilitation.md
source: "https://greatcircle.com/blog/2026/04/21/self-blame-isnt-blameless/"
updated: 2026-07-11
---

# Self-Blame in Post-Incident Reviews

Brent Chapman argues that **self-blame is not blameless**. A review can be free of
finger-pointing and still fail, because the engineer at the centre of an incident
often blames *themselves* — "my bad, I'll be more careful next time" — and that
ends the investigation just as effectively as external blame would. The damage is
the same: the team accepts a simplified narrative and never reaches the systemic
contributors.

## Why self-blame is a failure mode

"I should have caught that" is a **thought-terminating cliché**. Once it is said and
accepted, the review stops looking. The systemic factors that actually shaped the
outcome go unexamined:

- slow or misleading dashboards
- inadequate deployment pipelines
- outdated runbooks
- schedule pressure that made the shortcut reasonable

Chapman links this to **incident heroism**: just as one person heroically holding a
system together during an incident masks the organisational gaps that made the
heroics necessary, one person absorbing all the blame afterwards masks the gaps that
made the mistake possible. Both patterns concentrate risk and learning in a single
individual instead of the system.

## Two borrowed concepts

| Concept | Origin | What it names |
|---|---|---|
| **Second-victim syndrome** | Healthcare / patient safety | The lasting guilt and anxiety a practitioner carries after being involved in an adverse event. Systemic reframing — not accepting the self-blame — is what helps them recontextualise their role. |
| **Superficial blamelessness** | Fred Hebert | A review that avoids retribution but still defaults to individualistic fixes ("be more careful", "add a checklist step") rather than systemic change. Blameless in tone, blameful in effect. |

## The facilitator's move

When self-blame surfaces, the author's recommended response is to redirect toward
**local rationality** — reconstructing why the action looked reasonable in the
moment rather than judging it with hindsight:

> "What were you seeing at the time? What information did you have? What made that
> action seem reasonable?"

These questions do three things at once: they signal that a shallow "my bad" is not
an acceptable stopping point, they normalise the engineer's decision-making, and they
reopen the investigation into the actual circumstances. Chapman frames the goal as
**organisational capability over individual heroics** — and reframes accountability
itself as *understanding how your company and its systems actually operate*, not
volunteering to carry the fault.

## Relationship to other notes

- [Swarming in Incident Response](incident-swarming.md) — the sibling from the same
  author, covering the *response* phase. Both rest on a genuinely blameless culture:
  swarming needs it so people feel safe volunteering; reviews need it so people feel
  safe surfacing systemic causes instead of absorbing the blame.
- [The Learning Organisation and AI Adoption](../leadership/learning-organisation.md)
  — states the general principle ("investigate the system, not the individual", via
  Edmondson's failure taxonomy). This note applies that principle to one specific
  moment: the point in a review where an engineer blames themselves.
- [Facilitating Technical Decisions](../leadership/decision-facilitation.md) — the
  redirect above is facilitation, not interrogation; drawing out local rationality is
  the same skill of surfacing reasoning rather than driving to a predetermined answer.
