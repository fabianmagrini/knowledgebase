---
type: reading
title: Ownership (Thorsten Ball)
description: "Thorsten Ball's end-to-end ownership checklist: taking responsibility for a problem from defining what it actually is through verifying it works in production and telling the people who need to know."
tags: [culture, reading]
topic: reading
status: notes
level: intermediate
related:
  - reading/building-software-is-learning.md
  - engineering/ai-native/modern-engineering-values.md
  - engineering/ai-native/own-the-outer-loop.md
  - case-studies/portkey-product-engineer-company.md
  - engineering/practices/release-confidence.md
source: "https://registerspill.thorstenball.com/p/ownership"
updated: 2026-07-19
---

# Ownership (Thorsten Ball)

Thorsten Ball describes what it means to **own the solution of a problem from end to
end**: not just writing the code, but taking responsibility for the whole arc from
working out what the problem actually is, through shipping, to confirming it works
in production and telling the people who need to know. He frames it as a mental
checklist for a small team — "we don't have PMs, we don't have a Q&A department" —
where the gaps are yours to close because no one else will.

## The end-to-end checklist

Ball's account of what taking ownership involves, roughly in order:

- **Define the problem** — separate the *actual problem* ("performance is bad") from
  a *proposed solution* ("migrate from X to Y"), and weigh the trade-offs before
  committing to an approach.
- **Think it through** — edge cases, failure modes, data flow, and how you would
  test it. (One testing option he mentions in passing: "you can ask an agent to run
  through test scenarios" — a single aside, not the focus.)
- **Align and communicate** — check the work fits the roadmap and that the right
  people know it is happening.
- **Execute** — "with precision, with care, with a sense of urgency."
- **Test it manually** yourself, not only via automation.
- **Verify in production** — "make sure it lands in production and *works in
  production*." Deployment is not the finish line.
- **Close the loop** — inform colleagues of relevant changes, notify affected
  customers, announce it to the world if appropriate, then watch logs and handle
  follow-ups.

## The load-bearing idea

The essay's core is not the list but the accountability behind it:

> What's not okay is to implicitly assume that someone else will do the things here
> that you haven't thought about.

Ownership is precisely the refusal to leave those gaps for an unnamed someone. Ball
pairs this with a personal quality bar — *"would I show this to John Carmack?"* — and
the blunt instruction to *"not half-ass things"* and to keep **peripheral vision**
for the consequences around the change, not just the change itself.

## Context and caveats

Ball is explicit that this is calibrated for a **small team** without dedicated PM
or QA roles, and that expectations are context-dependent: juniors should *aspire* to
this while asking for help, and not every item applies to every task. It is a
disposition to grow into, not a gate to fail people on.

## Relationship to other notes

- [Building Software Is Learning](building-software-is-learning.md) — the same
  author's companion essay; that one is about software work as a learning process,
  this one about the responsibility for seeing that work all the way through.
- [Modern Engineering Values](../engineering/ai-native/modern-engineering-values.md)
  — lists "ownership" as one of a practitioner's core values; this note is the
  concrete, checklist-level expansion of that single word.
- [Own the Outer Loop](../engineering/ai-native/own-the-outer-loop.md) — the
  agentic-era sibling: humans own the *accountability boundary* around agent work.
  Ball's checklist is what that human ownership looks like task-by-task, whether the
  code was written by a person or an agent.
- [The Product Engineer Company (Portkey)](../case-studies/portkey-product-engineer-company.md)
  — the same end-to-end-ownership ethos scaled into an operating model (engineers
  own the whole product slice, no PMs).
- [Release Confidence as a System Property](../engineering/practices/release-confidence.md)
  — "works *in* production" and closing the loop are individual-scale versions of
  the system-scale release-confidence discipline.
