---
name: nuxt-code-generation-contract
description: "Mandatory output contract for Nuxt: directory layout, Zod schemas, SSR state matrices, Vitest. Trigger on feature generation."
license: UNLICENSED
---

# nuxt-code-generation-contract

## Objective

Standardize the format, SSR architecture, and minimum completeness of agent deliveries in Nuxt 3, Nuxt 4, and Nuxt 5.

## Compatibility (Cursor, Codex, Claude Code)

- Agent-vendor agnostic: treat as a mandatory delivery protocol.
- Prefer deterministic, reviewable outputs over conversational suggestions.
- Do not invent external APIs, plugins, or third-party modules silently without declaring assumptions.

## Apply When

- Creating or modifying a Nuxt page (`pages/`), component (`components/`), or composable (`composables/`).
- Implementing a Nitro API endpoint (`server/api/`) or server middleware.
- Refactoring an SSR or hybrid rendering flow.
- Reviewing PRs or verifying whether generated Nuxt code meets production quality.

## Mandatory Delivery Protocol

Every Nuxt feature delivery MUST provide:

1. **Declared File Tree**: Relative paths of all created/modified files before code (`app/pages/...` or `pages/...`, `server/api/...`, `types/...`, `tests/...`).
2. **Boundary Contracts**:
   - Typed API contracts with Zod or TypeScript schemas.
   - Nitro event handlers using `readValidatedBody(event, schema)` or typed query parsing.
   - Consistent error responses via `createError({ statusCode, statusMessage })` without leaking internal stack traces.
3. **SSR & State Lifecycle**:
   - Data fetching via `useAsyncData` or `useFetch` with explicit, stable keys.
   - Full screen state handling: **pending (skeleton/loading)**, **success**, **empty**, and **error/retry**.
   - Shared reactive state via `useState()`, never mutable global singletons that leak across requests in SSR.
4. **Security & BFF Baseline**:
   - Zero secrets exposed in `runtimeConfig.public`.
   - Sensitive tokens stored strictly in HttpOnly, SameSite, Secure cookies.
   - External third-party APIs proxied via `server/api/` (BFF) with input validation and rate limiting.
5. **Actionable Test Matrix (Vitest / @nuxt/test-utils)**:
   - Server API contract tests (200, 400 validation error, 401 unauthenticated).
   - Component / Composable unit tests with mock SSR state.
   - Verification commands (`npx nuxi typecheck`, `npm run test`, `npm run lint`).

## Mandatory Output Format

1. **Objective & Nuxt Version**: Feature summary and target Nuxt version (3, 4, or 5).
2. **File Structure**: Tree of files to create or modify.
3. **Contracts & Schemas**: TypeScript interfaces and Zod validation schemas.
4. **Server API Implementation**: Nitro handlers in `server/api/`.
5. **Composables & State**: Data fetching logic with `useAsyncData`.
6. **UI Components & Pages**: Presentation layer with loading, empty, and error states.
7. **Automated Tests**: Vitest / `@nuxt/test-utils` tests.
8. **Verification Commands**: Exact commands to validate locally.

## Additional Resources

- For checklist templates and complete slice examples, read `reference.md`.
