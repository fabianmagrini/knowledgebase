---
type: index
title: Reading
description: "Notes and summaries from books, papers, and articles."
tags: [meta, reading]
status: complete
updated: 2026-06-13
---

# Reading

Notes and summaries from books, papers, and articles.

## Format

Each note should include:
- **Source** — title, author, URL or ISBN
- **Key takeaways** — bullet points
- **Notes** — deeper thoughts or quotes

## Articles

### Code Review

- [How to Review Code](https://dev.to/akdevcraft/how-to-review-code-2gam) — AKDevCraft
- [10 Tips for Better Code Reviews](https://medium.com/@domen.lanisnik/10-tips-for-better-code-reviews-6eb2fff2a85f) — Domen Lanišnik
- [Make Code Reviews Work](https://polarsquad.com/blog/make-code-reviews-work) — Polar Squad
- [Code Review Best Practices](https://www.michaelagreiler.com/code-review-best-practices/) — Michaela Greiler
- [Best Practices for Peer Code Review](https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/) — SmartBear
- [Code Review Best Practices](https://www.qodo.ai/blog/code-review-best-practices/) — Qodo
- [Common Code Review Mistakes to Avoid](https://graphite.dev/guides/common-code-review-mistakes-to-avoid) — Graphite
- [Code Review Techniques](https://www.awesomecodereviews.com/code-reading/code-review-techniques/) — Awesome Code Reviews
- [Common Code Review Mistakes Developers Make](https://axolo.co/blog/p/common-code-review-mistakes-developers-make) — Axolo

### Architecture & Performance

- [How is Linear so fast? A technical breakdown](https://performance.dev/how-is-linear-so-fast-a-technical-breakdown) — performance.dev → see case study: [Linear's Performance Architecture](../case-studies/linear-performance-architecture.md)
- [Reverse Engineering ChatGPT Web](https://performance.dev/chatgpt) — Dennis Brotzky (performance.dev) → see case study: [ChatGPT's Web Performance Architecture](../case-studies/chatgpt-web-performance.md)
- [Building App-like Experiences with Next.js 16.3](https://nextjs.org/blog/building-app-like-experiences-with-nextjs-16-3) — Aurora Scharff (Next.js blog) — a feature tour across four demo apps: Cache Components, Partial Prefetching, `'use cache'`/`cacheTag`/`updateTag`, optimistic updates, View Transitions, client-cache hydration. No note: the same 16.3 release is already covered from a better angle in [Vercel's Agent Loop for Instant Navigations](../case-studies/vercel-v0-instant-navigations.md), which holds the App Shell mechanics, Suspense-boundary placement and the `instant()` helper *and* extracts an argument (frameworks can ship verifiers; primitives cannot); the rest here is API surface that will date, and `useOffline` is flagged experimental and not recommended for production. Two things worth remembering: **nest Suspense boundaries rather than making them siblings** — siblings resolve independently and "can push each other around as they land", while a nested boundary waits for the one above it, so the page settles top-down with the work still running in parallel (the reveal is serialised, not the fetching); and the demo apps are open source — **Huddle ships in equivalent TanStack Query and SWR variants**, a rare side-by-side of the same app under two client-cache libraries

### Domain Engineering

- [Fintech Engineering Handbook](https://w.pitula.me/fintech-engineering-handbook/) — Voytek Pituła → notes: [Fintech Engineering Handbook](fintech-engineering-handbook.md)

### AI Engineering

- [Agentic AI in the Software Development Lifecycle](https://arxiv.org/abs/2604.26275) — Happy Bhati (arXiv 2604.26275) → notes: [Agentic AI in the SDLC — A Research Survey](agentic-sdlc-survey.md)
- [Building Effective AI Agents: Architecture Patterns and Implementation Frameworks](https://resources.anthropic.com/hubfs/Building%20Effective%20AI%20Agents-%20Architecture%20Patterns%20and%20Implementation%20Frameworks.pdf) — Anthropic → notes: [Building Effective Agents — Workflow & Agent Patterns](building-effective-agents.md)
- [Multi-Agent Coding Without Worktree Chaos](https://davidwells.io/blog/multi-agent-coding-without-worktree-chaos) — David Wells → notes: [Multi-Agent Coding Without Worktree Chaos](multi-agent-coding-coordination.md)
- [How I use LLMs as a Staff Engineer in 2026](https://www.seangoedecke.com/how-i-use-llms-in-2026/) — Sean Goedecke → notes: [How I Use LLMs as a Staff Engineer (2026)](how-i-use-llms-2026.md)
- [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — Andrej Karpathy → notes: [The LLM-Maintained Wiki](llm-maintained-wiki.md)
- [We are now factory engineers, not product engineers](https://www.warp.dev/blog/we-are-now-factory-engineers-not-product-engineers) — Warp → notes: [Factory Engineers, Not Product Engineers](factory-engineers.md)
- [Adapting to AI: What Is Software Engineering?](https://blog.colinbreck.com/adapting-to-ai-what-is-software-engineering/) — Colin Breck → notes: [What Is Software Engineering? (Adapting to AI)](what-is-software-engineering-ai.md)
- [The New SDLC With Vibe Coding](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding) — Addy Osmani, Shubham Saboo & Sokratis Kartakis (Kaggle) → notes: [The New SDLC with Vibe Coding](new-sdlc-vibe-coding.md)
- [Building Software Is Learning](https://registerspill.thorstenball.com/p/building-software-is-learning) — Thorsten Ball → notes: [Building Software Is Learning](building-software-is-learning.md)
- [Agentic AI Architecture](https://www.infoq.com/minibooks/agentic-ai-architecture/) — InfoQ eMag (ed. Rafał Gancarz) → notes: [Agentic AI Architecture (InfoQ eMag)](agentic-ai-architecture-emag.md) — signpost
- [Are we offloading too much of our thinking to AI?](https://www.artfish.ai/p/offloading-thinking-to-ai) — Yennie Jun → notes: [Offloading Thinking to AI](offloading-thinking-to-ai.md) — personal essay; the counterweight to the delegation notes
- [Five studies that are changing how we think about AI in software engineering](https://newsletter.getdx.com/p/five-studies-that-are-changing-how) — Brian Houck → notes: [Five Studies on AI and Software Engineering Productivity](ai-productivity-research.md) — signpost to five peer-reviewed studies; the measurement layer under the AI-native cluster
- [Human Judgment Doesn't Leave the Software Factory. It Relocates.](https://addyo.substack.com/p/human-judgment-doesnt-leave-the-software) — Addy Osmani — place humans upstream at intent and design plus at critical gates, rather than counting on removing them. No note: the thesis is already held almost verbatim in [Agentic Code Review](../engineering/ai-native/agentic-code-review.md) ("the human does not leave; the human moves up a loop") and [Own the Outer Loop](../engineering/ai-native/own-the-outer-loop.md), and the placement argument is in [Light and Dark Software Factories](../engineering/ai-native/light-and-dark-factories.md). Carries sponsored content. Three operational details worth remembering: a **run-status taxonomy** (success / flawed / blocked / manual, only success ships, with timing per status), **issue labels used as queues and locks** for agent triage, and the observation that a factory reading GitHub issues or Slack as its work queue is **reading attacker-controllable text** and needs sandboxing — an intake-side injection surface neither [Securing AI Agent Skills](../engineering/security/agent-skill-security.md) nor the code-review notes currently cover
- [Practical Loop Engineering](https://addyo.substack.com/p/practical-loop-engineering) — Addy Osmani — delegating tasks to agents via measurable stopping conditions while keeping judgement; four loop types (manual, goal-based, time-based, proactive) and the Goal-vs-Loop primitives. No note: stopping conditions are already the execution contract in [Agentic Autonomy Levels](../engineering/ai-native/agentic-autonomy-levels.md) and "completion criteria written before execution" in [Long-Running Agents](../engineering/ai-native/long-running-agents.md); the term *loop engineering* is already attributed to him in [Light and Dark Software Factories](../engineering/ai-native/light-and-dark-factories.md); the rest is Claude Code product surface that will date. Two things worth remembering from it: **brownfield codebases need stricter oversight than greenfield**, and an infinite-loop tell is **the same command repeated three times without change**
- [Agentic Code Quality](https://addyo.substack.com/p/agentic-code-quality) — Addy Osmani — quality as constraints set around agents rather than a final review; the scaling trilemma (scale verification, cut velocity, or lower the bar). No note: the argument is covered in more depth by [Backpressure Loops](../engineering/ai-native/agent-backpressure-loops.md), [CI/CD as the Control Plane](../engineering/ai-native/ci-cd-ai-engineering.md) and [Agentic Code Review](../engineering/ai-native/agentic-code-review.md)
- [The Anatomy of an Agent Harness](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness) — Vivek Trivedy (LangChain) — "Agent = Model + Harness", derived working-backwards from desired behaviour: filesystems, sandboxes, memory, context management, planning, self-verification. No note: covered across [Harness Engineering](../engineering/ai-native/harness-engineering.md), [Long-Running Agents](../engineering/ai-native/long-running-agents.md) and [CRESS](../engineering/ai-native/cress-context-engineering.md). Its one unheld idea is **harness–model co-evolution** — models overfitting to specific harness tool logic, which would make "own the harness, rent the model" harder over time
- [Kafka App? There's a Skill for That](https://www.etsy.com/codeascraft/kafka-app-thereas-a-skill-for-that) — Etsy Code as Craft — agent Skills as reusable playbooks for a specific domain, invoked by slash command (`/new-streaming-feature`), with the agent generating code, validating configs and opening PRs. No note: **etsy.com blocks automated retrieval**, so this was never read in full — worth revisiting if the text becomes available, as the production-skills gap it would fill is otherwise covered only by [Stripe's Kai platform](../case-studies/stripe-kai-agent-platform.md)
- [GAN-Inspired Multi-Agent Harnesses for Long-Running Autonomous Software Engineering](https://medium.com/@gwrx2005/gan-inspired-multi-agent-harnesses-for-long-running-autonomous-software-engineering-architecture-37a8c2d59b6b) — Jung-Hua Liu — an academic-style formalisation of Anthropic's harness-design work into a Decomposer–Executor–Verifier abstraction (GADC) with a harness-complexity curve. No note: all empirical grounding is Anthropic's, captured directly in [Harness Design for Long-Running App Development](../engineering/ai-native/harness-design-experiments.md); the formalisation adds vocabulary rather than evidence

### Engineering Craft & Culture

- [Ownership](https://registerspill.thorstenball.com/p/ownership) — Thorsten Ball → notes: [Ownership (Thorsten Ball)](ownership-thorsten-ball.md)
