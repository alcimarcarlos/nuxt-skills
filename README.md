# Nuxt Skills

## Objetivo

Skills para Nuxt 3, Nuxt 4 e Nuxt 5 cobrindo arquitetura, SSR/Nitro, auth, data fetching, segurança, performance, i18n, acessibilidade, testes, SEO, uploads, observabilidade e Amplify Gen 2.

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

- Nuxt 3
- Nuxt 4
- Nuxt 5
- Vue
- Nitro
- TypeScript
- AWS Amplify Gen 2

## Como Escolher Skills

1. Leia `AGENTS.md` para as regras gerais da coleção.
2. Escolha a menor skill que cobre a tarefa.
3. Use `nuxt-version-compat-guard` como baseline quando a tarefa cruzar vários temas.
4. Leia `reference.md` apenas quando a skill ou a complexidade da tarefa pedir.
5. Valide com os comandos disponíveis no projeto alvo.

## Skills Disponíveis

| Skill | Quando usar |
| --- | --- |
| `amplify-nuxt-nitro-server` | Integra AWS Amplify Gen 2 em rotas e middleware Nitro (server/api, server/middleware) com contexto isolado por pedido: runWithAmplifyServerContext, cookies via H3Event, utilitário runAmplifyApi. Usar ao implementar server/api que chamam Auth/Data, proteger endpoints com sessão Cognito, endurecer BFF (validação, CORS, erros), otimizar middleware e queries, ou quando plugins Nuxt não aplicam ao diretório server/. |
| `amplify-nuxt-ssr-plugins` | Configura plugins Nuxt (.client/.server) para AWS Amplify Gen 2 com SSR: Amplify.configure(amplify_outputs), generateClient tipado, runWithAmplifyServerContext, cookies Cognito via useCookie e provide em useNuxtApp. Usar ao criar ou corrigir integração Amplify em Nuxt 3/4, erros "Library not configured", Data/Auth em useAsyncData, performance de cliente/SSR, superfície de auth/cookies, ou antes de tocar em server/api sem utilitário Nitro. |
| `nuxt-3-accessibility` | Acessibilidade em Nuxt 3 (a11y): semântica, foco, teclado, ARIA, contrastes, formulários, modais e validação contínua. |
| `nuxt-3-auth-session` | Padrões de autenticação e sessão em Nuxt 3: cookies HttpOnly, middleware, refresh/rotacionamento, CSRF/origin checks e proteção de rotas. |
| `nuxt-3-core` | Padrões essenciais de arquitetura e DX para Nuxt 3 (Nuxt app, runtimeConfig, rotas, composables, componentes, camadas), com foco em previsibilidade e manutenção. |
| `nuxt-3-data-fetching` | Padrões para fetching em Nuxt 3/4/5: useAsyncData/useFetch, chaves estáveis, cache, dedupe, transform/pick, erros e compatibilidade SSR. |
| `nuxt-3-i18n` | Internacionalização em Nuxt 3: estratégia de rotas/locales, fallback, formatação, SEO multi-língua e checklists de tradução. |
| `nuxt-3-modules-and-layers` | Produtividade e escala em Nuxt 3: layers, modules, auto-imports, organização de features, compartilhamento de código e governança de dependências. |
| `nuxt-3-observability` | Observabilidade em Nuxt 3: logging seguro, correlação, métricas de server/api, captura de erros SSR/client e hygiene de PII. |
| `nuxt-3-performance-rendering` | Performance e rendering em Nuxt 3/4/5: routeRules, caching, payload minimization, lazy-loading, hydration, imagens e orçamento de JS. |
| `nuxt-3-security` | Hardening OWASP para Nuxt 3/4/5 (SSR/SSG/híbrido): headers/CSP, cookies, SSR isolation, validação, rate limit, CORS e proteção de segredos (inclui notas para Nuxt 5/Nitro v3). |
| `nuxt-3-seo-meta` | SEO e metadados em Nuxt 3: useHead/useSeoMeta, SSR/SSG, canonical, robots, sitemap, open graph, i18n e performance de indexação. |
| `nuxt-3-server-api-nitro` | Boas práticas para `server/api` (Nitro/H3) em Nuxt 3/4/5: contratos, validação, errors, cookies, proxy seguro, caching e integração com serviços externos (compatível com Nitro v3 do Nuxt 5). |
| `nuxt-3-testing-quality` | Qualidade em Nuxt 3: estratégia de testes (unit/integration/e2e), contract tests de server/api, gates de CI (lint/typecheck/build) e prevenção de regressões. |
| `nuxt-3-uploads` | Uploads seguros em Nuxt 3: limites, validação, armazenamento (S3/R2), URLs assinadas, scanning e prevenção de abuso. |
| `nuxt-4-accessibility` | Acessibilidade em Nuxt 4 (a11y): semântica, foco, teclado, ARIA, contrastes, formulários, modais e validação contínua. |
| `nuxt-4-auth-session` | Padrões de autenticação e sessão em Nuxt 4: cookies HttpOnly, middleware, refresh/rotacionamento, CSRF/origin checks e proteção de rotas. |
| `nuxt-4-core` | Padrões essenciais de arquitetura e DX para Nuxt 4 (Nuxt app, runtimeConfig, rotas, composables, componentes, camadas), com foco em previsibilidade e manutenção. |
| `nuxt-4-data-fetching` | Padrões para fetching em Nuxt 4: useAsyncData/useFetch, chaves estáveis, cache, dedupe, transform/pick, erros e compatibilidade SSR. |
| `nuxt-4-i18n` | Internacionalização em Nuxt 4: estratégia de rotas/locales, fallback, formatação, SEO multi-língua e checklists de tradução. |
| `nuxt-4-modules-and-layers` | Produtividade e escala em Nuxt 4: layers, modules, auto-imports, organização de features e governança de dependências. |
| `nuxt-4-observability` | Observabilidade em Nuxt 4: logging seguro, correlação, métricas de server/api, captura de erros SSR/client e hygiene de PII. |
| `nuxt-4-performance-rendering` | Performance e rendering em Nuxt 4: routeRules, caching, payload minimization, lazy-loading, hydration, imagens e orçamento de JS. |
| `nuxt-4-security` | Hardening OWASP para Nuxt 4 (SSR/SSG/híbrido): headers/CSP, cookies, SSR isolation, validação, rate limit, CORS e proteção de segredos. |
| `nuxt-4-seo-meta` | SEO e metadados em Nuxt 4: useHead/useSeoMeta, canonical, robots, sitemap, open graph e SSR/SSG. |
| `nuxt-4-server-api-nitro` | Boas práticas para `server/api` (Nitro/H3) em Nuxt 4: contratos, validação, errors, cookies, proxy seguro, caching e integração com serviços externos. |
| `nuxt-4-testing-quality` | Qualidade em Nuxt 4: estratégia de testes (unit/integration/e2e), contract tests de server/api e gates de CI (lint/typecheck/build). |
| `nuxt-4-uploads` | Uploads seguros em Nuxt 4: limites, validação, armazenamento (S3/R2), URLs assinadas, scanning e prevenção de abuso. |
| `nuxt-5-accessibility` | Acessibilidade em Nuxt 5 (a11y): semântica, foco, teclado, ARIA, contrastes, formulários e modais (inclui cuidados SSR do Nuxt 5). |
| `nuxt-5-auth-session` | Padrões de autenticação e sessão em Nuxt 5 (Nitro v3): cookies HttpOnly, middleware, refresh/rotacionamento, CSRF/origin checks e proteção de rotas (com nota de imports explícitos do H3). |
| `nuxt-5-core` | Padrões essenciais de arquitetura e DX para Nuxt 5 (Nitro v3, Vite 6 env API): runtimeConfig, rotas, composables, server/api e práticas de migração. |
| `nuxt-5-data-fetching` | Padrões para fetching em Nuxt 5: useAsyncData/useFetch, chaves estáveis, cache, dedupe, transform/pick e SSR (com atenção a mudanças de infra do Nuxt 5). |
| `nuxt-5-i18n` | Internacionalização em Nuxt 5: estratégia de rotas/locales, fallback, formatação, SEO multi-língua e checklists de tradução. |
| `nuxt-5-modules-and-layers` | Produtividade e escala em Nuxt 5: layers, modules, auto-imports e governança de dependências (considerando Vite 6 env API e Nitro v3). |
| `nuxt-5-observability` | Observabilidade em Nuxt 5 (Nitro v3): logging seguro, correlação, métricas de server/api, captura de erros SSR/client e hygiene de PII. |
| `nuxt-5-performance-rendering` | Performance e rendering em Nuxt 5: routeRules, caching, payload minimization, lazy-loading, hydration e orçamento de JS (considerando mudanças do Nitro v3). |
| `nuxt-5-security` | Hardening OWASP para Nuxt 5 (Nitro v3): headers/CSP, cookies, SSR isolation, validação, rate limit, CORS, proteção de segredos e imports explícitos de H3 quando necessário. |
| `nuxt-5-seo-meta` | SEO e metadados em Nuxt 5: useHead/useSeoMeta, canonical, robots, sitemap, open graph e SSR/SSG/híbrido. |
| `nuxt-5-server-api-nitro` | Boas práticas para `server/api` (Nitro v3/H3) em Nuxt 5: contratos, validação, errors, cookies, proxy seguro, caching e integrações (imports explícitos quando auto-imports estiverem off). |
| `nuxt-5-testing-quality` | Qualidade em Nuxt 5: estratégia de testes (unit/contract/e2e), gates de CI e prevenção de regressões com foco em mudanças de infra do Nuxt 5. |
| `nuxt-5-uploads` | Uploads seguros em Nuxt 5 (Nitro v3): limites, validação, URLs assinadas, scanning e prevenção de abuso. |
| `nuxt-bff-hardening` | Prever/prevenir/corrigir riscos de BFF em Nuxt 3/4: remover proxy catch-all, aplicar allowlist, validação, timeouts, limites, rate limit, CORS e erros públicos seguros. |
| `nuxt-ci-cd` | CI/CD para Nuxt 2/3: quality gates (lint/typecheck/test/build), scanning de deps, ambientes, secrets, preview deploy e checklist de release. |
| `nuxt-multitenant-merchants` | Padrão multi-tenant por host em Nuxt 3/4: MerchantContext, separação public/private, BFF seguro, tipagem e governança de branding por tenant. |
| `nuxt-privacy-lgpd` | Conformidade e privacidade (LGPD) em apps Nuxt: minimização, consentimento, retenção, direitos do titular, cookies, logs, vendors e segurança operacional. |
| `nuxt-secret-scanning` | Prever/prevenir/corrigir vazamento de segredos em apps Nuxt: remoção de tokens do repo, padrões runtimeConfig, gitleaks/trufflehog, pre-commit e gates de CI. |
| `nuxt-secrets-and-config` | Governança de configuração e segredos em Nuxt 3/4: runtimeConfig, envs por ambiente, zero-secrets no client, secret scanning e padrões multi-tenant. |
| `nuxt-secure-logging` | Prever/prevenir/corrigir riscos de logging em Nuxt 3/4: remover logs ruidosos, evitar PII/tokens, correlation id, erros públicos seguros e observabilidade mínima. |
| `nuxt-version-compat-guard` | Evita implementar em Nuxt 3/4 coisas já descontinuadas em Nuxt 4/5. Use ao criar/refatorar features para manter retrocompatibilidade e reduzir custo de migração. |

## Qualidade e Validação

Execute o menor conjunto relevante que existir no projeto alvo:

- `npm run build`
- `npm run typecheck`
- `npm test`
- `npm run lint`
- `nuxi typecheck`

## Notas de Uso

- Confirme a versão real do Nuxt antes de escolher skills por versão.
- Use a menor skill aplicável e adicione nuxt-version-compat-guard para migrações ou compatibilidade.
- Use as skills Amplify apenas quando o projeto realmente usa Amplify Gen 2.

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
for d in skills/*; do
  name="$(basename "$d")"
  ln -sfn "../../skills/$name" ".cursor/skills/$name"
done
```

## Prompt Base

```text
Siga AGENTS.md, escolha a menor skill aplicável em skills/<nome>/SKILL.md e carregue reference.md somente se necessário.

Contexto:
- Stack: Nuxt 3, Nuxt 4, Nuxt 5, Vue, Nitro, TypeScript, AWS Amplify Gen 2
- Objetivo: <descreva a tarefa>
- Restrições: <auth, dados, UX, performance, compatibilidade>
- Validação esperada: <testes/build/lint>
```
