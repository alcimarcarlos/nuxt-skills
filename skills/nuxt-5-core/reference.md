## Nuxt 5 Core — reference

### Checklist rápido

- **Config**: `runtimeConfig` privado vs `runtimeConfig.public`, `routeRules`, módulos.
- **Nitro v3**: se auto-imports estiverem desabilitados, importe utilitários explicitamente de `h3`.
- **Vite 6 env API**: prefira configurações compartilhadas e plugins compatíveis com múltiplos ambientes.
- **SSR isolation**: evitar mutáveis em escopo de módulo.

### Snippet: imports explícitos (quando necessário)

```ts
import { getQuery, getRouterParams, readBody, getHeader, setHeader, setCookie, createError } from 'h3'
```

