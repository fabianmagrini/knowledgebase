---
type: note
title: The Four Abstraction Levels of Refinement
description: "Refinement fails because four conversations — problem, functional solution, technical steps, work slicing — run at once; the remedy is a linear first pass through them, and arriving with finished user stories makes it worse rather than better."
tags: [decision-making, communication, culture, reading]
topic: product
status: notes
level: intermediate
related:
  - product/prioritisation-as-a-symptom.md
  - product/explore-vs-exploit.md
  - reading/building-software-is-learning.md
  - engineering/ai-native/spec-driven-development.md
  - engineering/architecture/agile-design-decisions.md
  - engineering/architecture/over-engineering.md
  - engineering/ai-native/agile-in-the-age-of-ai.md
  - engineering/ai-native/loop-driven-development.md
  - reading/the-capability-overhang.md
source: "https://mdalmijn.com/p/mastering-the-four-abstraction-levels"
updated: 2026-10-25
---

# The Four Abstraction Levels of Refinement

Maarten Dalmijn (September 2026) argues that refinement sessions fail for a structural reason
rather than a preparation one: four different conversations are happening at once.

> The problem with this approach that we're trying to have four entirely different
> conversations at the same time that all depend on each other.

The four levels, in the order he puts them:

| # | Level | The question |
|---|---|---|
| **1** | **Problem** | What is the user need, and why does it matter? |
| **2** | **Functional solution** | How do we intend to solve it, from the user's side? |
| **3** | **Technical steps** | What has to be built to make that work? |
| **4** | **Work slicing** | How do we cut it into increments we can ship and learn from? |

The remedy is sequencing. Traverse the levels **linearly on the first pass**, top to bottom,
and only then move between them freely:

> The higher abstraction levels are anchored in the lower levels. Everything is connected to
> each other. If you discuss all of them at once, then the picture becomes murky and causes a
> complexity explosion in our heads.

The stated failure mode is attentional rather than analytical — *"everyone zones out, because
we're trying to have four different conversations at the same time where everybody will care
about different things."* People disengage from the three levels that are not theirs.

This is newsletter opinion, not research: no case data, no measurement, and the four levels are
presented as diagram labels that are never defined in prose. Dalmijn wrote *Driving Value with
Sprint Goals: **Humble** Plans, Exceptional Results*, and the "humble" vocabulary below comes
straight from it — this is substantially the book's thesis applied to one ceremony.

## User Fairytales

The most useful piece of vocabulary, and a name for a failure nothing else here has one for:

> Some User Stories are actually real-world stories of Users that contain the problem we're
> trying to solve while other User Stories are reverse engineered from functional or technical
> implementation details. That means they're actually not User Stories but **User Fairytales**.

The format is the problem. Because a user story can sit at any one of the four levels — or span
all of them — the notation hides which level a statement belongs to: *"Are we talking about what
the user needs? Are we talking about how it's going to work? Or are we talking about both?"*

His practical rule is to stop using the form when it stops carrying a user need: keep user
stories for level 1, and when breaking work into functional or technical pieces, **abandon the
user-story vocabulary** so nobody mistakes an implementation step for a need.

