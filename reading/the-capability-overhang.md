---
type: reading
title: The Capability Overhang
description: "Ethan Mollick's name for a premise four notes here already rely on — current AI capability far exceeds its utilisation, so the binding constraint is absorption — plus the jagged frontier, agency, and Rieseberg's self-efficacy mechanism for why agency goes unexercised, with altitude as the one axis Mollick's advantages don't cover."
tags: [ai-engineering, culture, reading]
topic: reading
status: notes
level: beginner
related:
  - engineering/ai-native/scaling-ai-adoption.md
  - leadership/learning-organisation.md
  - leadership/magical-thinking.md
  - engineering/ai-native/modern-engineering-values.md
  - reading/ai-productivity-research.md
  - reading/offloading-thinking-to-ai.md
  - engineering/ai-native/brownfield-agentic-engineering.md
  - reading/how-i-use-llms-2026.md
  - leadership/learning-culture-ai-agents.md
  - engineering/architecture/data-readiness-for-agents.md
  - engineering/ai-native/cress-context-engineering.md
  - engineering/ai-native/prompt-engineering-for-programmers.md
  - leadership/revised-rules-engineering-leadership.md
  - engineering/ai-native/linters-over-ai-review.md
  - engineering/ai-native/harness-engineering.md
  - reading/state-of-tech-2026.md
  - product/four-abstraction-levels-of-refinement.md
  - leadership/finding-problems-to-solve.md
  - engineering/ai-native/harness-design-experiments.md
  - engineering/ai-native/ai-gateway-control-plane.md
source: "https://www.oneusefulthing.org/p/the-overhang; https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/"
updated: 2026-10-25
---

# The Capability Overhang

Ethan Mollick (September 2026) argues that AI capability already far exceeds what anyone has
actually absorbed — a **capability overhang** — which makes the practical question about
utilisation rather than about what models will be able to do next.

**This is a personal essay, not a study**, filed for the vocabulary rather than the evidence.
The piece is about general knowledge work, not software engineering, and it promotes a book
pre-order. Its support for the overhang claim is a set of demonstrations, which this note
deliberately does not carry — see the caveat below.

## Why the term is worth having

The repo has been arguing the overhang for months without a word for it. Four notes rest on the
same premise:

| Note | The premise, unnamed |
|---|---|
| [Scaling AI Adoption in the SDLC](../engineering/ai-native/scaling-ai-adoption.md) | Adoption is an organisational programme, "not a licensing exercise" |
| [The Learning Organisation and AI Adoption](../leadership/learning-organisation.md) | Organisations struggle with adoption "for lack of learning structures, not technical limits" |
| [Magical Thinking in Engineering Leadership](../leadership/magical-thinking.md) | Procurement substituted for process change — the AI-tooling version of the "one weird trick" |
| [A Learning Culture for AI-Augmented Teams](../leadership/learning-culture-ai-agents.md) | Integrating agents changes how software gets built, not just what is installed |

All four say the gap is organisational rather than technical. None names **the gap itself**, which
is what "overhang" supplies: the distance between what the tools can already do and what a given
organisation has learned to get out of them. Having the noun makes it a thing you can measure
your own position against rather than a diffuse complaint about adoption.

## The jagged frontier

Mollick's established coinage, also absent from these notes until now: AI performance boundaries
are **inconsistent and unpredictable** rather than uniformly strong or weak. Capability is not a
line you are above or below; it is ragged, and the ragged parts are not where intuition puts
them.

This is load-bearing for two notes that assume it without saying it:

- [Brownfield Agentic Engineering](../engineering/ai-native/brownfield-agentic-engineering.md) —
  zones work *because* the terrain varies unpredictably. If capability were uniform you would set
  one policy; because it is jagged, you map regions and let the map decide.
- [Data Readiness for Agents](../engineering/architecture/data-readiness-for-agents.md) — the
  insistence that a contract breach override the model's own confidence is a response to
  jaggedness: a model is equally confident on both sides of the frontier, so its confidence
  cannot tell you which side you are on.

## The four advantages, honestly accounted

