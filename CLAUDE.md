# Claude Code Instructions

Use `AGENTS.md` como orientação principal desta coleção.

## Como Usar

1. Identifique a menor skill aplicável em `skills/<skill-name>/SKILL.md`.
2. Use `nuxt-version-compat-guard` como baseline quando a tarefa cruzar vários temas.
3. Leia `reference.md` somente quando a skill pedir ou quando a tarefa exigir mais detalhe.
4. Preserve padrões locais do projeto alvo antes de introduzir abstrações novas.
5. Ao concluir, relate validações executadas e pendências.

## Regras

- Prefira diffs mínimos e contíguos; preserve tipos, docstrings e comentários existentes.
- Não edite aliases em `.cursor/skills`; edite `skills/`.
- Mantenha respostas e mudanças verificáveis por Cursor, Codex, Claude Code e Copilot.
- Não assuma bibliotecas opcionais sem confirmação no projeto alvo.
