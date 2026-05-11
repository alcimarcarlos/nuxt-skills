---
name: nuxt-4-data-fetching
description: Padrões para fetching em Nuxt 4: useAsyncData/useFetch, chaves estáveis, cache, dedupe, transform/pick, erros e compatibilidade SSR.
---

# Nuxt 4 Data Fetching

## Workflow

1. Classifique o dado: público/privado, cacheável/não-cacheável, depende de cookie/session?
2. Escolha caminho: `useAsyncData`/`useFetch` direto vs `server/api` como BFF.
3. Defina `key` determinística.
4. Transform/pick para reduzir payload e evitar vazamento.
5. Modele estados: loading/success/empty/error.

## Reference

Leia `reference.md`.

