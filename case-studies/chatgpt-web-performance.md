---
title: ChatGPT's Web Performance Architecture
tags: [architecture, performance, system-design, reading]
topic: case-studies
status: notes
level: intermediate
related:
  - case-studies/linear-performance-architecture.md
  - engineering/practices/performance-testing-strategy.md
  - engineering/architecture/thin-shell-startup-performance.md
source: "https://performance.dev/chatgpt"
updated: 2026-07-11
---

# ChatGPT's Web Performance Architecture

Dennis Brotzky reverse-engineers the `chatgpt.com` web app by inspecting its live
HTML, JavaScript, CSS, and network traffic — he is explicit that he has not seen
OpenAI's source. His central claim is that a single constraint drives every decision:
**let anyone in the world use AI with zero friction**. Serving roughly a billion
*anonymous* users makes the performance work a consequence of that goal, achieved with
mainstream technologies applied with unusual discipline. *(All figures below are the
author's own measurements/observations, not OpenAI disclosures.)*

## The constraint dictates the architecture

Because most users are logged-out and global, client-side rendering is off the table —
too slow to first paint, too dependent on a round trip. The app commits to
**streaming server-side rendering** and a **render-first** approach: paint the shell
before verifying auth, served by a parallel `/backend-anon/` API surface.

The author frames this as the deliberate opposite of Anthropic's enterprise choice
(authentication walls, simpler operations): OpenAI accepts GPU cost and bot-defence
complexity as the price of frictionless access.

## Startup discipline

> "The network is the enemy" — every new origin adds DNS and TLS cost.

| Technique | Detail |
|---|---|
| **Streaming SSR** | React 19 + React Router 7 flush the shell immediately; Suspense boundaries fill via parallel streams |
| **Tiny logged-out document** | ~84 KB compressed, ~30 KB real markup, **548 DOM nodes** after hydration; ~50–65 ms TTFB (to a Vancouver laptop) |
| **No webfonts** | System font stack; KaTeX math fonts load on demand |
| **Per-route CSS chunking** | `root.css`, `conversation.css`, `code-block.css`, `math.css` split by route |
| **Deferred imports** | A flag (`deferStartupImportsUntilComposerTTFI`) holds non-critical JS until the input is interactive |
| **First-party assets** | All chunks/fonts from `chatgpt.com/cdn/assets`, 30-day cache, no CORS overhead |
| **Minimal preloading** | 14 `modulepreload`s for critical files only (contrasted with Linear precaching ~1,200 assets) |

## Flags, rendering, and defence

- **Server-evaluated flags.** Statsig with **556 gates, 144 configs, 192 experiment
  layers**, inlined as a **377 KB JSON bootstrap** so gate decisions need no network
  call. Flag names are hashed to deter leak-mining.
- **Incremental streaming render.** The response is an SSE `text/event-stream`; markdown
  is re-parsed and re-rendered per token, with CodeMirror 6 for code blocks. Maths
  renders **twice** — KaTeX for sight plus hidden MathML for screen readers and
  copy-as-maths.
- **No virtualization.** The full message DOM is kept in memory (so find-in-page works);
  conversations are assumed short enough to afford it.
- **"Prepaid" bot defence.** Cloudflare proof-of-work and an anti-abuse iframe run during
  page idle, *before* the user submits, so the check is already paid by send time.
- **Instrumentation.** Every load phase is measured — TTFB and *composer TTFI* (time to
  first interactive for the message input) — on the principle that you can't improve what
  you don't measure.

## The generalisable pattern

The note's takeaway is that **the constraint, not the technology, is the architecture**.
ChatGPT and Linear both achieve measured speed with mainstream tools and obsessive
discipline, but from opposite premises — because their users are opposite.

## Relationship to other notes

- [Linear's Performance Architecture](linear-performance-architecture.md) — the direct
  contrast, and the same performance.dev author/method. Linear inverts client/server to
  *hide the network* for logged-in power users; ChatGPT streams from the server and
  renders-first for anonymous global users. Same discipline, opposite bet, opposite
  constraint.
- [Performance Testing Strategy](../engineering/practices/performance-testing-strategy.md)
  — the measurement discipline (TTFB, composer TTFI) that makes these gains observable
  and defensible rather than anecdotal.
- [Thin-Shell Startup Performance](../engineering/architecture/thin-shell-startup-performance.md)
  — the same startup-waterfall levers (critical-path preloading, deferred non-critical
  imports, code/CSS splitting) analysed as a general pattern rather than one app.
