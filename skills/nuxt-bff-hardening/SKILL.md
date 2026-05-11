---
name: nuxt-bff-hardening
description: Prever/prevenir/corrigir riscos de BFF em Nuxt 3/4: remover proxy catch-all, aplicar allowlist, validação, timeouts, limites, rate limit, CORS e erros públicos seguros.
---

# Nuxt BFF Hardening

## Objective

Eliminar padrões perigosos (ex: `server/api/[...path].ts` com bearer token) e substituir por BFF seguro e auditável.

## Workflow (Predict → Prevent → Correct)

1. **Predict (encontrar risco)**
   - Procure `server/api/[...path]`, `$fetch(`${base}/${path}`)` e headers `Authorization` montados com token do tenant.
   - Procure ausência de: allowlist, schema validation, timeout, request size limit, rate limit.
2. **Prevent (padrão novo)**
   - Padronize handlers por recurso (`server/api/events/*`, `server/api/checkout/*`) ou um proxy com allowlist rígida.
   - Defina “contratos” (schemas) para `params/query/body` e shape de resposta.
3. **Correct (refactor seguro)**
   - Remova o catch-all.
   - Introduza `MerchantContext` (public vs secret) e injete token **somente** server-side.
   - Adicione: timeout, error mapping, body limits, rate limit, CORS explícito.

## Mandatory Requirements

- Allowlist de **paths + métodos** quando houver proxy.
- Timeouts para upstream.
- Sanitização de erros: nunca repassar erro cru do upstream para o client.
- Limites de request (body size + upload size) no edge e/ou server.

## Anti-patterns

- Proxy catch-all com bearer token.
- Repassar headers do client para upstream sem filtro.
- Aceitar URL/path arbitrário do client.

## Reference

Leia `reference.md` para templates copiáveis.

