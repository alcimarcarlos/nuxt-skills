## Nuxt 3 i18n — reference

### Checklist “copiar e colar”

- **Locales**
  - Lista de `locales` e `defaultLocale`
  - Fallback chain (ex: `pt-BR` -> `pt` -> `en`)
  - Política de missing keys (log em dev, não quebrar prod)

- **Formato**
  - `Intl.DateTimeFormat` / `Intl.NumberFormat`
  - Moeda consistente por locale
  - Pluralização via lib i18n (não concatenação)

- **SEO**
  - `hreflang` configurado
  - `noindex` para rotas privadas
  - Canonical por locale

### Snippet: formatação com Intl — copiar e colar

```ts
export function formatMoney(value: number, locale: string, currency: string) {
  return new Intl.NumberFormat(locale, { style: 'currency', currency }).format(value)
}
```

