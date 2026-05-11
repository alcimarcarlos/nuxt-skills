## Nuxt 3 Uploads — reference

### Checklist (copiar e colar)

- **Limites**
  - Max size por arquivo (ex: 5–20MB)
  - Max count por request
  - Rate limit por IP/user
  - Timeout do request (server)

- **Validação**
  - Allowlist de MIME (`image/jpeg`, `image/png`, `application/pdf`, etc.)
  - Nome do arquivo: normalize (sem path), limite de tamanho, sem caracteres suspeitos
  - Nunca confiar em “extension”

- **Storage**
  - Preferir URL assinada (PUT) e depois confirmar no server
  - ACL mínima (private por padrão)
  - Separar buckets/prefixos por ambiente (`dev/staging/prod`)

- **Abuso**
  - Quota por usuário/tenant
  - Scan antivírus (assíncrono) quando necessário
  - Remover EXIF de imagens se houver risco de geolocalização

---

### Exemplo: endpoint que cria “intenção” de upload (server/api) — copiar e colar

Padrão: client pede permissão, server valida, devolve “upload plan”.

`server/api/uploads/init.post.ts`:

```ts
import { z } from 'zod'

const Body = z.object({
  filename: z.string().min(1).max(180),
  mime: z.string().min(1).max(100),
  size: z.number().int().positive().max(20_000_000),
})

const ALLOWED_MIME = new Set(['image/jpeg', 'image/png', 'application/pdf'])

function safeName(input: string) {
  // simplista: em produção, refine conforme suas regras
  return input.replaceAll('\\', '/').split('/').pop()!.replace(/[^\w.\-]/g, '_')
}

export default defineEventHandler(async (event) => {
  const body = Body.parse(await readBody(event))
  if (!ALLOWED_MIME.has(body.mime)) {
    throw createError({ statusCode: 415, statusMessage: 'Unsupported media type' })
  }

  const filename = safeName(body.filename)
  const key = `uploads/${crypto.randomUUID()}-${filename}`

  // TODO: gerar URL assinada no seu provider (S3/R2/etc)
  // const { url, headers } = await signPutUrl({ key, mime: body.mime, size: body.size })

  return {
    key,
    // url,
    // headers,
  }
})
```

> Nota Nuxt 5 (Nitro v3/h3 v2): em server routes, use `status/statusText` (ex.: `HTTPError`).

### Exemplo: upload via server/api (fallback) — copiar e colar

Se você aceitar upload pelo server, imponha limite de tamanho e valide content-type.
Em produção, prefira **streaming** e limites no proxy/edge também.

