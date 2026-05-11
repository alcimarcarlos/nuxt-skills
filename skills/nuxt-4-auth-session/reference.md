## Nuxt 4 Auth & Session — reference

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

