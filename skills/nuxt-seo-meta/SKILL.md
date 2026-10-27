---
name: nuxt-seo-meta
description: "SEO & metadata in Nuxt: useHead, useSeoMeta, canonical URLs, sitemaps, Open Graph tags. Trigger on SEO optimization."
license: UNLICENSED
---

# Nuxt SEO & Meta

## Workflow

1. Identifique se a rota é indexável e qual estratégia (SSR/SSG/prerender).
2. Defina `title`, `description`, `og:*`, `twitter:*`, `canonical` e `robots` por página.
3. Garanta consistência de URLs (trailing slash, redirects 301).
4. Gere sitemap/robots quando aplicável e valide com ambiente de preview.
5. Evite conteúdo “vazio” em SSR (dados críticos devem renderizar server-side).

## Defaults

- Preferir `useSeoMeta`/`useHead` na página (ou composable dedicado) com contratos claros.
- Sempre setar canonical em páginas públicas importantes.
- Rotas privadas devem ser `noindex`.

## Anti-patterns

- Metas definidas apenas no client (impacta crawler).
- Conteúdo principal dependente de fetch apenas client-side em rota indexável.
