---
name: nuxt-5-performance-rendering
description: "Performance e rendering em Nuxt 5: routeRules, caching, payload minimization, lazy-loading, hydration e orçamento de JS (considerando mudanças do Nitro v3)."
license: UNLICENSED
---

# Nuxt 5 Performance & Rendering

## Workflow

1. Identifique modo (SSR/SSG/híbrido) e gargalo (TTFB, LCP, JS, hidratação, API).
2. Use `routeRules` para definir estratégia por rota (prerender/SWR/headers).
3. Minimize payload no server (BFF) e evite double fetch.
4. Aplique lazy-loading e adie hidratação onde fizer sentido.

## Defaults

- Otimize cache/payload primeiro.
- Em Nuxt 5, revalide comportamento de caching quando atualizar Nitro.

## Reference

Leia `reference.md`.
