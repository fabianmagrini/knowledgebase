---
title: Visual Regression Testing (Chromatic + Storybook)
tags: [testing, ci-cd, code-review]
topic: engineering/practices
status: notes
level: intermediate
related:
  - engineering/practices/performance-testing-strategy.md
  - engineering/ai-native/ci-cd-ai-engineering.md
  - engineering/architecture/design-systems-ai-control-plane.md
  - engineering/architecture/micro-frontend-principles.md
  - engineering/ai-native/quality-first-ai-coding.md
  - leadership/learning-culture-ai-agents.md
source: "https://www.chromatic.com"
updated: 2026-06-29
---

# Visual Regression Testing (Chromatic + Storybook)

Visual regression testing asks a different question from a normal unit test.
Instead of asserting behaviour —

```ts
expect(button).toHaveText("Save")
```

— it asks: *"Does this component still **look** exactly as approved?"* It renders
each component, captures a screenshot, and diffs it pixel-by-pixel (with
intelligent diffing) against a previously approved baseline.

[Chromatic](https://www.chromatic.com) is the common managed implementation of
this for frontend teams: a cloud platform for visual testing, UI review, and
component documentation, built to integrate with Storybook. It catches
unintended visual change before it ships — the visual analogue to the automated
gates in [CI/CD as the Control Plane](../ai-native/ci-cd-ai-engineering.md).

## How it works

```text
Developer → open PR
  → Storybook builds all component stories
  → Chromatic uploads the Storybook
  → screenshots generated for each story
  → compared against the approved baseline
  → visual differences surfaced
  → reviewer approves or rejects
  → merge
```

A change to CSS, Tailwind classes, design tokens, spacing, typography, responsive
layout, or theme is highlighted automatically — e.g. "padding changed by 4px" —
with no manual screenshot comparison.

## Core capabilities

- **Visual regression testing** — the primary feature; pixel diffs against the
  baseline, with intentional changes approved into a new baseline.
- **Storybook hosting** — every build (and every PR) gets its own hosted URL, so
  designers, QA, and product can review without running the project locally.
- **Pull-request reviews** — integrates with GitHub, GitLab, and Bitbucket;
  posts a summary ("42 unchanged, 3 changed") and lets reviewers approve, reject,
  inspect, or ignore.
- **Component documentation** — the hosted Storybook doubles as living docs of
  every component state (Primary, Secondary, Danger, Disabled, Loading…).
- **Interaction testing** — runs Storybook `play` functions so interactive
  behaviour, not just initial render, is verified.
- **Accessibility** — automated a11y checks against stories (missing labels,
  colour contrast, ARIA, keyboard navigation).
- **Design review** — designers approve UI changes straight from the PR,
  reducing manual comparison in design tools.

## Why Storybook matters

Chromatic tests **isolated components**, not whole pages. Each component can have
many stories — Primary, Secondary, Loading, Disabled, Icon, Small, Large, Dark
Theme, High Contrast — and **each story is an independent visual test**. This
component-driven granularity is what makes the diffs precise and the failures
actionable.

## CI/CD integration

```text
GitHub Action → npm test → Storybook build → Chromatic upload
  → visual regression tests → status check → merge
```

Many teams make the Chromatic status check mandatory before merge, so a visual
regression blocks the PR exactly like a failing unit test.

## Where it fits in the testing strategy

| Tool | Purpose |
|---|---|
| Vitest | Unit tests |
| React Testing Library | Component behaviour |
| Chromatic | Visual regression testing |
| Playwright | End-to-end browser testing |

These complement rather than replace one another — Chromatic owns the "does it
still look right" layer that behavioural and E2E tests don't cover. See
[Performance Testing Strategy](performance-testing-strategy.md) for the
analogous reasoning on the performance layer.

## Strengths

- Very easy Storybook integration and an excellent visual-diff UI
- Strong PR workflow and design-system support
- Cloud-hosted Storybook with minimal infrastructure to maintain
- A natural fit for component-driven development

## Limitations

- Works best when the app already uses Storybook extensively
- Component-level, not complete user journeys (pair with Playwright)
- Cloud-based — evaluate against strict data-residency or air-gapped needs
- Large Storybooks (thousands of stories) increase build time and cost

## Fit for AI-native frontends

For React/TypeScript, Module Federation, and design-system work, visual
regression is especially valuable as an automated quality gate:

- **Shared design-system validation** — every change to a common component in the
  [design system](../architecture/design-systems-ai-control-plane.md) is visually
  verified before release.
- **Microfrontend independence** — each team
  ([microfrontend principles](../architecture/micro-frontend-principles.md))
  visually tests its own components while keeping a consistent look and feel.
- **AI-generated code safety** — a fast, automated check that AI-assisted UI
  changes haven't silently altered layout or styling. This is the visual arm of
  the "red-team AI code" discipline in
  [A Learning Culture for AI-Augmented Teams](../../leadership/learning-culture-ai-agents.md)
  and complements [Quality-First AI Coding](../ai-native/quality-first-ai-coding.md).
- **Design collaboration** — designers review UI changes from the PR without a
  local setup.

As code generation accelerates and the volume of UI change grows, an automated
visual gate sits alongside unit tests, linting, and E2E tests as a cheap,
high-signal way to keep that change intentional.
