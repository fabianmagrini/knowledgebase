---
title: Thin Shell + Platform Runtime Remote
tags: [architecture, system-design, microservices]
topic: engineering/architecture
status: notes
level: intermediate
related:
  - engineering/architecture/microfrontend-shell-platform.md
  - engineering/architecture/thin-shell-startup-performance.md
  - engineering/architecture/micro-frontend-principles.md
  - engineering/architecture/composable-architecture.md
updated: 2026-06-22
---

# Thin Shell + Platform Runtime Remote

A refinement of the [shell-as-platform-runtime](microfrontend-shell-platform.md)
model. Rather than building one SPA shell that *contains* every platform service,
keep the shell a **thin runtime host** and load the platform services from a
separate, independently deployed **Platform Services Remote**. The shell boots the
runtime; the runtime provides the services; the product MFEs consume the runtime
contract.

```txt
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

## The key concept: shell as kernel loader

The clearest mental model is an operating system:

```txt
Shell                      = bootloader
Platform Services Remote   = operating system
MFEs                       = applications
```

The shell starts the runtime. The platform module provides the services. The MFEs
consume the runtime contract. The shell is deliberately small, stable, and boring.

## What the thin shell owns

Only bootstrapping concerns:

- app bootstrap and loading screen
- remote manifest discovery
- loading the platform module
- top-level error boundary
- a fallback experience if platform loading fails
- mounting the active MFE
- a very small routing bootstrap, if required

It should **not** own auth, permissions, navigation, HTTP, telemetry, or product
context directly — those move into the platform remote.

## What the platform remote owns

The platform module becomes the real application runtime, exposing a typed
contract:

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

## Layout: who renders the frame

A common question in this model is whether the *thin shell* or the *platform
runtime* owns the application layout. It should be the **platform runtime** — the
thin shell only boots and provides a fatal fallback. Layout is bound to platform
concerns:

```txt
layout = header + nav + breadcrumbs + permissions + session + notifications + theme
```

so it belongs alongside the navigation, session, permissions, theme/design-system,
notification, and accessibility services that already live in the runtime. In
practice the shell hands rendering to the platform, which wraps the active remote:

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

The MFE renders only the page content for its layout slot:

```tsx
export function AccountsPage() {
  return <AccountDashboard />
}
```

### Ownership split

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

### Outer frame vs. inner product layout

The platform owns the **outer** layout; the MFE still owns its **inner** layout:

```txt
Platform layout:  header / side nav / global frame / notifications
MFE layout:       tabs / filters / product subnav / master-detail / page sections
```

The rule of thumb: **the platform owns anything that should feel consistent across
the whole enterprise app; the MFE owns anything specific to its product journey.**

## Why extract it

The main benefit is **decoupling the shell's release cadence from the platform's
capability release cadence**. You get:

- a thinner shell that rarely needs redeploying
- independently deployable platform services with clear platform-team ownership
- consistent services across all MFEs
- an easier upgrade path and separately versioned platform contracts
- better testability of platform services in isolation

It also keeps the shell from becoming a *frontend monolith*.

## Recommended startup sequence

```txt
1.  Load shell index.html
2.  Fetch environment / runtime config
3.  Fetch remote manifest
4.  Load platform services remote
5.  Initialise platform runtime
6.  Resolve session / auth state
7.  Build navigation / routes
8.  Load active product MFE
9.  Pass platform contract into MFE
10. Render app
```

## Depend on the contract, not the implementation

The shell and MFEs must depend on a **stable platform contract**, never on
platform internals — otherwise the decoupling is lost.

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

## Versioning model

Version the platform contract explicitly so the runtime and its consumers can
evolve independently:

```ts
type PlatformRuntimeV1 = {
  version: "1.x"
  capabilities: string[]
  auth: AuthService
  navigation: NavigationService
  telemetry: TelemetryService
}
```

Each MFE then declares the platform version and capabilities it needs, which the
shell can check before mounting:

```json
{
  "name": "accounts",
  "requiresPlatform": "^1.4.0",
  "capabilities": ["auth", "navigation", "telemetry", "notifications"]
}
```

## Main risk: a distributed monolith

The platform remote becomes a distributed monolith if everything gets added to it.
Keep it strictly to cross-cutting concerns:

| Good platform services | Bad platform services |
|---|---|
| auth, session, navigation | account business rules |
| config, telemetry, permissions | payment workflows |
| notifications, HTTP wrapper | product form state |
| feature flags | customer onboarding logic |
| | domain-specific API orchestration |

This is the same boundary as the shell-platform note's "what not to put in the
shell" — it simply moves with the runtime when the runtime is extracted.

## The topology

A clean three-part separation, e.g. for an `app` product family:

```txt
app-shell             = boot and host
app-platform-runtime  = shared enterprise runtime
app-accounts-mfe      ┐
app-cards-mfe         ├ business capabilities
app-payments-mfe      ┘
```

This is the strongest model when the goal is to keep the SPA shell small, stable,
and boring while the platform and products evolve on their own cadence.

## Relationship to other notes

- [The Micro-Frontend Shell as Platform Runtime](microfrontend-shell-platform.md)
  — catalogues *what* the platform runtime contains. This note covers *where* the
  runtime lives: extracting it from the shell into its own remote. The two pair as
  a progression — contents, then packaging.
- [Microfrontend Architecture Principles](micro-frontend-principles.md) — the
  extracted platform remote is the sharpest expression of *platform-over-
  governance* and *independent deployability*.
- [Composable Architecture](composable-architecture.md) — the wider
  packaged-business-capability paradigm the shell, platform, and products compose
  within.
