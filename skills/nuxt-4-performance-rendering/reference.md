## Nuxt 4 Performance & Rendering — reference

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

---

### Exemplo: `routeRules` para híbrido intencional — copiar e colar

```ts
export default defineNuxtConfig({
  routeRules: {
    '/': { swr: 60 },
    '/docs/**': { prerender: true },
    '/app/**': { ssr: true, headers: { 'cache-control': 'no-store' } },
    '/api/**': { headers: { 'cache-control': 'no-store' } },
  },
})
```

