---
type: note
title: Forms as a State Problem
description: "the mental model for React forms (the four jobs; controlled vs uncontrolled; touched vs dirty; the submission lifecycle) and the native-first tool-selection ladder from React 19 server actions to client form libraries"
tags: [react, reading]
topic: languages-and-frameworks
status: notes
level: intermediate
related:
  - engineering/practices/api-contract-functional-testing.md
source: "https://upskills.dev/tutorials/react-forms-done-right"
updated: 2026-07-11
---

# Forms as a State Problem

Vu Nguyen's tutorial argues the durable idea behind React forms is to treat a form
as a **state problem first, and a UI problem second** — then choose the tool to match
the complexity, rather than reaching for a library by reflex. The tutorial itself walks
through concrete archetypes (a React 19 waitlist signup, a multi-step wizard, an
editable table); the transferable part captured here is the mental model and the
tool-selection ladder.

## The mental model

- **A form does four jobs:** *capture* input, *verify* it, *recover* from errors, and
  *commit* the result. Most form complexity is one of these four done poorly.
- **Controlled vs uncontrolled.** Controlled inputs keep value in React state (every
  keystroke re-renders); uncontrolled inputs let the DOM hold the value and read it on
  submit. The choice is a re-render/performance trade-off, not a style preference.
- **Touched vs dirty.** *Touched* = the user has interacted with a field; *dirty* = its
  value differs from the initial. They drive *when* to show validation — showing errors
  on untouched fields is the classic annoyance.
- **The submission lifecycle.** Idle → validating → submitting → success/error is a
  state machine; modelling it explicitly is what makes disabled buttons, spinners, and
  error recovery behave.

## Tool selection: fundamentals first

The tutorial's recommended progression — reach for the next tier only when complexity
demands it:

| Complexity | Approach |
|---|---|
| Simple, server-committed (e.g. a signup) | Native React 19: `useActionState` + a server action + Zod validation, minimal client JS |
| Rich client interaction, multi-step, async checks | A client form library (the tutorial uses TanStack Form) with Zod schema composition |
| Async validation (e.g. "is this email taken?") | Debounce input and cancel in-flight requests with `AbortController` to avoid race conditions |
| Repeating rows / field arrays | Isolate re-renders per row; validate across rows with Zod `superRefine` |

The through-line: **validation lives in a schema (Zod), not scattered through handlers**,
and the framework choice follows the state complexity rather than leading it.

## Relationship to other notes

- [API Spec, Contract, and Functional Testing](../engineering/practices/api-contract-functional-testing.md)
  — the *verify* job is schema validation at the client boundary; it is the UI-side
  analogue of validating a request against an API contract or spec. A Zod form schema
  plays the role on the client that an OpenAPI/contract check plays at the service edge.
