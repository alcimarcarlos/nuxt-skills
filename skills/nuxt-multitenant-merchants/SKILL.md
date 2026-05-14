---
name: nuxt-multitenant-merchants
description: "Padrão multi-tenant por host em Nuxt 3/4: MerchantContext, separação public/private, BFF seguro, tipagem e governança de branding por tenant."
license: UNLICENSED
---

# Nuxt Multi-tenant Merchants

## Workflow

1. Defina o identificador de tenant (host/subdomínio) e uma allowlist de tenants suportados.
2. Separe **config pública** (brand/SEO) da **config secreta** (tokens).
3. No server: resolver `MerchantContext` por request e anexar a `event.context`.
4. No client: expor apenas `merchantPublic`.
5. No BFF: cada endpoint usa `merchantSecret` apenas no server e só para recursos allowlisted.

## Defaults

- Tenant resolution: `getRequestURL(event).host` + parsing determinístico.
- `MerchantContext` tipado (sem `any`).
- Branding em `runtimeConfig.public.merchants` ok; segredos em env/private.

## Anti-patterns

- Repetir mapa de merchant no client com tokens.
- Proxy catch-all com bearer token.
- Tenant aceitando qualquer string sem validação.

## Reference

Leia `reference.md`.
