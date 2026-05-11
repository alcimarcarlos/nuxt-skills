## Nuxt Skills (Cursor / Codex / Claude Code)

Pacote de skills para **Nuxt 3, Nuxt 4 e Nuxt 5** focado em **boas práticas, produtividade, conformidade e segurança**.

### Estrutura

- `skills/<skill-name>/SKILL.md`: entrada principal da skill (formato compatível com `~/.codex/skills`)
- `skills/<skill-name>/reference.md`: detalhes, snippets e checklists estendidos (quando aplicável)

### Instalação (recomendado)

Essas skills seguem o formato `SKILL.md` com frontmatter YAML, compatível com:

- **Codex/Cursor**: `~/.codex/skills/<skill-name>/SKILL.md`
- **Claude Code (user scope)**: `~/.claude/skills/<skill-name>/SKILL.md`
- **Claude Code (project scope)**: `.claude/skills/<skill-name>/SKILL.md` dentro do repositório do projeto

#### Instalação para Codex/Cursor

1. Crie/garanta o diretório `~/.codex/skills`
2. Copie (ou faça symlink) de cada pasta em `skills/*` para `~/.codex/skills/<skill-name>`

Exemplo com symlink:

```bash
mkdir -p ~/.codex/skills
for d in skills/*; do
  name="$(basename "$d")"
  ln -sfn "$(pwd)/$d" "$HOME/.codex/skills/$name"
done
```

#### Instalação para Claude Code (user scope)

```bash
mkdir -p ~/.claude/skills
for d in skills/*; do
  name="$(basename "$d")"
  ln -sfn "$(pwd)/$d" "$HOME/.claude/skills/$name"
done
```

### Skills incluídas

- Nuxt 3
  - `nuxt-3-core`
  - `nuxt-3-auth-session`
  - `nuxt-3-security`
  - `nuxt-3-performance-rendering`
  - `nuxt-3-data-fetching`
  - `nuxt-3-server-api-nitro`
  - `nuxt-3-testing-quality`
  - `nuxt-3-seo-meta`
  - `nuxt-3-modules-and-layers`
  - `nuxt-3-observability`
  - `nuxt-3-i18n`
  - `nuxt-3-accessibility`
  - `nuxt-3-uploads`
- Nuxt 4
  - `nuxt-4-core`
  - `nuxt-4-auth-session`
  - `nuxt-4-security`
  - `nuxt-4-performance-rendering`
  - `nuxt-4-data-fetching`
  - `nuxt-4-server-api-nitro`
  - `nuxt-4-testing-quality`
  - `nuxt-4-seo-meta`
  - `nuxt-4-modules-and-layers`
  - `nuxt-4-observability`
  - `nuxt-4-i18n`
  - `nuxt-4-accessibility`
  - `nuxt-4-uploads`
- Nuxt 5
  - `nuxt-5-core`
  - `nuxt-5-auth-session`
  - `nuxt-5-security`
  - `nuxt-5-performance-rendering`
  - `nuxt-5-data-fetching`
  - `nuxt-5-server-api-nitro`
  - `nuxt-5-testing-quality`
  - `nuxt-5-seo-meta`
  - `nuxt-5-modules-and-layers`
  - `nuxt-5-observability`
  - `nuxt-5-i18n`
  - `nuxt-5-accessibility`
  - `nuxt-5-uploads`
- Cross
  - `nuxt-privacy-lgpd`
  - `nuxt-ci-cd`
  - `nuxt-secrets-and-config`
  - `nuxt-multitenant-merchants`
  - `nuxt-bff-hardening`
  - `nuxt-secret-scanning`
  - `nuxt-secure-logging`
  - `nuxt-version-compat-guard`