His prescription is to stop competing with the models and lean on four human advantages. Two are
held here already, in more operational form:

| Advantage | Status |
|---|---|
| **Deep knowledge** — specialist expertise that extracts better output | Adjacent. [CRESS](../engineering/ai-native/cress-context-engineering.md) and [Prompt Engineering for Programmers](../engineering/ai-native/prompt-engineering-for-programmers.md) treat this as *context supplied to the model*; Mollick's version is about what the human brings, which is a different emphasis on the same mechanism |
| **Wide knowledge** — cross-disciplinary familiarity that spots when the model is doing it wrong, including knowing the vocabulary to correct it | Adjacent, and the sharpest of the four. His example is knowing enough design language to stop a model "adding eyebrows" to a headline — you cannot ask for the right thing without the word for it |
| **Taste** — curation and rejection, now that generation is cheap | **Held, with more teeth.** [Modern Engineering Values](../engineering/ai-native/modern-engineering-values.md): "everyone can generate a lot of bullshit all day long", with taste as the **gating function** rather than a sensibility |
| **Agency** — *"willingness to test the boundaries of what's possible when everybody is equally confused"* | **New, and the one worth keeping** |

**Agency is the honest one.** The clause that earns it is "when everybody is equally confused" —
an admission that nobody knows where the frontier sits, including the people writing about it.
That is the same epistemic position these notes keep running into from the other side: every
provenance flag in this repo about unvalidated claims, vendor benchmarks and asserted design
properties is the same observation stated as caution rather than as invitation. Both responses
are reasonable; they are in tension, and worth holding together rather than resolving.

His term for the failure mode on the other side — **"slop"**, a flood of similar-quality output —
is already held three times over: slop pull requests in
[Revised Rules of Engineering Leadership](../leadership/revised-rules-engineering-leadership.md),
"slop cannons" in [Linters Over AI Review](../engineering/ai-native/linters-over-ai-review.md),
and slop as a named harness failure mode in
[Harness Engineering](../engineering/ai-native/harness-engineering.md).

## The human side: self-efficacy as the mechanism

Mollick names the gap and prescribes leaning on the four advantages, but says nothing about
**why people don't** — agency is listed as an advantage without an account of what suppresses it.
[Felix Rieseberg](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/)
(October 2026) supplies one: *"We humans have always been held back by what we believe
possible"* — psychology's **self-efficacy**, the belief in one's own capability that correlates
with what one actually accomplishes. Behind it, Locke & Latham's goal-setting research over 35
years: *"Humans who are given specific hard goals perform better than those who are simply told
to try their best."*

> **Interest declared.** Rieseberg is an **Anthropic engineering manager** who has led
> engineering for Claude.ai, Cowork and Claude Code Desktop — an employee arguing for more
> ambitious use of his employer's model. He discloses it in the piece (*"I work on Claude"*).
> A personal essay on motivation, with no measurement.

His framework has four axes, and **two of them are Mollick's advantages renamed**:

| Rieseberg's axis | Relation to the four above |
|---|---|
| **Depth** — field-expert rigour | ≈ **deep knowledge** |
| **Range** — the work seen from other fields | ≈ **wide knowledge** |
| **Speed** | He drops it himself: *"well established and requires little creativity in how you approach AI, so I'll skip this one"* |
| **Altitude** | **The one genuinely new axis** |

**Altitude** is *"going up in abstraction and considering the outcome rather than the individual
task"*, driven by the question *"what do you want to happen next?"* His examples are concrete
enough to transfer: rather than asking Claude to fix individual crashes, asking it to *"simply
keep our apps crash-free"*; rather than filling a quarterly deck template, *"Tell me what changed
this quarter, why, and what we should do about it."*

The generalisable move: **when execution gets cheap, go up a level from the task to the condition
that keeps generating the task.** That is the same ladder
[The Four Abstraction Levels of Refinement](../product/four-abstraction-levels-of-refinement.md)
climbs from the other end — problem before solution — and the same instinct as
[Finding Problems to Solve](../leadership/finding-problems-to-solve.md).

Two techniques worth keeping from the other axes:

