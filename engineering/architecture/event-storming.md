---
type: note
title: Event Storming
description: "the collaborative DDD discovery workshop: the three levels (big picture → process → software design), the sticky-note grammar, and how clusters of domain events surface bounded contexts"
tags: [architecture, system-design, microservices]
topic: engineering/architecture
status: notes
level: intermediate
related:
  - engineering/architecture/ddd-strategic-design.md
  - engineering/architecture/bounded-context-canvas.md
  - engineering/architecture/team-topologies.md
  - leadership/decision-facilitation.md
source: "Alberto Brandolini — Introducing EventStorming (2013)"
updated: 2026-06-21
---

# Event Storming

Event Storming, devised by Alberto Brandolini, is a collaborative workshop for exploring a domain
quickly by mapping its **domain events** on a long wall of sticky notes. Domain experts and
developers model together in the same room, so knowledge is shared rather than handed off through a
spec. It is the discovery technique that most naturally feeds
[Domain-Driven Design strategic design](ddd-strategic-design.md): the clusters of events it
surfaces become candidate [bounded contexts](bounded-context-canvas.md).

## The three levels

Event Storming is run at increasing resolution depending on the goal:

| Level | Purpose | Output |
|---|---|---|
| **Big Picture** | Explore the whole business line; build shared understanding and surface conflict | A timeline of domain events across the org; hotspots |
| **Process Modelling** | Zoom into one process; add the commands, actors, and policies that drive events | A causal model of one workflow |
| **Software Design** | Detail one bounded context for implementation | Aggregates, read models, and the seeds of an event-driven design |

## The notation (sticky-note grammar)

A consistent colour vocabulary keeps the wall legible:

- **Domain event** (orange) — something that happened, in past tense: *"Order Placed"*. The
  backbone of the model.
- **Command** (blue) — an action/intent that causes an event: *"Place Order"*.
- **Actor** (small yellow) — the person/role issuing a command.
- **Policy** (lilac) — a reactive rule: *"whenever X, do Y"* — links an event to a downstream command.
- **Aggregate** (large yellow) — the consistency boundary commands land on and events emit from.
- **Read model** (green) — the information an actor needs to decide.
- **External system** (pink) — a system outside the boundary that emits or consumes events.
- **Hotspot** (red/rotated) — a question, conflict, or risk to return to. Capturing disagreement
  *visibly* is a primary output, not a distraction.

## Why it works

- **Collapses the knowledge silo.** Experts and engineers build one model together, so the
  ubiquitous language forms live rather than being reverse-engineered from code.
- **Events first.** Starting from what *happened* (not data or UI) keeps the focus on business
  behaviour, which is more stable than structure.
- **Surfaces boundaries cheaply.** Where the language and the pace of change shift along the
  timeline is where a [bounded context](ddd-strategic-design.md) — and often a
  [team boundary](team-topologies.md) — should fall.

## Facilitation notes

Unlimited modelling space (a roll of paper, not a whiteboard), no premature structure, and active
management of the loudest voices. As a high-stakes group modelling exercise it leans on the same
[facilitation discipline](../../leadership/decision-facilitation.md) as any technical decision:
maximise signal, make disagreement explicit, let the group own the model.

## Relationship to other notes

- [DDD Strategic Design](ddd-strategic-design.md) — Event Storming is the *discovery* activity;
  strategic design is the *theory* of the boundaries it reveals.
- [Bounded Context Canvas](bounded-context-canvas.md) — the natural next step: take one context an
  Event Storm surfaced and design it in detail.
- [Team Topologies](team-topologies.md) — the fracture planes a storm exposes are candidates for
  team boundaries, via the inverse Conway manoeuvre.
