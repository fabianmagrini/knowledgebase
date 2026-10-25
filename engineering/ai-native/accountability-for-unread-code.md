---
type: note
title: Accountability for Unread Code
description: "The moral crumple zone applied to agent-authored code, the two costs (checking unread work versus undoing failures the checks miss), why an oracle written by the generator proves nothing, the 14% figure evidencing review's non-detection function — and the same failure in prose, where no CI exists."
tags: [ai-engineering, code-review, testing, culture, reading]
topic: engineering/ai-native
status: notes
level: intermediate
related:
  - engineering/ai-native/substitution-myth-in-code-review.md
  - case-studies/intercom-ai-pr-approval.md
  - engineering/ai-native/review-replacement.md
  - engineering/ai-native/agentic-code-review.md
  - engineering/ai-native/dark-factories-examined.md
  - engineering/ai-native/harness-design-experiments.md
  - case-studies/cursor-agent-swarm-economics.md
  - engineering/ai-native/brownfield-agentic-engineering.md
  - reading/ai-productivity-research.md
  - engineering/architecture/comprehension-as-architecture.md
  - case-studies/vercel-v0-instant-navigations.md
  - engineering/ai-native/activity-metrics-obsolete.md
  - case-studies/doordash-flag-cleanup-agents.md
  - case-studies/github-copilot-rust-migration.md
  - reading/state-of-tech-2026.md
  - engineering/ai-native/agentic-verification.md
  - languages-and-frameworks/rust-for-agentic-development.md
  - case-studies/anthropic-scion-source-control.md
  - engineering/architecture/design-docs.md
  - reading/how-i-use-llms-2026.md
  - engineering/ai-native/dora-ai-capabilities.md
  - case-studies/anthropic-formal-verification-at-scale.md
source: "https://addyo.substack.com/p/the-code-nobody-reads; https://alifeengineered.substack.com/p/on-the-death-of-amazons-writing-culture"
updated: 2026-10-26
---

# Accountability for Unread Code

Addy Osmani (September 2026) argues that line-by-line reading is disappearing but **review — in
the sense of someone being answerable for what ships — cannot**. The transition requires
replacing reading with checking; skipping both is the failure.

**Provenance.** Sponsored content (Teleport, the same sponsor as his brownfield piece; he notes
pausing future sponsors on taking a new full-time role). The Anthropic figures are
vendor-reported, and the Teleport case study is the sponsor's own. The two strongest things in
the piece — Elish's concept and the Microsoft study — are external to both.

## The moral crumple zone

The concept this cluster was missing, borrowed from **Madeleine Clare Elish**:

> "Madeleine Clare Elish has a name for what happens to people at the edge of automated systems:
> the **moral crumple zone**. In a car, the crumple zone is built to absorb the impact so the
> passengers don't have to."

A human positioned at the edge of an automated system absorbs the blame for failures they were
never empowered to prevent. The structure *looks* accountable — there is a name on the approval
— while the person named had no realistic capacity to catch the problem.

**This names a hazard these notes have been circling for weeks without a word for it.**
[Replacing Code Review With Upstream Verification](review-replacement.md) observes that every
middle position on the review spectrum "retains something both endpoints lack: a named human
accountable for a specific change."
[The Substitution Myth in Code Review](substitution-myth-in-code-review.md) carries Allspaw's
"skin in the game." [Intercom](../../case-studies/intercom-ai-pr-approval.md) reports
accountability **relocating from reviewer to author** under auto-approval.

Read together with Elish, the Intercom arrangement has a sharp edge those notes do not draw:
**"the author is accountable" becomes a crumple zone when the author did not read it either.**
Moving responsibility to whoever opened the PR is only meaningful if that person had the capacity
to understand what they shipped. Where an agent wrote it and nobody read it, naming an owner
distributes liability without distributing control — which is the arrangement Elish's term
exists to criticise.

