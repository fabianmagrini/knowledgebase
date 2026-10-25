---
type: note
title: DORA on AI — The Amplifier and the J-Curve
description: "The primary source for two claims this repo held second-hand: AI amplifies existing capability rather than creating it, and adoption runs through a J-curve whose exit DORA admits it cannot yet describe — plus the research lead proposing code review be thrown out, which the repo has evidence against."
tags: [ai-engineering, observability, culture, code-review, ci-cd, reading]
topic: engineering/ai-native
status: notes
level: intermediate
related:
  - concepts/devops-capability-model.md
  - engineering/ai-native/apex-framework.md
  - engineering/ai-native/scaling-ai-adoption.md
  - engineering/ai-native/activity-metrics-obsolete.md
  - engineering/ai-native/substitution-myth-in-code-review.md
  - engineering/ai-native/accountability-for-unread-code.md
  - engineering/ai-native/review-replacement.md
  - leadership/learning-organisation.md
  - leadership/magical-thinking.md
  - engineering/practices/change-absorption-capacity.md
  - engineering/architecture/data-readiness-for-agents.md
  - reading/ai-productivity-research.md
  - engineering/ai-native/team-topologies-agentic-platform.md
  - engineering/ai-native/dark-factories-examined.md
  - engineering/architecture/llm-platform-engineering.md
source: "https://www.infoq.com/presentations/dora-ai-adoption-engineering-performance/"
updated: 2026-10-26
---

# DORA on AI — The Amplifier and the J-Curve

**Nathen Harvey, who leads Google Cloud's DORA team** (QCon London, recorded 21 October 2026).
The title is the thesis: *AI is an Amplifier: Scale High Performance, Not Dysfunction.* Survey of
*"nearly 5,000 people"*, fielded June–July 2025; full reports at `dora.dev/dora-report-2025` and
`dora.dev/dora-aicmr`.

**This is the primary source for two claims these notes already carried at second hand.**
[Activity Metrics Under AI](activity-metrics-obsolete.md) records the amplifier effect
*"attributed to DORA 2025"* with the note that the attribution was the new part, and flags the
J-curve as **"asserted rather than shown"**. Both are below, from the person who runs the
research.

> **Provenance, and his own caveat is better than most.** Self-reported survey data, as all DORA
> data is, and he says so: *"Ninety percent of people tell the truth on surveys, 10% lie."* He is
> also explicit that the model cannot be used the way readers want to use it — *"we have this
> amazing capability. We can say, here's the shape of this complex world. Let's change just one
> thing and see what happens… You can't. It's impossible. You can't do that in your
> organization."* And then:
>
> > Don't believe me. Don't believe our research… You don't work for the world. You work at the
> > organization that you work at, and in its context… You've got to contextualize what we've
> > found. **Take our findings and use them as your hypothesis.**
>
> That is the correct instruction for every framework in these notes, stated by the author of one
> of them.

## Adoption is near-universal and tells you nothing

> Ninety percent of our survey respondents said yes [to using AI professionally]

Against which, the figures that complicate that headline:

| | |
|---|---|
| Rely on AI *"a little or not at all"* | **~35%** |
| Median time working with AI | **two hours** in an eight-hour day |
| Perceived productivity **decreased** | ~**5%** |
| Code quality *"a little bit worse"* | ~**10%** |
| Trust it *"a little or not at all"* | **30%** |
| Trust it *"a great deal"* | ~**11%** |
| **Software delivery instability** | **up** with adoption |
| Burnout and friction | *"basically stayed at zero"* |

**Delivery instability rising is the finding that should travel**, because it is the one nobody
quotes. The same dataset shows individual effectiveness as the most-improved outcome — so the
gains are local and the costs are systemic, which is the amplifier argument in two rows.

The six-week line is the compressed version, and he takes it from a LinkedIn post rather than the
survey:

> someone lamenting the fact that they can now build something in hours, and it takes six weeks
> still for that thing to make it into the hands of a customer, to get into production

That is [Change Absorption Capacity](../practices/change-absorption-capacity.md) as a complaint.

## The amplifier, and why trust is the loop

The mechanism: AI does not create capability, it magnifies whatever is already there — so strong
practice plus AI compounds and weak practice plus AI degrades faster. These notes already argue
this from two directions: [The Learning Organisation](../../leadership/learning-organisation.md)
(adoption fails for lack of learning structures, not technical limits) and
[Magical Thinking](../../leadership/magical-thinking.md) (procurement substituted for process
change). **What was missing was the attribution and the instability number.**

