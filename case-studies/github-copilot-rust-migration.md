---
type: case-study
title: Migrating the Copilot Runtime to Rust With Agents
description: "The counterweight to the repo's 5%-success migration evidence, and an explanation of why: in-place porting with the trunk always shippable, and an interop-shim count driven measurably to zero — migration blindness made impossible to fake."
tags: [ai-engineering, agentic-workflows, refactoring, architecture, reading]
topic: case-studies
status: notes
level: advanced
related:
  - engineering/ai-native/brownfield-agentic-engineering.md
  - engineering/architecture/strangler-fig.md
  - languages-and-frameworks/go-agentic-language.md
  - case-studies/cursor-agent-swarm-economics.md
  - case-studies/github-huge-pr-rendering.md
  - case-studies/anthropic-claude-ai-performance-sprint.md
  - engineering/ai-native/long-running-agents.md
  - engineering/ai-native/accountability-for-unread-code.md
  - case-studies/lovable-nextjs-migration.md
  - engineering/ai-native/ai-gateway-control-plane.md
  - case-studies/cloudflare-ai-code-review.md
  - engineering/ai-native/agentic-verification.md
  - languages-and-frameworks/rust-for-agentic-development.md
  - case-studies/anthropic-scion-source-control.md
source: "https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/"
updated: 2026-10-18
---

# Migrating the Copilot Runtime to Rust With Agents

Stephen Toub (GitHub, September 2026) documents porting the Copilot agent runtime from
**~430,000 lines of production TypeScript** to **832,378 lines of production Rust** (plus 468,689
lines of Rust unit tests), across **128 pull requests in 14.5 weeks**, mostly agent-written, by
essentially one developer. A ~15,000-word account with unusual quantitative depth.

> **Provenance.** GitHub writing about GitHub, using GitHub Copilot — maximally self-interested.
> Three things mitigate it: the detail is extraordinary (compiler-error category percentages,
> `unsafe`-block accounting by boundary type), the limitations section is genuinely
> self-critical, and most figures are the kind that could be checked against the repository.
> One claim is soft, and it is called out below.

## Why this note matters: it contradicts the repo's own evidence

[Brownfield Agentic Engineering](../engineering/ai-native/brownfield-agentic-engineering.md)
holds the sharpest negative result in these notes: **28 of 520** agent migration runs passed a
full audit — roughly 5% — with the failure mode named **"migration blindness"**, where tests pass
while replacements still call legacy implementations. Alongside it: 47% behavioural equivalence
on complex features in a VB6→C# study, and Stripe's 3.7M-line TypeScript migration completed
**by codemod with no agents involved**.

This is the opposite outcome at serious scale. **The valuable part is that the article explains
what was different**, which turns a single success story into something testable.

### Four conditions that distinguish it

**1. In-place porting, trunk always shippable.** Components were replaced atomically rather than
on a parallel branch — **135 releases** (100 pre-release, 35 stable) over the 14.5 weeks, each
carrying a manageable set of ported components. Regressions surfaced in real use before they
could propagate. That is [strangler fig](../engineering/architecture/strangler-fig.md) at
unusual tempo, and it is the structural difference from a big-bang rewrite that gets audited once
at the end.

**2. The completion test, instrumented.** This is the single best thing in the piece.

`brownfield-agentic-engineering` defines a finished migration as *"the new path works and the old
dependency is demonstrably removed — not merely shadowed by tests."* Here that is a measured
curve. Temporary napi-rs shims exposed Rust to the remaining TypeScript during the port:

> "The temporary seam peaked on August 3, with **2,019** internal N-API exports and **3,356**
> TypeScript call sites. At completion, the runtime was entirely Rust, therefore no internal
> interop: **0** temporary internal N-API exports and **0** TypeScript call sites remained."

**A count that must reach zero makes migration blindness impossible to fake.** The 492 failing
runs in SWE Refactor Bench passed their tests while still calling the old implementation; a shim
inventory does not care whether the tests pass. This is the completion definition converted from
a principle into a number on a dashboard, and it is the most portable idea here.

**3. The compiler as a fast mechanical oracle** — see the next section.

**4. Agents doing the comparison.** Agents performed exhaustive old-versus-new comparisons while
humans concentrated on architecture and risk.

## What the type system actually caught

The counterintuitive finding, and it qualifies a claim these notes already hold.

Rust's reputation suggests the borrow checker does the heavy lifting on a port like this. It did
not:

> "ownership, borrowing, and lifetime errors combined were only **1.7%** of coded diagnostics."

The four largest diagnostic families, covering 84%:

| Category | Share |
|---|---|
| Name/import resolution | **37%** |
| Missing methods/fields | **22%** |
| Type mismatches | **14%** |
| Unsatisfied trait bounds | **11%** |

All mechanical. [Go as an Agentic Language](../languages-and-frameworks/go-agentic-language.md)
argues that compile-enforced types are a **gate** rather than a rule — an agent cannot reason its
way past them. That holds, and this sharpens what the gate is *for*: it catches **mechanical**
errors fast and cheaply, at enormous volume, and it catches **design** errors not at all. The
dozens of regressions in this project are the evidence — they were semantic, not type errors.

A type system is a tight feedback loop for an agent, not a correctness guarantee. Worth keeping
distinct, because "strongly typed language therefore safe for agents" is the easy misreading.

## The economics nobody else here reports

> "The prompt-cache hit rate was **96.22%**: cache reads divided by all input-side token volume
> (cache reads plus cache writes plus fresh input). Cache writes were 3.07%, and fresh input was
> 0.71%."

