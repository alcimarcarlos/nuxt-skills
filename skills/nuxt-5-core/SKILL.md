---
name: nuxt-5-core
description: Padrões essenciais de arquitetura e DX para Nuxt 5 (Nitro v3, Vite 6 env API): runtimeConfig, rotas, composables, server/api e práticas de migração.
---

# Nuxt 5 Core

## Workflow

1. Identifique versão do Nuxt e `future.compatibilityVersion` quando aplicável.
2. Localize `nuxt.config.*`, `app.vue`, `server/`, `plugins/`, `middleware/`, `composables/`, `pages/`.
3. Defina a fronteira do feature (UI, data, server/api, auth) e aplique convenções do repo.
4. Escolha o padrão de dados: `useAsyncData`/`useFetch` (SSR-friendly) + server routes quando necessário.
5. Garanta estados previsíveis e isolamento SSR (sem singletons mutáveis por request).

## Defaults

- Prefira **Nuxt 5 conventions**: `pages/`, `composables/`, `server/api`, `plugins/`.
- Use `runtimeConfig` para segredos e chaves; nunca embedar segredo em `public`.
- Centralize acesso a API externa em `server/api` (BFF) quando precisar ocultar tokens/normalizar payloads/policy.
- Nuxt 5 (Nitro v3): não dependa de auto-imports; use imports explícitos de `h3` quando necessário.
- Nuxt 5 (Vite 6 env API): evite patterns de config client/server divergentes que dependam de hooks antigos.

## Anti-patterns (não fazer)

- Guardar token em `localStorage` como padrão.
- Cache mutável em nível de módulo para dados por-request (SSR leak).
- Proxy catch-all com bearer token.

## Reference

Leia `reference.md` para checklists e exemplos.

