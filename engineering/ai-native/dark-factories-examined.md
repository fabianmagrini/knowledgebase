---
type: note
title: Dark Factories Examined
description: "Tracing the dark-factory claim to its sources: the coiner stops short of it, the popularisers call it unproven, and the real risk is the accidental version — review collapsing without anything built to replace it."
tags: [ai-engineering, agentic-workflows, code-review, reading]
topic: engineering/ai-native
status: notes
level: intermediate
related:
  - engineering/ai-native/light-and-dark-factories.md
  - engineering/ai-native/agentic-code-review.md
  - reading/ai-productivity-research.md
  - case-studies/openai-agent-first-harness.md
  - case-studies/intercom-ai-pr-approval.md
  - case-studies/rewind-ai-pr-approval.md
  - engineering/ai-native/agentic-autonomy-levels.md
  - engineering/ai-native/ai-native-engineering-overview.md
  - engineering/ai-native/tdd-in-the-agent-loop.md
source: "https://kachar.dev/blog/the-lights-were-never-off"
updated: 2026-08-16
---

# Dark Factories Examined

Ilko Kacharov (July 2026) traces the **dark factory** claim — code shipping with no human
review — back through its citations, and finds the qualifiers dropping at each retelling.

The method is what makes it useful: not an experiment, but **document archaeology** on what
people actually said versus what got quoted. It is the counterpart to
[Light and Dark Software Factories](light-and-dark-factories.md), which takes the concept at
face value.

> The last step keeps moving. It has never left.

## Following the citations back

| Source | What they actually say |
|---|---|
| **Dan Shapiro**, who coined the autonomy levels | Stops at Level 4; calls Level 5 "nearly unbelievable" |
| **Simon Willison**, who popularised the framing | Later calls it "basically unproven" |
| **StrongDM, OpenAI** — the teams cited as examples | Never use the phrase; they say *software factory* or *harness engineering* |

The manufacturing precedent gets the same treatment. FANUC's 1981 lights-out plant ran for 16
hours with robots building robots — and **humans did final assembly the next morning**. Every
"30-day unattended" citation, Kacharov reports, traces to a single 2003 *Business 2.0*
paragraph.

> **Correction to these notes.** [Light and Dark Software Factories](light-and-dark-factories.md)
> cites FANUC and Xiaomi as lights-out precedent, folded in from Osmani's account. On this
> reading that precedent is thinner than it is usually presented: the endpoint moved, it did
> not disappear. That note now carries a pointer here.

## Three versions of the thing

The taxonomy worth keeping:

| Version | Status |
|---|---|
| **Marketed** | Does not exist — "0% human involvement" |
| **Engineered** | Real, expensive, narrow, roughly a year old. StrongDM: 32k lines with three people, holdout scenarios, isolation |
| **Accidental** | Arriving now at most companies, by default rather than design |

**The engineered version is not what the marketing describes.** Everyone quoting "code must
not be reviewed by humans" skips the stack underneath it: entropy control, merge policy,
verification against holdout scenarios, legibility constraints, isolation. StrongDM's stated
floor is **$1,000+ of tokens per engineer per day**. That is a deliberate, costly system, not
an absence of one.

## The accidental version is the actual finding

Faros data across **22,000 developers**:

| | |
|---|---|
| PRs opened by agents | **under 1%** |
| Unreviewed merges | **+31.3%** |
| Incidents | **+242%** |
| PR size | **+51%** |
| Review time | **5× longer** |

Agents are barely opening PRs, and review has still collapsed. Kacharov's reading:
**teams stopped reading code without building anything to replace the reading.**

That is the same Faros dataset [Agentic Code Review](agentic-code-review.md) cites for code
churn and defect rates — a different cut, and the more alarming one, because it does not
require anyone to have adopted a dark factory on purpose. The engineered version is a
deliberate choice a few organisations have made; the accidental one is a default that arrives
while the debate is about the marketed one.

## Self-report is the weak link

The **METR randomised controlled trial**: experienced developers were **19% slower** with AI
while believing they were **20% faster** — a 39-point gap between perception and measurement.

This is harder evidence for the direction
[Five Studies on AI Productivity](../../reading/ai-productivity-research.md) points at with
Vella & Blincoe's productivity-experience decoupling, where 84% reported gains while reported
experience worsened. Both say the same uncomfortable thing: **the practitioner's sense of
their own throughput is not a measurement**, which undercuts most published accounts of
AI-assisted productivity — including several in these notes.

## Two defences worth naming

- **Scenarios** — holdout tests stored **outside** the codebase, where the agent cannot reach
  them. This is the concrete answer to the *test manipulation* failure
  [Agentic Code Review](agentic-code-review.md) names: an agent that can edit the assertions
  it is judged against will eventually edit them.
- **Reward hacking** — the general form: agents gaming narrow tests kept in the repository
  they are modifying. Also *Digital Twin Universe*, behavioural clones of SaaS tools (Okta,
  Slack, Sheets) that let verification run without touching the real ones.

*Golden principles* — custom linters enforcing architecture mechanically — appear here as they
do in [OpenAI's Agent-First Harness](../../case-studies/openai-agent-first-harness.md), which
is the same practice observed from inside.

## Caveats the author states

- The Faros figures are **vendor data**: correlation with statistical significance, not
  causation.
- OpenAI's account comes with "no rate limits internally" — conditions that do not generalise.
- The METR trial used **year-old models** and studied assisted coding, not autonomous
  pipelines, so it is context rather than proof of the central claim.

## Relationship to other notes

- [Light and Dark Software Factories](light-and-dark-factories.md) — the concept taken at face
  value; this is the audit of where it came from. Both can be read together: Osmani's
  lit/dark placement argument survives even if the "dark" end turns out to be unoccupied.
- [Intercom](../../case-studies/intercom-ai-pr-approval.md) and
  [Rewind](../../case-studies/rewind-ai-pr-approval.md) — the *engineered* version, and both
  refuse large or complex changes rather than running unattended across the board. Stripe's
  1,300 agent-written PRs a week are human-reviewed twice over, which fails the dark
  definition on its own terms.
- [Agentic Autonomy Levels](agentic-autonomy-levels.md) — Shapiro's levels are the ladder
  being mis-cited; that note's insistence on autonomy as a calibrated safety property is the
  position this defends.
