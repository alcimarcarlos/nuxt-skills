---
name: nuxt-accessibility
description: "Web accessibility (a11y) in Nuxt & Vue: semantic HTML, keyboard focus, ARIA, contrast. Trigger on accessible UI."
license: UNLICENSED
---

# Nuxt Accessibility (a11y)

## Workflow

1. Identifique o tipo de UI: forms, modais, menus, listas, tabelas, toasts.
2. Garanta semântica HTML antes de ARIA (botões/links/cabeçalhos corretos).
3. Foco: ordem de tab, foco visível, trap de foco em modal, retorno de foco.
4. Teclado: navegação completa sem mouse, atalhos não conflitam.
5. Leitores de tela: labels, mensagens de erro, `aria-live` para feedback.
6. Verifique contraste e tamanhos de toque.

## Defaults

- Preferir elementos nativos (`button`, `a`, `input`, `label`) e atributos corretos.
- Form errors com associação (`aria-describedby`) e resumo quando útil.
- Modais: `role="dialog"`, `aria-modal="true"`, focus trap, ESC fecha.

## Anti-patterns

- `div` clicável sem `role`, sem `tabindex`, sem handlers de teclado.
- Placeholder como label.
- Remover outline sem substituir por foco visível.

## Reference

Leia `reference.md` para checklists copiáveis.
