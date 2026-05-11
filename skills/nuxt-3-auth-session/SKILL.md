---
name: nuxt-3-auth-session
description: Padrões de autenticação e sessão em Nuxt 3: cookies HttpOnly, middleware, refresh/rotacionamento, CSRF/origin checks e proteção de rotas.
---

# Nuxt 3 Auth & Session

## Workflow

1. Escolha modelo: sessão opaca (recomendado) vs JWT. Prefira sessão opaca + cookie HttpOnly.
2. Defina endpoints internos em `server/api/auth/*` (login, logout, me, refresh).
3. Padronize cookie: `HttpOnly`, `Secure` (prod), `SameSite`, `Path=/`, nome com `__Host-` quando possível.
4. Proteja rotas com `route middleware` (client) + checagem server-side real (nunca confiar só no client).
5. Defina expiração/rotação: curta no access, refresh com rotação e revogação.

## Defaults

- **Sem tokens no client**: nada de `localStorage`.
- **Sessão opaca**: cookie referencia uma sessão armazenada no server (DB/Redis) ou backend dedicado.
- **Origin checks** em mutações cookie-based (mitiga CSRF por navegadores modernos).

## Anti-patterns

- Guardar JWT long-lived no client.
- “Auth só no middleware do client”.
- Cookies sem `Secure`/`HttpOnly`/`SameSite` em produção.

## Reference

Leia `reference.md` para exemplos copiar-e-colar.