Osmani's test for staying out of it is a good one precisely because it is cheap: **"can I explain
this?"** If the answer is no, the signature is decoration.

## The two costs

The cleanest framing in the piece, and better than anything the cluster holds:

> "How fast a team or an industry gets there depends on two costs: the cost of checking work
> nobody read, and the cost of undoing a failure the checks miss."

| Option | What it costs |
|---|---|
| Read it | Human attention, which does not scale with agent output |
| **Check it** | Building and maintaining trustworthy verification |
| **Undo it** | Incident response, rollback, reputational and regulatory cost |
| Neither | Unsustainable |

The last row is not hypothetical. It is what the Faros data in
[Dark Factories Examined](dark-factories-examined.md) measures — **+31.3% unreviewed merges and
+242% incidents** in teams that stopped reviewing without building anything in review's place.
That is the "neither" column with a number attached, and it is the strongest empirical support
for this framing anywhere in these notes.

## Review was never mainly about defects — with evidence

The piece supplies something
[The Substitution Myth in Code Review](substitution-myth-in-code-review.md) argues without data.
From a 2013 Microsoft study:

> "Of the **570** review comments the researchers classified, only **14%** were about defects.
> The rest were about teaching, sharing context, suggesting better approaches and keeping team
> norms."

Developers' top *stated* reason for reviewing was finding defects; their actual comments were
mostly something else. That is independent corroboration of Allspaw's seven non-detection
functions, from thirteen years earlier and from a different tradition entirely — and it means the
substitution argument rests on measurement rather than on assertion.

It also sharpens the practical conclusion. If 86% of review output was teaching, context and
norm-maintenance, then a detector replacing review removes the 14% bottleneck and silently
deletes the rest.

## The oracle has to be independent of the generator

Stated more sharply here than elsewhere in these notes: **tests written by the system that wrote
the code prove very little.** Independence must come from outside — *"a spec a person wrote, a
reference implementation, a proof."*

Two anchors:

| Case | Detail |
|---|---|
| **Nicholas Carlini's C compiler** | 16 agents, ~**$20K**, ~**100K lines of Rust**, using **GCC as the reference**. His stated lesson: *"the task verifier is nearly perfect, otherwise Claude will solve the wrong problem."* |
| **SQLite** | Its test suite is **590× larger** than its source code |

