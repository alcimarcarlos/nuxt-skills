# Referência — Amplify Gen 2 + Nuxt (SSR e Nitro)

## Documentação oficial (prioridade)

| Tópico | URL |
|--------|-----|
| Índice Amplify para LLMs (`llms.txt`) | https://docs.amplify.aws/ai/llms.txt |
| Skill oficial Amplify Gen 2 (backend, `ampx`, multi-framework) | https://github.com/awslabs/agent-plugins/tree/main/plugins/aws-amplify/skills/amplify-workflow |
| Data a partir do runtime servidor Nuxt (Gen 2) | https://docs.amplify.aws/javascript/build-a-backend/data/connect-from-server-runtime/nuxtjs-server-runtime/ |
| Categorias Amplify no Nuxt 3 (Vue — exemplos amplos) | https://docs.amplify.aws/vue/frontend/server-side-rendering/nuxt/ |
| SSR genérico (contexto) | https://docs.amplify.aws/javascript/frontend/server-side-rendering/ |
| Regras de autorização Data (deny-by-default) | https://docs.amplify.aws/react/build-a-backend/data/customize-authz/ |
| Segredos e variáveis (Gen 2) | https://docs.amplify.aws/react/deploy-and-host/fullstack-branching/secrets-and-vars/ |
| Boas práticas de segurança Amplify Hosting | https://docs.aws.amazon.com/amplify/latest/userguide/security-best-practices.html |
| Library not configured | https://docs.amplify.aws/javascript/build-a-backend/troubleshooting/library-not-configured/ |
| Nuxt — documentação geral | https://nuxt.com/docs/getting-started/introduction |
| Amplify UI (Vue) | https://ui.docs.amplify.aws/vue/getting-started/introduction |

## Gen 2 Data vs guias Vue com `aws-amplify/api`

- O guia **Nuxt.js server runtime** (JavaScript, Gen 2) usa `generateClient` de **`aws-amplify/data`** e **`aws-amplify/data/server`**, com `amplify_outputs.json`.
- O guia **Vue / Nuxt 3** em alguns exemplos usa **`aws-amplify/api`** e `generateClient<Schema>()` com o mesmo `outputs`; é válido noutros contextos, mas **para Data Gen 2** o projeto deve seguir **um** modelo consistente (preferir `aws-amplify/data` quando o backend for `defineData` Gen 2).
- **Gen 1** (`amplifyconfiguration.json`, documentação sob `/gen1/`) não deve ser misturado com Gen 2 no mesmo skill path salvo migração explícita.

## Plugins: nomes e ordem

- Prefixo numérico (`01.`, `02.`) controla a ordem de registo: https://nuxt.com/docs/guide/directory-structure/plugins#registration-order
- `.client.ts` e `.server.ts`: https://nuxt.com/docs/guide/directory-structure/plugins
- `enforce: 'pre'` nos plugins Amplify para configurar antes do restante código da aplicação.

## Cookies Cognito e SSR

- A documentação AWS constrói nomes de cookies a partir de `CognitoIdentityServiceProvider.<userPoolClientId>.LastAuthUser` e tokens associados.
- Usar `useCookie` **no `setup()` do plugin** para mapear nome → ref e evitar **cross-request pollution**.
- Opções típicas: `sameSite: 'lax'` (ou `strict` se o fluxo permitir), `secure: true` em HTTPS, `expires` alinhado à política de refresh (exemplo na doc: ~30 dias).
- Se o adapter **não** implementar `set`, tokens refrescados no servidor podem não voltar ao browser; avaliar implementação completa do adapter conforme o guia.

## Nitro: `server/api` e `server/middleware`

- O ambiente `server/` **não** herda plugins Nuxt; é necessário ficheiro utilitário (ex.: `server/utils/amplifyUtils.ts`) que:
  - recebe `H3Event`;
  - cria `CookieStorage.Adapter` com `parseCookies`, `setCookie`, `deleteCookie`;
  - monta `keyValueStorage`, token provider, credentials provider;
  - exporta `runAmplifyApi(event, (contextSpec) => …)` chamando `runWithAmplifyServerContext`.
