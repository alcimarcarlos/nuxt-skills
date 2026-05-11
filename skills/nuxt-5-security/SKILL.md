---
name: nuxt-5-security
description: Hardening OWASP para Nuxt 5 (Nitro v3): headers/CSP, cookies, SSR isolation, validação, rate limit, CORS, proteção de segredos e imports explícitos de H3 quando necessário.
---

# Nuxt 5 Security

## Workflow

1. Identifique threat model mínimo: SSR? cookies? endpoints em `server/api`? login? uploads?
2. Garanta **segredos** em `runtimeConfig` privado e sem vazamento no client.
3. Configure headers e CSP (preferencialmente via `nuxt-security`).
4. Revise auth/session: **cookies HttpOnly**, `SameSite`, `Secure`, rotação/expiração e origin checks.
5. Audite `server/api`: validação de entrada, rate limiting, tamanho de body, logs sem PII.
6. Nuxt 5 (Nitro v3): se auto-imports estiverem off, use imports explícitos de `h3`.

## Defaults

- Use `nuxt-security` para headers e CSP quando aplicável.
- Tokens/sessões: **HTTP-only cookies**; evitar `localStorage`.
- SSR safety: `useState` para state compartilhado; evitar estado global mutável em módulos.
- Nunca confie em dados do client: valide no server (schema/guard) para qualquer mutação.

## Mandatory Requirements

- CSP (nonce/hash quando SSR/SSG), `frame-ancestors`, `object-src 'none'`, `base-uri 'none'`.
- CORS explícito (origens, métodos, headers) — negar por padrão.
- Rate limit e limites de request (body size) em endpoints sensíveis.

## Reference

Leia `reference.md`.