His loop — *"trust begets adoption, begets trust"* — is worth holding against the 30%/11% trust
split above. If trust is both an input to and an output of adoption, then an organisation that
starts with weak verification has no way to bootstrap it, which is the same reinforcing structure
the amplifier describes.

## The J-curve, including the part DORA does not know

The shape: early easy wins, then a trough where delivery instability rises and trust problems
surface, then recovery.

> Anytime you take on something new, your organization will likely go through this pattern…
> There's going to be some low-hanging fruit… Then all the low-hanging fruit will be consumed.
> Now you've got to get to the hard stuff. That's when it sucks… Software delivery instability
> starts to go up. You dip into this trough… There is another side. We've seen this all before…
> The same thing with SRE practices…

And then the admission:

> **What we don't yet know… how do you get there? How do you get to the other side?
> Collectively, we're learning that right now.**

**That is the most useful sentence in the talk and the one most likely to be dropped in
retelling.** A J-curve quoted as reassurance — "push through, it gets better" — is a different
claim from a J-curve whose exit route is unknown. The cloud and SRE precedents establish that
organisations *have* emerged from comparable troughs; they do not establish how, or that this one
has the same shape.

## The AI Capabilities Model

Capabilities that convert adoption into organisational outcomes rather than individual ones.
**The transcript names six; he refers to seven.** Recorded as six rather than guessing at a
seventh from the report, which is not read here:

1. A clear and communicated **AI stance**
2. A **healthy data ecosystem** with access to internal data
3. Strong **version control** practices
4. Working in **small batches**
5. **User-centric** focus
6. **Quality internal platforms**

Rows 2 and 6 are the ones with homes in these notes already —
[Data Readiness for Agents](../architecture/data-readiness-for-agents.md) is row 2 at
implementation depth, and [LLM Platform Engineering](../architecture/llm-platform-engineering.md)
is row 6 for the serving layer. Rows 3 and 4 are classic Accelerate capabilities
([the DevOps Capability Model](../../concepts/devops-capability-model.md)) surviving unchanged
into the AI-era model, which is itself a finding: the practices that made continuous delivery
work are the ones that make AI pay off.

Note how this sits against two neighbouring frameworks. [APEX](apex-framework.md) already folds
in *"DORA's AI-readiness capabilities"* as survey dimensions — this is the primary statement of
them, and APEX remains the scoreboard to this model's preconditions.
[Scaling AI Adoption](scaling-ai-adoption.md) organises the same territory into five enabler
categories; the two are competing taxonomies of one problem, and neither is derived from the
other.

### Seven team profiles, two of them named

The research also clusters teams into seven profiles. The transcript names two:

| Profile | As described |
|---|---|
| **Constrained by process** | *"Teams are running on a treadmill. Despite working on stable systems, their effort is consumed by inefficient processes, leading to high burnout and low impact."* |
| **Harmonious high achievers** | *"A virtuous cycle, stable, low-friction environment, empowered teams delivering high-quality work sustainably and without burnout."* |

The other five are referred to but not named. *Constrained by process* is the useful one, because
it describes a team whose **systems are fine and whose process is the binding constraint** — a
configuration no amount of AI adoption helps, and the clearest instance of the amplifier failing
to amplify anything worth having.

## Where this note disagrees with him

Harvey declares for incrementalism — *"I am a big proponent of Kaizen and continuous improvement,
not Kaikaku, radical change"* — and then proposes the most radical change in the talk:

> Maybe it's time code reviews go away. Maybe it's time they go away. How uncomfortable does that
> make you?… Why do we have code reviews? To validate that there are missing tests… To learn…
> Two brains think better than one… Maybe it's time to throw out code reviews.

