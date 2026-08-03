---
type: note
title: Storybook for React Component Development
description: "Storybook as a development practice rather than a test harness: modelling component states explicitly instead of reproducing them in a running app, what deserves a story, and how stories become documentation and tests."
tags: [react, testing, reading]
topic: languages-and-frameworks
status: notes
level: intermediate
related:
  - languages-and-frameworks/react-forms.md
  - languages-and-frameworks/react-state-management.md
  - engineering/practices/visual-regression-testing.md
  - engineering/architecture/design-systems-ai-control-plane.md
source: "https://flaviocopes.com/storybook-tutorial/"
updated: 2026-08-03
---

# Storybook for React Component Development

Storybook is a workbench for building UI components in isolation. It is
framework-agnostic; this note is written from a React treatment, and the setup mechanics of
the source tutorial are deliberately left out — those belong in the official docs and date
quickly. What follows is the practice.

## The core move: model the state, don't reproduce it

The principle worth carrying:

> Instead of waiting for the API to fail, we select the Error story.

In a running application, seeing a component's error state means *engineering* that state —
throttling the network, breaking an endpoint, forcing a bad response. Empty states need an
empty account; loading states need a slow connection; a long-content overflow needs
pathological data.

Storybook inverts this. Each state is **declared as a story** and opened directly. The cost
of visiting a state drops from "reproduce the conditions" to "click the name", which changes
what actually gets built and reviewed: states that are expensive to reach are states that
quietly go unhandled.

This is the same instinct as
[Forms as a State Problem](react-forms.md) — enumerate the states (idle, validating,
submitting, success, error) and model them explicitly rather than letting them emerge from
handlers.

## What a story is

A story is a named, rendered instance of a component in one state. In practice a story file
carries:

- **Meta** — the component under test plus shared configuration
- **Args** — the props for this instance, which Storybook also exposes as interactive controls
- **One export per state** — `Default`, `Loading`, `Error`, `LongContent`, and so on

Because args are declarative, the same definitions drive the rendered example, the controls
panel, and the generated documentation.

## The capability surface

| Capability | What it is for |
|---|---|
| **Controls** | Change args live in the UI — explore the prop space without editing code |
| **Decorators** | Wrap stories in required context: theme providers, routers, layout, mock stores |
| **Play functions** | Script interactions (type, click, tab) so a story exercises behaviour, not just initial render |
| **A11y addon** | Automated accessibility checks per story — labels, contrast, ARIA, keyboard reachability |
| **Viewports** | Render the same story at mobile and desktop sizes |
| **Network mocking** | Give data-fetching components deterministic responses, so async states are stable |
| **Test runner (Vitest)** | Execute stories as tests in CI, turning the story set into a regression suite |

**Decorators are the part most often underused.** A component needing a theme, a router and a
query client is exactly the component nobody writes stories for, because setting it up feels
like work. A decorator does that once for the file.

## Which states deserve a story

The tutorial's implicit selection criteria, made explicit:

- Every state with **distinct visual output** — loading, empty, error, populated
- **Boundary content** — the longest realistic string, the largest count, the smallest viewport
- States that are **hard to reach in the running app**, which is precisely where bugs live
- Not every prop permutation. Stories are a curated set of meaningful cases, not a
  combinatorial sweep

The framing that keeps the set honest: **stories are the component's documentation.** A story
exists because it shows a reader something true about how the component behaves — not to
raise a coverage number.

## Stories as the substrate for testing

Once states are declared, other tooling consumes them. Play functions and the a11y addon make
each story an executable check, and the Vitest integration runs the set in CI.

The visual-regression layer builds on the same foundation — see
[Visual Regression Testing (Chromatic + Storybook)](../engineering/practices/visual-regression-testing.md),
where each story becomes an independent screenshot diff. The dependency runs one way and is
worth stating plainly: **visual regression coverage is only ever as good as the stories
written.** A component whose error state was never modelled has no error-state baseline, and
nothing will catch it breaking. Deciding what deserves a story is therefore upstream of the
entire visual-testing pipeline, not a detail of it.

## Relationship to other notes

- [Forms as a State Problem](react-forms.md) — the same enumerate-the-states discipline
  applied to form lifecycles; a form's states are natural story candidates.
- [State Propagation Is Not State Management](react-state-management.md) — components with
  external state need decorators supplying that context, which is a decent smell test for how
  much a component depends on ambient state.
- [Visual Regression Testing (Chromatic + Storybook)](../engineering/practices/visual-regression-testing.md) —
  the downstream consumer: that note covers the pixel-diff pipeline, this one covers writing
  the stories it runs on.
- [Design Systems as the AI Control Plane](../engineering/architecture/design-systems-ai-control-plane.md) —
  a component library's stories are the machine-readable record of what its components can do.