- **Replacing nouns with verbs** — a quarterly review becomes *"getting busy people to believe a
  story about cause and effect"*, after which you *"assemble the crew"* of fields that would
  attack that verb rather than the noun. A reframing device these notes do not otherwise hold.
- **"Use an outside judge: Do *not* ask the model to judge itself."** Worth noting this is not
  new, only newly personal: it is the planner/generator/evaluator split in
  [Harness Design for Long-Running Apps](../engineering/ai-native/harness-design-experiments.md),
  borrowed there from generative adversarial networks on the grounds that a model evaluating its
  own work over-praises it. Same principle, stated as individual practice rather than harness
  architecture.

**Where the piece is weakest is its evidence, and it is the same weakness as the overhang's.**
Three supports are offered, and all three are selection effects: George Dantzig copying two
unsolved statistics problems off a blackboard in 1939 believing they were homework; Roger
Bannister *"remained the only human to do so for a mere 46 days"*; and Patrick Collison's *Fast*
list, *"chronicling the many things humans have accomplished when given both audacious goals and
tight deadlines."* Dantzig is one graduate student, and nobody collects the cases where an
unreasonable goal produced nothing. The Bannister framing implies a psychological barrier fell,
which is a contested reading — training and pacing methods were improving at the same time. The
*Fast* list is curated achievements with **no denominator**.

The caveat below applies in the same shape: an ambition overhang and a survivorship illusion
look identical from inside an anecdote.

**His stated limits are better than most**, and worth carrying because they bound the advice:
*"There are currently limits ('Claude, go make money' doesn't seem to work for most businesses
by itself in 2026)"*; altitude *"works less well for creative endeavors"*; and the whole approach
presumes a machine with rights to install software and access to broad data — which quietly
excludes most regulated environments, where
[the governance seam](../engineering/ai-native/ai-gateway-control-plane.md) exists precisely to
stop that.

## The caveat that matters

**The overhang is asserted from demonstrations, not measured.** The article's evidence is a set
of impressive artefacts — a 1977 text game converted into a playable 3D game, a 27,000-book
library reconstructed in 3D from photographs, an AI assembling a book trailer in Blender with
generated voices and sound — each framed as work that "would typically require weeks of human
work."

This note does not carry those examples, for three reasons. They are unverifiable from outside,
they will date within months as the named models are superseded, and "weeks of human work" is an
unmeasured counterfactual of exactly the kind these notes flag elsewhere.

That matters because the repo holds the measured side.
[Five Studies on AI and Software Engineering Productivity](ai-productivity-research.md) is
considerably more equivocal — in particular about the gap between *perceived* and *measured*
speedup. A capability overhang and an overestimated capability look identical from inside a
demonstration, and the demonstrations cannot tell you which you are looking at. The concept is
useful; the support offered for it is the weakest part of the piece.

## Relationship to other notes

- [Scaling AI Adoption in the SDLC](../engineering/ai-native/scaling-ai-adoption.md) and
  [The Learning Organisation](../leadership/learning-organisation.md) — the two notes this most
  directly names a premise for. They say *how* to close the gap; this says what to call it.
- [Five Studies on AI and Software Engineering Productivity](ai-productivity-research.md) — the
  empirical counterweight, and the reason to hold the overhang as a frame rather than a finding.
- [Modern Engineering Values](../engineering/ai-native/modern-engineering-values.md) — taste as
  the gating function, which is Mollick's third advantage already operationalised for engineering.
- [Offloading Thinking to AI](offloading-thinking-to-ai.md) — the direct counterweight on
  *agency*. Mollick urges testing the boundaries; Jun warns that delegating the thinking erodes
  the autonomy doing so depends on. Read as a pair: one argues for exploring what the tools can
  do, the other for noticing what you stop being able to do.
- [How I Use LLMs as a Staff Engineer (2026)](how-i-use-llms-2026.md) — the same advantages
  expressed as a concrete delegation map rather than as categories.
- [Brownfield Agentic Engineering](../engineering/ai-native/brownfield-agentic-engineering.md) —
  zones as the practical answer to a jagged frontier.
