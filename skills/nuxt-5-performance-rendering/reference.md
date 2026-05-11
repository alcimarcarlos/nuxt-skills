## Nuxt 5 Performance & Rendering — reference

### Checklist

- `routeRules` por rota (prerender/SWR/SSR/no-store)
- Payload minimization no BFF
- Lazy components e hidratação atrasada quando aplicável

### Exemplo: `routeRules` — copiar e colar

```ts
export default defineNuxtConfig({
  routeRules: {
    '/': { swr: 60 },
    '/app/**': { headers: { 'cache-control': 'no-store' } },
  },
})
```

