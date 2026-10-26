---
name: nuxt-data-fetching
description: "Padrões para fetching em Nuxt (3/4/5)/4/5: useAsyncData/useFetch, chaves estáveis, cache, dedupe, transform/pick, erros e compatibilidade SSR."
license: UNLICENSED
---

# Nuxt Data Fetching (Nuxt 3/4/5)

## Workflow

1. Classifique o dado: público/privado, cacheável/não-cacheável, depende de cookie/session?
2. Escolha caminho:
   - Public + cacheável: `useAsyncData`/`useFetch` direto (ou server/api com cache)
   - Precisa segredo/normalização: `server/api` como BFF + `useFetch` nele
3. Defina `key` determinística (rota + params + filtros).
4. Normalize resposta (transform/pick) e defina contrato (tipos).
5. Modele estados: loading / success / empty / error.

## Defaults

- Prefira `useAsyncData` para SSR previsível e controle fino (`transform`, `pick`, `watch` explícito).
- Evite refetch implícito; seja intencional com `watch` e chaves.
- Erros: mapear para UI sem vazar detalhes; log server-side com correlação.

## Anti-patterns

- `await $fetch(...)` em muitos componentes (duplicação, difícil cachear).
- “Key” instável (inclui objetos não serializáveis).
- Expor tokens no client ao consumir APIs externas.

## Reference

Leia `reference.md`.
