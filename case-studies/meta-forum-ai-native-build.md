---
type: case-study
title: Meta's Forum — Human-on-the-Loop in Practice
description: "The fourth agent-first product account here, earning its place on three things: human-on-the-loop stated as four verbs rather than a label, 'verified production-ready outcomes' as a definition of done, and a sandbox build flavour where prototype code physically does not exist in the production binary."
tags: [ai-engineering, agentic-workflows, testing, code-review, architecture, reading]
topic: case-studies
status: notes
level: intermediate
related:
  - case-studies/openai-agent-first-harness.md
  - case-studies/ramp-inspect-agent-platform.md
  - case-studies/anthropic-ai-native-teams.md
  - engineering/ai-native/agentic-code-review.md
  - engineering/ai-native/activity-metrics-obsolete.md
  - engineering/ai-native/dora-ai-capabilities.md
  - tools/claude-code-steering-mechanisms.md
  - case-studies/slack-agentic-e2e-testing.md
  - engineering/ai-native/agentic-verification.md
  - engineering/architecture/skeleton-architecture.md
  - engineering/practices/feature-flags-and-branch-by-abstraction.md
  - engineering/ai-native/brownfield-agentic-engineering.md
  - engineering/ai-native/harness-design-experiments.md
  - engineering/ai-native/review-replacement.md
  - product/four-abstraction-levels-of-refinement.md
source: "https://engineering.fb.com/2026/10/15/ml-applications/how-meta-built-forum-ai-native-engineering/"
updated: 2026-11-02
---

# Meta's Forum — Human-on-the-Loop in Practice

Nine Meta engineers (October 2026) on building **Forum**, a standalone Facebook Groups app, with
agents as participants in the development loop rather than as autocomplete. *"Forum reached core
feature parity with Facebook Groups in eight weeks."*

