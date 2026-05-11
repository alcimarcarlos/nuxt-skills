## Nuxt Secret Scanning & Hygiene — reference

### Checklist “copiar e colar”

- **Detectar**
  - `rg "Bearer\\s+|recaptcha|apiKey|Authorization:"`
  - Auditar `nuxt.config.*` e `app/**`

- **Prevenir**
  - Secret scanner no CI (PR + schedule)
  - Hook pre-commit para bloquear padrões conhecidos
  - Documentar envs esperadas no README

- **Corrigir**
  - Remover segredos do código
  - Rotacionar/invalidar tokens
  - Revisar logs para vazamento

### Exemplo: gate simples (falhar se houver Bearer hardcoded)

```bash
rg -n "Bearer\\s+[A-Za-z0-9._-]{8,}" . && exit 1 || exit 0
```

### Sugestões de ferramentas

- **gitleaks**: bom para CI/pre-commit
- **trufflehog**: bom para varredura mais profunda