A fairytale is [over-engineering's requirements failure](../engineering/architecture/over-engineering.md)
caught one stage earlier. That note argues over-engineering is really a requirements problem
wearing a design costume, and that the diagnostic is asking *why* something is built this way.
A user story reverse-engineered from a predetermined implementation is exactly the artefact that
makes that question unanswerable — the "why" has already been overwritten by the "how".

## The preparation paradox

The claim most likely to be argued with:

> The more and better you prepare for refinement as Product Manager by having a set of finished
> work items, the worse your refinement session will usually be.

His reasoning: *"The amount of preparation is rarely the problem for your refinement, it's the
level of collaboration, exploration and discussion."* Arriving with crystallised work items
silences the conversation that was supposed to happen — so better templates and more exhaustive
prep make things worse, and better **facilitation** is the actual lever.

**The paradox undercuts itself.** His own first recommendation still asks for prepared,
problem-focused stories, which is preparation. The defensible version of the claim is narrower
and survives: preparation that **pre-commits levels 2–4** destroys the session; preparation that
sharpens level 1 is what makes it possible. It is a claim about the *kind* of preparation, not
the amount — and stated that way it is no longer paradoxical, just a distinction worth holding.

## Slicing, Gall's Law, and the humble first milestone

Level 4 is where he invokes **Gall's Law**:

> A complex system that works is invariably found to have evolved from a simple system that
> worked. A complex system designed from scratch never works and cannot be patched up to make
> it work.

With the consequence stated bluntly: *"If your first milestone isn't a simple system, you've
already screwed up and set yourself up for failure from the start."* His sizing heuristic is to
think in **weeks** for the first version; longer implies complexity has already been assumed in.

Good slicing is therefore about **deferring decisions** until the team knows more — creating
*"humble slices of work where we can work with what we do know to discover what we don't know."*

That is [Building Software Is Learning](../reading/building-software-is-learning.md) in product
vocabulary. Thorsten Ball argues misalignment between builder and requester is inevitable and
can only be accelerated through, not engineered away; Dalmijn's humble slice is the unit that
acceleration runs on. Both reject the linear execution of a predetermined spec, and both land on
feedback speed as the thing to optimise — which is also the mechanism behind
[Prioritisation as a Symptom](prioritisation-as-a-symptom.md): when shipping is cheap, getting
the order wrong is cheap.

## The agentic reading — an extension, not his argument

The article does not mention AI, agents or LLMs anywhere. The connection below is this knowledge
base's, and worth stating because it inverts a working assumption elsewhere in it.

[Spec-Driven Development](../engineering/ai-native/spec-driven-development.md) argues the spec is
the primary artefact, raised *up* in abstraction above implementation. What it does not say is
what a spec must keep **separate** — and the four levels are a serviceable answer. A spec that
silently mixes a user need, a chosen functional approach, a technical step and a slicing decision
gives an agent no way to tell which is which, because the agent has the same problem the room
does: it cannot see which level a line belongs to. The failure is worse with an agent, though,
because an agent will not zone out. It will implement a level-3 step as faithfully as a level-1
need, and the pre-committed solution gets built without anyone noticing the problem was never
discussed.

This puts **"don't arrive with finished work items" in direct tension with the agentic
instinct** to pre-write the most detailed spec possible before handing off. If Dalmijn is right
that crystallising levels 2–4 in advance destroys the thinking, then detail is not a free good in
a spec either — and the distinction drawn above is what resolves it: specify level 1 exhaustively,
hold levels 2–4 loosely, and let the agent loop supply the rest. That is the same division
[loop-driven development](../engineering/ai-native/loop-driven-development.md) already relies on,
arrived at from the human side.

## What the piece does not cover

- **The levels are asserted, not argued.** They appear as diagram labels with no definitions, no
  derivation and no discussion of whether four is the right number or these the right four.
- **No evidence of any kind** — no team, no before-and-after, no measurement of the cognitive
  overload that is the whole mechanism.
- **Nothing on async or distributed teams.** The entire remedy is a facilitated synchronous
  meeting, which is the format a great many teams no longer have.
- **No account of who decides.** If level 1 does not resolve in one session, the article offers
  nothing on how to proceed, how long to keep trying, or who breaks a tie.
- **Facilitation is named as the lever and then left alone** — it is asserted to matter more
  than preparation, without a single technique for doing it.

## Relationship to other notes

- [Prioritisation as a Symptom](prioritisation-as-a-symptom.md) — the adjacent altitude. That
  note is about choosing *between* pieces of work; this one is about working out what a single
  piece of work actually is. Both end up relying on cheap shipping.
- [Building Software Is Learning](../reading/building-software-is-learning.md) — the humble slice
  is the unit Ball's learning loop runs on; same argument, product vocabulary.
- [Over-Engineering Is Solving the Wrong Problem](../engineering/architecture/over-engineering.md)
  — a User Fairytale is that note's requirements failure caught one stage upstream.
- [Spec-Driven Development](../engineering/ai-native/spec-driven-development.md) — the four
  levels as a taxonomy of what a spec must keep separate, and the tension over how finished a
  spec should be before handoff.
- [Agile Design Decisions and Principles](../engineering/architecture/agile-design-decisions.md)
  — the BDUF critique this inherits: the objection is to freezing a solution early, not to
  thinking early.
- [Agile in the Age of AI](../engineering/ai-native/agile-in-the-age-of-ai.md) — keeps the
  ceremonies and changes their application; this is one ceremony's worth of that argument,
  written without reference to AI at all.
