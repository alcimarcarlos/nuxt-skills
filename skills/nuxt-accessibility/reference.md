## Nuxt 3 Accessibility — reference

### Checklist “copiar e colar”

- **Semântica**
  - `button` para ações, `a` para navegação real
  - `h1..h6` hierárquicos
  - `main`, `nav`, `header`, `footer` quando aplicável

- **Foco**
  - Foco visível (não remover outline sem alternativa)
  - Modal com focus trap + retorno ao gatilho
  - Skip link no topo (`Pular para conteúdo`)

- **Forms**
  - `label` associado ao `input`
  - Erro com `aria-describedby` apontando para texto de erro
  - Estado inválido: `aria-invalid="true"`

- **Feedback**
  - Toasts/mensagens importantes via `aria-live="polite"`/`assertive`

### Exemplo: input com erro acessível — copiar e colar

```vue
<template>
  <div>
    <label for="email">Email</label>
    <input
      id="email"
      v-model="email"
      type="email"
      autocomplete="email"
      :aria-invalid="!!error"
      :aria-describedby="error ? 'email-error' : undefined"
    />
    <p v-if="error" id="email-error" role="alert">{{ error }}</p>
  </div>
</template>
```

