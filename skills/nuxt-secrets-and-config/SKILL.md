---
name: nuxt-secrets-and-config
description: "Governance of configuration and environment variables in Nuxt: runtimeConfig, multi-environment setups, zero-secrets in client bundles, and multi-tenant config management."
license: UNLICENSED
---

# Nuxt Secrets & Config

## Workflow

1. Inventarie configs: o que é **público** (branding, gtag, recaptcha site key) vs **privado** (tokens, API keys).
2. Garanta que segredos estejam **somente** em `runtimeConfig` privado e carregados via ambiente (CI/hosting).
3. Proíba segredos em:
   - `runtimeConfig.public`
   - composables/client
   - arquivos versionados
4. Adicione bloqueios:
   - secret scanning (CI + pre-commit)
   - code review checklist
5. Multi-tenant: separar `merchantPublic` vs `merchantSecret` e resolver por host no server.

## Defaults

- `runtimeConfig.public`: apenas valores que podem ir para o browser.
- Tokens de upstream: **somente server-side** (Nitro handlers).
- “Um arquivo por segredo” não; use variáveis bem nomeadas e padronizadas por tenant.

## Anti-patterns

- Token hardcoded em `nuxt.config.ts`/composables.
- “Um proxy genérico” que injeta bearer token em qualquer path.
- Logs com env/config.

## Reference

Leia `reference.md` para checklists copiáveis.
