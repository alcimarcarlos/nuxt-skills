---
name: nuxt-systematic-debugging
description: "Systematic root-cause debugging protocol for Nuxt (3/4/5) and Nitro: prohibits guessing, enforces minimal failing Vitest test reproducers, single-variable fixes, and non-regression verification."
license: UNLICENSED
---

# Nuxt Systematic Debugging

## Objective

Eliminate guesswork ("shotgun debugging") by enforcing a strict 4-step scientific debugging method for triaging and resolving defects across Nuxt pages, composables, and Nitro server endpoints.

## Compatibility (Cursor, Codex, Claude Code)

- Strict operational gate: agents must not alter production source code until a minimal failing Vitest or Nitro test reproducer is written.
- Always isolate whether the failure is on the server (SSR), client (hydration), or Nitro API boundary.

## Mandatory 4-Step Protocol

### Step 1: Formulate Root-Cause Hypothesis
- Inspect the browser console, Nitro server logs, and hydration warnings.
- Determine the execution domain: Server-only, Client-only, or Universal/Hydration.
- Formulate an explicit hypothesis: *"The bug occurs because composable X relies on client-only API Y during SSR pre-render."*

### Step 2: Create Minimal Failing Reproducer
- Create or add a test in `test/...` using `@nuxt/test-utils` or Vitest that triggers the exact bug condition.
- Run the test:
  ```bash
  npm run test -- test/bug-reproducer.test.ts
  ```
- **Verification Gate**: The test MUST fail with the reported error.

### Step 3: Surgical Fix (Single Variable)
- Make the smallest possible change to resolve the root cause.
- Follow the **Minimal Diff Mandate**: never rewrite unaffected components or packages.

### Step 4: Non-Regression Verification
- Re-run the reproducer test to verify it passes.
- Run the full test suite and typechecker:
  ```bash
  npx nuxi typecheck
  npm run test
  ```

## Anti-Patterns (Strictly Forbidden)

- **Shotgun Debugging**: Modifying multiple files randomly without a failing test reproducer.
- **Error Silencing**: Wrapping broken code in `catch () {}` without structured recovery.
- **Hydration Bypass**: Silencing hydration errors with `v-if="false"` hacks instead of aligning initial SSR and client state.

## Additional Resources

- Read `reference.md` for triage commands and reproducer templates.
