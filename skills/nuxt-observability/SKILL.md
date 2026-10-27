---
name: nuxt-observability
description: "Observability in Nuxt: structured logging, correlation IDs, server/api metrics, error capture. Trigger on telemetry/monitoring."
license: UNLICENSED
---

# Nuxt Observability

## Workflow

1. Mapear pontos de falha: SSR render, data fetching, `server/api`, integrações upstream.
2. Adicionar correlation id e propagação (request -> logs -> upstream).
3. Padronizar erros: mensagem segura ao client, detalhe no server.
4. Medir: latência por endpoint, taxa de erro, cache hit/miss, tamanhos de payload.
5. Auditar logs: remover PII, tokens, cookies, headers sensíveis.

## Defaults

- Logs estruturados (JSON) no server quando possível.
- Erros no client sem vazamento de segredos; report com contexto mínimo (route + build/version + correlation id).
- Não logar body/headers por padrão.

## Anti-patterns

- “Log everything” (custo + risco de PII).
- Sem correlação: impossível debugar incidentes.
