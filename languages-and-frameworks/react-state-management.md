---
type: note
title: State Propagation Is Not State Management
description: "Alex Russell's argument that React's state libraries propagate change notifications rather than manage state, because they carry no model of time — and what conflict resolution would actually require"
tags: [react, architecture, reading]
topic: languages-and-frameworks
status: notes
level: intermediate
related:
  - languages-and-frameworks/react-forms.md
  - case-studies/linear-performance-architecture.md
  - concepts/resilient-software-design.md
  - languages-and-frameworks/react-storybook.md
source: "https://infrequently.org/2026/07/state-management/"
updated: 2026-07-26
---

# State Propagation Is Not State Management

Alex Russell argues that the tools the React ecosystem calls "state management" — Redux,
Zustand, Jotai, and React's own primitives — do not manage state. They **propagate change
notifications**. What they implement is closer to an event bus or pub/sub: something changed,
here is the new value, re-render. That is a real and useful job, but it is not the job the
name claims.

This is an argument rather than a study — built through conceptual analysis and Socratic
dialogue, with no benchmarks or data. It is also a deliberately strong statement of a
definitional position, and worth reading as such.

## The distinction

| | What it does | What it needs |
|---|---|---|
| **State propagation** | Notifies subscribers that a value changed, and re-renders | A subscription mechanism |
| **State management** | Applies changes correctly *over time* and resolves conflicts between them | A model of ordering — Russell's example is **vector clocks** |

The dividing line is time. A propagation library receiving two updates has no basis for
deciding which one should win, because it holds no representation of when each happened
relative to the other — Russell's **temporal void**. It applies whichever arrived last. That
is correct only when "last to arrive" happens to mean "most recent", which stops being true
as soon as updates come from more than one source at different rates.

The React-specific version of the confusion is conflating **component-local state** — which
genuinely is just a value plus a re-render — with **application-wide state**, where multiple
writers and ordering are real problems. The same tools and the same vocabulary get used for
both, so the second problem inherits a solution shaped for the first.

## What would actually manage state

Russell points to tools built around conflict resolution rather than notification. Listed as
his recommendations, not endorsements:

| Tool | Ground |
|---|---|
| **Y.js** | CRDT-based, best known for collaborative text |
| **Zero** | Live collaboration and sync |
| **Fluid Framework** | Microsoft's open-source sync system |
| *Honourable mentions* | PouchDB, RxDB, Replicache |

What these share is that synchronisation and conflict resolution are the *product*, not a
layer bolted above a notification system. None of them is React-specific, which is a hint
about where the problem actually lives.

## When this matters, and when it doesn't

Worth holding the argument at the right scope. Most applications have one client per user,
one writer, and no concurrent-edit problem — for those, a propagation library is not merely
adequate, it is the correct amount of machinery, and reaching for a CRDT would be
over-engineering. Russell's claim is definitional (these tools are misnamed and the missing
capability is real) rather than a recommendation that every app adopt a sync engine.

The argument bites when an application has **multiple concurrent writers, offline editing, or
several update sources at different rates** — at which point the conflict-resolution problem
is already present whether or not the chosen library acknowledges it, and the usual symptom
is state that intermittently goes backwards.

## Relationship to other notes

- [Forms as a State Problem](react-forms.md) — the local end of the same spectrum: a form is
  state plus a lifecycle, with a single writer and no ordering problem. That note's advice to
  match the tool to the complexity is this argument at component scale.
- [Linear's Performance Architecture](../case-studies/linear-performance-architecture.md) —
  what a genuine sync engine looks like in production. That note documents *what* Linear
  built (IndexedDB as source of truth, server as sync target, optimistic updates); this one
  explains *why* that is a different category of thing rather than an aggressive cache.
- [Resilient Software Design](../concepts/resilient-software-design.md) — the eventual-consistency
  and conflict-resolution problems here are the distributed-systems ones arriving on the client.
