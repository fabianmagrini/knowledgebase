---
type: case-study
title: Formal Verification at Scale With LLMs
description: "The answer to a question these notes recorded as unanswered eight days earlier — whether a model can actually discharge a proof obligation: 239 entry points across 123 OSS-Fuzz libraries proved crash-free, at roughly 33 lines of Rocq per instruction, with the spec-reality gap visible inside their own experiment."
tags: [testing, security, ai-engineering, agentic-workflows, system-design, reading]
topic: case-studies
status: notes
level: advanced
related:
  - languages-and-frameworks/rust-for-agentic-development.md
  - engineering/ai-native/agentic-verification.md
  - engineering/ai-native/accountability-for-unread-code.md
  - engineering/ai-native/spec-driven-development.md
  - engineering/security/secure-sdlc.md
  - engineering/ai-native/agentic-autonomy-levels.md
  - case-studies/github-copilot-rust-migration.md
  - reading/multi-agent-coding-coordination.md
  - case-studies/cursor-agent-swarm-economics.md
  - case-studies/anthropic-scion-source-control.md
  - engineering/architecture/functional-core-imperative-shell.md
  - case-studies/airbnb-database-workload-replay.md
source: "https://www.anthropic.com/research/formal-verification"
updated: 2026-10-26
---

# Formal Verification at Scale With LLMs

Anthropic with **Theorem** (October 2026), fifteen authors including **Nicholas Carlini** — whose
GCC-as-reference C compiler is already held in
[Accountability for Unread Code](../engineering/ai-native/accountability-for-unread-code.md) —
and Nickolai Zeldovich.

> **Declaring an interest, and then arguing for less scepticism than usual.** Anthropic research
> about Claude's own capability, with a commercial partner, read with Claude. On its face
> maximally self-interested. **But the proofs are machine-checked by Rocq and a subset is
> published**, which is a categorically different epistemic position from every self-reported
> figure elsewhere in these notes. A Rocq-checked proof is accepted by the checker or it is not;
> the claim does not rest on trusting the authors' reading of their own results. What remains
> trusted shrinks to two things: that Rocq is correct, and that the formal semantics describe the
> real machine. The second is where the whole argument actually lives, and the authors say so.

## Why this note exists: it answers a recorded absence

[Rust for Agentic Development](../languages-and-frameworks/rust-for-agentic-development.md) was
added eight days earlier. Matsakis's central idea there is **proof as the licence for autonomy** —
*"do whatever you want, as long as you can prove that the code still computes the correct
result"* — and that note's own limitations section says:

> **No evidence agents can drive the proof tools.** Verus, Creusot, Aeneas and Kani are
> research-grade… Whether a model can usefully discharge a proof obligation — the thing the
> entire autonomy argument depends on — is not examined.

This is that evidence. Separately,
[Accountability for Unread Code](../engineering/ai-native/accountability-for-unread-code.md)
holds that oracle independence must come from outside the generator — *"a spec a person wrote, a
reference implementation, a proof"* — and **a proof was the one of the three with no instance in
these notes.**

## What was proved

> Claude successfully patched the bugs it found and then proved that there are no crashes on any
> input (up to 64 MB) for **239 entry points** across **123 different OSS-Fuzz libraries**

The scale of the artefact: about **180 million lines of Rocq**, with *"a typical proof running to
about 600,000 lines"* against binaries of *"a median length of 18,000 RISC-V instructions."*

**Roughly 33 lines of proof per instruction.** That ratio is the most portable number here,
because the repo has almost nothing on what rigorous verification costs in artefact size. It
belongs beside the one existing figure — SQLite's test suite being **590× larger than its
source** — as the second entry in a very short list. Both say the same thing: the verification
artefact dwarfs the thing verified, and most codebases are nowhere near paying it.

## The bugs, and why they are the argument for proof over fuzzing

Found *during* proof attempts, on libraries that are **already fuzzed** — OSS-Fuzz is Google's
continuous fuzzing programme, so these are not unexamined codebases:

| Bug | What it needed |
|---|---|
| Counter underflow in a decompressor → out-of-bounds write | inputs **around 20 MB** |
| Out-of-bounds read | **64 MB input and over 2 GB memory** |
| **CVE-2026-56132** in libexpat, rediscovered | deeply nested input |
| Logic bug — file restriction not enforced | never crashes at all |

**The shared property is the finding.** Three of the four need inputs a fuzzer is unlikely to
reach by search, and the fourth produces no crash, so no crash-oracle would ever flag it. A proof
quantifies over the input space instead of sampling it, which is precisely the distinction
[Agentic Verification](../engineering/ai-native/agentic-verification.md) draws when it says a
proof is *"a different kind of thing from an oracle. It does not sample behaviour, so there is no
sampling to be wrong about."* This is that claim with four concrete instances attached.

## What the proofs assume — carry this with the headline

The authors are direct, and the scope is narrow:

> [the proofs] assume that the program runs as a single-threaded static binary with a fixed
> memory budget on a RISC-V CPU using Linux OS

So **not** covered: x86 or ARM, dynamic linking against glibc (only static musl), entry points
not tested, dead code, misuse by calling code, and *"issues where the real machine does something
the model doesn't describe."*

That last clause is the **spec-reality gap** named by the people who did the work. A proof is a
conditional: *if* the semantics describe the machine, *then* the property holds. Verification
moves the trust rather than eliminating it — from the code to the model of the machine — and the
honest version of "proved crash-free" is "proved crash-free on a machine we specified, which is
not the machine it runs on."

