## Nuxt BFF Hardening — reference

### Checklist “copiar e colar”

- **Proxy**
  - Allowlist: paths permitidos + métodos permitidos
  - Timeout upstream
  - Request size cap
  - Rate limit (edge/Redis preferível)
  - CORS explícito (negar por padrão)
  - Error mapping (mensagem pública segura)

---

### Template: allowlist proxy (server/api/proxy.get.ts) — copiar e colar

```ts
import { z } from 'zod'

const Query = z.object({
  resource: z.enum(['events', 'tickets']),
})

const ALLOW: Record<string, { methods: Array<'GET' | 'POST'>; pathPrefix: string }> = {
  events: { methods: ['GET'], pathPrefix: 'events' },
  tickets: { methods: ['GET'], pathPrefix: 'tickets' },
}

function publicError(statusCode: number, message: string) {
  return createError({ statusCode, statusMessage: message })
}

export default defineEventHandler(async (event) => {
  const merchant = event.context.merchant as { secret: { api: string; bearerToken: string } }
  const q = Query.parse(getQuery(event))

  const rule = ALLOW[q.resource]
  if (!rule) throw publicError(404, 'Not found')
  if (!rule.methods.includes(event.method as any)) throw publicError(405, 'Method not allowed')

  try {
    return await $fetch(`${merchant.secret.api}/${rule.pathPrefix}`, {
      method: event.method,
      timeout: 5000,
      headers: {
        Authorization: `Bearer ${merchant.secret.bearerToken}`,
        'Content-Type': 'application/json',
      },
    })
  } catch (_err) {
    throw publicError(502, 'Upstream unavailable')
  }
})
```

> Nota Nuxt 5 (Nitro v3/h3 v2): `statusCode/statusMessage` migram para `status/statusText` e o padrão recomendado em server routes é `HTTPError`.
> Veja `nuxt-5-server-api-nitro/reference.md` para o padrão novo (imports `nitro/h3` + `HTTPError`).

### Template: handler explícito (recomendado) — copiar e colar

Crie handlers por domínio, exemplo:

`server/api/events/[id].get.ts`:

```ts
import { z } from 'zod'

const Params = z.object({ id: z.string().min(1).max(120) })

export default defineEventHandler(async (event) => {
  const merchant = event.context.merchant as { secret: { api: string; bearerToken: string } }
  const { id } = Params.parse(getRouterParams(event))

  return await $fetch(`${merchant.secret.api}/events/${id}`, {
    timeout: 5000,
    headers: { Authorization: `Bearer ${merchant.secret.bearerToken}` },
  })
})
```

