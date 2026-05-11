## Nuxt 3 Security — reference

### Checklist de hardening (pragmático)

- **Config / segredos**
  - `runtimeConfig` privado para secrets
  - `runtimeConfig.public` só para valores não sensíveis (ex: `baseURL` público)
  - Sem `.env` commitado

- **Headers**
  - CSP com nonces (SSR) / hashes (SSG)
  - `frame-ancestors` (ou `X-Frame-Options` quando aplicável)
  - `X-Content-Type-Options: nosniff`
  - `Referrer-Policy` adequado
  - `Permissions-Policy` (mínimo necessário)

- **Cookies**
  - `HttpOnly`, `Secure` (em prod), `SameSite=Lax/Strict` conforme fluxo
  - Prefixos `__Host-` / `__Secure-` quando fizer sentido

- **Server endpoints (`server/api`)**
  - Validate input (schema)
  - Rate limit (por IP/user/session)
  - Body size cap
  - Sanitização de erros (não vazar stack/segredos)

- **SSR isolation**
  - Evitar caches mutáveis por módulo para dados por-request
  - Preferir `useState` e `event.context` (Nitro) quando necessário

### Sugestões de ferramentas (a depender do stack)

- **Headers/CSP**: `nuxt-security`
- **Validação**: zod/valibot (no server) ou validação manual consistente
- **Rate limit**: edge/proxy (Cloudflare) ou camada server (Nitro + store externo) conforme ambiente

---

### Exemplo: `nuxt-security` (headers + CSP) — copiar e colar

`nuxt.config.ts`:

```ts
export default defineNuxtConfig({
  modules: ['nuxt-security'],

  security: {
    headers: {
      crossOriginEmbedderPolicy: false, // ajuste se você usa iframes/third-party que quebrem COEP
      contentSecurityPolicy: {
        // strict CSP com nonces no SSR (padrão do módulo tende a fazer isso)
        value: {
          'base-uri': ["'none'"],
          'object-src': ["'none'"],
          'frame-ancestors': ["'none'"],
          'img-src': ["'self'", 'data:', 'https:'],
          'font-src': ["'self'", 'data:', 'https:'],
          'style-src': ["'self'", 'https:', "'unsafe-inline'"],
          'script-src': ["'self'", 'https:', "'strict-dynamic'", "'nonce-{{nonce}}'"],
          'script-src-attr': ["'none'"],
        },
      },
      referrerPolicy: 'no-referrer',
      xContentTypeOptions: 'nosniff',
    },
    // Em produção, prefira rate limit e body limits também no edge/proxy
    rateLimiter: {
      tokensPerInterval: 100,
      interval: 'minute',
    },
    requestSizeLimiter: {
      maxRequestSizeInBytes: 1_000_000, // 1MB
      maxUploadFileRequestInBytes: 5_000_000, // 5MB
    },
  },
})
```

Notas rápidas:
- CSP “perfeita” depende de analytics, fontes, CDNs e embeds; trate isso como **baseline** e refine por ambiente.
- Para rotas específicas, prefira `routeRules: { '/admin/**': { security: { ... }}}` quando aplicável.

### Exemplo: cookies HttpOnly de sessão (Nitro/H3) — copiar e colar

`server/api/auth/login.post.ts` (modelo):

```ts
export default defineEventHandler(async (event) => {
  // ... validar credenciais, criar sessionId/token opaco ...
  setCookie(event, '__Host-session', 'opaque-session-id', {
    httpOnly: true,
    secure: process.env.NODE_ENV === 'production',
    sameSite: 'lax',
    path: '/',
    // maxAge: 60 * 60 * 24 * 7, // 7 dias (ajuste)
  })

  return { ok: true }
})
```

Regras:
- **Não** armazenar token em `localStorage` como padrão.
- Use `__Host-` quando possível: exige `Secure`, `Path=/` e sem `Domain`.
- Nuxt 5 (Nitro v3): se seu projeto desabilitar auto-imports, importe helpers explicitamente (ex.: `setCookie`, `getHeader`, `setHeader`) do pacote `h3`.

### Exemplo: CORS deny-by-default (server) — copiar e colar

Quando expor endpoints para domínios externos, seja explícito. Exemplo via `server/plugins/cors.ts`:

```ts
export default defineNitroPlugin((nitroApp) => {
  nitroApp.hooks.hook('request', (event) => {
    const origin = getHeader(event, 'origin')
    const allowed = new Set(['https://app.exemplo.com'])
    if (origin && allowed.has(origin)) {
      setHeader(event, 'access-control-allow-origin', origin)
      setHeader(event, 'vary', 'origin')
      setHeader(event, 'access-control-allow-credentials', 'true')
      setHeader(event, 'access-control-allow-headers', 'content-type, authorization')
      setHeader(event, 'access-control-allow-methods', 'GET,POST,PUT,PATCH,DELETE,OPTIONS')
    }
  })
})
```

