## Nuxt Secure Logging — reference

### Checklist “copiar e colar”

- **Remover**
  - `console.log` em hooks de fetch (`onRequest`, `onResponse`)
  - logs de headers/body/cookies

- **Adicionar**
  - correlation id por request
  - redaction de campos sensíveis
  - erro público seguro (`statusMessage` genérico)

### Snippet: redaction simples

```ts
const SENSITIVE_KEYS = new Set(['authorization', 'cookie', 'set-cookie', 'password', 'token', 'accesstoken'])

export function redact(obj: Record<string, unknown>) {
  const out: Record<string, unknown> = {}
  for (const [k, v] of Object.entries(obj)) {
    out[k] = SENSITIVE_KEYS.has(k.toLowerCase()) ? '[redacted]' : v
  }
  return out
}
```

