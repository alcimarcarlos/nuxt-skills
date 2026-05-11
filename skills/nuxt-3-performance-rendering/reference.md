## Nuxt 3 Performance & Rendering — reference

### Checklist

- **Route strategy**
  - Rotas estáticas: prerender/SSG
  - Rotas “quase estáticas”: SWR/ISR (quando suportado pela infra)
  - Rotas privadas/personalizadas: SSR com cache seletivo (se possível)

- **Data**
  - `useAsyncData`/`useFetch` com `key` estável
  - Transformar e reduzir payload antes de enviar ao client

- **UI**
  - `Lazy*` para componentes abaixo da dobra
  - Evitar listas gigantes sem virtualização

- **Hydration**
  - Adiar hidratação de componentes não críticos (quando aplicável)
  - Remover dependências pesadas do bundle principal

- **Assets**
  - Otimização de imagens (formatos modernos, tamanhos responsivos)
  - Preload apenas do crítico

---

### Exemplo: `routeRules` para híbrido intencional — copiar e colar

`nuxt.config.ts`:

```ts
export default defineNuxtConfig({
  routeRules: {
    // Home: quase estática (cache no CDN / stale-while-revalidate)
    '/': { swr: 60 },

    // Conteúdo: pré-gerar quando possível (deploy-time)
    '/docs/**': { prerender: true },

    // Área autenticada: SSR (sem cache público)
    '/app/**': { ssr: true, headers: { 'cache-control': 'no-store' } },

    // API proxy interna (Nitro): nunca cachear pelo browser
    '/api/**': { headers: { 'cache-control': 'no-store' } },
  },
})
```

### Exemplo: cache-control por endpoint server-side — copiar e colar

Em handlers de `server/api`, você pode setar headers explicitamente:

```ts
export default defineEventHandler(async (event) => {
  setHeader(event, 'cache-control', 'public, max-age=0, s-maxage=60, stale-while-revalidate=300')
  return { ok: true }
})
```

### Exemplo: reduzir payload no server (BFF) — copiar e colar

```ts
type UpstreamUser = { id: string; email: string; name: string; roles: string[]; ssn?: string }

export default defineEventHandler(async () => {
  const user = await $fetch<UpstreamUser>('https://upstream.exemplo.com/me', { timeout: 5000 })
  return { id: user.id, name: user.name, roles: user.roles } // nunca retornar campos sensíveis
})
```

