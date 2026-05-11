---
name: amplify-nuxt-nitro-server
description: >-
  Integra AWS Amplify Gen 2 em rotas e middleware Nitro (server/api, server/middleware)
  com contexto isolado por pedido: runWithAmplifyServerContext, cookies via H3Event,
  utilitário runAmplifyApi. Usar ao implementar server/api que chamam Auth/Data,
  proteger endpoints com sessão Cognito, ou quando plugins Nuxt não aplicam ao
  diretório server/.
disable-model-invocation: true
---

# Amplify Gen 2 + Nuxt — Nitro (`server/`)

## Quando usar

- Ficheiros em `server/api/**`, `server/routes/**`, `server/middleware/**`, ou utilitários em `server/utils/**` que precisem de **Auth** ou **Data** Amplify.
- Proteger rotas HTTP com base em `fetchAuthSession` / `getCurrentUser` no servidor.
- Evitar duplicar lógica de cookies já descrita para plugins; aqui a fonte de verdade é o **`H3Event`** do pedido Nitro.

## Princípio

Os **plugins Nuxt** (`.server.ts` na raiz da app) **não** correm no runtime Nitro dos handlers. É obrigatório um **módulo utilitário** que receba `event` e invoque `runWithAmplifyServerContext` com um adapter de cookies derivado de `parseCookies` / `setCookie` / `deleteCookie`.

## Fluxo obrigatório

1. **Criar** `server/utils/amplifyUtils.ts` (ou nome acordado no projeto) que exporte:
   - `createCookieStorageAdapter(event)` → objeto compatível com `createKeyValueStorageFromCookieStorageAdapter`;
   - `createLibraryOptions(event)` → `tokenProvider` + `credentialsProvider`;
   - `runAmplifyApi(event, (contextSpec) => …)` → delega em `runWithAmplifyServerContext(amplifyConfig, createLibraryOptions(event), operation)`.

2. **Importar** apenas APIs de `aws-amplify/<categoria>/server` dentro do callback passado a `runAmplifyApi`.

3. **Em** `server/api/*.ts`: `defineEventHandler(async (event) => { … await runAmplifyApi(event, (ctx) => getCurrentUser(ctx)); })`.

4. **Middleware global Nitro** (opcional): em `server/middleware/*.ts`, validar sessão antes de rotas sensíveis; devolver 401/403 com `setResponseStatus` quando não houver tokens válidos.

5. **Data Gen 2**: usar `generateClient` de `aws-amplify/data/server` dentro de `runAmplifyApi` quando o guia do projeto seguir o stack Data (ver [reference.md](reference.md)).

## Verificação rápida

- [ ] Nenhum import direto de `aws-amplify/auth` (sem `/server`) em ficheiros sob `server/`.
- [ ] Nenhuma suposição de `useNuxtApp()` ou `useCookie()` de plugins — usar apenas APIs Nitro/h3 no handler.
- [ ] Operações Amplify sempre dentro de `runAmplifyApi` (ou equivalente) por pedido.
- [ ] Respostas de erro não expõem detalhes internos de Cognito/AppSync em produção.

## Referência

- Padrão oficial, exemplos de rota e links: [reference.md](reference.md)
