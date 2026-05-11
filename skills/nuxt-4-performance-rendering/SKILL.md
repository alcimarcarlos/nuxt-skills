---
name: nuxt-4-performance-rendering
description: Performance e rendering em Nuxt 4: routeRules, caching, payload minimization, lazy-loading, hydration, imagens e orçamento de JS.
---

# Nuxt 4 Performance & Rendering

## Workflow

1. Identifique modo (SSR/SSG/híbrido) e gargalo (TTFB, LCP, JS, hidratação, API).
2. Use `routeRules` para escolher estratégia por rota (prerender, SWR, cache headers).
3. Minimize payload: transform/pick no server e no `useAsyncData`.
4. Aplique lazy-loading: componentes `Lazy*`, split de páginas, adiar hidratação quando fizer sentido.
5. Otimize imagens e fontes (compressão, tamanhos, preload seletivo).

## Defaults

- Otimize **cache + payload** antes de micro-otimizações.
- Use `routeRules` para híbrido intencional.

## Reference

Leia `reference.md`.

