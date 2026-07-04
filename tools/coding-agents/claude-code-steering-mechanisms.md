---
title: Claude Code Steering Mechanisms
tags: [ai-engineering, agentic-workflows, reading]
topic: tools/coding-agents
status: notes
level: intermediate
related:
  - engineering/practices/harness-engineering.md
  - engineering/practices/prompt-engineering-for-programmers.md
  - engineering/practices/cress-context-engineering.md
  - engineering/practices/ai-native-engineering-stack.md
source: "https://generativeprogrammer.com/p/10-claude-code-steering-mechanisms"
updated: 2026-07-05
---

# Claude Code Steering Mechanisms

Bilgin Ibryam (*The Generative Programmer*) reframes configuring Claude Code from "how do I
write good instructions?" to "**where should this instruction live** so it's visible when
needed, cheap when not, and enforced when it must be?" The failure mode he names is the
**gravitational pull toward `CLAUDE.md`** — cramming facts, procedures, boundaries, style,
and triggers into one file, turning it into a **mixed control plane** that bloats context and
behaves unreliably.

Although the mechanisms are Claude Code-specific, the organising principle generalises to any
agent [harness](../../engineering/practices/harness-engineering.md): **scope controls cost,
enforcement controls reliability.**

## Two dimensions

- **Scope** — how widely the instruction applies (this file / this path / this task / the
  whole session). Narrow scope means it loads only when relevant, saving context.
- **Enforcement** — whether it is *guidance* the model may forget, or a *hard boundary*
  enforced outside the model that cannot be negotiated away.

## The ten mechanisms

| # | Mechanism | What it is | Reach for it when |
|---|---|---|---|
| 1 | **`CLAUDE.md`** (project memory index) | Broadly useful repo facts: build/test commands, structure, conventions | Stable facts needed across many tasks — an index, not a manual |
| 2 | **Rules** (path-scoped) | Conventions under `.claude/rules/` with optional `paths`, loaded only near matching files | Monorepos / mixed stacks where different code needs different guidance |
| 3 | **Skills** (just-in-time procedures) | Reusable workflows whose body loads only on invocation; the description is the routing signal | Rarely-used procedures (release notes, incident analysis) you don't want costing context every turn |
| 4 | **Slash commands / manual skills** | Human-triggered workflows; `disable-model-invocation: true` stops auto-selection | Side-effecting ops (commit, deploy, migrate) where timing and human judgement matter |
| 5 | **Subagents** (isolated investigator) | Separate agent with its own prompt, tools, model, permissions; returns a focused result, not its transcript | Noisy work (broad search, log/security audit) that shouldn't flood the main thread |
| 6 | **Output styles** (session posture) | Modify the system prompt to set persistent role/tone/shape | Personas — architecture reviewer, terse implementer, teacher — where style, not correctness, is the point |
| 7 | **`--append-system-prompt`** (one-run overlay) | Temporary framing for a single invocation, no saved state | Scripts, CI jobs, one-off framing that shouldn't become permanent repo state |
| 8 | **MCP servers** (live capability boundary) | Controlled access to external systems (GitHub, Jira, DBs, observability) | Static context is stale or an *action* is required; keep `alwaysLoad` tools minimal |
| 9 | **Hooks** (event gate) | Code that runs mechanically at lifecycle events (`PreToolUse`, `PostToolUse`, session start, pre-compaction) | "Always do X when Y happens" — block/validate before a tool call, or format/log after |
| 10 | **Permissions** (hard boundary) | `allow`/`ask`/`deny` lists for tools, files, commands, domains, skills, enforced outside the model | Where "never" must truly hold — a denied action can't be talked back into |

## Choosing among them

The author's decision tree starts with one question:

**"Must this be guaranteed?"**

- **Yes** → a hard mechanism: **permissions** (allow/ask/deny) or **hooks** (block/validate).
- **No** → route by what you're steering:
  - **Work** → skill, slash command, or subagent
  - **Context** → `CLAUDE.md` or a rule
  - **Voice** → output style or appended prompt
  - **External capability** → MCP server

## Practices

- **Don't repeat an instruction across mechanisms.** "Never edit production migrations" belongs
  in permissions or a hook as a hard boundary — not as `CLAUDE.md` prose the model might forget.
- **Load context strategically.** Path-scoped rules, nested `CLAUDE.md` files, and skill bodies
  return only when relevant; keep `alwaysLoad` MCP tools sparse.
- **Match mechanism to consequence.** Prose *guides* reasoning; schemas, tests, and hooks
  *enforce* correctness. Style guidance (output style) is not an operational boundary
  (permissions).
- **Write skill descriptions as routing signals** — "Create release notes from the current git
  diff and recent commits," not a generic title — so the agent knows when to invoke them.

## Relationship to other notes

- **[Harness Engineering](../../engineering/practices/harness-engineering.md)** — describes the
  harness *program* (Claude Code as an example) from the inside: its loop, tools, and patterns
  like progressive disclosure and skills. This note is the **user-facing** counterpart: how to
  *steer* that harness from outside.
- **[Prompt Engineering for Programmers](../../engineering/practices/prompt-engineering-for-programmers.md)**
  — about *writing* the prompt; this is about *where the instruction is placed* operationally.
- **[The AI-Native Engineering Stack](../../engineering/practices/ai-native-engineering-stack.md)**
  — these mechanisms are the concrete configuration surface of a coding agent within that stack.
