---
type: note
title: Rust for Agentic Development
description: "Niko Matsakis's argument that strong static constraints suit agentic development — and the inversion worth keeping: a proof obligation lets you grant an agent more freedom, not less, because 'do whatever you want, as long as you can prove the result' is only sayable when a machine can check the proof."
tags: [ai-engineering, agentic-workflows, system-design, testing, reading]
topic: languages-and-frameworks
status: notes
level: advanced
related:
  - languages-and-frameworks/go-agentic-language.md
  - case-studies/github-copilot-rust-migration.md
  - engineering/ai-native/agentic-verification.md
  - engineering/ai-native/agentic-autonomy-levels.md
  - engineering/ai-native/spec-driven-development.md
  - engineering/ai-native/agent-backpressure-loops.md
  - engineering/architecture/skeleton-architecture.md
  - engineering/ai-native/accountability-for-unread-code.md
source: "https://smallcultfollowing.com/babysteps/blog/2026/10/14/agentic-dev-and-rust/"
updated: 2026-10-18
---

# Rust for Agentic Development

Niko Matsakis (October 2026), a Rust language team lead, written as a companion to talks at
REBASE (SPLASH) and IWACO. The question behind it is existential for his field — whether
language design still matters when models write the code — and his answer is that it matters
more, because the constraints a language can express are what make agent output trustworthy.

He splits the "software factory" into three parts:

> *Design:* figure out and specify clearly what the code is supposed to do. *Construction:*
> author code that does what it is supposed to do. *Optimization:* optimize the code so that it
> runs efficiently.

His claim is that agents are already strong at **construction** and **optimisation** — *"agents
are really good at fine-tuning the performance of existing code"*, especially driven by a
profiler — and that **design** is the open frontier, where he is candid that Rust's role is
unclear. He cites Marc Brooker's *what's easy now, what's hard now* framing: tasks that were
hard because they were fiddly (a cryptographic implementation) automate, and the work that
gains value is the work that was never fiddly in the first place.

> **Provenance.** A position piece from the person who designs the language, arguing the language
> is well-positioned — self-interested in the benign way, but worth stating. More limiting:
> **there is no evidence of any kind in it** — no benchmark, no experiment, not one example of an
> agent working on Rust code. The proof tooling it rests on is research-grade. Read it as an
> argument about what to build, from someone with standing to build it, not as a finding.

## Types stop the agent doing wrong things; they do not say the right thing was done

The core reliability argument rests on Dijkstra (1970) — *"Testing can show the presence of bugs,
but not their absence"* — which turns out to be uncited anywhere else in these notes despite
being load-bearing for the entire verification cluster. Agent-written tests inherit the agent's
own misunderstanding of the problem, so a type system that rules out whole categories of bug
catches things no test the agent writes ever would.

Then the concession that makes the piece useful: **type systems are not enough.** They prevent
wrong actions, they do not establish that the right thing happened.

That is precisely where [the Copilot Rust migration](../case-studies/github-copilot-rust-migration.md)
arrived from the opposite direction, with measurement rather than argument. Ownership, borrowing
and lifetime errors were **1.7%** of coded diagnostics; four mechanical families (name
resolution, missing methods, type mismatches, trait bounds) were 84%; and the dozens of
regressions were **semantic, not type errors**. That note concluded a type system is a tight
feedback loop for an agent, not a correctness guarantee. Matsakis agrees with the diagnosis and
supplies the step past it, which the repo did not hold.

## Proof as the licence for autonomy

The best idea in the piece, and it inverts how constraint is framed nearly everywhere else in
these notes. Gates, backpressure, skeletons and enforced architecture rules all treat constraint
as a **brake** — making bad agent output hard to accept. Matsakis points out that a constraint
strong enough to be *checked* is also a constraint strong enough to let you stop supervising:

> This means that you can basically tell the agent "do whatever you want, as long as you can
> prove that the code still computes the correct result". These proofs can be done with theorem
> provers like Lean or Rocq.

So the stronger constraint buys **more** agent freedom, not less — his example is cryptographic
code, where aggressive optimisation is exactly the work you would never let an agent do
unsupervised, and a proof obligation is what makes it safe to. The Rust-ecosystem tools he names
are **Verus, Creusot, Aeneas and Kani**, with Lean and Rocq underneath.

This is the same move as the [execution contract](../engineering/ai-native/agentic-autonomy-levels.md)
— bound the tools, permissions and budget, then let the agent run inside the bound — except the
bound is a machine-checkable property of the output rather than a policy about the process. And
it is the strongest available answer to the oracle problem in
[Agentic Verification](../engineering/ai-native/agentic-verification.md): E2E tests, property
tests and differential tests are all *better* oracles, but a proof is a different kind of thing
from an oracle. It does not sample behaviour, so there is no sampling to be wrong about.

His north star for the language follows directly:

> A north star for Rust: **no more unsafe code**. By that, I don't mean that we never use the
> `unsafe` *keyword*. Rather, I mean that we have the power to prove that all the unsafe code we
> write is correct and cannot cause undefined behavior.

Worth setting against the Copilot migration's `unsafe` accounting — **158 blocks across 36
files, 100% at external boundaries, zero known regressions involving `unsafe`**. That project
reached safety by *inventorying and bounding* unsafe code, which is the discipline available
today; Matsakis is proposing to reach it by proving the blocks correct instead.

## "Markdown-driven development"

His name for the current state of the design layer, and an unflattering one:

> variations on "markdown-driven-development", developing docs and hoping that agents pay
> attention