### The gap appears inside their own experiment

The sharpest illustration is in a second case study rather than in the caveats. Claude wrote a
**Python interpreter in Rust**, proved its adherence to CPython semantics using **Verus**, and
then tested it:

> over **1.7 million** randomly generated Python programs… identical behavior with CPython in
> **99.95%** of tests

**A proof of semantic adherence sitting beside a 0.05% behavioural divergence means the spec did
not capture everything CPython does.** The proof was not wrong; the specification was incomplete.
That is the cleanest available demonstration of what a proof buys and what it does not, and it
is also why the 99.95% figure should not be read as a proof result at all — it is **differential
testing against a reference implementation**, which is
[Agentic Verification](../engineering/ai-native/agentic-verification.md)'s third technique and
[Airbnb's replay rig](airbnb-database-workload-replay.md)'s whole method. The two layers are
complementary: the proof covers the modelled semantics, the differential test catches where the
model and reality diverge.

## The feasibility argument, and the number it is missing

Three findings bear on whether this scales:

- **Proof cost falls with model capability.** On 36 verification tasks, *"Opus 5.5 proves half of
  them with about 40% fewer tokens than Opus 5."* This is the actual feasibility claim — the
  technique is not getting easier, the agent is getting cheaper at it.
- **Proof reuse pays.** With reuse across a shared corpus, *"agents needed 17% fewer tokens than
  when they worked alone."*
- **Shared workspace changed outcomes, not just throughput.** *"Some agents even succeeded after
  previously failing in a solo attempt."* That is a stronger multi-agent result than these notes
  hold anywhere — [Multi-Agent Coding Coordination](../reading/multi-agent-coding-coordination.md)
  and [Cursor's swarm](cursor-agent-swarm-economics.md) both treat coordination as a way to
  parallelise work that a solo agent could eventually do. Shared state making a previously
  impossible task possible is a different claim, and it is the one worth testing further.

**And the absence that matters most: there is no cost, compute or duration figure anywhere.**
*"Feasible at a much larger scale"* is a claim with its denominator missing. 180 million lines of
Rocq was not cheap, and nothing here lets a reader judge whether their own codebase is in range.
Compare [Carlini's compiler](../engineering/ai-native/accountability-for-unread-code.md) at
~**$20K** for ~100K lines of Rust, or the **96.22% prompt-cache hit rate** named in
[the Copilot Rust migration](github-copilot-rust-migration.md) as what made long-context
autonomy viable — both of those at least priced themselves.

## What was released

Proofs *"for fuzz tests that did not require patching"*, the RISC-V and OS semantics, and a
**Claude skill** for verifying your own code via Theorem Labs. Publishing the semantics matters
more than publishing the proofs: the semantics are the trusted component, so releasing them is
what makes the spec-reality gap auditable by someone else.

## What the piece does not cover

- **No cost, compute or wall-clock figures**, as above — the missing half of a feasibility claim.
- **The PDF reader number has no provenance.** *"We found as many security bugs in one week as
  are typically reported in a year"* in *"a widely used PDF reader"* — unnamed product, no
  methodology, no baseline for the annual figure. The most quotable line in the piece and the
  least checkable.
- **No comparison against the cheaper alternatives.** Nothing on what the same effort spent on
  sanitisers, targeted fuzzing, or property-based testing would have found, which is the decision
  an engineering team actually faces.
- **Nothing on maintenance.** A 600,000-line proof is an artefact that breaks when the code
  changes, and proof repair under ordinary development churn is not discussed.
- **Nothing on specification review.** If the semantics are the trusted base, who checks them,
  and how? The authors identify this as the load-bearing assumption and do not say how to
  discharge it.

## Relationship to other notes

- [Rust for Agentic Development](../languages-and-frameworks/rust-for-agentic-development.md) —
  the proposal this answers. Proof as the licence for autonomy, with the "can a model actually do
  it" objection now resolved and the cost objection still open.
- [Agentic Verification](../engineering/ai-native/agentic-verification.md) — a proof does not
  sample behaviour, demonstrated; and the Python experiment is its differential-testing technique
  running *underneath* a proof to catch what the spec missed.
- [Accountability for Unread Code](../engineering/ai-native/accountability-for-unread-code.md) —
  the third oracle-independence source, previously unillustrated. Also the home of the SQLite
  590× figure this sits beside, and of Carlini's compiler.
- [Spec-Driven Development](../engineering/ai-native/spec-driven-development.md) — its formality
  ladder tops out at machine-checkable specs (TLA+, Lean) with the advice to raise precision only
  where it matters. This is the top rung applied at a scale that makes "only where it matters" a
  live question rather than a theoretical one.
- [Functional Core, Imperative Shell](../engineering/architecture/functional-core-imperative-shell.md)
  — the design-side route to provability: pure functions are what proofs are tractable over, and
  the effects at the edge are where the machine model has to be trusted.
- [Secure SDLC](../engineering/security/secure-sdlc.md) — where a CVE rediscovery and
  memory-safety proofs land in delivery practice.
- [Multi-Agent Coding Coordination](../reading/multi-agent-coding-coordination.md) and
  [Cursor's Agent Swarm Economics](cursor-agent-swarm-economics.md) — shared workspace enabling
  previously failed tasks is a stronger coordination claim than either holds.
