---
type: case-study
title: Rendering Huge Pull Requests (GitHub Copilot App)
description: "Virtualisation split into two geometry domains because comments have no knowable height: deterministic code rows versus lazily measured blocks, height fingerprinting bucketed by width, and an unattended autopilot reading the app's own jank instrumentation."
tags: [performance, architecture, testing, reading]
topic: case-studies
status: notes
level: intermediate
related:
  - case-studies/chatgpt-web-performance.md
  - case-studies/linear-performance-architecture.md
  - case-studies/vercel-v0-instant-navigations.md
  - engineering/practices/spa-soak-testing.md
  - case-studies/rootly-pr-size-risk-labels.md
  - concepts/latency-patterns.md
  - engineering/architecture/thin-shell-startup-performance.md
  - case-studies/linear-ci-rework.md
  - case-studies/anthropic-claude-ai-performance-sprint.md
  - case-studies/github-copilot-rust-migration.md
source: "https://github.blog/engineering/user-experience/rendering-huge-pull-requests-in-the-github-copilot-app/"
updated: 2026-10-10
---

# Rendering Huge Pull Requests (GitHub Copilot App)

Alberto Gimeno (GitHub, September 2026) on rebuilding the pull-request diff viewer in the Copilot
app to stay smooth on extreme documents. Their stress case was a real open-source PR with
**"2,200 files, over a million changed lines, and more than 400 inline review comments."**

