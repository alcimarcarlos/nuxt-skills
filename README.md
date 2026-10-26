# Nuxt Skills

## Objetivo

Coleção modular e portátil de skills para **Nuxt 3, Nuxt 4 e Nuxt 5** cobrindo arquitetura, SSR/Nitro, auth, contratos de geração de código, data fetching, segurança, performance, i18n, acessibilidade, testes, SEO, uploads, observabilidade e Amplify Gen 2.

Este pacote não é uma aplicação final. Ele é uma coleção portátil de instruções para agentes de código trabalharem em projetos reais com padrões consistentes.

## Compatibilidade

| Agente | Entrada recomendada |
| --- | --- |
| Cursor | `.cursor/rules/skills.mdc` e aliases em `.cursor/skills/<skill-name>` |
| Codex | `skills/<skill-name>/SKILL.md` ou cópia/symlink em `$CODEX_HOME/skills` |
| Claude Code | `CLAUDE.md`, depois `skills/<skill-name>/SKILL.md` |
| GitHub Copilot | `.github/copilot-instructions.md`, apontando para `AGENTS.md` e `skills/` |

## Estrutura

- `AGENTS.md`: instruções operacionais para agentes.
- `CLAUDE.md`: ponto de entrada curto para Claude Code.
- `.cursor/rules/skills.mdc`: regra de descoberta para Cursor.
- `.cursor/skills/<skill-name>`: symlink para `skills/<skill-name>`.
- `.github/copilot-instructions.md`: instruções curtas para GitHub Copilot.
- `skills/<skill-name>/SKILL.md`: fonte canônica da skill.
- `skills/<skill-name>/reference.md`: detalhes carregados somente quando a skill pedir.

## Stack Coberta

- Nuxt 3, Nuxt 4 e Nuxt 5
- Vue 3
- Nitro
- TypeScript
- AWS Amplify Gen 2

## Como Escolher Skills

1. Leia `AGENTS.md` para as regras gerais da coleção.
2. Adote `nuxt-code-generation-contract` para definir entregas completas (árvore, tipos, testes e estados).
3. Use `nuxt-version-compat-guard` como baseline quando a tarefa cruzar versões ou arquiteturas legadas.
4. Escolha a skill de domínio mais específica (`nuxt-data-fetching`, `nuxt-security`, `nuxt-server-api-nitro`, etc.).
5. Leia `reference.md` apenas quando a skill ou a complexidade da tarefa pedir.
6. Valide com os comandos disponíveis no projeto alvo (`npx nuxi typecheck`, `npm test`).

## Skills Disponíveis (24 skills canônicas)

