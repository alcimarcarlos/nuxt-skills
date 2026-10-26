---
name: nuxt-testing-quality
description: "Qualidade em Nuxt (3/4/5): estratégia de testes (unit/integration/e2e), contract tests de server/api, gates de CI (lint/typecheck/build) e prevenção de regressões."
license: UNLICENSED
---

# Nuxt Testing & Quality

## Workflow

1. Classifique risco e camada: composable puro, componente, página, server/api.
2. Defina o tipo de teste mínimo que previne regressão (unit -> integration -> e2e).
3. Para `server/api`: teste contrato (status, shape, validações, auth).
4. Adicione gates: lint + typecheck + build + tests (onde aplicável).
5. Garanta que erros não vazem detalhes sensíveis em SSR/server.

## Defaults

- Preferir testes de **contrato** para endpoints e **composables** para lógica.
- Evitar testes frágeis acoplados a markup irrelevante.
- Tipagem (TS) como primeira linha de defesa.

## Anti-patterns

- “E2E pra tudo” sem cobertura de unit/contract: lento e frágil.
- Testes que dependem de rede real/credenciais reais por padrão.

## Reference

Leia `reference.md`.
