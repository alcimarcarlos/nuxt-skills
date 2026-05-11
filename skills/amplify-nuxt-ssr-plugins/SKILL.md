---
name: amplify-nuxt-ssr-plugins
description: >-
  Configura plugins Nuxt (.client/.server) para AWS Amplify Gen 2 com SSR:
  Amplify.configure(amplify_outputs), generateClient tipado, runWithAmplifyServerContext,
  cookies Cognito via useCookie e provide em useNuxtApp. Usar ao criar ou corrigir
  integração Amplify em Nuxt 3/4, erros "Library not configured", Data/Auth em
  useAsyncData, ou antes de tocar em server/api sem utilitário Nitro.
disable-model-invocation: true
---

# Amplify Gen 2 + Nuxt — plugins SSR

## Quando usar

- Criar ou alterar ficheiros em `plugins/` para Amplify com **renderização universal** (mesmo código no servidor e no cliente).
- Corrigir `NoCredentials`, library não configurada, ou chamadas Amplify no servidor sem contexto isolado.
- Preparar `useNuxtApp().$Amplify` como API única para páginas e composables.

## Pré-requisitos no projeto

- `amplify_outputs.json` na raiz do app Nuxt (ou caminho acordado no projeto), gerado pelo backend Gen 2.
- Dependência `aws-amplify` compatível com o backend; para Data Gen 2 seguir o guia que usa `aws-amplify/data` e `aws-amplify/data/server` (ver referência).
- Tipos `Schema` de `#/amplify/data/resource` ou caminho que o projeto use.

## Fluxo obrigatório

1. **Cliente** — ficheiro `plugins/01.amplify-apis.client.ts` (ou nome já usado no projeto; manter prefixo numérico baixo e `enforce: 'pre'`):
   - Importar `outputs` de `amplify_outputs.json`.
   - Chamar `Amplify.configure(outputs, { ssr: true })` no setup do plugin (ou condição `import.meta.client` / `process.client` alinhada à versão Nuxt do projeto).
   - Criar `generateClient<Schema>()` a partir de `aws-amplify/data` (Gen 2 Data) **ou** seguir o padrão do repositório se ainda usar `aws-amplify/api` por migração incremental.
   - `provide`: expor objeto estável (por exemplo `Amplify: { Auth: {…}, GraphQL/Data: { client } }`) para `useNuxtApp().$Amplify`.

2. **Servidor (render Nuxt)** — `plugins/01.amplify-apis.server.ts`:
   - `parseAmplifyConfig(outputs)`; construir storage a partir de `useCookie` para todos os cookies Cognito necessários (incluindo `LastAuthUser` e tokens), no **setup** do plugin para evitar mistura entre pedidos.
   - `createKeyValueStorageFromCookieStorageAdapter`, `createUserPoolsTokenProvider`, `createAWSCredentialsAndIdentityIdProvider`, `libraryOptions`.
   - Importar **apenas** APIs de `aws-amplify/auth/server`, `aws-amplify/data/server` (ou `storage/server` conforme necessidade).
   - Cada chamada envolve `runWithAmplifyServerContext(amplifyConfig, libraryOptions, (contextSpec) => api(contextSpec, …))`.
   - Opcional: implementar `set` no adapter de cookies para que refresh de tokens no SSR propague `Set-Cookie` ao cliente (ver referência).

3. **Ordem de plugins** — numerar para carregar antes de middleware que dependa de `$Amplify` (por exemplo `02.*` para redirects).

4. **Nitro (`server/`)** — **não** usar estes plugins dentro de `server/api` ou `server/middleware`. Criar utilitário `runAmplifyApi(event, op)` com cookies a partir de `H3Event` (`parseCookies`, `setCookie`, `deleteCookie`). Detalhes e exemplos: [reference.md](reference.md).

## Verificação rápida

- [ ] Cliente: `Amplify.configure` com `{ ssr: true }` antes de qualquer operação Amplify.
- [ ] Servidor: zero imports de `aws-amplify/auth` sem sufixo `/server` em ficheiros `.server.ts`.
- [ ] Todas as chamadas server-side dentro de `runWithAmplifyServerContext`.
- [ ] Cookies: `secure: true` em produção; `sameSite` alinhado ao fluxo de auth (lax/strict conforme risco).
- [ ] `authMode` das operações Data alinhado às regras do schema AppSync.

## Referência

- Links oficiais, diferenças Gen 1/Gen 2, Nitro e notas Nuxt 4: [reference.md](reference.md)