That is a precise label for a practice this knowledge base documents extensively and has no
critical name for — AGENTS.md conventions, [spec-driven development](../engineering/ai-native/spec-driven-development.md),
CRESS context engineering, skills files. The sting is in *hoping*: prose has no enforcement
mechanism, which is the same objection [skeleton architecture](../engineering/architecture/skeleton-architecture.md)
makes when it argues guardrails must be physically difficult to bypass rather than advisory, and
the same distinction as **gate vs rule** in
[backpressure loops](../engineering/ai-native/agent-backpressure-loops.md).

What he wants instead is a **design language** — a higher-level way to state architecture and
invariants that agents translate down into Rust. Note where this lands relative to
`spec-driven-development`: that note's formality spectrum already runs informal prose →
structured keywords (RFC 2119, EARS) → machine-checkable (TLA+, Lean), and argues to raise
precision only where it matters. Matsakis is making the same ladder argument from the language
designer's end, and pushing for the top rung to become ordinary rather than exceptional. He
offers no concrete design for it.

His two tooling asks are narrower and more actionable:

- **An extensible compiler.** Proof tools currently bolt on through macros and require pinned
  compiler versions, which keeps them out of normal workflows.
- **Separating interface from implementation** — *"having ways to separate out interface from
  implementation so that it's easier to review the interface in isolation or to see when the
  agent made changes there."* This is a review-economics argument: if humans are
  [looking at agent-generated code only rarely](../engineering/ai-native/accountability-for-unread-code.md),
  the language should make the part that still warrants reading separable from the part that
  does not.

## The fork with Go, which neither author states

[Go as an Agentic Language](go-agentic-language.md) and this piece are both language advocacy
for agentic development, and they disagree about what matters most in an agent loop — without
engaging each other.

| | The claim | What it optimises |
|---|---|---|
| **Francia / the Go team** | *"Multi-minute Rust/C++ builds waste every loop iteration"* — build time is the first weakness Go is credited with avoiding, alongside low distractor density and context efficiency | **Iteration speed**: more loops per hour, cheaper loops |
| **Matsakis** | *"agents will let data races and subtle bugs slip through that Rust would have prevented"* | **Constraint strength**: fewer loops needed, and what survives them is sounder |

Each names the other language's weakness and ignores the weakness named of its own.
**Compile time, build time, iteration speed and the learning curve are entirely absent from
Matsakis's post** — in a piece about agentic fit, the competing argument's lead objection goes
unaddressed. Francia, symmetrically, treats compile-enforced types as the strong form of static
checking and never considers proofs.

The honest reading is that the two arguments apply to different work rather than competing. Loop
frequency dominates when the bottleneck is how many attempts you can afford — exploratory work,
large mechanical migrations, anything where the agent is searching. Constraint strength dominates
when a single wrong answer is expensive and no test you can write would catch it — concurrency,
cryptography, memory-unsafe boundaries. The Copilot migration is a useful check here, because it
was both: Rust's compiler ran as a **fast mechanical oracle** at enormous volume *and* 96%
prompt-cache hit rates were named as what made the economics work. Iteration cost mattered; it
just was not the compiler that dominated it.

## What the piece does not cover

- **No evidence.** No benchmark, no experiment, no case example of an agent working on Rust.
- **No concession on compile times or the learning curve** — Rust's two standard objections,
  and the first is the competing argument's opening move.
- **No evidence agents can drive the proof tools.** Verus, Creusot, Aeneas and Kani are
  research-grade; his own extensibility complaint is that they need pinned compiler versions.
  Whether a model can usefully discharge a proof obligation — the thing the entire autonomy
  argument depends on — is not examined.
- **No concrete design language**, only the case that one is needed.
- **Nothing on cost.** Proof search is expensive in a way type checking is not, and the
  economics of running it inside an agent loop go unmentioned.

## Relationship to other notes

- [Go as an Agentic Language](go-agentic-language.md) — the opposing bet on what an agent loop
  needs, set out above. Read the two together; neither author read the other.
- [Migrating the Copilot Runtime to Rust With Agents](../case-studies/github-copilot-rust-migration.md)
  — the measurement this argues past. Its 1.7% borrow-checker figure is the evidence that types
  catch mechanical errors and not design errors, which is Matsakis's own premise, arrived at
  empirically.
- [Agentic Verification](../engineering/ai-native/agentic-verification.md) — three better
  oracles; a proof is a different category, since it does not sample behaviour.
- [Agentic Autonomy Levels](../engineering/ai-native/agentic-autonomy-levels.md) — a proof
  obligation is the execution contract expressed as a checkable property of the output rather
  than a policy about the process.
- [Spec-Driven Development](../engineering/ai-native/spec-driven-development.md) — the same
  formality ladder (prose → structured → Lean/TLA+) seen from the language-design end, with the
  argument that the top rung should become ordinary.
- [Backpressure Loops for Coding Agents](../engineering/ai-native/agent-backpressure-loops.md) —
  gate vs rule; "markdown-driven development" is the rule case, and proof is the strongest
  available gate.
- [Skeleton Architecture](../engineering/architecture/skeleton-architecture.md) — guardrails that
  are hard to bypass rather than advisory, which is the same objection to docs-and-hope.
- [Accountability for Unread Code](../engineering/ai-native/accountability-for-unread-code.md) —
  humans *"focused more on code comprehension"* and reading agent output *"only rarely"* is the
  premise behind the interface/implementation separation ask.
