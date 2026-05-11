## Nuxt Version Compatibility Guard — reference

### Nuxt 5 (Nitro v3) — mudanças que impactam “server code”

Quando você quer manter migração fácil para Nuxt 5, evite escrever código que:
- depende de propriedades Node-ish do event (preferir helpers / Web APIs)
- depende de `statusCode/statusMessage` em erros e redirects
- usa import paths antigos em módulos/plugins (quando você faz imports explícitos)

#### 0) Erros HTTP: `statusCode/statusMessage` → `status/statusText`

Para ter migração suave para Nuxt 5, **evite codar novos handlers** com `statusCode/statusMessage`.
Prefira este formato (Web standard):

```ts
throw createError({ status: 400, statusText: 'Bad request' })
```

Se você precisa manter compatibilidade com Nuxt 3/4 hoje, use um helper local que aceita ambos e normaliza no runtime.

#### 1) Route rules redirect: `statusCode` → `status`

Compat pattern (escreva **já** no formato novo, que funciona como intenção):

```ts
export default defineNuxtConfig({
  routeRules: {
    '/old': { redirect: { to: '/new', status: 302 } },
  },
})
```

#### 2) callHook: não usar `.then()`

```ts
// bom em Nuxt 4 e pronto para Nuxt 5
await nuxtApp.callHook('my:hook', data)
```

#### 3) Vite config por ambiente: evitar `extendViteConfig(..., { client/server })`

Preferir plugin com `applyToEnvironment`/`configEnvironment` (padrão do Nuxt 5):

```ts
// pseudo-exemplo: adaptar ao seu módulo/plugin
addVitePlugin(() => ({
  name: 'my-plugin',
  configEnvironment(name, config) {
    if (name === 'client') {
      config.optimizeDeps ||= {}
      config.optimizeDeps.include ||= []
      config.optimizeDeps.include.push('my-package')
    }
  },
  applyToEnvironment(env) {
    return env.name === 'client'
  },
}))
```

### Migration readiness checklist (para Nuxt 5)

- Não há `extendViteConfig` com `{ client/server }`
- Nenhum `callHook(...).then(...)`
- Redirect route rules usam `status`
- Código server não loga headers/body por padrão
- BFF sem proxy catch-all; endpoints allowlisted/handlers explícitos

