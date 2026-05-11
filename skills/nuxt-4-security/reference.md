## Nuxt 4 Security — reference

### Checklist de hardening (pragmático)

- **Config / segredos**
  - `runtimeConfig` privado para secrets
  - `runtimeConfig.public` só para valores não sensíveis
  - Sem `.env` commitado

- **Headers**
  - CSP com nonces (SSR) / hashes (SSG)
  - `frame-ancestors`
  - `X-Content-Type-Options: nosniff`
  - `Referrer-Policy`
  - `Permissions-Policy`

- **Cookies**
  - `HttpOnly`, `Secure` (em prod), `SameSite=Lax/Strict`
  - Prefixos `__Host-` / `__Secure-`

- **Server endpoints (`server/api`)**
  - Validate input (schema)
  - Rate limit
  - Body size cap
  - Sanitização de erros

---

### Exemplo: `nuxt-security` (headers + CSP) — copiar e colar

`nuxt.config.ts`:

```ts
export default defineNuxtConfig({
  modules: ['nuxt-security'],
  security: {
    headers: {
      contentSecurityPolicy: {
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
  },
})
```

