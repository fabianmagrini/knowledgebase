---
type: reading
title: Preceptorship for Early-Career Engineers
description: "Russinovich and Hanselman on the talent-pipeline problem agents create — AI boost for seniors, AI drag for juniors, a narrowing pyramid — and a preceptor model borrowed from nursing: trained senior mentors, 3–5 learners each, chat-log review, and a Socratic early-career mode for coding assistants."
tags: [ai-engineering, leadership, culture, reading]
topic: reading
status: notes
level: intermediate
related:
  - leadership/learning-culture-ai-agents.md
  - engineering/ai-native/accountability-for-unread-code.md
  - engineering/architecture/comprehension-as-architecture.md
  - reading/ai-productivity-research.md
  - reading/offloading-thinking-to-ai.md
  - engineering/ai-native/scaling-ai-adoption.md
  - reading/the-capability-overhang.md
  - reading/what-is-software-engineering-ai.md
  - leadership/engineering-leadership-overview.md
source: "https://cacm.acm.org/opinion/redefining-the-software-engineering-profession-for-ai/"
updated: 2026-11-28
---

# Preceptorship for Early-Career Engineers

Mark Russinovich (Azure CTO) and Scott Hanselman (Microsoft), *"Redefining the Software Engineering
Profession for AI"*, Communications of the ACM, Opinion, 5 March 2026. The thesis, verbatim:

> We must keep hiring EiC developers, accept that they initially *reduce* capacity, and
> deliberately design systems that make their growth an explicit organizational goal. The path
> forward is a culture of *preceptorship at scale*.

The temptation they are arguing against is compressed into four words: **"Hire seniors, automate
juniors."**

> **Provenance.** An opinion piece by two Microsoft executives — the authors' viewpoint, not a
> corporate position, per secondary coverage (LeadDev, DevOps.com). The productivity examples are
> Microsoft's own and self-reported: **Project Societas** (seven part-time engineers, a
> consumer-ready Office Agent preview in 10 weeks, 110,000+ lines, 98% AI-generated) and **Aspire**,
> a Microsoft product. **The preceptor model is a proposal, not a result** — no trial, a ratio that
> is *"estimated"*, and nothing on cost, preceptor compensation, or how learning would be measured.
> The labour figure (−13%) is correlational; the MIT essay study behind "cognitive debt" is a narrow
> task. The piece also assumes *"an effectively unlimited inference budget"*, which says more about
> where the authors sit than about most organisations. The term and model are borrowed from
> nursing, where Hanselman's wife went through a hospital preceptor programme.

## AI boost, AI drag

The same tools produce opposite effects by seniority:

- **AI boost** — senior engineers' throughput multiplies as their work shifts from authoring to
  *directing*: specifying goals, verifying output, integrating.
- **AI drag** — early-in-career (EiC) developers lack the judgment and context to steer, verify and
  integrate agent output, so on an agentic team they initially slow it down.

The mechanism is the **agentic engineering intern**: a frontier agent behaves like an intern, and
an EiC developer cannot supervise an intern. The worked example is the sharp part. Faced with a
crash from a race condition, the agent inserts a `sleep` — which masks the bug, does not actually
reduce the race risk, and which it **cannot justify when challenged**, then admits was wrong. In
the next figure an experienced engineer directs the agent to insert sleeps *deliberately*, to make
the race reproduce reliably for debugging. **Same edit, opposite purpose** — and only someone who
understands synchronisation can tell which one they are looking at. That is the whole argument in
one diff.

The catalogue of failures they report "from multiple agentic AI projects" is familiar from this
repo's review notes: claiming success with significant bugs present, inefficient algorithms,
duplicated code, dismissing crashes and hangs as out of scope, leaving debug code behind, and hacks
that pass specific tests without generalising. The new claim is not that agents do this, but that
**catching it is seniority-gated**.

## The narrowing pyramid

| | Traditional organisation | Under unchecked AI |
|---|---|---|
| **Shape** | Many EiCs per tech lead, ~10:1 | Lopsided; shrinking base |
| **What the base is for** | Augmenting capacity with simple bug fixes and features | Under economic pressure — agents do that work |
| **How leads are made** | EiCs absorb standards, architecture, build and test systems through routine tasks, and some rise | The routine tasks that did the teaching are gone |

Generative AI, they argue, acts as **seniority-biased technological change** — the term is from a
Harvard study of US résumé and job-posting data — *"disproportionately amplifying engineers who
already possess systems judgment"*. Cited labour data: after GPT-4's release, employment of
22–25-year-olds in highly AI-exposed jobs including software development **fell roughly 13% while
senior roles grew**.

The reframing worth keeping: in their proposed organisation the base of the pyramid stays, but its
purpose changes — **"focused on refreshing senior talent rather than augmenting the productivity of
the organization."** Juniors become an investment line, not a capacity line, which is why
accepting that they *reduce* capacity is in the thesis rather than in the caveats.