| Skill | Quando usar |
| --- | --- |
| `amplify-nuxt-nitro-server` | Integra AWS Amplify Gen 2 em rotas e middleware Nitro (server/api, server/middleware) com contexto isolado por pedido: runWithAmplifyServerContext, cookies via H3Event, utilitário runAmplifyApi. Usar ao implementar server/api que chamam Auth/Data, proteger endpoints com sessão Cognito, endurecer BFF (validação, CORS, erros), otimizar middleware e queries, ou quando plugins Nuxt não aplicam ao diretório server/. |
| `amplify-nuxt-ssr-plugins` | Configura plugins Nuxt (.client/.server) para AWS Amplify Gen 2 com SSR: Amplify.configure(amplify_outputs), generateClient tipado, runWithAmplifyServerContext, cookies Cognito via useCookie e provide em useNuxtApp. Usar ao criar ou corrigir integração Amplify em Nuxt 3/4, erros \"Library not configured\", Data/Auth em useAsyncData, performance de cliente/SSR, superfície de auth/cookies, ou antes de tocar em server/api sem utilitário Nitro. |
| `nuxt-accessibility` | Acessibilidade em Nuxt (3/4/5) (a11y): semântica, foco, teclado, ARIA, contrastes, formulários, modais e validação contínua. |
| `nuxt-auth-session` | Padrões de autenticação e sessão em Nuxt (3/4/5): cookies HttpOnly, middleware, refresh/rotacionamento, CSRF/origin checks e proteção de rotas. |
| `nuxt-bff-hardening` | Prever/prevenir/corrigir riscos de BFF em Nuxt 3/4: remover proxy catch-all, aplicar allowlist, validação, timeouts, limites, rate limit, CORS e erros públicos seguros. |
| `nuxt-ci-cd` | CI/CD para Nuxt 2/3: quality gates (lint/typecheck/test/build), scanning de deps, ambientes, secrets, preview deploy e checklist de release. |
| `nuxt-code-generation-contract` | Enforces a mandatory output contract for Nuxt (3/4/5) and Vue 3 code generation, ensuring directory structure, Nitro BFF boundaries, typed contracts, SSR state matrices, and security baselines. Trigger when implementing any Nuxt page, component, composable, or server/api endpoint. |
| `nuxt-core` | Padrões essenciais de arquitetura e DX para Nuxt (3/4/5) (Nuxt app, runtimeConfig, rotas, composables, componentes, camadas), com foco em previsibilidade e manutenção. |
| `nuxt-data-fetching` | Padrões para fetching em Nuxt (3/4/5)/4/5: useAsyncData/useFetch, chaves estáveis, cache, dedupe, transform/pick, erros e compatibilidade SSR. |
| `nuxt-i18n` | Internacionalização em Nuxt (3/4/5): estratégia de rotas/locales, fallback, formatação, SEO multi-língua e checklists de tradução. |
| `nuxt-modules-and-layers` | Produtividade e escala em Nuxt (3/4/5): layers, modules, auto-imports, organização de features, compartilhamento de código e governança de dependências. |
| `nuxt-multitenant-merchants` | Padrão multi-tenant por host em Nuxt 3/4: MerchantContext, separação public/private, BFF seguro, tipagem e governança de branding por tenant. |
| `nuxt-observability` | Observabilidade em Nuxt (3/4/5): logging seguro, correlação, métricas de server/api, captura de erros SSR/client e hygiene de PII. |
| `nuxt-performance-rendering` | Performance e rendering em Nuxt (3/4/5)/4/5: routeRules, caching, payload minimization, lazy-loading, hydration, imagens e orçamento de JS. |
| `nuxt-privacy-lgpd` | Conformidade e privacidade (LGPD) em apps Nuxt: minimização, consentimento, retenção, direitos do titular, cookies, logs, vendors e segurança operacional. |
| `nuxt-secret-scanning` | Prever/prevenir/corrigir vazamento de segredos em apps Nuxt: remoção de tokens do repo, padrões runtimeConfig, gitleaks/trufflehog, pre-commit e gates de CI. |
| `nuxt-secrets-and-config` | Governança de configuração e segredos em Nuxt 3/4: runtimeConfig, envs por ambiente, zero-secrets no client, secret scanning e padrões multi-tenant. |
| `nuxt-secure-logging` | Prever/prevenir/corrigir riscos de logging em Nuxt 3/4: remover logs ruidosos, evitar PII/tokens, correlation id, erros públicos seguros e observabilidade mínima. |
| `nuxt-security` | Hardening OWASP para Nuxt (3/4/5)/4/5 (SSR/SSG/híbrido): headers/CSP, cookies, SSR isolation, validação, rate limit, CORS e proteção de segredos (inclui notas para Nuxt 5/Nitro v3). |
| `nuxt-seo-meta` | SEO e metadados em Nuxt (3/4/5): useHead/useSeoMeta, SSR/SSG, canonical, robots, sitemap, open graph, i18n e performance de indexação. |
| `nuxt-server-api-nitro` | Boas práticas para `server/api` (Nitro/H3) em Nuxt (3/4/5)/4/5: contratos, validação, errors, cookies, proxy seguro, caching e integração com serviços externos (compatível com Nitro v3 do Nuxt 5). |
| `nuxt-testing-quality` | Qualidade em Nuxt (3/4/5): estratégia de testes (unit/integration/e2e), contract tests de server/api, gates de CI (lint/typecheck/build) e prevenção de regressões. |
| `nuxt-uploads` | Uploads seguros em Nuxt (3/4/5): limites, validação, armazenamento (S3/R2), URLs assinadas, scanning e prevenção de abuso. |
| `nuxt-version-compat-guard` | Evita implementar em Nuxt 3/4 coisas já descontinuadas em Nuxt 4/5. Use ao criar/refatorar features para manter retrocompatibilidade e reduzir custo de migração. |

## Instalação por Symlink

Para Codex:

```bash
mkdir -p "$HOME/.codex/skills"
for d in skills/*; do
  name="$(basename "$d")"
  ln -sfn "$(pwd)/$d" "$HOME/.codex/skills/$name"
done
```

Para Claude Code:

```bash
mkdir -p "$HOME/.claude/skills"
for d in skills/*; do
  name="$(basename "$d")"
  ln -sfn "$(pwd)/$d" "$HOME/.claude/skills/$name"
done
```

Para Cursor em um projeto consumidor:

```bash
mkdir -p .cursor/skills
for d in /caminho/para/nuxt-skills/skills/*; do
  name="$(basename "$d")"
  ln -sfn "$d" ".cursor/skills/$name"
done
```
