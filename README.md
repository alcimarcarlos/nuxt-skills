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
| `amplify-nuxt-nitro-server` | AWS Amplify Gen 2 in Nitro: runWithAmplifyServerContext, H3 cookies, Cognito API routes. Trigger on server-side Amplify. |
| `amplify-nuxt-ssr-plugins` | AWS Amplify Gen 2 in Nuxt SSR: typed generateClient, useCookie, provide in useNuxtApp. Trigger on universal Amplify. |
| `nuxt-accessibility` | Web accessibility (a11y) in Nuxt & Vue: semantic HTML, keyboard focus, ARIA, contrast. Trigger on accessible UI. |
| `nuxt-auth-session` | Authentication & session in Nuxt: HttpOnly cookies, route middleware, CSRF, SSR isolation. Trigger on auth flows. |
| `nuxt-bff-hardening` | Hardens Nuxt Nitro BFF: removes catch-all proxies, input validation, rate limiting, error masking. Trigger on server/api. |
| `nuxt-ci-cd` | Nuxt CI/CD pipelines: quality gates, typechecking, Vitest tests, secret scanning, preview builds. Trigger on CI workflows. |
| `nuxt-code-generation-contract` | Mandatory output contract for Nuxt: directory layout, Zod schemas, SSR state matrices, Vitest. Trigger on feature generation. |
| `nuxt-core` | Nuxt 3/4/5 core patterns: directory conventions (app/ vs root), runtimeConfig, composables. Trigger on general Nuxt tasks. |
| `nuxt-data-fetching` | Data fetching in Nuxt: useAsyncData, useFetch, stable keys, deduplication, transform, SSR caching. Trigger on data fetching. |
| `nuxt-i18n` | Internationalization in Nuxt (@nuxtjs/i18n): localized routing, locale fallbacks, multilingual SEO. Trigger on multilingual apps. |
| `nuxt-modules-and-layers` | Scalable architecture in Nuxt: layers, custom modules, auto-imports, multi-app code sharing. Trigger on modular projects. |
| `nuxt-multitenant-merchants` | Multi-tenant architecture in Nuxt: merchant context resolution, branded styling, isolated state. Trigger on multi-tenant apps. |
| `nuxt-observability` | Observability in Nuxt: structured logging, correlation IDs, server/api metrics, error capture. Trigger on telemetry/monitoring. |
| `nuxt-performance-rendering` | Performance & rendering in Nuxt: routeRules, CDN caching, lazy hydration, payload optimization. Trigger on performance tuning. |
| `nuxt-privacy-lgpd` | Privacy & LGPD/GDPR in Nuxt: consent management, data minimization, cookie banners, audit trails. Trigger on compliance. |
| `nuxt-secret-scanning` | Secret scanning in Nuxt: prevents leaked API keys, trufflehog/gitleaks rules, runtimeConfig audit. Trigger on secret safety. |
| `nuxt-secrets-and-config` | Configuration & secrets in Nuxt: private vs public runtimeConfig, zero-secrets in bundles. Trigger on env config. |
| `nuxt-secure-logging` | Secure logging in Nuxt: redaction of tokens/PII, correlation IDs, masked stacktraces. Trigger on logging setup. |
| `nuxt-security` | OWASP hardening in Nuxt: CSP headers, secure cookies, SSR state isolation, CORS, rate limits. Trigger on security audits. |
| `nuxt-seo-meta` | SEO & metadata in Nuxt: useHead, useSeoMeta, canonical URLs, sitemaps, Open Graph tags. Trigger on SEO optimization. |
| `nuxt-server-api-nitro` | Nitro server/api routes in Nuxt: typed contracts, Zod validation, error handling, cookie session. Trigger on Nitro endpoints. |
| `nuxt-systematic-debugging` | Nuxt systematic debugging: minimal Vitest reproducers, SSR vs client isolation. Trigger when diagnosing bugs. |
| `nuxt-testing-quality` | Testing quality in Nuxt: Vitest, @nuxt/test-utils, Playwright E2E, CI quality gates. Trigger when writing tests. |
| `nuxt-uploads` | Secure file uploads in Nuxt: size/MIME validation, S3/R2 presigned URLs, abuse prevention. Trigger on upload endpoints. |
| `nuxt-version-compat-guard` | Version compatibility guard: prevents deprecated APIs across Nuxt 3, 4, and 5. Trigger on migration/upgrades. |

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