This is the pipeline problem the repo had named and not addressed.
[Accountability for Unread Code](../engineering/ai-native/accountability-for-unread-code.md) lists
*preserve hands-on skills among junior engineers* as one of the least-held practices, and
[Comprehension as an Architectural Characteristic](../engineering/architecture/comprehension-as-architecture.md)
implies it: if comprehension is what keeps agent-written code safe, someone has to keep producing
people who comprehend.

## The preceptor model

- **Who** — preceptors are a **trained subset of the senior pool**, not every senior engineer.
  Preceptorship *"conveys both assessment and accountability"*: a professional role with
  responsibility for the learner's growth, not informal mentoring.
- **Ratio and duration** — **3–5 learners per preceptor** (estimated, varying with software
  complexity, learner experience and preceptor involvement), for **at least a year**.
- **Where** — in real product teams, not a training track.
- **How** — EiCs are *"invited into all aspects"* — prompting, debugging, reviewing — alongside the
  preceptor, so they see how expertise interacts with the agent. Their contribution is *learning in
  context*: surfacing misconceptions, asking why the agent's output fails. The preceptor's
  obligation is to **externalise senior judgment** — turning tacit expertise into teachable moments.
- **Chat-log review** — preceptors **review learners' agent conversations** to monitor progress and
  find knowledge gaps. This is the genuinely new mechanism: the agent transcript becomes a learning
  artefact the way a code review already is, and it exposes *how* a learner directed the work, not
  just what they shipped.

Note the arithmetic against the old pyramid: 10 EiCs per lead becomes 3–5 per preceptor, and
preceptors are a subset of seniors. The model therefore implies **fewer juniors per senior than
before**, not the same pyramid preserved — a narrower base, deliberately trained, rather than a
collapsed one.

## An EiC mode for coding assistants

The tooling half of the proposal: assistants should offer an explicit **EiC mode** defaulting to
**Socratic coaching before code generation** — challenging the learner, explaining its own
generation process, quizzing on key concepts and decisions, and tracking strengths and weaknesses
across sessions (which is what feeds the preceptor's chat-log review). Modelled on Khan Academy's
Khanmigo, and on Karpathy:

> I'm not going to present the solution before you guess. That would be wasteful…

[A Learning Culture for AI-Augmented Teams](../leadership/learning-culture-ai-agents.md) already
recommends *AI as a Socratic tutor, not an oracle* as a team habit. The difference is where it
lives: there it is a norm juniors are encouraged to follow; here it is a **tool default**, which
does not depend on the learner choosing the slower path.

## Supporting threads, held elsewhere

- **Mollick's verification paradox** — *"How do you train someone to verify work in fields they
  haven't mastered, when the AI itself prevents them from developing mastery?"* and *"becoming the
  audience rather than the magician"* (from *On Working with Wizards*). Mollick's adjacent framing
  is in [The Capability Overhang](the-capability-overhang.md).
- **Cognitive debt** — held with better evidence, via Storey, in
  [Five Studies on AI and Software Engineering Productivity](ai-productivity-research.md); the
  personal-scale version is [Offloading Thinking to AI](offloading-thinking-to-ai.md).
- **"Programming is not software engineering"** — the argument made at length in
  [What Is Software Engineering? (Adapting to AI)](what-is-software-engineering-ai.md).
- **The intern metaphor, inverted.** [Scaling AI Adoption](../engineering/ai-native/scaling-ai-adoption.md)
  organises adoption around *"treat AI as a highly capable, very fast junior"*. This piece asks the
  follow-on question that metaphor skips: if the agent occupies the junior's seat, where do the next
  seniors come from?

## What the piece does not cover

- **No evidence the model works.** Nursing precedent is the only support, and the secondary
  coverage notes hospitals value preceptorships as cost avoidance (retention, error reduction) —
  a business case software organisations would have to be persuaded applies to them.
- **No cost model.** A preceptor carrying five learners has less capacity for their own work; the
  boost the piece opens with is partly spent on the remedy it closes with, and that trade is not
  quantified.
- **No outcome measure** — how a programme would know a learner had acquired "systems taste".
- **No account of selection** — who becomes a preceptor, and whether the best directors of agents
  are the best teachers. The authors have said they are considering a follow-up on implementation.

## Relationship to other notes

- [A Learning Culture for AI-Augmented Teams](../leadership/learning-culture-ai-agents.md) — the
  team-habit version of protecting juniors; this is the organisational design.
- [Accountability for Unread Code](../engineering/ai-native/accountability-for-unread-code.md) and
  [Comprehension as an Architectural Characteristic](../engineering/architecture/comprehension-as-architecture.md)
  — the notes that named the pipeline problem this addresses.
- [Scaling AI Adoption](../engineering/ai-native/scaling-ai-adoption.md) — the "AI as junior"
  framing this piece answers.
- [Engineering Leadership Overview](../leadership/engineering-leadership-overview.md) — the map this
  sits on, as a hiring and organisation-design argument.
