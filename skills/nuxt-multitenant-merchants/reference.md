## Nuxt Multi-tenant Merchants — reference

### Checklist “copiar e colar”

- **Tenant resolution**
  - Allowlist (ex: `evenyx`, `acessoticket`, `sigpass`)
  - Tratamento de ambientes (`sandbox`, `staging`)

- **Config**
  - Public: logo, favicon, SEO, gtag, links
  - Private: bearer token, API keys

- **Server**
  - `event.context.merchant` tipado
  - Endpoints usam `merchant.secret` apenas server-side

### Exemplo: tipo do contexto

```ts
export type MerchantPublic = {
  name: string
  origin: string
  favIcon?: string
  gtag?: string
  seoMeta?: { title: string; description: string; url: string; image?: string }
}

export type MerchantSecret = {
  bearerToken: string
  api: string
  apiV2: string
}

export type MerchantContext = {
  tenant: string
  public: MerchantPublic
  secret: MerchantSecret
}
```

