---
title: Spec-Driven Development
tags: [ai-engineering, agentic-workflows, reading]
topic: engineering/practices
status: notes
level: intermediate
related:
  - engineering/practices/ai-dlc-methodology.md
  - engineering/practices/loop-driven-development.md
  - engineering/practices/eval-driven-ai-development.md
  - engineering/practices/agentic-sdlc.md
  - engineering/architecture/agile-design-decisions.md
  - engineering/architecture/design-docs.md
  - engineering/practices/ai-native-engineering-overview.md
  - reading/new-sdlc-vibe-coding.md
source: "https://brooker.co.za/blog/2026/04/09/waterfall-vs-spec"
updated: 2026-06-20
---

# Spec-Driven Development

In spec-driven development, the **specification — not the code — is the primary
artifact** that engineers write and iterate on; the implementation is generated
from it (increasingly by AI agents). Marc Brooker's argument, written in the
context of agentic AI coding, is mainly a rebuttal of a common objection: that
this is just **waterfall** in new clothes. He argues it is the opposite.

## "Up" is not "up-front"

The waterfall comparison conflates two different moves:

- **Up-front (waterfall)** — specifications are completed *before* implementation
  begins and then frozen. This fails because, as Brooker puts it, *it is extremely
  rare for a software project to know all of its requirements up-front*; software
  is **fundamentally iterative**.
- **Up (spec-driven)** — specifications are raised in *abstraction*, above the
  "muck of implementation", but remain **living artifacts** iterated on throughout.
  The spec is "the thing being iterated on, rather than the implementation".

The distinction is *when* and *how* the spec changes, not whether one exists.
Waterfall freezes the spec early; spec-driven keeps it upstream of the code and
edits it continuously. In that sense it is closer to the
[agile critique of Big Design Up Front](../architecture/agile-design-decisions.md)
than to waterfall.

## Why specs matter for AI agents

The payoff is **autonomy**. A clear spec is a *map* rather than turn-by-turn
prompting, so a team can "set an agent off building without a human inside the
tight loop". Brooker argues agents working from a spec produce *higher quality,
better designed, and better tested* code because they can see the big picture
instead of reacting prompt-by-prompt. The spec also stays **upstream**: most
changes are made to the spec and re-translated, not patched into the code.

This complements rather than replaces the iterative machinery elsewhere in the
cluster — [loop-driven development](loop-driven-development.md) is the loop the
agent runs, and [eval-driven development](eval-driven-ai-development.md) is how the
generated implementation is verified against what the spec demands.

## The formality spectrum

Specs are not one thing. They range across a spectrum of formality, chosen per
domain and per risk:

| Level | Form | Example use |
|---|---|---|
| **Informal** | Free-form prose, pictures, math | Most application logic |
| **Structured** | Keyword conventions — RFC 2119 (MUST/SHOULD), EARS | Requirements that need precision |
| **Formal** | Machine-checkable — TLA+, Lean | Critical algorithms and protocols |

Mixed media and mixed formality within one spec is expected: raise the precision
only where it matters. Where requirements **internally conflict**, resolving the
trade-off is human work — the spec makes the conflict visible, but judgement
decides it.

## Specs as the next abstraction layer

Brooker frames spec-driven development as the next rung on a long ladder of
programming abstraction: *switches → gates → instructions → lines of code →
specifications*. Each step raised what the programmer states and pushed the
mechanical translation downward. The new wrinkle is that the spec-to-code step is
now a **non-deterministic LLM translation** rather than a deterministic compiler,
which is why verification (evals, tests) matters more, not less. He is explicit
that this is early and that domain-specific tooling will emerge.

## Relationship to other notes

- [AI-DLC and the Reimagined SDLC](ai-dlc-methodology.md) — a specific named
  methodology; spec-driven development is the broader principle (spec as the
  primary, living artifact) that such methodologies operationalise.
- [Loop-Driven Development](loop-driven-development.md) — the iterative agent loop
  that runs *against* a spec.
- [Eval-Driven Development for AI Capabilities](eval-driven-ai-development.md) —
  verification of the non-deterministic spec-to-code translation.
- [The Agentic SDLC](agentic-sdlc.md) — the wider lifecycle in which agents run
  autonomously from specs.
- [Agile Design Decisions and Principles](../architecture/agile-design-decisions.md) —
  the BDUF critique spec-driven development inherits: design continuously, not
  up-front.
