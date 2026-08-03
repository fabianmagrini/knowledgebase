---
type: note
title: Over-Engineering Is Solving the Wrong Problem
description: "Over-engineering reframed as a requirements failure rather than a design failure: enough constraints leave exactly one solution, internal systems are products too, and the diagnostic is asking why things are built this way."
tags: [architecture, system-design, decision-making, reading]
topic: engineering/architecture
status: notes
level: intermediate
related:
  - concepts/constraints-as-a-lens.md
  - engineering/architecture/thinking-in-constraints.md
  - concepts/clean-code-and-solid.md
  - reading/building-software-is-learning.md
  - engineering/architecture/ddd-strategic-design.md
  - engineering/practices/software-design-principles.md
  - engineering/architecture/overview.md
source: "https://var0.xyz/posts/perfection-is-not-over-engineering.html"
updated: 2026-08-03
---

# Over-Engineering Is Solving the Wrong Problem

An argument (var0.xyz, July 2026) that the industry has quietly conflated two different
things. Teams say *"we don't want to build the perfect solution"* as though perfection were
the hazard, when the actual failure is elsewhere:

> Over-engineering is **solving the wrong problem**. That's the whole definition. Not "caring
> too much." Not "making it too good."

Pure argument — no data, and the worked example below is hypothetical. Its value is
definitional.

## Enough constraints leave one solution

The author's claim is that a perfect solution genuinely exists, conditional on a complete set
of requirements. Tighten the constraints far enough and the solution space collapses to a
single point — *"it's perfect **because** it's the only one that fits."*

The illustration: starting a new project with every language, tool and hosting model
available, serverless plus Python is a strong choice — no compilation step, upload to Lambda,
ship. For someone who doesn't know Python, or who must optimise for performance, it is the
wrong choice. Same problem space, different constraints, different "perfect". Narrow further
— Django or Flask? — and the answer still turns on which constraints are actually binding.

This is [Constraints as a Lens](../../concepts/constraints-as-a-lens.md) pushed to its limit.
That note holds that a constraint collapses an unmanageable space into a *tractable* one;
this argues that enough of them collapse it to a *singular* one. The practical instruction is
the same as in [Thinking in Constraints](thinking-in-constraints.md) — surface every
constraint rather than accepting the inherited ones.

## Systems are products

A libraries-and-internal-tools point that gets skipped:

> A library, an API, an internal tool… we like to pretend these are "purely technical," that
> they somehow sit outside the idea of a product. They don't.

Internal systems have users, those users have needs, and the shape of the right answer only
becomes visible once the thing is treated as a product with honestly-defined requirements.
The author's example: what a team needs might be better served by handing them a **package**
than by standing up an HTTP service. That decision is not discoverable from inside a purely
technical framing.

## The diagnostic

The tell that something is over-engineered:

> You start asking **why are things built the way they are?** and the answers don't hold.

The worked example is three people maintaining five microservices that share data between
them. The costs are concrete: what was a foreign key the database engine enforced becomes a
loose string id in a field, so integrity checks are gone — one service deletes a record and
the other keeps a dangling reference, finding out later the hard way. Set against that,
independent deploys, for a team of three working in one domain.

> You solved for a scaling and ownership problem that wasn't on the table.

Read through [DDD strategic design](ddd-strategic-design.md), this is a bounded-context
failure: services split along lines that don't correspond to real domain boundaries, so the
data keeps referencing across a seam that shouldn't have been cut.

The sharpest observation in the piece is what the signature is *not*:

> That's the signature. Not elegance. Not thoroughness. And it's not that these solutions are
> bad, usually they're the correct answer to the problems that were proposed. The problem is
> that those were problems you never had.

That distinguishes this from the over-abstraction caution in
[Clean Code and SOLID](../../concepts/clean-code-and-solid.md). The claim here is not that the
abstraction was too heavy — it is that the abstraction level was never the issue. Diligent
engineering against the wrong requirements produces something that looks like craft.

## The tension worth keeping

The conclusion is that over-engineering is a **failure of requirements gathering** — "call it
product engineering if you want."

That sits against [Building Software Is Learning](../../reading/building-software-is-learning.md),
where Thorsten Ball argues requirements *cannot* be fully known upfront: for anything new,
misalignment between builder and requester is inevitable rather than a process failure, and
the learning can only be accelerated, not avoided.

Both can hold, but not in their strongest forms. If requirements are partly discovered by
building, then "get every constraint on the table first" is an ideal rather than a procedure,
and the honest synthesis is narrower: **you can gather better requirements without gathering
complete ones, and most over-engineering comes from not trying.** The microservices example
supports that reading — nobody needed perfect foresight to ask whether independent deploys
were a problem the team actually had.

## Relationship to other notes

- [Constraints as a Lens](../../concepts/constraints-as-a-lens.md) — the constraint principle
  this pushes to its limit; arguably a fourth position on that hub's map.
- [Thinking in Constraints](thinking-in-constraints.md) — the practice of surfacing and
  challenging constraints, which is what this note says prevents over-engineering.
- [Clean Code and SOLID](../../concepts/clean-code-and-solid.md) — its over-abstraction
  caution is about *how much* abstraction; this argues the fault is *which problem*.
- [Building Software Is Learning](../../reading/building-software-is-learning.md) — the
  counterweight on whether complete requirements are obtainable at all.
