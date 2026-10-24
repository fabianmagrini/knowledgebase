---
type: reading
title: Ultimate — A Self-Extending Agent Harness
description: "One operator's personal harness that rebuilds itself while running: standing agents that never conclude, notes that deliver without triggering a turn, side chats that fork and inject-or-discard — and seven parallel feature streams against a repo that holds a three-agent human ceiling."
tags: [ai-engineering, agentic-workflows, architecture, reading]
topic: reading
status: notes
level: intermediate
related:
  - reading/multi-agent-coding-coordination.md
  - engineering/ai-native/harness-design-experiments.md
  - engineering/ai-native/harness-engineering.md
  - engineering/ai-native/long-running-agents.md
  - reading/reactive-reducer-orchestration.md
  - reading/building-effective-agents.md
  - engineering/ai-native/agentic-verification.md
  - engineering/ai-native/model-routing-and-ai-gateways.md
  - case-studies/cursor-agent-swarm-economics.md
source: "https://danielgriesser.com/posts/ultimate/"
updated: 2026-10-24
---

# Ultimate — A Self-Extending Agent Harness

Daniel Griesser (October 2026) on **Ultimate**, an agent harness he built for himself that
modifies and redeploys itself while running. He is Senior Director of Engineering at Sentry, but
this is a **personal project, not Sentry's work**.

> **Provenance, which has to come first.** There is **no measurement of any kind** here — no
> cost, no token counts, no time comparison, no quality assessment. One operator, one project,
> self-reported. His own disclaimer is the bluntest of any source in these notes: *"I don't
> really recommend it… There are no guarantees about what stays and what changes… use it at your
> own risk."*
>
> The genuine mitigation is that **the code is open source** (`github.com/HazAT/ultimate`), so
> the mechanisms below are inspectable — which is more than can be said for most of this
> cluster. Read it as a catalogue of techniques one person found worth building, not as evidence
> that they work.

The coordination layer is largely ground
[Multi-Agent Coding Without Worktree Chaos](multi-agent-coding-coordination.md) already covers:
coordinators dispatching workers and reviewers, a worktree per feature, messaging between
agents. Note that the two disagree on the foundation — Wells argues worktrees are the *wrong*
default for routine parallel work because they defer coordination to merge time, and Griesser
makes them the default and automates merge time instead. Four mechanisms are new here.

## Four mechanisms worth keeping

**Standing agents.** The idea the rest of the design hangs on:

> The lander is a standing agent, built into Ultimate. A standing agent is always there: it
> never gets concluded, so it keeps its conversation and everything it learned about the project.

[Long-Running Agents](../engineering/ai-native/long-running-agents.md) is about keeping a single
*run* durable against context rot and state loss. This is different: **non-termination as the
unit of accumulated project knowledge.** The agent is a long-lived process with a conversation
as its memory, rather than a task that completes.

**Notes — delivery decoupled from control flow.**

> A note is a message that doesn't trigger an agent turn. It's just there when the agent's next
> turn starts, like giving it a hint about what happened.

Wells' Agent Mail is explicit inter-agent messaging; this is sharper, because the interesting
property is what it *doesn't* do. A message that does not wake its recipient separates
**information arrival** from **execution scheduling** — the same instinct as
[Reactive Reducer Orchestration](reactive-reducer-orchestration.md), which takes the model out
of control flow entirely. Without it, every piece of context you want an agent to have is also
an interrupt.

**Side chats — forking the conversation.**

> When I press Tab, I switch into a side chat that forks off the Ultimate conversation… When I'm
> done, I either summarize and inject what happened back into the main conversation, or discard
> it.

**Inject-or-discard is the whole value**: exploratory work that would otherwise pollute the main
context either comes back compressed or leaves no trace. This is the practical form of
*"context resets beat compaction"* from
[Harness Design for Long-Running Apps](../engineering/ai-native/harness-design-experiments.md) —
except applied at the operator's discretion mid-session rather than as a scheduled reset.

**A harness that rebuilds itself while running.** The actual thesis, and nothing in these notes
covers it:

> On the server side, a supervisor holds the port. A new process starts and checks that it
> boots. If it does, the supervisor hands the port over, the browser just reconnects, and
> everything keeps going.

The harness is the thing under development *and* the thing doing the development. Ordinary
blue-green deployment mechanics, applied so that the tool never stops while improving itself.

