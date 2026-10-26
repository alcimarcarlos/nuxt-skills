---
name: nuxt-version-compat-guard
description: "Guards against deprecated APIs and features across Nuxt 3, 4, and 5: ensures future compatibility, smooth migration paths, and prevents tech debt."
license: UNLICENSED
---

# Nuxt Version Compatibility Guard (3 → 4 → 5)

## Objective

Quando estiver desenvolvendo em Nuxt 3 ou 4, esta skill força escolhas que **não** te prendem a APIs/configs já marcadas para remoção em Nuxt 4/5, e sugere padrões com **caminho de migração claro**.

## Workflow

1. Identifique o alvo real:
   - versão atual do projeto (Nuxt 3/4/5)
   - próxima versão alvo (ex.: “vamos migrar para Nuxt 5 em breve?”)
2. Antes de codar, passe por `Deprecation Matrix` abaixo e marque:
   - **Bloqueado**: não implementar
   - **Permitido com fallback**: implementar com padrão compatível
   - **OK**: estável
3. Aplique o “compat pattern” correspondente (snippets no `reference.md`).
4. Ao final, rode o checklist de “migration readiness”.

## Deprecation Matrix (alto impacto)

### Nuxt 3 → Nuxt 4

- **Project structure**
  - Preferir `app/` (Nuxt 4 default). Em Nuxt 3, já organizar no padrão `app/` reduz atrito.

- **Legacy Composition API (Bridge / @nuxtjs/composition-api)**
  - Evitar APIs legadas (`ssrRef`, `ssrPromise`, `useContext`, `withContext`, `onGlobalSetup`, etc.). Prefira `useState` + `useNuxtApp`.

### Nuxt 4 → Nuxt 5 (compatibilityVersion: 5)

- **Vite Environment API**
  - `extendViteConfig(..., { client/server })` **deprecado**.
  - Padrão futuro: Vite plugin com `applyToEnvironment()` + `configEnvironment()`.

- **Hookable `callHook`**
  - Não depender de `.then()` / `.catch()` em `callHook`. Preferir `await`.

## Mandatory Rules

- Não introduzir código novo com APIs “legadas/ponte” (Bridge/Composition API antigo).
- Para hooks: sempre usar `await` (compatível com Nuxt 4 e pronto para Nuxt 5).
- Evitar config Vite “por ambiente” com flags antigas; usar plugin compatível com Env API.

## Reference

Leia `reference.md` para os snippets e checklists “copiar e colar”.
