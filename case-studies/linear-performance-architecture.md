---
title: Linear's Performance Architecture
tags: [architecture, performance, system-design, reading]
topic: case-studies
status: notes
level: intermediate
related:
  - engineering/architecture/micro-frontend-principles.md
  - engineering/architecture/composable-architecture.md
  - engineering/architecture/thin-shell-startup-performance.md
  - engineering/practices/performance-testing-strategy.md
source: "https://performance.dev/how-is-linear-so-fast-a-technical-breakdown"
updated: 2026-06-22
---

# Linear's Performance Architecture

A breakdown of how the issue tracker Linear achieves its perceived speed —
interactions that resolve in milliseconds where a traditional app would show a
spinner for ~300ms. The author's central claim is that this is not the result of
a single optimisation but of an architectural decision made before any feature
code was written, then defended consistently for years: **hide network requests
from the user**.

## The architectural inversion

The foundational move is to invert the usual client/server relationship.

| | Traditional app | Linear |
|---|---|---|
| Source of truth | Server database | Browser (IndexedDB) |
| Server role | Source of truth | Sync target |
| Mutation flow | UI → network → server → UI | UI → local DB → UI, then async push to server |

The UI reads from a database that lives in the browser. A mutation applies
locally first and the change is reflected immediately; the write is pushed to the
server asynchronously. The author summarises the developer-facing model as simply
`issue.title = "..."; issue.save();` — no spinner, no await on the network in the
interaction path.

This is the **local-first** pattern: the client owns a full working copy of the
data, and synchronisation with the server is a background concern rather than a
precondition for the UI to respond.

## Sync engine and optimistic updates

- **Sync engine first.** Per the author, Linear's co-founder describes the sync
  engine as "literally the first lines of code" — built before features, not
  retrofitted. Data hydrates from IndexedDB into in-memory observables on load.
- **Optimistic updates.** Changes appear in the UI before the server confirms
  them. The server reply is described as "a small JSON envelope describing what
  moved" — a delta, not a full refetch.
- **Local-only search.** The command palette (`⌘K`) and search query the local
  in-memory pool, never the network, so results are instant.

## Granular reactivity

State is held in MobX observables that track individual properties rather than
whole collections. Applying a server delta updates only the specific cells that
changed — the article's phrase is **"one delta, one cell"**. A 50-issue update
triggers 50 cell re-renders, not a re-render of the whole list, which avoids the
cascading re-render cost that degrades large views.

**Data-level code splitting** extends this: heavy record types (issues, comments)
are lazily hydrated from IndexedDB only when needed rather than all at once.

## Build and initial-load discipline

The speed of the *first* load is treated as a separate problem from interaction
latency, and addressed by shipping less and parsing less:

- **Modern-browser-only targets** — no ES5 transpilation, no polyfills.
- **Aggressive code splitting** — hundreds of route-level chunks; each npm
  package gets its own cached chunk so one dependency change invalidates only
  that chunk. Preload directives (with matching `crossorigin`) parallelise chunk
  fetching.
- **Inlined critical path** — critical CSS and a small boot script are inlined in
  `<head>`. The boot script reads `localStorage` to restore theme and layout
  width before any bundle parses, avoiding a flash.
- **Service-worker precache** — the remaining assets (the article cites ~1,200
  hashed resources) are precached during the login screen.
- **Render-first, authenticate-second** — the app assumes the happy path based on
  the presence of local state and renders immediately, validating auth behind it.

## Animation discipline

Motion is used to mask latency, not add it:

- Animate only compositor-friendly properties (`transform`, `opacity`); never
  layout-triggering ones (`width`, `height`, `margin`, `padding`).
- Short durations (≈0.1s–0.25s) with asymmetric timing — instant appear, gentle
  fade on dismiss.
- Single-letter keyboard shortcuts and contextual shortcuts keep frequent actions
  off the pointer path entirely.

## Stack (as described)

- **Frontend:** React, TypeScript, MobX, Emotion + StyleX, ProseMirror + Yjs
  (collaborative rich text), Radix UI, Comlink (worker RPC), `idb` (IndexedDB),
  Rolldown via Vite.
- **Backend:** Node.js + TypeScript, PostgreSQL (partitioned 300 ways), Redis,
  Cloudflare Workers at the edge.

## Reported outcomes

These figures are reported by the author and are not independently verified:

- ~50% less code shipped; ~30% smaller after compression.
- 59% reduction in time-to-first-paint (Safari, active-issues view).
- 70–80% drop in memory usage.
- 10–30% faster cold page loads.

## The generalisable pattern: local-first sync

Stripped of the Linear specifics, the reusable idea is:

1. Give the client a complete local copy of its working data.
2. Make the local store the source of truth the UI reads from.
3. Apply mutations locally and optimistically; sync to the server in the
   background as deltas.
4. Use fine-grained reactivity so a sync delta touches only the affected view.
5. Treat first-load, animation, and shortcuts as separate latency problems with
   their own budgets.

The author's framing is that there is "no secret silver bullet" — speed is
"hundreds of decisions made correctly" held together by an architectural
commitment that the rest of the system is not allowed to violate.

## Relationship to other notes

- [Performance Testing Strategy](../engineering/practices/performance-testing-strategy.md)
  covers *measuring* server-side performance under load; this note covers
  *architecting* a client for perceived speed — the two are complementary.
- [Microfrontend Architecture Principles](../engineering/architecture/micro-frontend-principles.md)
  and [Composable Architecture](../engineering/architecture/composable-architecture.md)
  describe how to compose a frontend across teams and capabilities; this note is
  about a single application's client-data architecture and the latency budget,
  a different concern at a finer altitude.
