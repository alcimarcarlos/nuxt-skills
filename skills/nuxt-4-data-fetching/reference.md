## Nuxt 4 Data Fetching — reference

### Padrão BFF em `server/api`

- Use quando precisar de segredo, normalização, rate limit ou cache.

### Exemplo de key estável

```ts
const route = useRoute()
const key = computed(() => `products:${route.params.slug}:${route.query.page ?? 1}`)
```

