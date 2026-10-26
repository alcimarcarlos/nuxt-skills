#!/usr/bin/env python3
"""
Validates skills format, YAML frontmatter, markdown links, and symlink integrity.
"""
import os
import sys
import re

def validate_repo(repo_path):
    errors = 0
    warnings = 0
    skills_dir = os.path.join(repo_path, "skills")
    
    if not os.path.isdir(skills_dir):
        print(f"❌ ERROR: skills directory not found at {skills_dir}")
        return 1

    skill_folders = sorted([d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d))])
    print(f"🔍 Validating {len(skill_folders)} skills in {os.path.basename(repo_path)}...")

    for sf in skill_folders:
        sf_path = os.path.join(skills_dir, sf)
        skill_md = os.path.join(sf_path, "SKILL.md")
        
        if not os.path.isfile(skill_md):
            print(f"❌ ERROR: Missing SKILL.md in {sf}")
            errors += 1
            continue

        with open(skill_md, "r", encoding="utf-8") as f:
            content = f.read()

        lines = content.splitlines()
        if len(lines) > 160:
            print(f"⚠️  WARN: {sf}/SKILL.md has {len(lines)} lines. Consider delegating deep details to reference.md")
            warnings += 1

        # Check frontmatter delimiter
        if not content.startswith("---"):
            print(f"❌ ERROR: {sf}/SKILL.md does not start with YAML frontmatter (---)")
            errors += 1
            continue

        parts = content.split("---", 2)
        if len(parts) < 3:
            print(f"❌ ERROR: {sf}/SKILL.md invalid YAML frontmatter syntax")
            errors += 1
            continue

        fm = parts[1]
        name_match = re.search(r"^name:\s*(.+)$", fm, re.MULTILINE)
        desc_match = re.search(r"^description:\s*(.+)$", fm, re.MULTILINE)

        if not name_match:
            print(f"❌ ERROR: {sf}/SKILL.md missing 'name' in frontmatter")
            errors += 1
        else:
            declared_name = name_match.group(1).strip().strip('"\'')
            if declared_name != sf:
                print(f"❌ ERROR: {sf}/SKILL.md name '{declared_name}' does not match directory name '{sf}'")
                errors += 1

        if not desc_match:
            print(f"❌ ERROR: {sf}/SKILL.md missing 'description' in frontmatter")
            errors += 1
        else:
            desc = desc_match.group(1).strip().strip('"\'')
            if len(desc) < 25:
                print(f"⚠️  WARN: {sf}/SKILL.md description is too short ({len(desc)} chars)")
                warnings += 1

        # Check local markdown links [text](path)
        for link in re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content):
            href = link[1]
            if href.startswith(("http://", "https://", "#", "mailto:")):
                continue
            clean_href = href.split("#")[0]
            if not clean_href:
                continue
            target_path = os.path.normpath(os.path.join(sf_path, clean_href))
            if not os.path.exists(target_path):
                print(f"❌ ERROR: {sf}/SKILL.md broken link '{href}' -> {target_path}")
                errors += 1

    # Check symlinks in .cursor/skills if directory exists
    cursor_skills = os.path.join(repo_path, ".cursor", "skills")
    if os.path.isdir(cursor_skills):
        for item in os.listdir(cursor_skills):
            full_item = os.path.join(cursor_skills, item)
            if os.path.islink(full_item):
                target = os.readlink(full_item)
                resolved = os.path.normpath(os.path.join(cursor_skills, target))
                if not os.path.exists(resolved):
                    print(f"❌ ERROR: Broken symlink in .cursor/skills/{item} -> {target}")
                    errors += 1
        for sf in skill_folders:
            expected = os.path.join(cursor_skills, sf)
            if not os.path.exists(expected):
                print(f"⚠️  WARN: Skill {sf} missing symlink in .cursor/skills/")
                warnings += 1

    print(f"Finished: {errors} error(s), {warnings} warning(s).")
    return 1 if errors > 0 else 0

if __name__ == "__main__":
    current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    sys.exit(validate_repo(current_dir))
