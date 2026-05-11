---
name: nuxt-secure-logging
description: Prever/prevenir/corrigir riscos de logging em Nuxt 3/4: remover logs ruidosos, evitar PII/tokens, correlation id, erros públicos seguros e observabilidade mínima.
---

# Nuxt Secure Logging

## Workflow (Predict → Prevent → Correct)

1. **Predict**
   - Encontrar `console.log` em composables de fetch/auth.
   - Encontrar logs de `headers`, `body`, `cookies` e tokens.
2. **Prevent**
   - Logging server-side estruturado (quando necessário) e com redaction.
   - Correlation id por request.
   - “No body/headers by default”.
3. **Correct**
   - Remover logs client-side de request/response.
   - Criar helper de redaction e usá-lo nos pontos de log.
   - Padronizar erro público vs interno.

## Mandatory Requirements

- Nunca logar `Authorization`, cookies, tokens, emails/documentos por padrão.
- Em produção: logs mínimos + métricas; debug sob feature-flag.

## Reference

Leia `reference.md`.

