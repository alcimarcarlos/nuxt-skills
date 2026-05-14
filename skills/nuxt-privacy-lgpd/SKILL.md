---
name: nuxt-privacy-lgpd
description: "Conformidade e privacidade (LGPD) em apps Nuxt: minimização, consentimento, retenção, direitos do titular, cookies, logs, vendors e segurança operacional."
license: UNLICENSED
---

# Nuxt Privacy & LGPD

## Workflow

1. Inventariar dados: quais campos PII, base legal, finalidade, onde trafega e onde persiste.
2. Minimização: coletar/armazenar apenas o necessário; reduzir payloads no BFF (`server/api`).
3. Consentimento: separar cookies essenciais vs analytics/marketing; registrar consentimento.
4. Retenção: definir TTL por categoria e rotinas de expurgo; backups e logs também entram.
5. Direitos do titular: exportação, correção, exclusão, revogação de consentimento.
6. Vendors: mapear terceiros (analytics, payments, chat), DPAs e transferência internacional.

## Defaults

- **Deny by default** para trackers: só ativar após consentimento.
- Logs não devem conter PII/tokens por padrão.
- `runtimeConfig.public` não deve conter identificadores sensíveis.

## Anti-patterns

- “Logar tudo” em produção (inclui e-mails, tokens, payloads).
- Compartilhar dados pessoais com vendors sem consentimento/base legal.
- Sem política de retenção (dados ficam eternamente).

## Reference

Leia `reference.md` para checklists e snippets.
