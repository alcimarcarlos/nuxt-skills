# Referência — Amplify no Nitro (Nuxt `server/`)

## Documentação oficial

| Tópico | URL |
|--------|-----|
| Nuxt.js server runtime (Gen 2 Data, plugins + Nitro) | https://docs.amplify.aws/javascript/build-a-backend/data/connect-from-server-runtime/nuxtjs-server-runtime/ |
| Vue / Nuxt — utilitário `amplifyUtils` e `server/api/current-user` | https://docs.amplify.aws/vue/frontend/server-side-rendering/nuxt/ |
| `runWithAmplifyServerContext` (conceito) | https://docs.amplify.aws/javascript/frontend/server-side-rendering/ |
| Regras de autorização Data | https://docs.amplify.aws/react/build-a-backend/data/customize-authz/ |
| Troubleshooting library not configured | https://docs.amplify.aws/javascript/build-a-backend/troubleshooting/library-not-configured/ |

## Esqueleto do utilitário (conceito)

O handler Nitro recebe `H3Event`. O adapter de cookies:

- **get(name)** — lê de `parseCookies(event)` (ou mapa atualizado se guardar mutações em memória durante o pedido).
- **set(name, value, options)** — `setCookie(event, name, value, options)` para propagar tokens ao cliente quando aplicável.
- **delete(name)** — `deleteCookie(event, name)`.
- **getAll()** — lista de pares nome/valor para compatibilidade com o adapter Amplify.

`parseAmplifyConfig(outputs)` deve usar o mesmo `amplify_outputs.json` que o cliente.

## Data Gen 2 no Nitro

- Cliente tipado: `aws-amplify/data` + `generateClient<Schema>()`.
- Servidor: `aws-amplify/data/server` + `generateClient({ config: amplifyConfig })`; cada chamada a `models.*` ou `graphql` deve receber **`contextSpec`** como primeiro argumento, dentro de `runWithAmplifyServerContext`.
- Alinhar **`authMode`** com as regras do schema (user pool, identity pool, API key, etc.).

## Auth no Nitro

- `getCurrentUser`, `fetchAuthSession`, `fetchUserAttributes` de `aws-amplify/auth/server` apenas dentro do contexto isolado.
- Para apenas validar presença de sessão em middleware, `fetchAuthSession` costuma ser suficiente; mapear `session.tokens === undefined` para 401/403 conforme política do projeto.

## Armadilhas

- **Estado global** entre pedidos: não guardar `LibraryOptions` ou clientes Amplify em variáveis mutáveis partilhadas com dados do pedido anterior; construir por `event` (ou por função pura a partir de `event`).
- **Ler cookies só no início**: se `getAll` do adapter for apenas leitura do snapshot inicial, tokens atualizados durante o mesmo pedido podem não refletir; seguir o padrão da doc AWS para o adapter do projeto.
- **CORS e cookies**: rotas `server/api` chamadas de outros origens exigem configuração explícita de CORS e credenciais; não é específico Amplify mas bloqueia auth por cookie em SPAs noutro domínio.

## Relação com `amplify-nuxt-ssr-plugins`

- **Plugins**: SSR universal em `pages/` e composables com `useNuxtApp().$Amplify`.
- **Nitro**: mesma `amplifyConfig`, mas **outro** pipeline de cookies (`event`). Manter os dois consistentes (nomes de cookie, `secure`, `sameSite`).
