---
name: nuxt-3-core
description: Padrões essenciais de arquitetura e DX para Nuxt 3 (Nuxt app, runtimeConfig, rotas, composables, componentes, camadas), com foco em previsibilidade e manutenção.
---

# Nuxt 3 Core

## Workflow

1. Identifique versão do Nuxt, modo de renderização (SSR/SSG/híbrido) e hosting (Node, serverless, edge).
2. Localize `nuxt.config.*`, `app.vue`, `server/`, `plugins/`, `middleware/`, `composables/`, `pages/`.
3. Defina a fronteira do feature (UI, data, server/api, auth) e aplique convenções do repo.
4. Escolha o padrão de dados: `useAsyncData`/`useFetch` (SSR-friendly) + server routes quando necessário.
5. Garanta estados previsíveis (loading/success/empty/error) e isolamento SSR (sem singletons mutáveis por request).

## Defaults

- Prefira **Nuxt 3 conventions**: `pages/` para rotas, `composables/` para hooks, `server/api` para endpoints, `plugins/` para integrações.
- Use `runtimeConfig` para segredos e chaves; nunca embedar segredo em `public`.
- Centralize acesso a API externa em `server/api` (BFF) quando precisar ocultar tokens, normalizar payloads, ou aplicar rate limit.
- Prefira `useState` para state compartilhado entre componentes em SSR; evite `ref()` global fora de funções.
- Mantenha `middleware/` leve; nada de operações pesadas ou I/O desnecessário.

## Anti-patterns (não fazer)

- Guardar token em `localStorage` como padrão.
- Criar “service singletons” com cache mutável em nível de módulo (risco de vazamento cross-request em SSR).
- Colocar regras de negócio no componente de página quando a lógica é reutilizável/testável em `composables/` ou camada server.

## Reference

Leia `reference.md` para checklists e exemplos.

