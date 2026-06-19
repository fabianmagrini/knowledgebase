---
title: Generative UI
tags: [ai-engineering, architecture, system-design]
topic: engineering/architecture
status: draft
level: intermediate
related:
  - engineering/architecture/design-systems-ai-control-plane.md
  - engineering/architecture/composable-architecture.md
  - engineering/architecture/micro-frontend-canvas.md
  - engineering/practices/ai-native-engineering-stack.md
updated: 2026-06-19
---

# Generative UI

**Generative UI** is the practice of producing user interfaces with AI rather than
hand-authoring every screen. The term covers two genuinely different things, and
most confusion comes from conflating them:

- **Build-time (generative development)** — AI agents generate UI *code and
  components* during development. The artifact is source that humans review,
  commit, and ship like any other code.
- **Run-time (dynamic / adaptive UI)** — an LLM assembles or adapts the interface
  *live*, while the user is interacting. The artifact is a rendering decision made
  per request, not committed code.

They share a dependency — both need a constrained set of approved building blocks
to be safe — but they differ in *when* generation happens and *what* is generated.

## Build-time generative UI

Here agents emit UI code: components, screens, styles. This is the same loop as
any AI-assisted coding, and its governance is already covered in
[Design Systems as the AI Control Plane](design-systems-ai-control-plane.md):
the design system shrinks the solution space to approved primitives, codified as
typed component APIs, design tokens, lint rules, and codemods so the constraints
are machine-enforceable rather than prose. The output is reviewed by humans and
gated in CI; nothing reaches users that the team has not seen.

The rest of this note focuses on the newer, less-charted sense.

## Run-time generative UI

At run time the model decides *what interface to show*, often in response to the
user's intent or to the result of a tool call. Common patterns:

- **Structured output → component registry.** The model returns structured data
  (which component, which props) and the application maps it onto a **whitelisted
  set of components**. The model never emits raw HTML or markup that is rendered
  directly — it selects from a registry. This is the single most important safety
  boundary in run-time generative UI.
- **Streaming UI.** Components are streamed to the client as the model produces
  them, so a complex response renders progressively instead of after a long wait.
- **Tool-call-driven rendering.** A model's tool/function call (e.g. `getWeather`,
  `searchFlights`) is bound to a rich widget; invoking the tool renders the widget
  with the returned data, turning a chat turn into an interactive surface.
- **Adaptive / just-in-time interfaces.** The UI is personalised or re-arranged to
  the task and user — surfacing the relevant controls for *this* request rather
  than a fixed, one-size screen.

The mental shift mirrors the build-time one: the model does not *draw* UI, it
**composes from approved parts**. The component registry is to run-time generative
UI what the design system is to build-time — the constraint layer that makes
generation safe.

## Why the design system matters even more

The argument from [Design Systems as the AI Control Plane](design-systems-ai-control-plane.md)
applies with greater force at run time, because there is **no human review between
generation and the user**. A whitelisted, typed, accessible component library is
what lets you accept a model's UI decision without accepting a model's UI *output*:

- the model chooses a `Chart`, it cannot invent an inaccessible bespoke one;
- props are validated, so malformed selections fail safely rather than render
  broken;
- accessibility, theming, and interaction behaviour are guaranteed by the
  components, not by the model.

## Risks and how to contain them

- **Injection / unsafe rendering.** Never render model-produced markup or scripts
  directly — map structured output to a fixed component set. Treat model output as
  untrusted input.
- **Non-determinism.** The same request can yield different UI. Test with
  [eval-driven](../practices/eval-driven-ai-development.md) techniques: assert that
  outputs resolve to valid components with valid props, and snapshot the rendered
  result, rather than expecting one exact UI.
- **Hallucinated components.** Constrain the model to the registry (tool schemas /
  typed enums) so it cannot reference a component that does not exist; fall back to
  a safe default when it tries.
- **Accessibility & consistency.** Guaranteed by the component library, not the
  model — another reason the design system is a prerequisite, not an add-on.
- **Latency & cost.** Generating UI per request adds model latency and spend;
  streaming mitigates perceived latency, and caching/precomputing stable surfaces
  avoids regenerating what does not change.
- **UX unpredictability.** Users rely on spatial memory; a UI that re-arranges
  every time erodes learnability. Bound where generation is allowed to vary.

## When to use it — and when not to

Run-time generative UI suits surfaces that are **exploratory, data-dense, or
genuinely personalised**: assistants and copilots, dashboards assembled from a
query, search results that adapt to intent. It is a poor fit for **deterministic,
high-stakes flows** — checkout, payments, account settings, regulated forms —
where predictability, auditability, and a fixed, tested path matter more than
adaptivity. A common architecture is hybrid: generative surfaces for discovery,
fixed UI for commitment.

## Relationship to other notes

- [Design Systems as the AI Control Plane](design-systems-ai-control-plane.md) —
  the governance counterpart; the constraint layer both senses of generative UI
  depend on.
- [Composable Architecture](composable-architecture.md) — the approved primitives
  the model assembles from are a composability story at the UI layer.
- [The Micro-Frontend Canvas](micro-frontend-canvas.md) — boundary thinking for
  *which* surfaces are owned by whom still applies when those surfaces are
  generated.
- [The AI-Native Engineering Stack](../practices/ai-native-engineering-stack.md) —
  where UI generation fits in the broader tooling stack.
