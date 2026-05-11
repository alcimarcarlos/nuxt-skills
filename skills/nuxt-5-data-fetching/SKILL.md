---
name: nuxt-5-data-fetching
description: Padrões para fetching em Nuxt 5: useAsyncData/useFetch, chaves estáveis, cache, dedupe, transform/pick e SSR (com atenção a mudanças de infra do Nuxt 5).
---

# Nuxt 5 Data Fetching

## Workflow

1. Classifique o dado e requisitos de cache/auth.
2. Prefira `server/api` como BFF para segredos/normalização.
3. Use `useAsyncData`/`useFetch` com keys estáveis e refetch intencional.
4. Transform/pick para reduzir payload e evitar vazamentos.

## Reference

Leia `reference.md`.

