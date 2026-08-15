---
type: note
title: Soak Testing a Single-Page App
description: "Catching client-side memory leaks by repeating one workflow hundreds of times in a single browser context and asserting on DOM node and listener counts — with concrete Playwright/CDP technique and thresholds."
tags: [testing, performance, ci-cd, reading]
topic: engineering/practices
status: notes
level: intermediate
related:
  - engineering/practices/performance-testing-strategy.md
  - engineering/practices/visual-regression-testing.md
  - engineering/practices/test-coverage-policy.md
  - languages-and-frameworks/react-storybook.md
  - case-studies/linear-performance-architecture.md
  - engineering/architecture/thin-shell-startup-performance.md
  - case-studies/vercel-v0-instant-navigations.md
source: "https://denodell.com/blog/your-spa-is-leaking-memory-soak-test-it"
updated: 2026-08-08
---

# Soak Testing a Single-Page App

Den Odell (July 2026) argues that single-page applications leak memory undetected because the
page never reloads, and that frontend teams should adopt **soak testing** — long standard on
the backend — to catch it before production.

Practical how-to with evidence behind it, including working code and stated trade-offs.

## Why ordinary tests never see it

An end-to-end test starts a fresh browser context, performs a flow, and exits. Every leak is
cleaned up by the teardown it never had to survive. A real user opens the app on Monday and
still has the tab open on Thursday.

A client-side soak test inverts that: **repeat one workflow hundreds of times inside a single
browser context**, and compare resource counts before and after. This is a different mechanism
from the backend sense of soak recorded in
[Performance Testing Strategy](performance-testing-strategy.md) — that is hours of *load*
against a service; this is hours of *use* against one browser session.

## How common the problem is

A 2026 static analysis across **500 repositories** found:

| | |
|---|---|
| React/Vue/Angular repos leaving listeners, timers or subscriptions unremoved | **86%** |
| Share of detected issues that are **timer cleanup** | **~44%** |

Close to universal, and concentrated in one cause. Timers are the thing most likely to be
started in an effect and forgotten on unmount.

## The technique

Drive the flow with Playwright and read metrics from the Chrome DevTools Protocol:

- **A round trip, repeated** — a flow that returns to its starting state (open a drawer, close
  it) so anything retained is genuinely a leak rather than accumulated state
- **Measure via CDP** — heap size, DOM node count, event-listener count, before and after
- **Compress time** with `page.clock.install()` and `page.clock.runFor()`, so hours of polling
  and interval drift run in seconds
- **Mock the network** with `page.route()` so runs are deterministic
- **Heap snapshots filtered for detached nodes** when you need to find the specific culprit

### Thresholds

The part that turns this from a technique into a test you can commit:

- **Listener counts must not increase.** No jitter allowance — a listener is either removed or
  it is not.
- **DOM nodes may climb by roughly 100 across 200 loops.** That headroom absorbs garbage
  collection timing rather than tolerating a leak.

## Where it fits in the pipeline

**Nightly, not per-PR.** The run is slow by construction, and leak regressions are not the kind
of failure that needs to block a merge — they need to be found before a release. That places it
alongside the other slow, high-value checks rather than in the fast feedback path, the same
split [Visual Regression Testing](visual-regression-testing.md) makes for screenshot diffing.

### Limits

- **Chromium only** — CDP is unavailable in Firefox and Safari, so this measures one engine
- **Streamed responses resist mocking**, which limits coverage of flows built on them
- **Compressed clock and real-time polling need coordinating** — a mocked clock racing real
  network timing produces false results in both directions

## The architectures where this matters most

*The note's own reading.* The longer a session lives, the more a leak compounds — so this test
is most valuable precisely where these notes recommend long-lived clients.

[Linear's Performance Architecture](../../case-studies/linear-performance-architecture.md)
documents a local-first design where the browser holds the source of truth and the page
effectively never reloads. That is the ideal case for perceived speed and the worst case for
leaks: there is no navigation event to clear anything up. Likewise the persistent shell in
[Thin-Shell Startup Performance](../architecture/thin-shell-startup-performance.md) — a runtime
that stays resident is a runtime that accumulates.

The general form: **any architecture that avoids reloads inherits the obligation to prove it
does not accumulate.**

## Relationship to other notes

- [Performance Testing Strategy](performance-testing-strategy.md) — lists soak among the load
  test types; this is the client-side counterpart, with a different mechanism and different
  assertions.
- [Visual Regression Testing](visual-regression-testing.md) — the other Playwright-driven,
  nightly-cadence frontend check; both trade speed for a class of regression that unit tests
  structurally cannot see.
- [Storybook for React Component Development](../../languages-and-frameworks/react-storybook.md)
  — component-level testing catches behaviour; neither stories nor unit tests survive long
  enough to catch retention.

Other tooling named: Meta's **MemLab** as an alternative, a `playwright-soak-test` package, and
Gmail's decade-old internal practice as precedent.
