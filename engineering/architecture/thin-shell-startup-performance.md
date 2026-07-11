---
type: note
title: Thin-Shell Startup Performance
description: "the performance trade-off of the extracted-runtime model: the startup waterfall, fat-vs-thin shell comparison, platform-core/deferred split, shared-singleton dependencies, prefetch-on-intent, and the critical-path target"
tags: [architecture, system-design, microservices, performance]
topic: engineering/architecture
status: notes
level: intermediate
related:
  - engineering/architecture/thin-shell-platform-runtime.md
  - engineering/architecture/microfrontend-shell-platform.md
  - case-studies/linear-performance-architecture.md
  - case-studies/chatgpt-web-performance.md
  - engineering/practices/performance-testing-strategy.md
updated: 2026-06-22
---

# Thin-Shell Startup Performance

The [thin shell + platform runtime remote](thin-shell-platform-runtime.md) model
performs well *if the platform runtime is treated like a performance-critical
kernel*. Its defining risk is that extracting the runtime adds an extra critical
dependency to the startup path, turning first render into a **waterfall**:

```txt
index.html
  → shell bundle
    → remote manifest
      → platform runtime remote
        → platform init
          → layout render
            → active MFE remote
```

The platform runtime sits on the **critical rendering path**: the user cannot see
the real app frame until it loads (`shell → platform runtime → layout → MFE`). If
the platform remote is large or slow, the whole app feels slow even when the
product MFE is fast.

## Fat shell vs. thin shell

| | Fat shell (layout + services in shell) | Thin shell + platform remote |
|---|---|---|
| First render | Faster — fewer remote steps | Slower — extra network hop |
| Startup | Simpler, fewer failure points | More steps; platform remote is critical |
| Caching / versioning | Simpler | More complex |
| Releaseability | Shell grows into a frontend monolith | Independent platform deployment, cleaner ownership, reusable runtime |

The thin-shell model trades startup simplicity for deployment independence — so the
startup path has to be engineered deliberately to win the trade.

## The six performance risks

### 1. Startup waterfall

A sequential chain (shell → manifest → platform → config → auth → routes → MFE) is
slow. The shell should **aggressively parallelise** everything that has no hard
ordering dependency:

```txt
load shell
parallel:
  - manifest
  - platform remote
  - runtime config
  - auth / session check
  - active MFE prefetch
```

### 2. Platform runtime bloat

A runtime containing *everything* (auth + nav + layout + telemetry + flags + design
system + HTTP + analytics SDKs) makes first meaningful render slow. Split it into a
small **critical core** and a deferred remainder:

```txt
platform-core (required for first render)   platform-deferred (loaded after start)
- config                                     - analytics SDK
- session                                    - full telemetry
- layout shell                               - help widgets
- routing                                    - experimentation SDK
- nav skeleton                               - complex notification providers
- auth guard
```

### 3. Shared dependency duplication

Module Federation can accidentally load multiple copies of `react`, `react-dom`,
the router, design system, state/date/i18n libraries — hurting load time and
causing runtime bugs. Pin core libraries as strict singletons:

```ts
shared: {
  react: { singleton: true, requiredVersion: "^18.x" },
  "react-dom": { singleton: true, requiredVersion: "^18.x" }
}
```

But don't over-share — a shared dependency is a contract, so reserve it for the
genuinely cross-cutting core.

### 4. Layout delayed by remote loading

If the platform owns layout, users may see a blank screen until it loads. The thin
shell should render an immediate **minimal branded loading frame** (logo, skeleton,
fatal-error fallback, retry), which the platform then replaces with the real
layout.

### 5. MFE load time

Once the platform is ready, the active MFE is another remote load. The platform
should **prefetch on intent**:

```txt
current route MFE: load immediately
primary nav MFEs:  prefetch after idle
next likely route: prefetch on hover
```

### 6. Remote manifest latency

A manifest fetched before anything else is itself critical. Keep it tiny and
strongly cacheable with versioned URLs:

```json
{
  "platform": ".../platform/remoteEntry.js",
  "accounts": ".../accounts/remoteEntry.js"
}
```

## Recommended performance architecture

```txt
Thin Shell          tiny bundle · loading frame · fetch manifest · load platform · prefetch active MFE
Platform Core       layout · routing · session · config · nav shell · error handling
Platform Deferred   analytics SDKs · experimentation · help widgets · non-critical notifications
Product MFEs        route-level chunks · lazy page modules · product-specific state
```

## Critical-path target

First render should progressively reveal real content:

```txt
HTML → shell skeleton → platform layout → active MFE content
```

not a chain of empty states (`blank → spinner → spinner → spinner → app`).

## Three rules

1. **The shell must render an immediate skeleton.**
2. **The platform runtime must have a tiny critical core.**
3. **MFEs must be prefetched based on route and navigation intent.**

The biggest mistake is letting `app-platform-runtime` become a large remote bundle
that blocks everything.

## Relationship to other notes

- [Thin Shell + Platform Runtime Remote](thin-shell-platform-runtime.md) — the
  model this analyses; its release-cadence benefit is paid for with the startup
  cost engineered away here.
- [The Micro-Frontend Shell as Platform Runtime](microfrontend-shell-platform.md) —
  the fat-shell alternative whose faster first render is the baseline compared
  against above.
- [Linear's Performance Architecture](../../case-studies/linear-performance-architecture.md)
  — the same techniques at the single-app level: render-first skeletons,
  prefetching, code-splitting, and keeping the critical path tiny.
- [Performance Testing Strategy](../practices/performance-testing-strategy.md) —
  how to *measure* whether these critical-path targets are actually met.
