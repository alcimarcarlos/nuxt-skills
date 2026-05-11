# Instruções do agente — Amplify Gen 2 + Nuxt

Este ficheiro complementa as skills **Nuxt** deste repositório quando o trabalho envolve **AWS Amplify Gen 2** (Data, Auth, Storage, Functions) em aplicações **Nuxt** (SSR universal e Nitro).

## Princípios

- Tratar **Amplify Gen 2** como padrão: backend em TypeScript (`amplify/`), artefato `amplify_outputs.json` no frontend. Não misturar fluxos Gen 1 (`amplifyconfiguration.json`, CLI legado) salvo quando o repositório alvo for explicitamente legado.
- Respeitar a separação **Nuxt app (plugins, pages, composables)** versus **Nitro (`server/`)**: plugins Nuxt não executam dentro de `server/api` ou `server/middleware`; lá é obrigatório contexto isolado com cookies do `H3Event`.
- Usar a **menor skill aplicável** ao ficheiro ou tarefa; combinar skills apenas quando o trabalho cruzar domínios (por exemplo, SSR + autorização de schema + Nitro).
- Antes de alterar um projeto real, ler padrões existentes: `nuxt.config`, plugins `01.*`, `server/utils`, versão do Nuxt e de `aws-amplify`.
- Ao concluir, indicar comandos de validação executados ou pendentes (build, typecheck, testes, sandbox Amplify).

## Estrutura deste repositório (Amplify)

- `AGENTS.md`: governança global e ordem de decisão (este ficheiro).
- `README.md`: catálogo de todas as skills, incluindo Nuxt e Amplify.
- `skills/<nome>/SKILL.md`: fluxo principal e gatilhos por tema.
- `skills/<nome>/reference.md`: detalhes, links oficiais e armadilhas.

## Ordem de decisão

1. O código corre em **`server/`** (rotas API, middleware Nitro, cron jobs)?  
   → Skill **`amplify-nuxt-nitro-server`** (`runAmplifyApi` / `runWithAmplifyServerContext` com cookies do `H3Event`). Para contexto cruzado com a app universal, alinhar com **`amplify-nuxt-ssr-plugins`**.

2. O código corre em **plugins, pages, layouts, composables** com renderização universal?  
   → Skill `amplify-nuxt-ssr-plugins` como base.

3. Envolve **cookies Cognito, sessão, redirects, middleware de rota**?  
   → Skill `amplify-nuxt-ssr-plugins` + regras de segurança do projeto; consultar [Security best practices for Amplify](https://docs.aws.amazon.com/amplify/latest/userguide/security-best-practices.html) para hosting e cookies.

4. Envolve **regras de acesso ao Data (AppSync)**?  
   → Alinhar cliente e servidor com o schema (deny-by-default); ver [Customize your auth rules](https://docs.amplify.aws/react/build-a-backend/data/customize-authz/).

5. Envolve **segredos ou variáveis de build**?  
   → Segredos via console/sandbox e `secret()` no backend; não colocar valores sensíveis em environment variables de build (ver [Secrets and environment vars](https://docs.amplify.aws/react/deploy-and-host/fullstack-branching/secrets-and-vars)).

## Compatibilidade (Cursor, Codex, Copilot)

- **Cursor**: skills em `skills/<nome>/`; invocar pelo nome da skill ou pelo contexto do ficheiro. Para convenção `.cursor/skills/`, pode fazer symlink a partir de `skills/<nome>/`.
- **Codex / outros agentes**: copiar ou sincronizar pastas de skills para `.agents/skills/` no projeto consumidor, conforme a convenção da ferramenta.
- **GitHub Copilot**: manter `AGENTS.md` na raiz; opcionalmente um `.github/copilot-instructions.md` curto que remeta a este ficheiro e às skills relevantes (evitar ficheiros de instruções demasiado longos para code review).

## Barra mínima de qualidade

- `Amplify.configure` com `{ ssr: true }` no cliente, o mais cedo possível no ciclo de vida; evitar chamadas a APIs Amplify antes da configuração.
- No servidor Nuxt (render): apenas imports `aws-amplify/<categoria>/server` e execução dentro de `runWithAmplifyServerContext`.
- No Nitro: utilitário baseado em `H3Event` que cria storage a partir dos cookies do pedido; nunca reutilizar estado global de pedido a pedido.
- Tipagem com `Schema` gerado a partir de `amplify/data/resource` quando o projeto usar Amplify Data Gen 2.
- Documentar limitações conhecidas da doc AWS (ex.: exemplos com `process.client` vs `import.meta.client` em Nuxt 4).