The Carlini lesson is the general principle behind several results these notes already hold.
[Cursor's swarm](../../case-studies/cursor-agent-swarm-economics.md) worked because sqllogictest
is a genuine external oracle. [Vercel's `instant()`](../../case-studies/vercel-v0-instant-navigations.md)
manufactured one where none existed. And the **28 of 520** migration-blindness result in
[Brownfield Agentic Engineering](brownfield-agentic-engineering.md) — tests green while the
replacement still calls the legacy implementation — is exactly what a non-independent oracle
produces: the agent satisfied the check it was handed and solved the wrong problem.

The 590× figure is the uncomfortable half. If trustworthy checking is what replaces reading, SQLite
is the price list, and most codebases are nowhere near it.

## The same failure in prose, where there is no CI

Everything above concerns code.
[Steve Huynh](https://alifeengineered.substack.com/p/on-the-death-of-amazons-writing-culture)
(October 2026) describes the identical structure in documents at Amazon, and it is worth holding
beside the code case because **the compensating controls are absent**: an unread PR still meets
tests, linters and a pipeline; an unread document meets nothing.

His anecdote is a public failure of this note's own test. An L7 principal product manager opened
a review on a six-page document and *"two minutes into his presentation, it was blindingly
obvious to everybody in the room that he was reading the document for the first time."* **"Can I
explain this?"** answered in front of an audience.

Two coinages worth keeping:

- **"AI;DR"** — *AI; didn't read.* A senior engineer's tag for documents, on the reasoning that
  *"if a model wrote it, a model can summarize it."* The document twin of unread code, and a
  rational response: if the artefact was not authored, reading it closely is wasted effort.
- **"Meat proxies"** — the sharpest line, and it lands on performance reviews rather than on
  engineering: *"How absurd it is that the mechanism that was meant to be the primary driver of
  career growth conversations has devolved to managers being meat proxies for a conversation
  between two prompts."*

Reviews written with AI, aggregated with AI, humans copy-pasting between prompts. That is
**Elish's crumple zone with nothing in the loop at all** — the manager's name is on a career
decision whose reasoning no human produced or read. It is a worse case than the code one on both
costs above: there is no "check it" column, because no verification exists for a promotion
rationale, and the "undo it" cost falls on a person rather than a service.

Worth noting what this implies for the sector timelines below. Those forecast where line-by-line
*code* reading persists, graded by consequence. The document version has no equivalent gradient —
nobody has built evidence review for prose — so the artefacts carrying the highest personal
stakes are the ones with the least machinery behind them.

> **Provenance.** Huynh left Amazon in **2024** and states that *"everything after that date is
> secondhand"*; the L7 story reached him via an L6 who was present. He is a shareholder, writes
> for an audience, and says *"I'd like to be wrong about this."* Carried as a described failure
> mode, not as a measurement of Amazon.

## Practices, and the numbers to attribute

His practices, most of which the cluster already holds in some form: understand the problem before
agents write it; use "can I explain this?" as the accountability test; budget human attention by
change sensitivity rather than uniformly ([risk tiering](agentic-code-review.md),
[zones](brownfield-agentic-engineering.md)); keep checks independent of generation; **deliberately
preserve hands-on skills among junior engineers**; and be transparent about what was not carefully
reviewed. The last two are the least-held — the first is the pipeline problem
[Comprehension as an Architectural Characteristic](../architecture/comprehension-as-architecture.md)
implies without addressing, and the second is an honesty norm rather than a control.

**Vendor-reported, so attributed rather than relayed:** Anthropic engineers merging "about eight
times as much code per day" in Q2 2026 versus 2024, and automated review raising substantive
comments from **16% to 54% of PRs** while approval remains "still a human call."

The figure from the same source that cuts the other way is worth keeping for exactly that reason:
**"most said they could fully delegate only 0–20% of their work to Claude."** An 8× merge rate and
a 0–20% delegation ceiling are both self-reported from the same organisation, and they are hard to
hold together without concluding that the volume is concentrated in a narrow band of work.

**His sector timelines are forecasts, not findings:** line-by-line reading becoming unusual in
consumer/SaaS within ~2 years, enterprise and financial shifting from diff review to evidence
review over 3–5, and flight controls and critical medical retaining line-by-line reading for many
years. Recorded as a prediction.

## Relationship to other notes

- [The Substitution Myth in Code Review](substitution-myth-in-code-review.md) — the closest
  sibling and now its evidential leg. That note holds *what* review does (Allspaw) and *where the
  functions relocate* (Laycock); this adds measurement for the first and accountability for what
  remains unread.
- [Intercom's AI PR Approval](../../case-studies/intercom-ai-pr-approval.md) — accountability
  relocating to the author, read against Elish: a reassignment of responsibility without a
  reassignment of capacity is a crumple zone.
- [Dark Factories Examined](dark-factories-examined.md) — the "neither" column measured.
- [Replacing Code Review With Upstream Verification](review-replacement.md) — the five upstream
  layers are the "checking" column; this supplies the independence constraint that decides whether
  they work.
- [Harness Design for Long-Running App Development](harness-design-experiments.md) — the
  planner/generator/evaluator split exists for the reason named here: a model evaluating its own
  work over-praises it.
- [Brownfield Agentic Engineering](brownfield-agentic-engineering.md) — same author, same sponsor,
  and the migration-blindness result is this note's oracle-independence argument with a number.
- [Five Studies on AI and Software Engineering Productivity](../../reading/ai-productivity-research.md)
  — where the self-reported figures above should be read against peer-reviewed measurement.
