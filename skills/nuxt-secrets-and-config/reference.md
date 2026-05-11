## Nuxt Secrets & Config — reference

### Checklist “copiar e colar”

- **Separação**
  - `runtimeConfig.public`: ok para browser
  - `runtimeConfig`: server-only

- **Regras**
  - Nunca versionar `.env`
  - Nunca colocar token em `nuxt.config.*`
  - Nunca colocar token em `app/**`

- **CI**
  - Rodar secret scan em PR
  - Bloquear merge se detectar tokens/keys

### Convenção de envs (exemplo)

```bash
EVENYX_API_BASE_URL="https://api.evenyx.io/v1"
EVENYX_API_V2_BASE_URL="https://api.evenyx.io/v2"

MERCHANT_EVENYX_BEARER_TOKEN="..."
MERCHANT_ACESSOTICKET_BEARER_TOKEN="..."
MERCHANT_SIGPASS_BEARER_TOKEN="..."
MERCHANT_SANDBOX_BEARER_TOKEN="..."
```

