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
| `amplify-nuxt-nitro-server` | Integrates AWS Amplify Gen 2 in Nitro routes and middleware (server/api, server/middleware) with isolated request context: runWithAmplifyServerContext, cookies via H3Event, and runAmplifyApi utility. Use for server/api with Auth/Data, Cognito-protected endpoints, and BFF hardening. |
| `amplify-nuxt-ssr-plugins` | Configures Nuxt plugins (.client/.server) for AWS Amplify Gen 2 with SSR: Amplify.configure(amplify_outputs), typed generateClient, runWithAmplifyServerContext, Cognito cookies via useCookie, and provide in useNuxtApp. Use for universal rendering and data fetching. |
| `nuxt-accessibility` | Ensures web accessibility (a11y) in Nuxt 3/4/5 and Vue: semantic HTML, focus management, keyboard navigation, ARIA attributes, color contrast, accessible forms, modals, and continuous automated auditing. |
| `nuxt-auth-session` | Implements authentication and session management in Nuxt 3/4/5: HttpOnly cookies, route middleware guards, refresh/rotation flows, CSRF and origin validation, and SSR session isolation. |
| `nuxt-bff-hardening` | Hardens Nuxt Backend-For-Frontend (BFF) server routes in Nitro: removes catch-all proxies, enforces payload allowlists, validation schemas, timeouts, rate limiting, secure public error masking, and CORS controls. |
| `nuxt-ci-cd` | Standardizes CI/CD pipelines for Nuxt: quality gates (linting, typechecking, Vitest tests, build checks), dependency scanning, environment secret governance, preview deployments, and release checklists. |
| `nuxt-code-generation-contract` | Enforces a mandatory output contract for Nuxt (3/4/5) and Vue 3 code generation, ensuring directory structure, Nitro BFF boundaries, typed contracts, SSR state matrices, and security baselines. Trigger when implementing any Nuxt page, component, composable, or server/api endpoint. |
| `nuxt-core` | Core architectural patterns and DX for Nuxt 3/4/5: directory conventions (app/ vs root), runtimeConfig, routes, composables, components, layers, and migration standards. |
| `nuxt-data-fetching` | Data fetching patterns in Nuxt 3/4/5: useAsyncData, useFetch, stable deduplication keys, cache management, payload transforms/pick, error handling, and SSR compatibility. |
| `nuxt-i18n` | Internationalization in Nuxt 3/4/5 (@nuxtjs/i18n): localized routing strategies, fallback locales, formatting, multilingual SEO, and translation workflow checklists. |
| `nuxt-modules-and-layers` | Scalable project architecture in Nuxt 3/4/5: layers, custom modules, auto-imports, feature-based directory organization, shared cross-project code, and dependency governance. |
| `nuxt-multitenant-merchants` | Host-based multi-tenant architecture in Nuxt: MerchantContext resolution, public/private state separation, secure Nitro BFF, tenant-scoped branding, and typed configurations. |
| `nuxt-observability` | Observability and telemetry in Nuxt 3/4/5: structured logging, request correlation IDs, server/api metrics, SSR/client error capture, and PII redaction. |
| `nuxt-performance-rendering` | Performance optimization and rendering modes in Nuxt 3/4/5: routeRules, caching headers, payload size minimization, lazy hydration, image optimization, and JavaScript bundle budgeting. |
| `nuxt-privacy-lgpd` | Privacy, GDPR, and LGPD compliance in Nuxt: data minimization, consent management, retention policies, data subject rights, cookie banners, log hygiene, and vendor privacy audits. |
| `nuxt-secret-scanning` | Prevents and remediates secret leakage in Nuxt: removes committed secrets, enforces runtimeConfig patterns, git pre-commit hooks, trufflehog/gitleaks scanning, and CI secret gates. |
| `nuxt-secrets-and-config` | Governance of configuration and environment variables in Nuxt: runtimeConfig, multi-environment setups, zero-secrets in client bundles, and multi-tenant config management. |
| `nuxt-secure-logging` | Secure logging practices in Nuxt: eliminates noisy logs, redacts credentials and PII, adds correlation IDs, masks internal error stacks in production, and standardizes structured output. |
| `nuxt-security` | OWASP security hardening for Nuxt 3/4/5: HTTP security headers, CSP, secure cookie flags, SSR cross-request state leak isolation, input validation, rate limiting, and CORS. |
| `nuxt-seo-meta` | Search Engine Optimization (SEO) and metadata in Nuxt 3/4/5: useHead, useSeoMeta, SSR/SSG rendering, canonical URLs, robots.txt, sitemaps, Open Graph tags, and indexing performance. |
| `nuxt-server-api-nitro` | Best practices for server/api routes in Nitro (H3) for Nuxt 3/4/5: typed contracts, request validation, secure error responses, cookie handling, BFF proxying, and external service caching. |
| `nuxt-testing-quality` | Testing and quality assurance in Nuxt 3/4/5: test pyramid strategy (unit, component, and E2E), server/api contract tests with @nuxt/test-utils and Vitest, and CI quality gates. |
| `nuxt-uploads` | Secure file upload handling in Nuxt: file size/MIME limits, validation, cloud storage (S3/R2), presigned upload URLs, virus/malware scanning, and abuse prevention. |
| `nuxt-version-compat-guard` | Guards against deprecated APIs and features across Nuxt 3, 4, and 5: ensures future compatibility, smooth migration paths, and prevents tech debt. |

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