A fifth, smaller one worth recording because it answers an open problem:
[Harness Engineering](../engineering/ai-native/harness-engineering.md) names harnesses
*"growing into large, opaque monoliths"* as a failure mode without offering a remedy. Griesser's
is to make the harness audit itself — *"ask Ultimate itself to inspect tool calls and failed
tool calls, so we can codify tools, remove the ones we don't use anymore, and just get rid of
old stuff."* Failed tool calls as the signal for what to build, and unused ones as the signal
for what to delete.

## Model heterogeneity by role

> I used Opus 5.5 for almost everything. The workers are GPT 6.1 Sol, Astra reviews for
> correctness and Luna is the summary model, to save the precious tokens for Opus.

[Model Routing and AI Gateways](../engineering/ai-native/model-routing-and-ai-gateways.md)
covers routing by **cost** — cheapest model that is good enough per request. This is routing by
**role inside a single development loop**, across vendors: a frontier model holding the thread, a
different vendor's model doing bulk construction, a third reviewing for correctness, a cheap one
summarising. The repo had the principle and no concrete instance of it applied to coding work.

## The challenge to the parallelism ceiling

> On the left, seven features are in flight, each with its own coordinator, workers and
> reviewers… This is what a normal evening looks like.

Two things in these notes say that should not work. `multi-agent-coding-coordination` cites a
**~three parallel agents** comfortable human ceiling, and
[harness-design-experiments](../engineering/ai-native/harness-design-experiments.md) concludes —
from a controlled comparison with costs recorded — that **harness complexity should *decrease*
as models improve**, because scaffolding compensating for model limits should retire as the
limits lift. Ultimate is the maximal opposite case, built on current models.

**This does not overturn either, and should not be read as doing so.** A controlled comparison
with cost figures against one person's unmeasured evening is not an even contest, and seven
coordinators in flight is a claim about what he can *launch*, not about what the output was worth
— the post contains no quality or cost assessment to settle it.

What it does suggest is a distinction neither source draws. Anthropic measured harness complexity
as **scaffolding around a task**, which does retire as models improve. Griesser's complexity is
mostly **interface** — notes, side chats, standing agents, hot reload are all machinery for one
human to stay in contact with many concurrent streams. That kind of complexity tracks the number
of things being supervised rather than the capability of the model, so it would not be expected
to retire for the same reason. Worth holding as a hypothesis, since nothing here tests it.

## What it does not cover

- **No cost or token figures**, while running four models across seven parallel streams. The one
  number in the piece is 407 tests.
- **Nothing on what the self-rebuilding has broken.** A system that redeploys itself mid-session
  has an obvious failure class, and no incident is described.
- **No oracle behind the lander.** It *"resolves"* merge conflicts and merges when the tests
  pass, which makes the test suite the sole arbiter of a semantic decision — exactly the gap
  [Agentic Verification](../engineering/ai-native/agentic-verification.md) is about. A wrongly
  resolved conflict that still passes 407 tests is the case that matters, and it is not
  addressed.
- **No comparison against off-the-shelf harnesses.** Whether any of this beats Claude Code or
  Codex with a few scripts is never asked.

## Relationship to other notes

- [Multi-Agent Coding Without Worktree Chaos](multi-agent-coding-coordination.md) — the nearest
  sibling and the direct disagreement: Wells rejects worktrees for routine parallel work, this
  builds on them and automates the merge.
- [Harness Design for Long-Running App Development](../engineering/ai-native/harness-design-experiments.md)
  — the measured case for *less* harness; this is the maximal case for more, with the
  scaffolding-vs-interface distinction offered as a possible reconciliation.
- [Harness Engineering](../engineering/ai-native/harness-engineering.md) — the component anatomy;
  tool-call auditing is a remedy for the harness-entropy failure mode it names.
- [Long-Running Agents](../engineering/ai-native/long-running-agents.md) — durability of one run
  versus standing agents that never conclude.
- [Reactive Reducer Orchestration](reactive-reducer-orchestration.md) — the model out of control
  flow; non-waking notes are a smaller version of the same separation.
- [Model Routing and AI Gateways](../engineering/ai-native/model-routing-and-ai-gateways.md) —
  routing by cost; this is routing by role within one loop, across vendors.
- [Cursor's Agent Swarm Economics](../case-studies/cursor-agent-swarm-economics.md) — the
  measured version of parallel agent work, including the failure-mode catalogue and the cost
  figures this post has none of.
