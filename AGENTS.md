# Nuxt Skills Agent Instructions

Use este arquivo como orientação operacional para Cursor, Codex, Claude Code e GitHub Copilot.

## Princípios

- Use a menor skill aplicável em `skills/<skill-name>/SKILL.md`.
- Trate `skills/` como fonte canônica; `.cursor/skills/` contém apenas aliases.
- Leia `reference.md` somente quando a skill pedir ou quando a tarefa exigir detalhe adicional.
- Inspecione as convenções do projeto alvo antes de criar novos padrões.
- Prefira linguagem e passos agnósticos de ferramenta.
- Preserve segurança, validação, testes e performance como critérios explícitos de entrega.

## Stack Coberta

- Nuxt 3
- Nuxt 4
- Nuxt 5
- Vue
- Nitro
- TypeScript
- AWS Amplify Gen 2

## Ordem de Decisão

1. Identifique o domínio real da tarefa e as dependências já presentes no projeto alvo.
2. Escolha a skill principal mais específica.
3. Use `nuxt-version-compat-guard` como baseline quando houver múltiplas áreas.
4. Adicione skills complementares só quando houver risco real de segurança, dados, UX, performance ou testes.
5. Antes de editar, leia arquivos vizinhos e padrões existentes.
6. Ao finalizar, reporte validações executadas e pendências.

## Qualidade Mínima

- Confirme a versão real do Nuxt antes de escolher skills por versão.
- Use a menor skill aplicável e adicione nuxt-version-compat-guard para migrações ou compatibilidade.
- Use as skills Amplify apenas quando o projeto realmente usa Amplify Gen 2.
- Código deve seguir padrões locais do projeto alvo.
- Mudanças devem ser pequenas, verificáveis e fáceis de revisar.
- Não introduza frameworks, bibliotecas ou serviços opcionais só porque uma skill existe.

## Comandos de Validação

Use o menor conjunto que existir no projeto alvo:

- `npm run build`
- `npm run typecheck`
- `npm test`
- `npm run lint`
- `nuxi typecheck`

## Compatibilidade por Agente

- Cursor: use `.cursor/rules/skills.mdc` e `.cursor/skills/<skill-name>`.
- Codex: use `skills/<skill-name>/SKILL.md` ou instale em `$CODEX_HOME/skills`.
- Claude Code: comece por `CLAUDE.md` e depois pela skill específica.
- GitHub Copilot: mantenha `.github/copilot-instructions.md` curto e apontando para este arquivo.

## Formato de Resposta Recomendado

1. Objetivo
2. Arquivos alterados
3. Decisões de implementação
4. Testes e validação
5. Riscos, suposições e pendências
