---
name: amplify-nuxt-nitro-server
description: "Integra AWS Amplify Gen 2 em rotas e middleware Nitro (server/api, server/middleware) com contexto isolado por pedido: runWithAmplifyServerContext, cookies via H3Event, utilitário runAmplifyApi. Usar ao implementar server/api que chamam Auth/Data, proteger endpoints com sessão Cognito, endurecer BFF (validação, CORS, erros), otimizar middleware e queries, ou quando plugins Nuxt não aplicam ao diretório server/."
license: UNLICENSED
disable-model-invocation: true
---

# Amplify Gen 2 + Nuxt — Nitro (`server/`)

## Complementar com outras skills

- **Backend Gen 2** (`amplify/`, Lambdas, regras Data): **[amplify-workflow](https://github.com/awslabs/agent-plugins/tree/main/plugins/aws-amplify/skills/amplify-workflow)** (awslabs/agent-plugins). Esta skill cobre apenas **Nitro** (`server/`) com cookies e `runWithAmplifyServerContext`.

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

## Performance (resumo)

- **Por pedido**: manter construção de adapter e `libraryOptions` a partir de `event`; cachear só valores **imutáveis** do projeto (config parseada de `amplify_outputs`), nunca estado de sessão.
- **AppSync**: pedidos com seleção mínima de campos; usar paginação em listas; evitar N+1 de várias rotas internas quando um único handler pode compor a resposta.
- **Middleware global**: se só uma fração das rotas precisa de sessão, restringir o middleware a prefixos (`/api/protected/*`) para não correr `fetchAuthSession` em cada asset ou health check.

## Segurança (resumo)

- Validar **corpo, query e cabeçalhos** antes de encaminhar para AppSync ou Storage; tratar o handler como BFF, não como proxy transparente.
- Respostas **401/403** sem expor motivos internos (grupos, claims, nomes de recursos AWS) em produção.
- Rotas públicas (`server/api` sem auth): revisão explícita de rate limit, tamanho de payload e tipos MIME aceites.

## Verificação rápida

- [ ] Nenhum import direto de `aws-amplify/auth` (sem `/server`) em ficheiros sob `server/`.
- [ ] Nenhuma suposição de `useNuxtApp()` ou `useCookie()` de plugins — usar apenas APIs Nitro/h3 no handler.
- [ ] Operações Amplify sempre dentro de `runAmplifyApi` (ou equivalente) por pedido.
- [ ] Respostas de erro não expõem detalhes internos de Cognito/AppSync em produção.
- [ ] Performance: middleware/session só onde necessário; queries Data paginadas ou limitadas.
- [ ] Segurança: inputs validados; sem tokens em logs; endpoints sensíveis não são proxy aberto.

## Referência

- Padrão oficial, exemplos de rota e links: [reference.md](reference.md)
