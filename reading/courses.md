---
type: reference
title: Courses
description: "Structured learning material — courses, video series and book-plus-code packages — with what each covers, what it assumes, and why it is here. Distinct from the article captures in reading/README."
tags: [meta, ai-engineering, reading]
topic: reading
status: notes
updated: 2026-10-31
related:
  - engineering/ai-native/harness-engineering.md
  - engineering/ai-native/eval-driven-ai-development.md
  - engineering/ai-native/agentic-verification.md
  - engineering/ai-native/team-topologies-agentic-platform.md
  - engineering/ai-native/accountability-for-unread-code.md
  - engineering/ai-native/dark-factories-examined.md
  - case-studies/vercel-v0-instant-navigations.md
  - case-studies/anthropic-formal-verification-at-scale.md
---

# Courses

Structured learning material, as distinct from the one-off article captures indexed in
[reading/README.md](README.md). A course is a *commitment* rather than a read, so each entry
records what it assumes, what it costs in time, and **what it is for** — the gap it fills
relative to the rest of this knowledge base.

Entries are pointers, not summaries. A course that has been worked through and produced durable
ideas should graduate into a proper note in its topical folder, with this index retaining the
pointer.

> **Scope note.** Most of this knowledge base is about **building software with AI as a
> participant**, and it deliberately treats model internals as someone else's layer:
> [Harness Engineering](../engineering/ai-native/harness-engineering.md) holds that *"the model
> is effectively rented; the orchestration layer is owned and engineered"*, and
> [Team Topologies for the Agentic Platform](../engineering/ai-native/team-topologies-agentic-platform.md)
> files model hosting and fine-tuning as a complicated-subsystem that is *"optional unless doing
> sovereign inference or custom optimisation."* Courses on model internals are therefore
> **background rather than practice** — useful for knowing what is inside the rented thing, and
> not expected to produce notes in the engineering folders.

## AI Fundamentals

### Build a Reasoning Model (From Scratch) — Sebastian Raschka

- **Format** — a free video course of **8 videos, 11+ hours**, accompanying the book of the same
  name (Manning; print in colour via Amazon). Posted
  [here](https://magazine.sebastianraschka.com/p/building-reasoning-models), October 2026.
- **Prerequisites** — *"comfortable with Python and PyTorch"*. CPU is enough for early chapters;
  a GPU is needed for the training work.
- **Built on** — **Qwen3 0.6B** pre-trained weights, evaluated on **MATH-500**, with
  **DeepSeek R1** as the teacher for the distillation chapter.

| # | Chapter |
|---|---|
| 1 | Motivation and code setup |
| 2 | Loading a base model, text generation, and KV caching |
| 3 | **Building a verifier** for evaluation and reinforcement learning |
| 4 | Inference-time scaling: sampling and self-consistency |
| 5 | Inference-time scaling: scoring and self-refinement |
| 6 | Reinforcement learning: implementing **GRPO** for **RLVR** |
| 7 | Reinforcement learning: tracking, clipped policy ratios, and KL terms |
| 8 | Distilling a reasoning model |

**Why it is worth a pointer**, given the scope note above. Chapters 3 and 6 are the ones that
touch this knowledge base's concerns rather than only its background. **RLVR — reinforcement
learning with *verifiable* rewards — requires exactly the property the repo's oracle thread keeps
demanding**, one layer down:

| Where | The independent check |
|---|---|
| Agent loops | *"the task verifier is nearly perfect, otherwise Claude will solve the wrong problem"* — [Accountability for Unread Code](../engineering/ai-native/accountability-for-unread-code.md) |
| Frameworks | `instant()` turning "feels snappy" into a green-or-red oracle — [Vercel's agent loop](../case-studies/vercel-v0-instant-navigations.md) |
| Proof | Rocq as the checker — [Formal Verification at Scale](../case-studies/anthropic-formal-verification-at-scale.md) |
| **Training** | **a verifier scoring answers, as in chapters 3 and 6** |

And **reward hacking**, named in chapter 7's territory, is the same failure as agents gaming
narrow tests kept in the repository they are modifying — recorded in
[Dark Factories Examined](../engineering/ai-native/dark-factories-examined.md) and answered there
with holdout scenarios stored outside the codebase.

**Read the source post for what it is**: an announcement for a course and a book, so its
"taxonomies" are chapter headings rather than developed arguments. The course is the artefact;
the post is the advertisement. A shorter conceptual alternative exists — his ~90-minute
*AI Reasoning Models* course on LinkedIn Learning, covering inference-time scaling, RL and
distillation without the implementation.

## Other subjects

Nothing filed yet. Sections to add as material arrives rather than in advance — a heading with
no entries is the failure mode this index exists to avoid.
