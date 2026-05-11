---
name: nuxt-4-uploads
description: Uploads seguros em Nuxt 4: limites, validação, armazenamento (S3/R2), URLs assinadas, scanning e prevenção de abuso.
---

# Nuxt 4 Uploads

## Workflow

1. Prefira URL assinada (upload direto) vs upload via `server/api`.
2. Defina limites e allowlist de MIME.
3. Valide no server e registre “intenção”/metadata.
4. Pós-processamento: scan/thumbnail/strip EXIF quando necessário.

## Reference

Leia `reference.md`.

