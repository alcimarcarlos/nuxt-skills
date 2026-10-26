## Nuxt 3 Auth & Session — reference

### Checklist (copiar e colar)

- **Cookies**
  - `HttpOnly: true`
  - `Secure: true` (em produção)
  - `SameSite: 'lax'` (default seguro para a maioria dos apps)
  - `Path: '/'`
  - Preferir `__Host-<name>` quando possível

- **Endpoints internos**
  - `POST /api/auth/login`
  - `POST /api/auth/logout`
  - `GET /api/auth/me`
  - `POST /api/auth/refresh` (se usar refresh)

- **Proteção**
  - Client: `middleware/auth.ts` redireciona
  - Server: endpoints checam sessão e retornam 401/403

---

### Exemplo: login que seta cookie HttpOnly — copiar e colar

`server/api/auth/login.post.ts`:

```ts
import { z } from 'zod'

const Body = z.object({
  email: z.string().email(),
  password: z.string().min(8),
})

export default defineEventHandler(async (event) => {
  const body = Body.parse(await readBody(event))

  // TODO: validar credenciais e criar uma sessão real no seu backend/DB/Redis
  const sessionId = `sess_${crypto.randomUUID()}`

  setCookie(event, '__Host-session', sessionId, {
    httpOnly: true,
    secure: process.env.NODE_ENV === 'production',
    sameSite: 'lax',
    path: '/',
    maxAge: 60 * 60 * 24 * 7,
  })

  return { ok: true }
})
```

### Exemplo: logout — copiar e colar

`server/api/auth/logout.post.ts`:

```ts
export default defineEventHandler(async (event) => {
  // TODO: revogar sessão no store do server
  deleteCookie(event, '__Host-session', { path: '/' })
  return { ok: true }
})
```

### Exemplo: “me” — copiar e colar

`server/api/auth/me.get.ts`:

```ts
export default defineEventHandler(async (event) => {
  const sessionId = getCookie(event, '__Host-session')
  if (!sessionId) throw createError({ statusCode: 401, statusMessage: 'Unauthenticated' })

  // TODO: buscar sessão e usuário no server-side store
  return { id: 'user_123', name: 'User', roles: ['user'] }
})
```

> Nota Nuxt 5 (Nitro v3/h3 v2): erros em server routes passam a usar `status/statusText` (ex.: `HTTPError`).
> Veja `nuxt-5-server-api-nitro/reference.md`.

### Exemplo: route middleware de proteção (client) — copiar e colar

`middleware/auth.ts`:

```ts
export default defineNuxtRouteMiddleware(async () => {
  // se a rota for SSR, isso roda tanto no server quanto no client
  const { data, error } = await useFetch('/api/auth/me')
  if (error.value) return navigateTo('/login')
  if (!data.value) return navigateTo('/login')
})
```

### Exemplo: origin check para mutações cookie-based — copiar e colar

```ts
import type { H3Event } from 'h3'

function assertTrustedOrigin(event: H3Event, allowedOrigins: string[]) {
  const origin = getHeader(event, 'origin')
  if (!origin) return // alguns requests podem não ter Origin
  if (!allowedOrigins.includes(origin)) {
    throw createError({ statusCode: 403, statusMessage: 'Forbidden' })
  }
}
```

