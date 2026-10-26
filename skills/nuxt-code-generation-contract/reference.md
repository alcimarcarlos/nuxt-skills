# nuxt-code-generation-contract Reference

## Standard Nuxt Feature Slice Checklist

When implementing a feature in Nuxt 3/4/5, follow this order:

- [ ] **1. Types & Validation**: `shared/types/...` or `server/utils/schemas.ts` defining input/output schemas with Zod.
- [ ] **2. Server Endpoint**: `server/api/...` using `defineEventHandler`, input validation, and typed response.
- [ ] **3. Composable**: `composables/...` encapsulating `useAsyncData` with stable key and transformation.
- [ ] **4. UI Component / Page**: `pages/...` handling `pending`, `data`, `error`, and `refresh`.
- [ ] **5. Tests**: `test/server/...` and `test/components/...` using `@nuxt/test-utils`.

## Minimal Nitro Server API & Test Skeleton

```ts
// server/api/v1/orders.post.ts
import { z } from 'zod'

const createOrderSchema = z.object({
  items: z.array(z.object({
    productId: z.string(),
    quantity: z.number().int().positive()
  })).min(1)
})

export default defineEventHandler(async (event) => {
  const body = await readValidatedBody(event, (b) => createOrderSchema.safeParse(b))
  if (!body.success) {
    throw createError({
      statusCode: 422,
      statusMessage: 'Validation Failed',
      data: body.error.flatten()
    })
  }

  // Business logic or service call
  return { id: 'ord_123', status: 'pending' }
})
```