> **This is the fourth account of its kind in these notes**, after
> [OpenAI's agent-first harness](openai-agent-first-harness.md),
> [Ramp's Inspect platform](ramp-inspect-agent-platform.md) and
> [Anthropic's team structure](anthropic-ai-native-teams.md) — and **human-on-the-loop is
> already named** in [Agentic Code Review](../engineering/ai-native/agentic-code-review.md) as
> its central shift. So the framing is not what earns this a note; three specific mechanisms
> below are.
>
> **Provenance.** Meta on Meta, and the least quantified of the four accounts: *"small team"*
> with no count, no code-authorship fraction, and the one performance result given as
> *"materially reduced"* rather than measured. Against OpenAI's ~1M lines and ~1,500 PRs, this
> is an operating-model description rather than a data point.

## Human-on-the-loop, stated as a job rather than a label

The distinction the repo had as a term and not as a definition:

| | |
|---|---|
| **Human-in-the-loop** | *"the engineer drives every step and the AI assists inside it by autocompleting a function, suggesting a fix, or answering a question"* |
| **Human-on-the-loop** | *"the agent runs the iteration itself — plan, implement, build, test, correct, repeat — while the engineer **sets the goal, watches the run, steps in when it drifts, and approves the result**"* |

`agentic-code-review` uses the term for a *review-stage* shift — the reviewer stops reading every
diff. This states it as the whole iteration, with **four verbs** that amount to a job description:
set, watch, intervene, approve. Worth having, because "human-on-the-loop" is otherwise the kind of
phrase that can be adopted without changing anything.

Note what the second verb assumes. *Watching the run* is a real cost that neither this piece nor
the others price — and it is the same cost
[Harness Design for Long-Running Apps](../engineering/ai-native/harness-design-experiments.md)
measured from the other side at a **22× cost multiple** for the elaborate harness. Supervision is
not free just because it is not typing.

## "Verified, production-ready outcomes" — a definition of done, not a diagnostic

> We measured **verified, production-ready outcomes** — changes that build, pass tests, and
> survive review.

**This is the shape of answer [Activity Metrics Under AI](../engineering/ai-native/activity-metrics-obsolete.md)
asks for and does not supply.** That note rejects LOC, commits and PR counts, and its six
replacements are all *diagnostics* — review queue time, 14-day rework, validation failure rate,
post-deployment rework. Useful for noticing problems; none of them is a **definition of done**.
Meta's is: three conjunctive conditions, each mechanically checkable except the last.

Two observations the piece does not make.

**It writes human review into the metric.** *"Survive review"* is the third condition, which puts
this in direct opposition to [DORA on AI](../engineering/ai-native/dora-ai-capabilities.md), where
Nathen Harvey proposes *"maybe it's time to throw out code reviews."* Meta keeps review and makes
it the terminal gate — and their agents *verify before* review, filtering low-confidence output
upstream rather than replacing the check. That is the disciplined version
[Replacing Code Review With Upstream Verification](../engineering/ai-native/review-replacement.md)
argues for: add upstream layers, keep the named human at the end.

**It is a throughput metric in disguise, and that is the point.** Counting *verified* outcomes
rather than changes makes volume and quality the same number, so a flood of unverified output
scores zero. Compare the authorship counts running through these notes — Ramp's 75%, Rootly's
80%, OpenAI's ~3.5 PRs per engineer per day — all of which count changes and none of which
condition on the change being good.

## The sandbox build flavour — isolation by compilation

The best engineering idea in the piece:

> Our solution was a **separate build flavor**, a sandbox app that shares the exact same
> codebase, frameworks, and design system as production, but compiles prototype code *out* of the
> production build entirely via a plugin/socket architecture.

Three consequences, and the third is the one worth stealing:

- Designers and cross-functional partners could prototype *"without needing an engineer in the
  loop for each change"*
- Sandbox work ports to production *"with no rebuild"* — same codebase, same design system
- **"No prototype code could crash the production app because it physically didn't exist in that
  build."**

**That is isolation by compilation rather than by convention or by flag**, and it is a harder
guarantee than anything else in these notes.
[Feature Flags and Branch by Abstraction](../engineering/practices/feature-flags-and-branch-by-abstraction.md)
keeps unreleased code *in* the binary behind a runtime condition — which means a flag bug, a
stale default or a code path reached unexpectedly can still execute it. Compiling it out removes
the failure mode rather than gating it. The cost is that the two builds can diverge, and the
mitigation is the shared codebase and design system.

It is also [Skeleton Architecture](../engineering/architecture/skeleton-architecture.md)'s central
principle applied to the build graph: guardrails must be *"physically difficult for AI to
bypass"* rather than advisory. An agent cannot talk its way past a module that is not linked.

And it answers a question the repo recorded as unanswered. `dora-ai-capabilities` carries
Harvey's **builder experience** proposal — *"How do I help Jane from accounting ship that
application that she dreamed up last night… How do we make it safe for there to be more
builders?"* — and notes that *"make it safe"* is doing a lot of work with **no mechanism
offered**. This is a mechanism: let non-engineers build in a flavour whose code cannot reach
production, in the same codebase so the work is portable when it is ready.

## Navigation agents, and the failure that costs more than the technique

> We deployed **navigation agents** that interact with the live app exactly like a person would.
> These agents perform actions, read the screen, and report regressions.

That is the goal-based testing mode in
[Slack's agentic E2E experiment](slack-agentic-e2e-testing.md), running in a shipped product
rather than an experiment. The named failure is the more useful half:

> the agent losing track of where it was in the app — editing the home feed when asked to change
> the group home screen, or **guessing at screen coordinates**

**Spatial disorientation is a distinct failure class** and these notes did not hold it. It
belongs beside [Agentic Verification](../engineering/ai-native/agentic-verification.md)'s argument
that E2E is the ground truth for agent-written code, as the price of using it that way: an agent
driving a UI has to maintain a model of *where it is*, and when that model drifts it acts
confidently on the wrong screen. The fix implied by the text is **direct state inspection rather
than descriptions** — give the agent the app's actual state instead of asking it to infer
position from what it sees.

The same post also reports autonomous stress-testing finding a memory regression: *"The agent
isolated a repro, proposed a fix, and verified it — all during development, before the app reached
users."* The effect is *"materially reduced on-device memory growth and page faults"*, with no
figures, which is a shame given it is the clearest instance of an agent closing a loop the authors
describe.

## The five components, and one detail better than the repo's version

Rules, Skills, Agents, Commands, Hooks:

| Component | As defined |
|---|---|
| **Rules** | *"permanent project instructions. When the agent repeats a mistake more than twice, we encode the correction once."* |
| **Skills** | *"turn team conventions into loadable steps the agent can invoke"* |
| **Agents** | *"automate checks that previously required a manual pass"* |
| **Commands** | *"chain skills and agents into workflows. They assess complexity, reproduce a bug, plan and implement a fix, create the pull request, and run a multi-stage review."* |
| **Hooks** | *"automated triggers, such as running a linter after every agent turn, checking simulator connectivity before install"* |

Four of the five appear in
[Claude Code Steering Mechanisms](../tools/claude-code-steering-mechanisms.md)'s ten under the
same names — independent convergence on one taxonomy, which is mild evidence the taxonomy is
real rather than one tool's vocabulary.

**The rules definition is the detail worth taking.** That note organises mechanisms by *scope* and
*enforcement* and never says **when** something earns promotion into a rule. Meta supplies a
trigger: *repeats a mistake more than twice*. A countable threshold turns a judgement call into a
rule of thumb, and it bounds the failure mode that note names — the **gravitational pull toward
`CLAUDE.md`**, where everything gets encoded because nothing says what shouldn't be.

## What the piece does not cover

- **Its own self-assessment is unreadable.** The *"What Worked, and What Did Not"* comparison is
  published **as images only**; the lists do not appear in the text. The most valuable section of
  the post is the one that cannot be read or quoted.
- **No numbers.** No team size, no code-authorship fraction, no figures on the memory result. For
  a post whose headline is eight weeks to feature parity, that is the whole claim resting on one
  duration.
- **Greenfield, and that is the condition that does not generalise.** Eight weeks to *core feature
  parity* on a new app is the easiest available setting.
  [Brownfield Agentic Engineering](../engineering/ai-native/brownfield-agentic-engineering.md)
  holds the counterweight — **28 of 520** agent migration runs passing a full audit — and this
  piece does not claim otherwise, but neither does it say so.
- **The autonomy boundary is named and then left blank.** *"Some stages run autonomously today,
  while others still keep an engineer in each iteration"* — **which stages is never stated**, and
  that is precisely the useful detail. Every other account here is similarly vague about it.
- **Nothing on cost**, supervision time, or what *watching the run* actually consumes.
- **No account of the precision burden.** *"Agentic execution requires extreme precision.
  Ambiguity that an engineer might resolve through intuition results in agent failure"* is stated
  as a constraint without saying who pays it — specification work does not vanish because an
  agent is doing the implementation, and the four-abstraction-levels problem in
  [refinement](../product/four-abstraction-levels-of-refinement.md) is where that cost lands.

## Relationship to other notes

- [OpenAI's Agent-First Harness](openai-agent-first-harness.md) — the closest sibling and the
  better-instrumented one. Both organise around agent legibility and mechanically-enforced
  constraints; OpenAI reports volume, Meta reports an operating model.
- [Agentic Code Review](../engineering/ai-native/agentic-code-review.md) — where
  human-on-the-loop was already named; this supplies the definition.
- [Activity Metrics Under AI](../engineering/ai-native/activity-metrics-obsolete.md) — six
  diagnostics and no definition of done; "verified, production-ready outcomes" is one.
- [DORA on AI](../engineering/ai-native/dora-ai-capabilities.md) — Harvey proposes discarding code
  review; Meta writes *survive review* into its success metric, and supplies the
  builder-experience mechanism he left unspecified.
- [Feature Flags and Branch by Abstraction](../engineering/practices/feature-flags-and-branch-by-abstraction.md)
  and [Skeleton Architecture](../engineering/architecture/skeleton-architecture.md) — gating code
  at runtime versus compiling it out; the second is the harder guarantee and the same
  structural-not-advisory principle.
- [Slack's Agentic E2E Testing Experiment](slack-agentic-e2e-testing.md) and
  [Agentic Verification](../engineering/ai-native/agentic-verification.md) — navigation agents in
  production, with spatial disorientation as the cost of E2E-as-ground-truth.
- [Claude Code Steering Mechanisms](../tools/claude-code-steering-mechanisms.md) — the same
  five-of-ten taxonomy, plus the promotion trigger it lacks.
