## Nuxt CI/CD — reference

### Checklist “copiar e colar”

- **Quality gates**
  - `lint`
  - `typecheck`
  - `test` (unit/contract quando existir)
  - `build`

- **Segurança**
  - Dependency audit (PR + schedule)
  - Bloquear secrets em logs
  - Validar headers/CSP em preview (smoke)

- **Ambientes**
  - `runtimeConfig` por env
  - Secrets separados por env
  - Rotação de secrets

- **Deploy**
  - Preview deploy por PR
  - Smoke test pós-deploy (home + rota crítica + auth, se houver)

### Exemplo de comandos padrão (ajuste ao seu package manager)

```bash
npm ci
npm run lint
npm run typecheck
npm test
npm run build
```

