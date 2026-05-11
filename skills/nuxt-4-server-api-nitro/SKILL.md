---
name: nuxt-4-server-api-nitro
description: Boas práticas para `server/api` (Nitro/H3) em Nuxt 4: contratos, validação, errors, cookies, proxy seguro, caching e integração com serviços externos.
---

# Nuxt 4 Server API (Nitro)

## Workflow

1. Localize handlers em `server/api/**` e plugins em `server/plugins/**`.
2. Defina contrato do endpoint (input/output) e valide input no server.
3. Padronize respostas e erros (mapear erros internos para mensagens seguras).
4. Proteja endpoints: auth (cookie), rate limit, limites de request.
5. Integrações externas: timeouts, retries controlados, logs com correlação.

## Defaults

- Validar `params/query/body`.
- Timeout em chamadas upstream.
- Segredos só no `runtimeConfig` privado.

## Reference

Leia `reference.md`.

