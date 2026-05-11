---
name: nuxt-4-observability
description: Observabilidade em Nuxt 4: logging seguro, correlação, métricas de server/api, captura de erros SSR/client e hygiene de PII.
---

# Nuxt 4 Observability

## Workflow

1. Mapear pontos de falha: SSR render, data fetching, `server/api`, integrações upstream.
2. Adicionar correlation id e propagação.
3. Padronizar erros: mensagem segura ao client, detalhe no server.
4. Auditar logs: remover PII/tokens/cookies/headers sensíveis.