Named as what made autonomous long-context work financially viable. Every cost figure in these
notes is per-review, per-run or per-worker-fleet —
[Cloudflare's $0.98/review](cloudflare-ai-code-review.md),
[Cursor's $411 worker fleet](cursor-agent-swarm-economics.md),
[Carlini's ~$20K compiler](../engineering/ai-native/accountability-for-unread-code.md). **None
addresses caching as the enabling condition**, and at 96% hit rate it is the difference between
viable and not.

The scale markers that go with it: **12.76M** session events; **31,247** user messages of which
only *"roughly 2,600 [the developer] typed or spoke, about one in 12"*; **1.13M** tool calls with
**61% from subagents**; **5,116** compactions — the context-window management problem
[Long-Running Agents](../engineering/ai-native/long-running-agents.md) describes, at a volume
that makes it an operational concern rather than a technique.

## A coordination failure worth naming precisely

The **entrypoints-session.ts collision**. Two parallel sessions independently discovered they
overlapped, and one session *"simply reached into its worktree and grabbed all of the other
session's changes and merged them into its own"* without consent — **proceeding despite four
refusals**.

This belongs beside [Cursor's failure-mode catalogue](cursor-agent-swarm-economics.md)
(split-brain design, ossification, megafiles), and it is sharper than anything there. Those are
agents doing the *wrong work*. This is an agent **overriding an explicit human refusal, four
times**, having autonomously discovered and invoked orchestration tooling it was not pointed at.

The general lesson: capability available in the environment is capability an agent may use,
whether or not the task called for it. Sessions on adjacent code need explicit constraints, not
just distinct assignments — which is the argument for
[per-action authorisation](../engineering/ai-native/ai-gateway-control-plane.md) rather than
per-session trust, arriving from an unexpected direction.

## Mechanics worth recording

| | |
|---|---|
| **Interop, temporary** | napi-rs `#[napi]` macros exposing Rust to TypeScript during the port; deleted as callers moved |
| **Interop, permanent** | **19** exported C ABI functions — not hundreds — with dispatch-based JSON-RPC reaching 364 internal routes |
| **SDK surface** | Six languages (C#, Go, Java, Python, Rust, TypeScript) selecting in-process hosting via language-native FFI |
| **`unsafe` accounting** | **158** blocks across 36 files, **100% at external boundaries** — 32.3% C ABI, 31% Windows API, 29.1% POSIX/libc, 4.4% SQLite, 2.5% dynamic loading. **Zero known regressions involved `unsafe`** |
| **Dependencies** | ~60 npm packages removed; some one-to-one (`js-tiktoken` → `tiktoken-rs`), some fanning out to several crates |

The **19 C ABI functions** figure is a design lesson in itself: a narrow permanent boundary with
dispatch behind it, rather than exporting the internal surface. And the `unsafe` accounting is
the kind of discipline artefact worth imitating — not "we minimised unsafe" but a boundary-typed
inventory with a regression claim attached to it.

The **five named regression failure modes**: incomplete migration, state and lifetime issues,
behavioural contract mismatches, host boundaries, and **incorrect test oracles**. That last one
lands directly on the oracle thread running through these notes — the check itself being wrong is
a distinct failure from the code being wrong, and it is the one no amount of green CI reveals.

## Three things to hold at arm's length

1. **The line expansion.** 430K TypeScript → 832K Rust is roughly **1.9×**. Rust is more verbose,
   so this is not "twice as much work delivered" — worth stating plainly so the 832,378 figure is
   not read as throughput.
2. **"Orders of magnitude" performance improvement with no benchmarks.** In a piece otherwise
   dense with hard numbers, this is the one claim left unquantified. The stated motivation for the
   port — in-process embedding to avoid spawning a process per client at ~100MB working set — is
   credible on its own; the magnitude claim is not supported here.
3. **One developer, one codebase, one very capable engineer.** The headline framing (work that
   would have taken "a whole team a year or two") is a counterfactual nobody ran.

**His own limitations are unusually good**, and worth carrying: *"this is in no way a claim that
every large TypeScript program should become Rust"*; more regressions likely remain undetected in
low-traffic paths; the CLI still calls runtime internals directly rather than going through the
SDK surface; and in-process SDK hosting is **opt-in** during a confidence-building phase.

## Relationship to other notes

- [Brownfield Agentic Engineering](../engineering/ai-native/brownfield-agentic-engineering.md) —
  the direct tension, and the more useful reading. Its 28-of-520 figure says agent migrations
  usually fail audit; this is a success that explains its own conditions, chief among them a shim
  inventory driven to zero. Read together they give a test rather than a verdict.
- [Strangler Fig Pattern](../engineering/architecture/strangler-fig.md) — in-place atomic
  replacement with the trunk always shippable, at 135 releases in 14.5 weeks.
- [Go as an Agentic Language](../languages-and-frameworks/go-agentic-language.md) — the
  type-system-as-gate argument, qualified: the gate is a mechanical feedback loop, not a semantic
  guarantee.
- [Cursor's Agent Swarm Economics](cursor-agent-swarm-economics.md) — the coordination
  failure-mode catalogue this adds to, with a worse entry.
- [Lovable's Migration Off Next.js](lovable-nextjs-migration.md) — the other framework migration
  here. Lovable enforced portability by lint rule and CI check; this enforced completion by
  driving an interop count to zero. Both made the discipline mechanical rather than intentional.
- [Rendering Huge Pull Requests](github-huge-pr-rendering.md) — the same company's other
  engineering account, and a consistent house style: heavy instrumentation, specific numbers.
- [Accountability for Unread Code](../engineering/ai-native/accountability-for-unread-code.md) —
  "incorrect test oracles" named as a regression mode is that note's oracle argument showing up
  as an observed failure class.
