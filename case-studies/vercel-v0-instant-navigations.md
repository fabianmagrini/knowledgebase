---
type: case-study
title: Vercel's Agent Loop for Instant Navigations
description: "Turning 'feels snappy' into a deterministic test so an agent could loop on it — and the argument that frameworks matter more in the agent era because they can ship verifiers primitives cannot."
tags: [ai-engineering, testing, performance, architecture, reading]
topic: case-studies
status: notes
level: intermediate
related:
  - engineering/architecture/primitives-over-frameworks.md
  - engineering/architecture/design-systems-ai-control-plane.md
  - engineering/ai-native/agent-backpressure-loops.md
  - engineering/ai-native/light-and-dark-factories.md
  - engineering/practices/spa-soak-testing.md
  - engineering/ai-native/agentic-autonomy-levels.md
  - engineering/ai-native/skill-engineering-disciplines.md
  - languages-and-frameworks/react-storybook.md
source: "https://nextjs.org/blog/making-v0-navigations-instant"
updated: 2026-08-16
---

# Vercel's Agent Loop for Instant Navigations

Jude Gao (Vercel, August 2026) describes using a coding agent in a loop to make navigations
instant in v0, Vercel's own product.

> **Provenance.** Vercel writing about Vercel's framework, Vercel's product and Vercel's
> distributed Skills. The results graph is shown but no before/after figures appear in the
> text; "16 new tests" is the only hard number. The Next.js mechanics will date. The idea
> underneath will not.

## The problem the framework solved first

Dynamic, personalised apps had no good route to instant navigation: static prerendering is
impractical when pages contain personal data, and marking every link fully prefetched is
expensive and strains servers. Next.js 16.3 lets dynamic content be **prerendered while users
browse**, cached in the browser — components either define a Suspense loading state or mark
part of the UI `'use cache'`, and that shell can be loaded before navigation without fully
rendering the target page.

That is context. The interesting part is what it made testable.

## Making a fuzzy quality deterministic

The `instant()` Playwright helper pauses a navigation and asserts which parts of the UI are
visible **without any network request**:

```ts
await instant(page, async () => {
  await page.getByRole('link', { name: 'Chats' }).click();
  await expect(page.getByTestId('app-title')).toBeVisible();
});
```

If the expected content was blocked by the network, the test fails.

**This converts a judgement call into a green-or-red oracle.** Everyone can tell a snappy app
from a janky one; almost nobody could previously assert it deterministically. That matters far
beyond Next.js, because it is precisely the kind of signal an agent can close a loop on:

- [Backpressure Loops for Coding Agents](../engineering/ai-native/agent-backpressure-loops.md)
  — machine-readable feedback the agent can act on without a human in the path
- [Light and Dark Software Factories](../engineering/ai-native/light-and-dark-factories.md) —
  a loop earns unattended operation when verification rests on **green-or-red oracles** rather
  than judgement. This manufactures one where none existed.
- [Agentic Autonomy Levels](../engineering/ai-native/agentic-autonomy-levels.md) — the
  execution contract's **measurable stopping condition**, for an attribute that previously had
  no measure

The same shape as [Soak Testing a Single-Page App](../engineering/practices/spa-soak-testing.md):
both take a class of frontend quality that unit tests structurally cannot see and turn it into
a Playwright assertion that runs in CI.

## What made the loop run unattended

Three stated requirements, and they generalise:

| Requirement | In this case |
|---|---|
| **A verifiable goal** | A failing test that terminates the loop once it passes |
| **Guardrails** | A Skill carrying proven, framework-idiomatic patterns to move the code toward the goal |
| **Real feedback** | Production metrics confirming the loop had the intended effect |

The cycle: define the goal → write it as a test and confirm it fails → apply a fix from the
Skill → rebuild and re-run → repeat until instant → **ship the test to CI**.

That last step is the one most easily skipped. The tests were kept, and the stated reason is
worth recording: they guard against regression "especially important as agents make changes
that could undo these optimizations." The loop's artefact is not just the fix — it is the
constraint that stops a later agent removing it.

Most fixes were unremarkable: moving dynamic data access below a Suspense boundary so the rest
of the page could be included in the prerendered shell. Some required larger refactors, such as
lifting a blocking dependency out of the root layout — which is the case the piece argues loops
handle well, because the agent can keep iterating against an objective signal.

## The argument against primitives

The closing claim is a direct challenge to
[Primitives Over Opinionated Frameworks](../engineering/architecture/primitives-over-frameworks.md),
and it is a mechanism rather than a preference:

> An agent can write any code it wants to, but a framework's job is to constrain it so it
> produces better UIs than it would on its own.

**Frameworks can ship verifiers; primitives cannot.** `instant()` works *because* it is deeply
integrated — it knows what a navigation is, what the shell contains, and what was fetched. A
generic test helper has no access to any of that, and a hand-owned layer over unopinionated
primitives would have to build the verifier itself before it could run this loop at all.

That is a real cost the primitives argument does not price. Its case is that libraries bundle
constraint choices made for someone else's problem; the counter here is that some of those
choices come with **machinery for checking you have satisfied them**, and that machinery gets
more valuable as more code is agent-written.

The two positions can be held together as a question rather than a rule: *does this dependency
come with a verifier I would otherwise have to build?* If it does, the opinion layer is buying
something the primitives case does not account for. If it does not, the original argument
stands.

This is also
[Design Systems as the AI Control Plane](../engineering/architecture/design-systems-ai-control-plane.md)
generalised — constraint as the thing that makes agent output good, moved from component
libraries up to frameworks.

## Skills as the distribution mechanism

The patterns the agent applied arrived as an installable Skill
(`next-cache-components-optimizer`), with a second one for migrating apps not yet on Cache
Components. That is framework-idiomatic knowledge shipped as an agent artefact rather than as
documentation — the practice
[Skill Engineering Disciplines](../engineering/ai-native/skill-engineering-disciplines.md)
describes, with the framework author as publisher.

Worth noting the shape: the framework ships the *verifier* and the *patterns* together. The
test says whether you are done; the Skill says how to get there.

## Relationship to other notes

- [Primitives Over Opinionated Frameworks](../engineering/architecture/primitives-over-frameworks.md)
  — the argument this contests, with the verifier question as the reconciliation.
- [Soak Testing a Single-Page App](../engineering/practices/spa-soak-testing.md) — the sibling
  technique: another invisible frontend quality made assertable in CI.
- [Design Systems as the AI Control Plane](../engineering/architecture/design-systems-ai-control-plane.md)
  — the same constraint-makes-agents-better thesis one layer down.
