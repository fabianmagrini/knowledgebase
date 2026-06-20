---
title: Swarming in Incident Response
tags: [leadership, culture, communication, reading]
topic: sre
status: notes
level: intermediate
related:
  - leadership/learning-organisation.md
  - leadership/decision-facilitation.md
  - leadership/managed-disruption.md
  - leadership/engineering-leadership-overview.md
  - concepts/resilient-software-design.md
source: "https://greatcircle.com/blog/2026/03/24/swarming-is-a-feature/"
updated: 2026-06-20
---

# Swarming in Incident Response

Brent Chapman argues that **swarming** — the spontaneous convergence of responders
on an incident, without being formally paged — is *a feature to facilitate, not a
bug to suppress*. People with relevant knowledge self-select in, often before the
incident commander even realises they are needed. He likens it to a **"white blood
cell response"**: an organisational immune reaction that matches expertise to a
problem faster than any formal routing process can.

> This is an organisational phenomenon, not an AI or software one — "swarming" here
> means *human* responders self-organising.

## Command-driven vs swarming

| Command-driven model | Swarming |
|---|---|
| On-call engineer → incident commander → deliberate paging | Responders self-select based on relevant expertise |
| One person must diagnose *and* route — bottlenecked by their knowledge | Expertise arrives faster than formal routing allows |
| Early diagnosis is often wrong, so the wrong teams get paged first | Self-selection avoids miscasting responders |

The command model is tidy on paper but bottlenecks through a single person's
understanding; swarming bypasses that. This is a
[Theory of Constraints](../concepts/theory-of-constraints.md)-style point: the
bottleneck is the router, and swarming relieves it.

## Swarming is not freelancing

Chapman is careful to distinguish **swarming** (coordinated self-selection toward
the shared response) from **freelancing** (uncoordinated individuals each doing
their own thing). The difference is coordination, not spontaneity — which is why
the enabling infrastructure below matters.

## Infrastructure that enables swarming

- **Visible response channels** — automated announcements of declared incidents
  with links and predictable naming (e.g. an `#inc-` prefix), surfaced across
  dashboards and chat.
- **A prepared, standing channel** — keep an `#incident-next` channel ready for
  informal response; formal declaration simply **renames** it, preserving the
  investigation history and the people already present.
- **Clear onboarding** — pinned situation summary, role assignments, and current
  status, with the expectation that arrivals **self-brief before** asking for an
  assignment (so scrollback doesn't overwhelm newcomers).
- **Asynchronous participation** — chat-first response (Slack over Zoom) lets people
  monitor and contribute without demanding real-time presence.

## What enables it vs what suppresses it

| Enables | Suppresses |
|---|---|
| A **blameless culture** where volunteering carries no risk | Blame-oriented cultures where stepping in is dangerous |
| Clear visibility of active incidents | Hidden or hard-to-find incident channels |
| Low friction to join and contribute | No onramp for newcomers; overwhelming scrollback |

The cultural precondition is the load-bearing one: swarming only happens where
people feel safe volunteering.

## Relationship to other notes

- [The Learning Organisation and AI Adoption](../leadership/learning-organisation.md) —
  the psychological safety and generative culture that note describes are exactly
  what let responders volunteer without fear; swarming is that culture under
  incident pressure.
- [Facilitating Technical Decisions](../leadership/decision-facilitation.md) —
  coordinating a swarm is facilitation, not command; both move away from a single
  decision bottleneck.
- [Managed Disruption](../leadership/managed-disruption.md) — incidents are acute
  disruption; swarming is how an organisation absorbs it in the moment.
- [Resilient Software Design](../concepts/resilient-software-design.md) — a
  cross-cluster bridge: swarming is *organisational* resilience (graceful
  degradation and recovery in the response system) mirroring the *software*
  resilience patterns there.
