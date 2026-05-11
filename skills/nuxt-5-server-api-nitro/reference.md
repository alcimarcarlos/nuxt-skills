## Nuxt 5 Server API (Nitro) — reference

### Nota (Nitro v3): imports explícitos

```ts
import { getQuery, getRouterParams, readBody, HTTPError } from 'nitro/h3'
```

### Padrão de erro HTTP (Nuxt 5 / h3 v2)

Em server routes, prefira `HTTPError` com `status/statusText`:

```ts
export default defineEventHandler(() => {
  throw new HTTPError({ status: 400, statusText: 'Bad request' })
})
```

Nota:
- No lado Vue (`app/`), `createError` do Nuxt continua sendo o padrão para erros “de app”.

