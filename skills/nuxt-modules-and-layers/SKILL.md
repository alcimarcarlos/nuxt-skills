---
name: nuxt-modules-and-layers
description: "Scalable architecture in Nuxt: layers, custom modules, auto-imports, multi-app code sharing. Trigger on modular projects."
license: UNLICENSED
---

# Nuxt Modules & Layers

## Workflow

1. Identifique repetição: config duplicada, plugins repetidos, UI/feature comum.
2. Decida: extrair para **layer** (app internal) ou **module** (reutilizável).
3. Defina contratos: quais composables/components/runtimeConfig o layer expõe.
4. Controle dependências: evitar acoplamento circular, limitar “global magic”.
5. Documente convenções mínimas (readme do layer/module).

## Defaults

- Layer: para compartilhar **config + UI + features** dentro do monorepo.
- Module: para compartilhar integração “plugável” (config, runtime hooks, auto-imports).
- Evite “barrel exports” gigantes; prefira APIs pequenas e estáveis.

## Anti-patterns

- “God layer” com tudo dentro.
- Module que injeta comportamento crítico sem documentação e sem opt-out.
