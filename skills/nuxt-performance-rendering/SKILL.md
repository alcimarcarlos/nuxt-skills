---
name: nuxt-performance-rendering
description: "Performance e rendering em Nuxt (3/4/5)/4/5: routeRules, caching, payload minimization, lazy-loading, hydration, imagens e orçamento de JS."
license: UNLICENSED
---

# Nuxt Performance & Rendering (Nuxt 3/4/5)

## Workflow

1. Identifique modo (SSR/SSG/híbrido) e gargalo (TTFB, LCP, JS, hidratação, API).
2. Use `routeRules` para escolher estratégia por rota (prerender, SWR, cache headers).
3. Minimize payload: `pick`/transform no server e no `useAsyncData`.
4. Aplique lazy-loading: componentes `Lazy*`, split de páginas, adiar hidratação quando fizer sentido.
5. Otimize imagens e fontes (compressão, tamanhos, preload seletivo).

## Defaults

- Prefira otimização de **arquitetura de dados** (cache + payload) antes de micro-otimizações reativas.
- Use `routeRules` para **híbrido intencional** (não “SSR tudo” por padrão).
- Evite “double fetch” e refetch desnecessário.

## Anti-patterns

- Enviar objetos gigantes para o client quando só precisa de 5 campos.
- Hidratar widgets pesados “acima da dobra” sem necessidade.
- Fazer fetch no `mounted()` quando `useAsyncData` resolve SSR e cache.

## Reference

Leia `reference.md` para checklist e padrões.
