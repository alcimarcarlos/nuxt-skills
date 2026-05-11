## Nuxt 5 Security — reference

### Nota (Nitro v3): imports explícitos

Se seu setup desabilitar auto-imports, importe utilitários explicitamente:

```ts
import { setCookie, getHeader, setHeader, createError } from 'h3'
```

### Exemplo: `nuxt-security` (baseline) — copiar e colar

```ts
export default defineNuxtConfig({
  modules: ['nuxt-security'],
  security: {
    headers: {
      referrerPolicy: 'no-referrer',
      xContentTypeOptions: 'nosniff',
    },
    requestSizeLimiter: {
      maxRequestSizeInBytes: 1_000_000,
      maxUploadFileRequestInBytes: 5_000_000,
    },
  },
})
```

