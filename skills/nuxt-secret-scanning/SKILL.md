---
name: nuxt-secret-scanning
description: Prever/prevenir/corrigir vazamento de segredos em apps Nuxt: remoção de tokens do repo, padrões runtimeConfig, gitleaks/trufflehog, pre-commit e gates de CI.
---

# Nuxt Secret Scanning & Hygiene

## Workflow (Predict → Prevent → Correct)

1. **Predict**
   - Buscar por `Bearer `, `apiKey`, `recaptcha`, `token`, `secret`, `Authorization:` no repo.
   - Auditar `nuxt.config.*` e `app/**` (client) com prioridade.
2. **Prevent**
   - Padrão: segredos só via `runtimeConfig` privado.
   - CI: secret scanning em PR + schedule.
   - Pre-commit: bloquear commits com segredos.
3. **Correct**
   - Rotacionar tokens vazados.
   - Remover do histórico se necessário (política do time).
   - Adicionar regressão: teste/checagem que falha se `runtimeConfig.public` contiver chaves proibidas.

## Mandatory Requirements

- Nunca versionar `.env`.
- Nunca colocar bearer tokens em `runtimeConfig.public` ou em `app/**`.
- Rotacionar qualquer token encontrado no git.

## Reference

Leia `reference.md` para comandos e templates.

