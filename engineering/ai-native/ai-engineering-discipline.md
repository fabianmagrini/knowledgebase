---
title: AI Demands More Engineering Discipline
tags: [ai-engineering, observability, testing, reading]
topic: engineering/ai-native
status: notes
level: intermediate
related:
  - engineering/ai-native/own-the-outer-loop.md
  - engineering/ai-native/agentic-code-review.md
  - engineering/ai-native/eval-driven-ai-development.md
  - engineering/practices/change-absorption-capacity.md
  - engineering/ai-native/ci-cd-ai-engineering.md
  - engineering/ai-native/quality-first-ai-coding.md
  - engineering/ai-native/ai-native-engineering-overview.md
  - engineering/ai-native/trust-factory.md
  - reading/what-is-software-engineering-ai.md
source: "https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline"
updated: 2026-06-20
---

# AI Demands More Engineering Discipline

Charity Majors argues that AI-generated code — now competent at the level of a
median engineer — does **not** reduce the need for engineering rigour; it
*increases* it, while moving where the rigour lives. The discipline shifts **from
reviewing code to validating behaviour**. (Majors writes from an observability
practitioner's vantage — Honeycomb — so the heavy emphasis on observability should
be read in that light.)

## The inverted economics

When code became cheap and **regenerable**, treating it as a precious artifact
became obsolete. Majors' framing: *"code as a materialized view of understanding
that is useful while current, disposable when stale."* The danger is letting code
be the *only* place knowledge lives — **"code becomes precious when it is the only
place knowledge lives"**, and with AI that is unacceptable. The remedy is to encode
system knowledge **outside** the code: in tests, evals, traces, and architecture
artifacts.

Her analogy is **immutable infrastructure / Phoenix architectures** (Chad Fowler):
once you regenerate rather than edit in place, you are forced to understand
bootstrapping and dependencies and to externalise that knowledge. Regenerable code
demands the same. *"Mutation accumulates entropy. Replacement resets it."*

## Discipline moves to behavioural validation

Human validation is, she argues, the weakest link — machines will outpace us at
reading diffs — so requirements should be encoded into things that observe the
running system rather than inspect the source:

- **Observability-driven validation** — characterization tests, capture/replay,
  traffic splitting, and distributed traces that reveal *what the system actually
  does*, not what it should do.
- **Production as a stage of development** — *"production is not what happens after
  development is over; production is a stage of development"*; *"only prod is prod.
  Test in prod, or live a lie."* Her own practice: kill the oldest Kafka node via
  cron every Tuesday, so bootstrapping is validated through chaos, not theory.
- **Regenerability test** — can you delete the implementation and rebuild it
  identically from the externalised specs, tests, and traces?

This is the operations/QA discipline that software engineers historically
dismissed, now load-bearing.

## What fails without it

Treating "AI writes decent code" as permission to skip validation produces
nondeterministic production behaviour, drift between specification and
implementation, systems nobody truly understands, and an inability to regenerate or
migrate code safely.

## Recommendations

1. Invest in **evals and automated tests** that capture user-visible behaviour.
2. Build **architecture artifacts separate from code**, and regenerate code from
   them.
3. **Instrument everything** with traces *before* AI accelerates adoption.
4. Establish **ownership and specs** that survive code regeneration.
5. Adopt **short feedback loops** now, before the pressure increases.

She positions discipline as the competitive edge separating shipping teams from
vibe-coders, explicitly rejecting both "SaaS is dead" hype and do-nothing
skepticism. Cited influences include Chad Fowler's Phoenix architectures and Martin
Fowler's "Relocating Rigor".

## Relationship to other notes

- [Agentic Code Review](agentic-code-review.md) — the same shift seen from the
  review side: when humans can't keep pace, verification has to move; this note
  argues it moves into observability and production.
- [Eval-Driven Development](eval-driven-ai-development.md) — evals and behavioural
  tests are the externalised knowledge Majors wants standing in for precious code.
- [Change Absorption Capacity](../practices/change-absorption-capacity.md) — "instrument
  everything" and behavioural verification are exactly the telemetry that raises a
  system's capacity to absorb agent-speed change.
- [CI/CD as the Control Plane](ci-cd-ai-engineering.md) — the deterministic gates
  this discipline runs through.
- [Quality-First AI Coding](quality-first-ai-coding.md) — the writing-side
  counterpart; both insist AI raises, not lowers, the quality bar.
