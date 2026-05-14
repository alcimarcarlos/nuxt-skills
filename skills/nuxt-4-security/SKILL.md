---
name: nuxt-4-security
description: "Hardening OWASP para Nuxt 4 (SSR/SSG/híbrido): headers/CSP, cookies, SSR isolation, validação, rate limit, CORS e proteção de segredos."
license: UNLICENSED
---

# Nuxt 4 Security

## Workflow

1. Identifique threat model mínimo: SSR? cookies? endpoints em `server/api`? login? uploads?
2. Garanta **segredos** em `runtimeConfig` privado e sem vazamento no client.
3. Configure headers e CSP (preferencialmente via `nuxt-security`).
4. Revise auth/session: **cookies HttpOnly**, `SameSite`, `Secure`, rotação/expiração e origin checks.
5. Audite `server/api`: validação de entrada, rate limiting, tamanho de body, logs sem PII.
6. Adicione gates: lint + typecheck + deps audit + checagem de headers em ambiente de preview.

## Defaults

- Use `nuxt-security` para headers e CSP quando aplicável.
- Tokens/sessões: **HTTP-only cookies**; evitar `localStorage`.
- SSR safety: `useState` para state compartilhado; evitar estado global mutável em módulos.
- Nunca confie em dados do client: valide no server (schema/guard) para qualquer mutação.

## Mandatory Requirements

- Remover/evitar `X-Powered-By` (quando possível).
- CSP (nonce/hash quando SSR/SSG), `frame-ancestors`, `object-src 'none'`, `base-uri 'none'`.
- CORS explícito (origens, métodos, headers) — negar por padrão.
- Rate limit e limites de request (body size) em endpoints sensíveis.

## Anti-patterns (não fazer)

- Credenciais/tokens no `runtimeConfig.public`.
- Endpoints em `server/api` que proxyam sem validação e sem limites.
- Logar payloads com PII/tokens.

## Reference

Leia `reference.md` para uma checklist de auditoria e exemplos de configuração.