**His stated reasons for having code review are almost exactly the functions these notes hold
evidence about.** *"To learn"* and *"two brains think better than one"* are two of
[Allspaw's seven non-detection functions](substitution-myth-in-code-review.md) — bidirectional
cognition and learning — and his proposed substitutes are LLM pair programming and LLM-written
tests.

That is the substitution myth as Allspaw defines it: replacing a function with a tool that
performs a superficially similar action while lacking what made the original work. Three things
in these notes bear on it directly:

- **The measurement.** [Accountability for Unread Code](accountability-for-unread-code.md)
  carries a 2013 Microsoft study in which only **14% of 570** review comments concerned defects;
  the rest were teaching, context, better approaches and norms. Throwing out review removes the
  14% bottleneck and **silently deletes the other 86%** — which is precisely the two functions he
  names as reasons to have kept it.
- **Confusion as signal.** The sharpest item in Allspaw's list is structurally unavailable to a
  model: a reviewer saying *"I don't understand this"* is a measurement of the code taken using
  the reviewer as the instrument. An LLM has no state corresponding to incomprehension, so the
  signal is not degraded by automation but absent.
- **Accountability.** *"An agent that 'signs off' on a pull request bears no consequences."* With
  Elish's **moral crumple zone**, moving responsibility to an author who did not read the change
  either distributes liability without distributing control.

**The sympathetic reading, which the repo also holds.**
[Replacing Code Review With Upstream Verification](review-replacement.md) makes a disciplined
version of the same move — retire review *into* five upstream layers rather than simply removing
it — and that note's own conclusion is that every middle position *"retains something both
endpoints lack: a named human accountable for a specific change."* Harvey's proposal has the
first half and not the second. Read charitably he is arguing for relocation and phrasing it as
deletion; read literally, he is recommending the configuration
[Dark Factories Examined](dark-factories-examined.md) measures at **+31.3% unreviewed merges and
+242% incidents** — teams that stopped reading without building anything in reading's place.

Given that his own survey reports **delivery instability rising**, recommending the removal of
the last synchronous check is the least internally consistent part of the talk.

## Two reframings worth keeping

**"That math doesn't math."** His argument against role replacement, and it is cleaner than most:

> how much time a week does a software engineer typically spend actually writing code? The ranges
> vary pretty wildly, but 10%, 15%, 30% at the high end… It's going to take away that thing that
> you do 10% of your time, so therefore we don't need you anymore. That math doesn't math to me
> either.

Note the arithmetic he leaves implicit: two hours in an eight-hour day *is* 30%, so the median
respondent's AI usage already occupies the whole of the upper estimate for time spent coding.

**Agent experience and builder experience.** The platform's customer list changes twice over:

> It's not just other developers I'm building for, I'm also building for the bots. I need to
> improve my developer experience. I also need to improve the **agent experience**.

> now everyone in your organization is a builder… How do I help Jane from accounting ship that
> application that she dreamed up last night and built with an AI? That sounds scary, doesn't it?
> **Maybe that's the new platform engineering.** How do we make it safe for there to be more
> builders across our organization?

The second is a genuine addition to
[Team Topologies for the Agentic Platform](team-topologies-agentic-platform.md), which treats the
platform team's users as engineers. A platform whose users include non-engineers shipping
AI-built applications is a different enabling problem — and *"make it safe"* is doing a lot of
work in that sentence, with no mechanism offered.

## What the talk does not cover

- **The seventh capability and five of the seven profiles are not named**, so the frameworks are
  only partly recoverable from the talk.
- **No effect sizes for the capabilities.** Which of the six matters most, and by how much, is
  not given — only that they drive outcomes in combination.
- **Nothing on how to exit the J-curve**, acknowledged as unknown.
- **No mechanism for the builder-experience proposal** beyond naming it as the new job.
- **Self-report throughout**, including the productivity and quality figures. These notes hold
  the counterweight: [Five Studies on AI Productivity](../../reading/ai-productivity-research.md)
  and METR's measured **−19%** against a believed **+20%**, a 39-point gap that makes any
  *perceived*-productivity figure — including the ones above — weak evidence about output.

## Relationship to other notes

- [Activity Metrics Under AI](activity-metrics-obsolete.md) — where the amplifier effect and
  J-curve were held second-hand; this is the primary source, and it supplies the instability
  finding that note lacked.
- [The DevOps Capability Model](../../concepts/devops-capability-model.md) — the Accelerate
  canon. Version control and small batches appear unchanged in the AI model, which is the
  continuity claim.
- [The APEX Framework](apex-framework.md) — the scoreboard to this model's preconditions; APEX
  already cites these capabilities at second hand.
- [Scaling AI Adoption in the SDLC](scaling-ai-adoption.md) — a competing five-category taxonomy
  of the same problem.
- [The Substitution Myth in Code Review](substitution-myth-in-code-review.md) and
  [Accountability for Unread Code](accountability-for-unread-code.md) — the evidenced rebuttal to
  the code-review recommendation, including the 14%-of-570 measurement.
- [Replacing Code Review With Upstream Verification](review-replacement.md) — the disciplined
  version of the same move, and the charitable reading of it.
- [The Learning Organisation](../../leadership/learning-organisation.md) and
  [Magical Thinking](../../leadership/magical-thinking.md) — the amplifier argument as these
  notes already made it, now with an attribution.
- [Five Studies on AI Productivity](../../reading/ai-productivity-research.md) — the measured
  counterweight to every self-reported figure here.
