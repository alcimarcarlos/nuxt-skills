# nuxt-systematic-debugging Reference

## Diagnostic Commands

```bash
# Typecheck application without starting dev server
npx nuxi typecheck

# Run Vitest in single-run mode
npx vitest run test/bug-reproducer.test.ts

# Inspect Nitro build output
npx nuxi build --prerender
```

## Minimal Failing Test Template (Vitest / @nuxt/test-utils)

```ts
import { describe, it, expect } from 'vitest'
import { $fetch, setup } from '@nuxt/test-utils/e2e'

describe('reproduces bug: checkout order endpoint returns 400 on empty items', async () => {
  await setup()

  it('rejects order with 422', async () => {
    const response = await $fetch('/api/v1/orders', {
      method: 'POST',
      body: { items: [] },
      ignoreResponseError: true,
    })

    // Must fail before fix is applied
    expect(response.statusCode).toBe(422)
  })
})
```
