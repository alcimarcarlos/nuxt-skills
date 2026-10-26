---
name: nuxt-i18n
description: "Internacionalização em Nuxt (3/4/5): estratégia de rotas/locales, fallback, formatação, SEO multi-língua e checklists de tradução."
license: UNLICENSED
---

# Nuxt i18n

## Workflow

1. Defina idiomas suportados e a estratégia de URL (prefixo por locale ou domínio).
2. Defina fallback (ex: `pt-BR` -> `pt` -> `en`) e política para chaves faltantes.
3. Padronize formatação: datas, moeda, números, pluralização.
4. SEO: `hreflang`, canonical por locale, rotas indexáveis corretamente.
5. Qualidade: auditoria de strings hardcoded e chaves órfãs.

## Defaults

- Strings em UI nunca hardcoded em componentes “core”.
- Separar conteúdo “copy” (marketing) de strings de produto quando fizer sentido.
- Testar layout com strings longas (alemão) e RTL (quando aplicável).

## Anti-patterns

- Montar frases concatenando tokens (quebra pluralização/ordem).
- Não ter fallback definido e quebrar SSR.

## Reference

Leia `reference.md` para checklists copiáveis.
