## Nuxt Privacy & LGPD — reference

### Checklist “copiar e colar”

- **Inventário de dados**
  - Campos PII (ex: nome, email, telefone, documento, endereço, IP)
  - Finalidade e base legal por campo
  - Onde coleta (page/form), onde processa (`server/api`), onde armazena (DB, cache, logs)

- **Minimização**
  - Payloads reduzidos no server (retornar só campos necessários)
  - Evitar enviar PII em querystring

- **Cookies**
  - Separar: essenciais (sessão) vs não essenciais (analytics)
  - Consentimento explícito para não essenciais
  - Registro do consentimento (timestamp + versão + categorias)

- **Logs/observabilidade**
  - Não logar body/headers por padrão
  - Remover/mascarar email, telefone, documento
  - Correlation id no lugar de PII

- **Retenção**
  - TTL por categoria (ex: sessões, eventos, uploads temporários)
  - Expurgo automático + auditoria de expurgo

- **Direitos do titular**
  - Endpoint/processo de exportação (portabilidade)
  - Endpoint/processo de exclusão
  - Revogação de consentimento

---

### Exemplo: “mascarar PII” em logs — copiar e colar

```ts
function maskEmail(email: string) {
  const [u, d] = email.split('@')
  if (!u || !d) return '[email]'
  return `${u.slice(0, 2)}***@${d}`
}

function safeLog(obj: Record<string, unknown>) {
  const cloned = structuredClone(obj)
  if (typeof cloned.email === 'string') cloned.email = maskEmail(cloned.email)
  return cloned
}
```

### Exemplo: feature flag para trackers após consentimento — copiar e colar

```ts
export function useConsent() {
  const consent = useCookie('consent', { sameSite: 'lax' })
  const hasAnalytics = computed(() => consent.value?.includes('analytics') ?? false)
  return { consent, hasAnalytics }
}
```
