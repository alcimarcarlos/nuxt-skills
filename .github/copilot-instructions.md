# GitHub Copilot Instructions

This repository is a portable skill package for Cursor, Codex, Claude Code, and Copilot.

- Follow `AGENTS.md` for operational rules.
- Use the smallest matching `skills/<skill-name>/SKILL.md`.
- Use `nuxt-version-compat-guard` as the baseline when work crosses multiple areas.
- Load `skills/<skill-name>/reference.md` only when the skill asks for it or the task needs details.
- Treat `.cursor/skills/` as aliases; edit canonical files under `skills/`.
- Prefer local project conventions over new abstractions.
- Report validation commands run or pending.
