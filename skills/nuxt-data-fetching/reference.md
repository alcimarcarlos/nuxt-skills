## Nuxt 3 Data Fetching — reference

### Padrão de “BFF” em `server/api`

- Use quando:
  - precisa de segredo (API key)
  - precisa normalizar/filtrar payload
  - precisa rate limit / cache

### Exemplo de key estável

```ts
const route = useRoute()
const key = computed(() => `products:${route.params.slug}:${route.query.page ?? 1}`)
```

### Transform / pick

- Use para reduzir payload e “congelar” contrato pro client.
- Evite passar campos sensíveis por acidente.