- Exemplo oficial: rota `server/api/current-user.ts` com `getCurrentUser` de `aws-amplify/auth/server` dentro de `runAmplifyApi`.

## Nuxt 3 vs Nuxt 4 — guards de runtime

- Documentação AWS ainda mostra `process.client` nalguns exemplos Vue.
- Em Nuxt 3.14+ e Nuxt 4, preferir **`import.meta.client`** / **`import.meta.server`** quando o projeto já adotar esse padrão, mantendo a mesma lógica Amplify.

## Performance

- **Bundle**: importar apenas `aws-amplify/*` necessários por ficheiro; evitar barris personalizados que reexportem todo o SDK para a árvore do cliente.
- **Hidratação**: dados obtidos no SSR devem hidratar o estado inicial sem segundo round-trip idêntico no cliente (padrões Nuxt de `useAsyncData` com payload partilhado); evitar `refreshNuxtData` em cascata em cada `onMounted` sem debounce.
- **AppSync**: listagens com paginação (`nextToken`) em vez de pedir coleções completas; filtrar no servidor com índices/schema em vez de filtrar grandes listas só no browser.
- **Auth**: `fetchAuthSession` tem custo — cachear o resultado **dentro do mesmo pedido** de render (por exemplo composable por request) quando vários componentes precisam da mesma sessão, sem partilhar entre pedidos.

## Segurança (checklist)

- Nunca commitar `amplify_outputs.json` com dados sensíveis se a política do repositório proibir; em muitos projetos o ficheiro é gerado no CI — seguir convenção do repositório alvo.
- Não colocar segredos de OAuth ou chaves em variáveis de ambiente de build em texto claro; usar [Secrets](https://docs.amplify.aws/react/deploy-and-host/fullstack-branching/secrets-and-vars/) no backend Amplify e `secret()` na definição de recursos.
- Em hosting no domínio `amplifyapp.com`, avaliar prefixo `__Host-` em cookies sensíveis (ver user guide AWS link acima).
- Garantir que operações `list`/`get`/`mutation` usam o **`authMode`** correto para cada regra (`userPool`, `identityPool`, `apiKey`, etc.).
- **CSRF**: para mutações sensíveis via cookies de sessão no mesmo domínio, alinhar com a política do projeto (SameSite, tokens anti-CSRF em formulários, ou BFF que só aceita pedidos same-origin).
- **XSS**: tratar conteúdo vindo de Data como não confiável até sanitizado; o Cognito não substitui escaping em templates Vue.
- **Redirects**: após login/logout, usar URLs relativas ou allowlist de destinos para evitar open redirect.

## Limitações conhecidas (doc e runtime)

- **`onMounted`**: só corre no cliente; sessão ou listagens Amplify necessárias no HTML inicial têm de ser obtidas no **servidor de render** (plugin `.server.ts` + `runWithAmplifyServerContext`) ou via `useAsyncData` / `useFetch` que chamem código já contextualizado — ver discussões em [aws-amplify/docs](https://github.com/aws-amplify/docs) sobre guias Nuxt/SSR.
- **Versão do SDK**: comparar exemplos da AWS com a versão de `aws-amplify` no `package.json`; APIs e paths (`aws-amplify/data` vs `aws-amplify/api`) evoluem entre releases.
- **Duas fontes de verdade**: alterações em `amplify/data/resource.ts` exigem `npx ampx sandbox` (ou pipeline) para regenerar `amplify_outputs.json` antes de alinhar tipos `Schema` no Nuxt.

## Disclaimer da AWS

Os guias Nuxt declaram que os exemplos **podem não refletir as melhores práticas** de cada projeto; complementar sempre com convenções locais (estrutura de pastas, testes E2E de sessão, lint).
