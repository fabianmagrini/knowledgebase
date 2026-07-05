---
title: DoorDash's AI Code Reviewer
tags: [ai-engineering, code-review, agentic-workflows, reading]
topic: case-studies
status: notes
level: intermediate
related:
  - case-studies/cloudflare-ai-code-review.md
  - engineering/ai-native/agentic-code-review.md
  - engineering/practices/code-review-policy.md
  - engineering/ai-native/cress-context-engineering.md
source: "https://careersatdoordash.com/blog/doordash-built-an-ai-code-reviewer-engineers-actually-listen-to/"
updated: 2026-07-05
---

# DoorDash's AI Code Reviewer

DoorDash built an AI code-review agent whose defining bar is **behavioural**, not detection:
not "does it find things," but *"do engineers change their code when it comments, and do teams
keep it enabled?"* At the scale described — 10,000+ pull requests a week across 56 repositories —
the enemy is noise, so the whole system optimises for **precision over recall**.

> The metrics below are DoorDash-reported. The primary source blocks automated fetching; details
> here are drawn from a third-party (ZenML LLMOps) writeup of the article and corroborated by
> search, so treat specifics as second-hand.

## Three-agent architecture: notice, then verify

The current system separates the two things a senior reviewer does:

- **Lead scout** — a *noticing* agent that produces investigation leads without verifying them
  ("this deletion looks suspicious," "this enum case isn't handled in the sibling file," "this
  error path silently swallows failures").
- **Two deep reviewers** — receive the scout's curated leads, drop the false ones, and confirm
  the rest with focused attention rather than exhaustively evaluating every line.

Splitting *noticing* from *verification* is what lets the system go deep on what matters without
spending attention on routine changes.

### How it got there (three versions)

| Version | Design | Why it fell short |
|---|---|---|
| **V1 — specialist fan-out** | Many narrow specialists (security, testing, performance, quality) | Caught mechanical bugs but missed architectural issues — no agent saw the big picture |
| **V2 — parallel general reviewers** | Two general reviewers with full change context | Better on architecture, but attention diffused across too many domains; critical issues got lost |
| **V3 — lead scout + verification** | Scout notices, deep reviewers verify | Mirrors how senior engineers actually review |

## Domain-specific review profiles

Review knowledge is captured as **profiles** — rule sets **dynamically routed by the code
touched** (a payment-service-provider change loads PSP + monetary-security rules; a consumer-feed
PR loads entirely different ones). Profiles are mined from four company-specific sources:

- **AGENTS.md** files (invariants/conventions, excluding setup/build instructions)
- **Historical PR reviews** (what senior engineers flag repeatedly)
- **Slack decisions** ("don't do X" threads, design decisions, post-mortems)
- **Incident history** (patterns that caused outages)

### The false-positive filter

Every candidate rule must survive a three-part cut — drop it if:

1. **CI already catches it**,
2. the **LLM would know it from general training**, or
3. there's **no concrete file-and-line evidence** in the codebase.

What survives is genuinely *DoorDash-specific* review knowledge — the stuff a senior engineer on
that team would catch. This is essentially the [CRESS](../engineering/ai-native/cress-context-engineering.md)
**Empirical** and **Small** principles applied to review context: keep only what's grounded in the
real codebase and not already covered elsewhere.

## Precision over recall

> The single most important decision was refusing to optimise for comprehensive coverage.

Before any comment posts, it survives a **"disprove-it pass"** — the system explicitly tries to
*falsify its own finding*; claims that can't withstand scrutiny are dropped. Posted comments are
anchored to specific lines with **quoted evidence** from the actual code. The disprove-it pass is
the [CRESS](../engineering/ai-native/cress-context-engineering.md) **Refutable** principle turned
into a gate: a finding must be defensible or it doesn't ship. The payoff is trust — low false
positives prevent engineers muting notifications.

## Reported results

| Measure | Value |
|---|---|
| Acceptance on high/critical findings | **60.2%** (up from 46% in the prior system) |
| Acceptance on non-cherry-picked webhook findings | 59.0% |
| Scale | 10,000+ weekly PRs, 56 repositories |
| Cost / time per review | ~$3, ~7 minutes |

## Distinctive vocabulary

**Lead scout** (noticing agent), **disprove-it pass** (self-falsification before posting),
**review profiles** (dynamically-routed domain rule sets), **cross-boundary drift** (one side of
an interface updates but siblings don't), **silent behaviour changes** (same type signature,
different runtime semantics), **soft vs hard timeout** (layered handling of stuck runs).

## Relationship to other notes

- **[Cloudflare's AI Code Review System](cloudflare-ai-code-review.md)** — the sibling case study.
  Both are production multi-agent reviewers optimised against false positives, but via different
  routes: Cloudflare uses 7 specialists + a judge with "What NOT to Flag" negative prompting and
  risk/model tiering; DoorDash uses a scout→verify split, company-mined domain profiles, and a
  disprove-it pass, measuring success by *acceptance rate*.
- **[Agentic Code Review](../engineering/ai-native/agentic-code-review.md)** — the general pattern
  and policy; this is one production realisation.
- **[Code Review Policy](../engineering/practices/code-review-policy.md)** — how AI review fits the
  human review/approval policy.
- **[CRESS Principles for Context Engineering](../engineering/ai-native/cress-context-engineering.md)**
  — the false-positive filter and disprove-it pass are the Empirical/Small/Refutable principles
  applied to review context.
