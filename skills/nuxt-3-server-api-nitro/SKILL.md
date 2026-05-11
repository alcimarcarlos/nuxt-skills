---
name: nuxt-3-server-api-nitro
description: Boas práticas para `server/api` (Nitro/H3) em Nuxt 3/4/5: contratos, validação, errors, cookies, proxy seguro, caching e integração com serviços externos (compatível com Nitro v3 do Nuxt 5).
---

# Nuxt Server API (Nitro)

## Workflow

1. Localize handlers em `server/api/**` e plugins em `server/plugins/**`.
2. Defina contrato do endpoint (input/output) e valide input no server.
3. Padronize respostas e erros (mapear erros internos para mensagens seguras).
4. Proteja endpoints: auth (cookie), rate limit, limites de request.
5. Integrações externas: timeouts, retries controlados, circuit breaker (quando necessário), logs com correlação.

## Defaults

- Sempre validar entrada (params, query, body).
- Nunca repassar erro cru de upstream para o client.
- Segredos apenas via `runtimeConfig` privado.
- Para auth cookie-based: confirmar origem (Origin/Referer) quando aplicável.
- Nuxt 5 (Nitro v3): prefira imports explícitos de utilitários H3 quando seu projeto desabilitar auto-imports.

## Anti-patterns

- Proxy cego para upstream (vira “open proxy” ou vaza headers/segredos).
- `console.log` com tokens/PII.
- Sem timeout em chamadas externas.

## Reference

Leia `reference.md` para checklist e padrões.

