## Nuxt 3 Server API (Nitro) — reference

### Checklist por endpoint

- **Input validation**
  - `params`, `query`, `body` com schema (ou validação manual consistente)
  - Normalizar tipos (string -> number, etc.)

- **AuthZ**
  - Autenticar (session cookie) quando necessário
  - Autorizar (papéis/escopo) no server

- **Upstream calls**
  - Timeout definido
  - Não encaminhar headers sensíveis automaticamente
  - Mapear erros upstream -> erro seguro pro client

- **Observability**
  - Correlation id
  - Logs sem PII
  - Métricas (latência, taxa de erro)

---

### Nota Nuxt 5 (Nitro v3): auto-imports

Em alguns setups do Nuxt 5, auto-imports do Nitro/H3 podem estar desabilitados por padrão.
Se `getQuery`, `getRouterParams`, `readBody`, `setCookie` etc. não existirem no seu contexto, **importe explicitamente** de `h3`.

### Exemplo: contrato + validação (Zod) — copiar e colar

`server/api/users/[id].get.ts`:

```ts
import { z } from 'zod'

const ParamsSchema = z.object({ id: z.string().uuid() })

type UserResponse = { id: string; name: string; roles: string[] }

export default defineEventHandler(async (event) => {
  const params = ParamsSchema.parse(getRouterParams(event))

  // Exemplo: buscar em upstream/DB
  const user = await $fetch<UserResponse>(`https://upstream.exemplo.com/users/${params.id}`, {
    timeout: 5000,
  })

  return user
})
```

### Exemplo: erro seguro e padronizado — copiar e colar

```ts
function publicError(statusCode: number, message: string) {
  return createError({ statusCode, statusMessage: message })
}

export default defineEventHandler(async (event) => {
  try {
    // ...
    throw new Error('upstream exploded: secret details')
  } catch (_err) {
    // log detalhado no server (sem PII) + mensagem genérica ao client
    throw publicError(502, 'Upstream unavailable')
  }
})
```

> Nota Nuxt 5 (Nitro v3/h3 v2): `statusCode/statusMessage` migram para `status/statusText`.
> Veja `nuxt-5-server-api-nitro/reference.md` para o padrão novo.

### Exemplo: proxy seguro (allowlist) — copiar e colar

Nunca aceite URL arbitrária do client. Restrinja com allowlist:

```ts
const ALLOWED = new Set(['users', 'products'])

export default defineEventHandler(async (event) => {
  const q = getQuery(event)
  const resource = typeof q.resource === 'string' ? q.resource : null
  if (!resource) throw createError({ statusCode: 400, statusMessage: 'Bad request' })
  if (!ALLOWED.has(resource)) throw createError({ statusCode: 404, statusMessage: 'Not found' })

  return await $fetch(`https://upstream.exemplo.com/${resource}`, { timeout: 5000 })
})
```

### Exemplo: rate limit simples por IP (in-memory) — copiar e colar

Útil só em single-instance/dev. Em produção, prefira edge/Redis:

```ts
const buckets = new Map<string, { n: number; resetAt: number }>()

export default defineEventHandler(async (event) => {
  const ip = getRequestIP(event) ?? 'unknown'
  const now = Date.now()
  const b = buckets.get(ip) ?? { n: 0, resetAt: now + 60_000 }
  if (now > b.resetAt) {
    b.n = 0
    b.resetAt = now + 60_000
  }
  b.n++
  buckets.set(ip, b)
  if (b.n > 60) throw createError({ statusCode: 429, statusMessage: 'Too many requests' })

  return { ok: true }
})
```

