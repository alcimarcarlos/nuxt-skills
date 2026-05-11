## Nuxt 4 Core — reference

### Checklist rápido

- **Config**: `nuxt.config.ts` define `runtimeConfig` (privado/público), `modules`, `routeRules`, `nitro` e `imports` conforme padrão local.
- **Rotas**: `pages/` e `definePageMeta` (layout/middleware/seo).
- **State SSR-safe**: `useState` (por-key) para state compartilhado; evitar mutáveis em escopo de módulo.
- **Data**: `useAsyncData`/`useFetch` com `key` estável; sanitizar payload; tratar erro.
- **Server**: `server/api/*` como BFF para segredos, normalização e policy.

### Padrões recomendados

- **Runtime config**
  - Segredos: `runtimeConfig.<private>`
  - Exposição permitida: `runtimeConfig.public`

- **Composables**
  - `useXxx()` deve ser “thin”: orquestra estado, chama server/api, expõe API clara.
  - Evite `watch` “solto”; prefira `computed` e callbacks explícitos.

- **Pages**
  - Página é composição de componentes + binding de estado, não “camada de domínio”.

### Snippets úteis

Exemplo de estado SSR-safe:

```ts
export function useCartState() {
  const items = useState('cart:items', () => [] as Array<{ id: string; qty: number }>)
  const count = computed(() => items.value.reduce((n, it) => n + it.qty, 0))
  return { items, count }
}
```

