---
title: The Trust Factory
tags: [ai-engineering, culture, testing, reading]
topic: engineering/practices
status: notes
level: intermediate
related:
  - engineering/practices/agile-in-the-age-of-ai.md
  - engineering/practices/release-confidence.md
  - engineering/practices/modern-engineering-values.md
  - engineering/practices/ai-engineering-discipline.md
  - leadership/learning-organisation.md
  - engineering/practices/ai-native-engineering-overview.md
source: "https://newsletter.kentbeck.com/p/trust-factory"
updated: 2026-06-20
---

# The Trust Factory

Kent Beck reframes Extreme Programming (XP) as a system for **manufacturing trust**, not just
producing code. His central worry about AI-accelerated development: *"we're accumulating code
faster than we are accumulating trust."* Features now appear faster than the trust that makes them
safe to depend on, and that gap is where instability lives.

## The asymmetry: code vs. trust

The argument turns on a difference in kind between the two things a team produces.

| | Code | Trust |
|---|---|---|
| State | Binary — it works or it doesn't | Continuous — accumulates by degrees |
| Direction | Reversible (revert, rewrite) | **Asymmetrical and irreversible** — builds slowly, evaporates instantly |
| What AI does to it | Accelerates production dramatically | Largely untouched, or actively eroded |

Because trust is slow to build and instant to lose, optimising only for code output quietly
runs the system down: you take on *trust debt* that no amount of generated code repays.

## XP as a three-level trust factory

Beck reads the XP practices→principles→values structure as three reinforcing layers, each
producing trustworthiness in a different way:

| Level | Examples | How it builds trust |
|---|---|---|
| **Practices** (concrete actions) | Programmer testing, pairing, continuous integration, weekly planning, customer involvement, continuous deployment, refactoring, observability | Encourage people to *act* trustworthily and make trustworthiness visible |
| **Principles** (guiding concepts) | Humanity, mutual benefit, improvement, flow, redundancy | Create the psychological safety in which trust can form |
| **Values** (foundational beliefs) | Communication, simplicity, feedback, courage, respect | Establish shared purpose — the *why* trust is worth building |

The practices aren't just engineering hygiene; each is a mechanism that turns work into evidence
of trustworthiness.

## How "genie" development erodes trust

Beck uses **"genie"** for wish-granting AI code generation. Its risks are framed in trust terms:

- **Non-obvious failure.** Generated software fails in scenarios that aren't visible up front, so
  apparent progress outruns demonstrated reliability.
- **Single-player development.** Solo human-plus-genie work removes the person-to-person
  interactions (pairing, review, planning) where trust is actually built.
- **Reactive management.** Prioritising tactical wins over strategic success, and ignoring future
  optionality, spends trust for short-term output.

## The counter-move: "slow development"

Beck's prescription is deliberately paced development — frequent person-to-person interaction,
structural improvement (refactoring), reinforcing purpose, and quality assurance — which
*paradoxically increases long-term velocity* by accumulating institutional trust. The shape of the
claim is the familiar one: output is not value, and effort is not progress.

## Relationship to other notes

- [Agile in the Age of AI](agile-in-the-age-of-ai.md) — the closest companion. Both argue
  *output ≠ value* and that AI's speed strains the feedback loops between people. That note frames
  the issue as Agile principles persisting under AI; this one names the scarce resource —
  **trust** — and gives XP's three-level structure as the factory that produces it.
- [Release Confidence as a System Property](release-confidence.md) — a complementary sense of
  "trust." That note engineers *confidence into the technical system* (understandable, owned,
  self-explaining, consistent); Beck's trust is *interpersonal and institutional*. Together they
  cover the machine side and the human side of the same word.
- [Modern Engineering Values](modern-engineering-values.md) — another "values still hold under AI"
  account; Beck supplies the specific XP practices/principles/values stack and the trust mechanism
  behind each layer.
- [AI Demands More Engineering Discipline](ai-engineering-discipline.md) — the discipline that
  rebuilds the trust genie development erodes: validating behaviour, observability, not trusting
  generated code on sight.
- [The Learning Organisation and AI Adoption](../../leadership/learning-organisation.md) —
  psychological safety as the cultural precondition; Beck locates it at the *principles* level of
  the factory *(in leadership)*.
