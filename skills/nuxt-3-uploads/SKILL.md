---
name: nuxt-3-uploads
description: Uploads seguros em Nuxt 3: limites, validação, armazenamento (S3/R2), URLs assinadas, scanning e prevenção de abuso.
---

# Nuxt 3 Uploads

## Workflow

1. Decida o modelo: upload direto do client com **URL assinada** (preferido) vs upload via `server/api`.
2. Defina limites: tamanho, tipos MIME permitidos, contagem, rate limit.
3. Valide no server: metadata + (quando aplicável) assinatura/ACL do objeto.
4. Nunca confie só no MIME do browser; se necessário, faça verificação adicional.
5. Pós-processamento: antivírus/scan, thumbnails, stripping de EXIF (quando necessário).

## Defaults

- Para storage externo: **pre-signed URL** + callback/registro no server.
- Para arquivos sensíveis: criptografia em repouso + ACL mínima + TTL/retention.
- Sempre setar `cache-control` apropriado (público para assets públicos, privado para sensíveis).

## Anti-patterns

- Upload “livre” sem limites/rate limit.
- Aceitar `content-type` arbitrário e servir de volta sem headers corretos.
- Expor bucket/credenciais no client.

## Reference

Leia `reference.md` para exemplos copiar-e-colar.

