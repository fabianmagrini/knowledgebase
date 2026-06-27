---
title: "Your Micro-Frontend Shell Should Be a Platform Runtime, Not a Layout Wrapper"
description: "Build the host shell as an enterprise runtime, extract it into its own remote, and keep startup fast."
date: 2026-06-28
draft: true
---

# Your Micro-Frontend Shell Should Be a Platform Runtime, Not a Layout Wrapper

Most teams that adopt Module Federation start by treating the host shell as a layout wrapper: a header, a sidebar, and a `<div>` where the active micro-frontend (MFE) mounts. That works until the second team ships. Then every remote reinvents auth, every remote wires up its own HTTP client, navigation drifts, and telemetry is a different shape in every product area.

The shell is the wrong place to be minimal. In an enterprise SPA hosting Module Federation MFEs, the shell should be a **platform runtime** — it owns the cross-cutting *enterprise runtime* so each remote can focus on its own domain.

This post walks through three decisions, in order:

1. **What** the runtime should own (and what it shouldn't).
2. **Where** that runtime should live — and why, at scale, you extract it out of the shell entirely.
3. **How** to keep the result fast, because extracting the runtime puts it squarely on the critical rendering path.

---

## Part 1 — The shell as a platform runtime

The shell's job is to provide the services every product area needs, so remotes *consume* them rather than reimplement them. Concretely, that's around eighteen services.

| # | Service | Owns | Notes |
|---|---|---|---|
| 1 | **Routing** | Top-level routing; which MFE mounts for each route | Route registry, lazy remote loading, guards, fallbacks, 404/unauthorized, deep links |
| 2 | **Session / authentication** | The user session | Login/logout orchestration, token refresh, timeout, SSO, secure token handoff to remotes |
| 3 | **Authorization / entitlements** | What the user may see and do | Role/permission lookup, route + menu + action-level checks |
| 4 | **Navigation / menu** | Global navigation | Primary/side nav, breadcrumbs, active state, permission-filtered menus, cross-MFE nav APIs |
| 5 | **Layout** | The application frame | Header, sidebar, footer, content container, skeletons, error boundaries, full-screen mode |
| 6 | **Remote module registry** | Where MFEs live | Remote manifest loading, env-specific URLs, version metadata, health/fallback, canary rollout |
| 7 | **Feature flags** | Flag evaluation | Enable/disable MFEs, experiments, phased rollout, kill switches, cohort targeting |
| 8 | **Configuration** | Runtime config | API base URLs, env metadata, CDN paths, tenant/brand config, telemetry keys |
| 9 | **Event bus / messaging** | Loose shell↔MFE communication | Cross-MFE events, commands, session/navigation events — *use sparingly* |
| 10 | **Notifications** | Toasts, alerts, banners | Outage/maintenance banners, contextual notifications |
| 11 | **Error handling** | Consistent error UX | Global boundary, remote-load-failure handling, forbidden/unauthorized, retry, correlation IDs |
| 12 | **Observability / telemetry** | Standardised instrumentation | Page/route views, remote load times, Core Web Vitals, errors, tracing headers |
| 13 | **API client / platform HTTP** | Shared HTTP abstraction | Auth headers, correlation IDs, retry/timeout, error mapping, interceptors |
| 14 | **Design system integration** | Shared UI foundations | Theme provider, tokens, CSS baseline, dark/light, density, brand switching |
| 15 | **State / context** | A *small* set of global state | Current user, selected account/customer, tenant/brand, locale, workspace, session status |
| 16 | **Localisation** | Language and formatting | Locale selection, date/currency formatting, translation loading, timezone handling |
| 17 | **Accessibility / focus** | Cross-MFE a11y conventions | Focus restore on navigation, skip links, page-title and route announcements, modal stacking |
| 18 | **MFE lifecycle** | How remotes mount/unmount/fail | Mount/unmount contract, cleanup hooks, readiness signals, version checks, degraded mode |

Four of these are worth dwelling on:

- **Authorization** is a capability check, not a UI concern. Expose it as a simple predicate the shell and remotes share:

  ```ts
  can("accounts.transfer")
  can("cards.freeze")
  can("admin.viewAudit")
  ```

- **Remote registry** decouples deployment from the build. The shell loads a manifest at runtime rather than baking remote URLs into the bundle:

  ```json
  {
    "accounts": {
      "remoteEntry": "https://cdn/app/accounts/remoteEntry.js",
      "scope": "accounts",
      "module": "./Routes"
    }
  }
  ```

- **Event bus** is powerful and easily abused. Prefer explicit contracts over a global free-for-all; reserve the bus for genuinely cross-cutting signals such as `session:expired` or `customer:selected`.

- **Error handling** matters more here than in a monolith, because remotes load *independently* — a single remote failing to load must not take down the frame.

### The platform contract

Expose a small, typed contract to remotes rather than letting each one wire up its own cross-cutting concerns:

```ts
type ShellPlatform = {
  auth: AuthService
  navigation: NavigationService
  permissions: PermissionService
  config: ConfigService
  notifications: NotificationService
  telemetry: TelemetryService
  http: HttpService
  eventBus: EventBus
  logger: LoggerService
}
```

Remotes receive it through the mount contract:

```ts
mount(container, { platform, routeParams, initialContext })
```

or a shared provider:

```tsx
<ShellPlatformProvider value={platform}>
  <RemoteApp />
</ShellPlatformProvider>
```

### What *not* to put in the shell

The failure mode is a shell that grows into a giant shared application — a distributed monolith with a single chokepoint. Keep product concerns out:

- individual product workflows and domain business rules
- MFE-specific forms and page-level UI state
- feature-specific API orchestration and validation
- complex shared stores used by everyone

The cleanest test is on state. *Good* shell-owned state is global context: current user, tenant, locale, selected account. *Bad* shell-owned state is page/form state and domain state owned by a single product area. The shell owns the **enterprise runtime**, not every product concern.

### Where to start

You don't need all eighteen on day one. A strong foundation is twelve: routing, auth/session, authorization, navigation, layout, remote registry, runtime config, notifications, error handling, observability, HTTP client, and feature flags. Add localisation, a11y conventions, design-system providers, lifecycle, the event bus, and shared state as the platform matures.

---

## Part 2 — Extract the runtime: the thin shell

Owning those services is right. Putting them all *inside* the shell is not — at least not once you have several teams and a platform team that wants to ship on its own cadence.

The refinement: keep the shell a **thin runtime host** and load the platform services from a separate, independently deployed **Platform Services Remote**. The shell boots the runtime; the runtime provides the services; the product MFEs consume the runtime contract.

```text
┌──────────────────────────┐
│ Thin SPA Shell            │
│ - bootstraps app          │
│ - loads platform runtime  │
│ - mounts MFEs             │
└─────────────┬────────────┘
              ▼
┌──────────────────────────┐
│ Platform Services Remote  │
│ - auth/session            │
│ - navigation              │
│ - permissions             │
│ - telemetry               │
│ - config                  │
│ - notifications           │
│ - HTTP client             │
│ - feature flags           │
└─────────────┬────────────┘
              ▼
┌──────────────────────────┐
│ Product Microfrontends    │
│ - accounts                │
│ - cards                   │
│ - payments                │
└──────────────────────────┘
```

The clearest mental model is an operating system:

```text
Shell                      = bootloader
Platform Services Remote   = operating system
MFEs                       = applications
```

The shell starts the runtime. The platform module provides the services. The MFEs consume the contract. The shell is deliberately small, stable, and boring.

### What the thin shell owns

Only bootstrapping concerns: app bootstrap and loading screen, remote manifest discovery, loading the platform module, a top-level error boundary, a fallback if platform loading fails, mounting the active MFE, and a very small routing bootstrap if required.

It does **not** own auth, permissions, navigation, HTTP, telemetry, or product context. Those move into the platform remote, which becomes the real application runtime:

```ts
export type PlatformRuntime = {
  auth: AuthService
  session: SessionService
  permissions: PermissionService
  navigation: NavigationService
  config: ConfigService
  telemetry: TelemetryService
  logger: LoggerService
  http: HttpService
  notifications: NotificationService
  featureFlags: FeatureFlagService
  eventBus: EventBus
}
```

The shell loads and initialises it first, then passes it to each MFE:

```ts
const platform = await loadRemote<PlatformRuntime>("platform/Runtime")
await platform.init({ environment, tenant, manifestUrl })

remote.mount(container, {
  platform,
  route,
  userContext: platform.session.currentUser,
})
```

### Who renders the layout?

A common question: in this model, does the *thin shell* or the *platform runtime* own the application layout? It should be the **platform runtime** — the thin shell only boots and provides a fatal fallback. Layout is bound to platform concerns:

```text
layout = header + nav + breadcrumbs + permissions + session + notifications + theme
```

So the shell hands rendering to the platform, which wraps the active remote:

```tsx
// thin shell
const platform = await loadPlatformRuntime()
platform.renderApp({ container: document.getElementById("root"), remoteManifest })
```

```tsx
// inside the platform runtime
<AppProviders>
  <AppLayout>
    <Header />
    <SideNav />
    <Breadcrumbs />
    <NotificationHost />
    <MainContent>
      <RemotePage />
    </MainContent>
  </AppLayout>
</AppProviders>
```

The MFE renders only the content for its slot:

```tsx
export function AccountsPage() {
  return <AccountDashboard />
}
```

| Concern | Owner |
|---|---|
| HTML bootstrap | Thin shell |
| App frame | Platform runtime |
| Header / sidebar / nav | Platform runtime |
| Breadcrumb rules | Platform runtime, with route metadata from MFEs |
| Page title | Platform runtime, with MFE input |
| Product page content | MFE |
| Product-specific layout | MFE |
| Full-screen escape mode | Platform runtime controls, MFE requests |

The rule of thumb: **the platform owns anything that should feel consistent across the whole enterprise app; the MFE owns anything specific to its product journey** — its tabs, filters, sub-nav, and master-detail layout.

### Why bother extracting it?

The payoff is **decoupling the shell's release cadence from the platform's**. You get a thinner shell that rarely redeploys, independently deployable platform services with clear platform-team ownership, consistent services across all MFEs, separately versioned platform contracts, and platform services you can test in isolation. It also keeps the shell from quietly becoming a frontend monolith.

### Depend on the contract, not the implementation

The decoupling only holds if the shell and MFEs depend on a **stable platform contract**, never on internals:

```ts
// Good — public contract
platform.auth.getAccessToken()
platform.navigation.navigate("/accounts")
platform.telemetry.trackPageView(...)

// Bad — reaching into internals
platformAuthStore.dispatch(...)
platformInternalRouter._history.push(...)
platformAxiosInstance.interceptors...
```

Version that contract explicitly so the runtime and its consumers evolve independently, and let each MFE declare what it needs:

```json
{
  "name": "accounts",
  "requiresPlatform": "^1.4.0",
  "capabilities": ["auth", "navigation", "telemetry", "notifications"]
}
```

The risk to watch is the same one from Part 1, relocated: the platform remote becomes a distributed monolith if you let product logic leak in. Keep it strictly to cross-cutting concerns (auth, session, navigation, config, telemetry, permissions, notifications, HTTP, feature flags) and keep account business rules, payment workflows, and product form state out.

The end state is a clean three-part topology:

```text
app-shell             = boot and host
app-platform-runtime  = shared enterprise runtime
app-accounts-mfe      ┐
app-cards-mfe         ├ business capabilities
app-payments-mfe      ┘
```

---

## Part 3 — Keep startup fast

Extraction buys deployment independence, but it isn't free. You've added a critical dependency to the startup path, and a naive implementation turns first render into a **waterfall**:

```text
index.html
  → shell bundle
    → remote manifest
      → platform runtime remote
        → platform init
          → layout render
            → active MFE remote
```

The platform runtime now sits on the **critical rendering path**: the user can't see the real frame until it loads. If the platform remote is large or slow, the whole app feels slow even when the product MFE is fast.

| | Fat shell (services in shell) | Thin shell + platform remote |
|---|---|---|
| First render | Faster — fewer remote steps | Slower — extra network hop |
| Startup | Simpler, fewer failure points | More steps; platform remote is critical |
| Caching / versioning | Simpler | More complex |
| Releaseability | Grows into a monolith | Independent deploy, cleaner ownership, reusable |

The thin-shell model trades startup simplicity for deployment independence — so you have to engineer the startup path deliberately to win the trade. Six risks, with their mitigations:

**1. The startup waterfall.** A sequential chain is the default and it's slow. Parallelise everything without a hard ordering dependency:

```text
load shell
parallel:
  - manifest
  - platform remote
  - runtime config
  - auth / session check
  - active MFE prefetch
```

**2. Platform runtime bloat.** A runtime that contains *everything* makes first meaningful render slow. Split it into a small critical core and a deferred remainder:

```text
platform-core (required for first render)   platform-deferred (loaded after start)
- config                                     - analytics SDK
- session                                    - full telemetry
- layout shell                               - help widgets
- routing                                    - experimentation SDK
- nav skeleton                               - complex notification providers
- auth guard
```

**3. Shared dependency duplication.** Module Federation will happily load multiple copies of `react`, `react-dom`, the router, and your design system — hurting load time and causing subtle runtime bugs. Pin the genuinely cross-cutting core as strict singletons:

```ts
shared: {
  react: { singleton: true, requiredVersion: "^18.x" },
  "react-dom": { singleton: true, requiredVersion: "^18.x" }
}
```

But don't over-share — a shared dependency is a contract.

**4. Layout delayed by remote loading.** Because the platform owns layout, users can see a blank screen until it loads. The thin shell should render an immediate, minimal branded loading frame (logo, skeleton, fatal-error fallback, retry) that the platform then replaces.

**5. MFE load time.** Once the platform is ready, the active MFE is another remote load. Prefetch on intent:

```text
current route MFE: load immediately
primary nav MFEs:  prefetch after idle
next likely route: prefetch on hover
```

**6. Remote manifest latency.** A manifest fetched before anything else is itself critical. Keep it tiny and strongly cacheable with versioned URLs.

Put together, the performance architecture looks like this:

```text
Thin Shell          tiny bundle · loading frame · fetch manifest · load platform · prefetch active MFE
Platform Core       layout · routing · session · config · nav shell · error handling
Platform Deferred   analytics SDKs · experimentation · help widgets · non-critical notifications
Product MFEs        route-level chunks · lazy page modules · product-specific state
```

And the target for first render is *progressive reveal*, not a chain of empty states:

```text
HTML → shell skeleton → platform layout → active MFE content
```

not `blank → spinner → spinner → spinner → app`.

---

## Three rules to take away

1. **The shell renders an immediate skeleton.** Never a blank page waiting on a remote.
2. **The platform runtime has a tiny critical core.** Everything non-essential is deferred.
3. **MFEs are prefetched on route and navigation intent.**

The single biggest mistake is letting `app-platform-runtime` swell into a large remote bundle that blocks everything. Treat it like a performance-critical kernel and the thin-shell model gives you the best of both worlds: a small, stable, boring shell, and a platform and products that evolve on their own cadence.
