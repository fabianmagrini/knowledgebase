---
title: Loop-Driven Development
tags: [ai-engineering, testing, ci-cd, reading, agentic-workflows]
topic: engineering/practices
status: notes
level: intermediate
related:
  - engineering/practices/agent-backpressure-loops.md
  - engineering/practices/harness-engineering.md
  - engineering/practices/eval-driven-ai-development.md
  - engineering/practices/agentic-sdlc.md
  - engineering/practices/test-coverage-policy.md
  - engineering/practices/ai-native-engineering-stack.md
  - engineering/practices/change-absorption-capacity.md
  - engineering/practices/prompt-engineering-for-programmers.md
  - standards/open-knowledge-format.md
  - engineering/practices/spec-driven-development.md
source:
  - "https://generativeprogrammer.com/p/from-test-driven-to-loop-driven-development"
  - "https://addyo.substack.com/p/loop-engineering"
updated: 2026-06-20
---

# Loop-Driven Development

Software engineering has always run as a feedback loop. Test-driven development made that loop
explicit at the unit level (write a failing test → make it pass → refactor). The argument here is
that AI agents extend the same loop to larger work units — tasks, pull requests, migrations —
giving **loop-driven development**. It differs from TDD in *scale and scope*, not principle: the
engineer's job becomes designing the loop around the agent rather than writing the code inside it.

## The five-component loop

A loop wraps a unit of work with:

| Component | Role |
|---|---|
| **Trigger** | What starts the loop — a human, a schedule, or an event |
| **Goal** | The desired end state |
| **Harness** | The agent's environment (tools, sandbox, context) |
| **Verifier** | The check that decides whether to continue or stop |
| **State** | Persistent memory across iterations |

## The engineering leverage stack

The article frames five additive eras: each layer keeps the capabilities of the ones below and
adds a new control surface. The leverage point migrates *upward* over time.

| Era | Period | Adds | Limitation it exposes |
|---|---|---|---|
| **Autocomplete** | 2021–2022 | Accept/reject inline suggestions | Narrow scope |
| **Prompt engineering** | 2022–2023 | Reason–act–observe cycles (ReAct), tools, goals | Drift and convergence |
| **Context engineering** | 2024–2025 | Repo context, files, tests, logs, conventions | Context without correctness |
| **Harness engineering** | 2025–2026 | Sandbox, verifier, CI, evals, review gates | (the checkable environment) |
| **Loop engineering** | now | Orchestration: worktrees, skills/playbooks, MCP, durable memory | Needs escalation safeguards |

The harness layer is the subject of [Harness Engineering](harness-engineering.md); loop
engineering wraps harnesses with recurring, decision-based orchestration.

> "The point of a harness is not to make the model magically correct. The point is to make the
> work observable, constrained, and checkable."

## Loop engineering: the anatomy of a loop

Loop engineering (era 5) is where the engineer stops prompting the agent turn-by-turn and instead
designs the system that prompts it — "you design the system that does it instead" (Addy Osmani). A
loop is a recursive goal: define a purpose and the agent iterates until it is complete. The
leverage moves from prompt engineering to loop architecture — as Boris Cherny puts it, "my job is
to write loops." Because Claude Code and Codex now share the same underlying pieces, the design
transfers across tools: design the loop, not the tool.

A loop is assembled from six parts:

| Component | Role |
|---|---|
| **Automations** | The heartbeat — scheduled discovery/triage. Codex automations route findings to a Triage inbox; Claude Code uses `/loop` (cadence re-runs) and `/goal` (iterate until conditions hold). |
| **Worktrees** | Parallel safety — Git worktrees isolate concurrent agents so they do not collide on the same files. |
| **Skills** | Encoded project knowledge (`SKILL.md` plus optional scripts) so conventions are not re-derived each run — the cure for *intent debt*. |
| **Plugins / connectors** | MCP integrations to real tools (issue trackers, databases, staging, Slack) so the loop acts in the actual environment, not just the filesystem. |
| **Sub-agents** | Separation of maker and checker — a second agent verifies, because "the model that wrote the code is way too nice grading its own homework." |
| **Memory / state file** | The spine — external persistence (Markdown, a Linear board) of what was attempted, passed, and pending. "The agent forgets, the repo doesn't." |

### A loop in practice

A morning automation runs a triage skill over CI failures, issues, and recent commits, and writes
the findings to a state file. For each actionable item it opens an isolated worktree; one
sub-agent drafts a fix and a second reviews it against the project skills and tests; connectors
open the PR and update the ticket; anything unhandled lands in a triage inbox for a human. The next
day's run resumes from the saved state — designed once, operated without continuous prompting.

## The verifier principle

The verifier is what separates a loop from vague iteration: without it you have *repeated
prompting*; with it the loop converges toward the goal. Verifiers can be **deterministic** (tests,
builds, linters) or **probabilistic** (reviewer models). The principle: separate maker from
checker, and run deterministic checks before probabilistic ones. Real-time feedback that makes the
agent self-correct before a human is involved is [backpressure](agent-backpressure-loops.md) — one
form of in-loop verification.

## Why judgement intensifies

- **Safety scales with autonomy.** The more autonomy the loop has, the stronger the checks must
  be. Expanded delegation demands expanded guardrails.
- **Control-point migration.** Engineers trade fine-grained code authorship for system-level
  decisions — choosing goals, designing context, setting permissions, defining checks, assessing
  acceptable risk.
- **Skills as infrastructure.** Reliable loops need durable playbooks and scoped skills, so
  conventions are not rediscovered on every run.

## Anti-patterns

- **Unverified loops** — without a verifier, a loop wastes hours, mutates the repository, and
  produces plausible but problematic work.
- Treating expanded autonomy as a reason to *relax* constraints rather than strengthen them.

## Cautions for the human in the loop

Automating the loop sharpens three problems rather than removing them:

- **Verification burden remains.** "A loop running unattended is also a loop making mistakes
  unattended." Maker/checker separation raises confidence but does not transfer responsibility —
  "done" is a claim, not proof.
- **Comprehension debt.** The faster loops ship, the wider the gap between code that exists and
  code anyone understands — unless developers actively read what is generated. This is the
  understanding-side analogue of [change absorption capacity](change-absorption-capacity.md).
- **Cognitive surrender.** As loops succeed it becomes tempting to stop forming independent
  judgements and simply accept outputs. The same loop accelerates deep work for one engineer and
  replaces thinking for another — "the loop doesn't know the difference. You do."

> Build the loop, but build it "like someone who intends to stay the engineer, not just the person
> who presses go."

## References

The TDD-to-loops framing credits Martin Fowler (TDD), the ReAct paper, and AutoGPT. The
loop-engineering anatomy and cautions draw on Addy Osmani's
[Loop Engineering](https://addyo.substack.com/p/loop-engineering), which in turn cites Peter
Steinberger (stop prompting agents; build loops that prompt them) and Boris Cherny ("my job is to
write loops").

## Relationship to other notes

- [Harness Engineering](harness-engineering.md) — era 4 of the stack: the environment a single
  agent run executes in. This note wraps harnesses in a recurring control loop.
- [Backpressure Loops for Coding Agents](agent-backpressure-loops.md) — by the same author;
  backpressure is the in-loop verification/feedback component of the loop.
- [Eval-Driven Development](eval-driven-ai-development.md) — evals are probabilistic verifiers.
- [The Agentic SDLC](agentic-sdlc.md) — the lifecycle-level cybernetic loop; this is the
  practitioner-tooling articulation of the same idea.
- [Test Coverage Policy](test-coverage-policy.md) — the TDD lineage the loop generalises from.
