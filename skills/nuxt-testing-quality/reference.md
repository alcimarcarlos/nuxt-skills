## Nuxt 3 Testing & Quality — reference

### Gates recomendados (CI)

- `lint`
- `typecheck`
- `build`
- `test` (unit/contract)

### Foco por camada

- **Composables**: unit (puro) + mock de `$fetch`/clients quando necessário
- **Componentes**: rendering + estados (loading/error/empty)
- **Server/api**: contract tests (auth/validação/status/body)
- **E2E**: smoke por fluxo crítico (login + principal jornada)

