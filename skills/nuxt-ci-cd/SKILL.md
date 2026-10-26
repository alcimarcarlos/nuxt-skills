---
name: nuxt-ci-cd
description: "Standardizes CI/CD pipelines for Nuxt: quality gates (linting, typechecking, Vitest tests, build checks), dependency scanning, environment secret governance, preview deployments, and release checklists."
license: UNLICENSED
---

# Nuxt CI/CD

## Workflow

1. Defina gates mínimos: lint, typecheck, tests, build.
2. Garanta caches: pnpm/yarn/npm cache + cache de build quando seguro.
3. Segurança: audit de dependências, SAST básico, checagem de headers/CSP em preview.
4. Ambientes: dev/staging/prod com secrets separados; configurar `runtimeConfig` por ambiente.
5. Deploy: preview por PR + produção com tags/releases.

## Defaults

- Falhar o pipeline se `lint`, `typecheck` ou `build` falhar.
- Rodar scans de dependências em PR e em schedule.
- Nunca expor secrets em logs.

## Anti-patterns

- Deploy sem build verificado.
- Mesmos secrets para staging e prod.
- Sem preview deploy: bugs de SSR e headers passam.

## Reference

Leia `reference.md` para checklists copiáveis e exemplos de pipeline.