These notes hold four frontend-performance case studies and nothing on virtualisation mechanics
— and one of them,
[ChatGPT's Web Performance Architecture](chatgpt-web-performance.md), records the opposite
decision: *"No virtualization. The full message DOM is kept in memory (so find-in-page works);
conversations are assumed short enough to afford it."* This is the other end of that trade, where
virtualisation is not optional and the interesting problem is what defeats it.

**Provenance.** GitHub writing about GitHub's own product. Mitigating: the figures are concrete
and checkable, and the extreme case is a named open-source pull request rather than a synthetic
benchmark.

## Why comments break virtualisation

Virtualisation needs to know how tall a row is before painting it, so it can compute scroll
geometry without rendering everything. Code rows cooperate. Comments do not — their height
depends on:

- Markdown that wraps differently at different widths
- Expandable `details` blocks
- Reply composers
- Images, and **"async assets that change height when they finish loading"**

Each of those is only resolvable *after* render, and the last one changes height after the render
has already happened. So a single virtualisation strategy over the whole document either
mis-measures the comments or gives up the pre-paint geometry that makes the code fast.

## Two-domain geometry

The architectural answer, and the transferable idea: **do not pick one strategy for the
document — split it by whether height is knowable.**

| | Code rows | Comment blocks |
|---|---|---|
| Height | Deterministic, computed upfront | Dynamic, measured lazily and cached |
| Renderer | **"An imperative, recycled code-row renderer (no React component per row)"**, typed-array maths | Identity-based anchoring |
| Measurement scope | — | Bounded to viewport **±2400px** |
| Contract | *All heights known before paint* | Measured, with an off-screen fallback |

The code half is made possible by **structure-first streaming** — backend-owned diff documents
that send structure before content — so geometry can be computed before any content arrives.
Their verdict on that half: *"on pure code this design is the right one."* The comment half is
where the engineering goes.

This is worth generalising. The usual framing of virtualisation is a binary — virtualise or
don't, as ChatGPT's note frames it. The better question is **which parts of this document have
computable geometry**, because those parts can be fast by construction while the awkward
remainder gets the expensive treatment and nothing else does.

## Height fingerprinting

The cache detail worth stealing. A measured height is recorded against a fingerprint of the
content hash **plus** the width it was last measured at, *"rounded into buckets, so an ordinary
window resize doesn't invalidate every measurement in the document."*

Bucketing the width is the clever half. Width is the thing that actually changes comment heights,
and it is also the thing users change constantly by dragging a window — so an exact-width key
would throw away the entire cache on the most common interaction. Buckets keep the cache valid
through routine resizing and invalidate only when the width moves far enough to plausibly reflow
the markdown.

## Measurement off the hot path

Per-block `ResizeObserver`s were replaced by an **idle-gated batched pass**, paired with scroll
anchoring to stop the viewport jumping when a measurement lands. The correction rules:

- **Suppress corrections during active scrolling** — a geometry fix mid-scroll is what users
  perceive as jank.
- **Collapse multiple resizes into one commit per frame.**
- **Treat on-screen measurements as ground truth**, with off-screen measurement as fallback.

The pattern underneath is the one
[Latency Patterns](../concepts/latency-patterns.md) calls out as the general case: the work still
happens, it just stops happening on the path the user is waiting on. Same move as Linear's
[non-blocking cache writes moved off the CI critical path](linear-ci-rework.md) — different
domain, identical reasoning.

## The measurement loop, which bridges clusters

Two automated lanes, and this is the part with the longest reach:

- A **headless probe lane** running declarative flows that read *"the app's own production
  instrumentation: React render counts, the performance timeline, and a requestAnimationFrame
  sampler."*
- An **autopilot** that *"drove the actual desktop app through the huge-pull-request flow,
  unattended, on a loop"* — toggling, resizing, deep file navigation — reading on-disk logs with
  no human in the path.

That is the same move as
[Vercel's Agent Loop for Instant Navigations](vercel-v0-instant-navigations.md): take a quality
everyone can perceive but nobody can assert, and convert it into a machine-readable signal so a
change → measure → improve loop can run without a human judging each result. Vercel did it for
navigation instantness with an `instant()` test helper; this does it for **jank**, via rAF
sampling and render counts.

Structurally the autopilot is also the client-side soak test from
[Soak Testing a Single-Page App](../engineering/practices/spa-soak-testing.md) — repeat one
workflow many times inside one long-lived context — pointed at render performance instead of
memory leaks. The two could share a harness.

**Stated precisely:** the article describes an automated loop with declarative flows. It does
**not** say an AI agent drives it, and this note does not imply one.

## The question the article does not ask

Recorded because it is the interesting tension. **Nothing in the piece considers whether
million-line pull requests should exist.** PR size is treated purely as a constraint to render
efficiently, never as a problem upstream — and this is the **Copilot app**, where the changes
being rendered are largely agent-authored.

That is a position, not a neutral choice. Set against
[Rootly Dropped Its Small-PR Rule](rootly-pr-size-risk-labels.md), which retired diff-size limits
on the reasoning that *"AI bugs are context bugs. The code works, but it's applied to the wrong
thing"* — Rootly concluded that size is the wrong axis and moved the gate to risk and rollout.
GitHub's answer is different in kind: make the diff *viewable* at any size.

Both can be sensible, and they are not substitutes. A viewer that handles a million lines solves
the rendering problem completely and the comprehension problem not at all — a reviewer who can
now scroll a million lines smoothly is no better placed to understand them. Tooling for huge
diffs and arguing against huge diffs are separate bets, and this piece only makes the first.

## Relationship to other notes

- [ChatGPT's Web Performance Architecture](chatgpt-web-performance.md) — the deliberate opposite:
  no virtualisation at all, justified by short conversations and find-in-page. Read as a pair,
  they frame the real question as *does this document have computable geometry* rather than
  *should we virtualise*.
- [Linear's Performance Architecture](linear-performance-architecture.md) — the third point on the
  client-performance triangle here, and the one that precaches aggressively.
- [Vercel's Agent Loop for Instant Navigations](vercel-v0-instant-navigations.md) — the same
  conversion of a perceptual quality into a loopable signal, for a different quality.
- [Soak Testing a Single-Page App](../engineering/practices/spa-soak-testing.md) — the autopilot
  is this technique aimed at render performance rather than leaks.
- [Rootly Dropped Its Small-PR Rule](rootly-pr-size-risk-labels.md) — the upstream position this
  piece declines to take.
- [Latency Patterns](../concepts/latency-patterns.md) — precomputation (heights before paint) and
  getting work off the critical path, both worked out concretely here.
- [Thin-Shell Startup Performance](../engineering/architecture/thin-shell-startup-performance.md)
  — the same critical-path discipline applied to application startup instead of scroll.
