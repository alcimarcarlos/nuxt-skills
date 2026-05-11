## Nuxt 5 Auth & Session — reference

### Nota (Nitro v3): imports explícitos

Se seu setup desabilitar auto-imports, importe utilitários explicitamente:

```ts
import { readBody, setCookie, createError, getHeader } from 'h3'
```

### Checklist (copiar e colar)

- Cookies HttpOnly + Secure (prod) + SameSite + Path=/
- Endpoints internos `server/api/auth/*`
- Middleware de rota (client) + checagem server-side real

