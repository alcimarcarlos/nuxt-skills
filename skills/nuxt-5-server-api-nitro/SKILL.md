---
name: nuxt-5-server-api-nitro
description: Boas práticas para `server/api` (Nitro v3/H3) em Nuxt 5: contratos, validação, errors, cookies, proxy seguro, caching e integrações (imports explícitos quando auto-imports estiverem off).
---

# Nuxt 5 Server API (Nitro)

## Workflow

1. Localize handlers em `server/api/**` e plugins em `server/plugins/**`.
2. Valide `params/query/body` e defina contrato de resposta.
3. Padronize erro público vs interno.
4. Proteja endpoints: auth, rate limit, limites de request.
5. Nitro v3: use imports explícitos de `h3` se auto-imports estiverem desabilitados.

## Reference

Leia `reference.md`.

