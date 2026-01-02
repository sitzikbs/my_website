# Scripts Directory

This directory contains utility scripts for maintaining and improving the website.

## 📁 Directory Structure

- **`/scripts/`** - Active, reusable maintenance scripts
- **`/scripts/archive/`** - One-time scripts (migration, fixes) - see archive/README.md

---

## Active Utility Scripts

### Accessibility & Quality

- **`check_accessibility.py`** - WCAG 2.1 AA compliance checker
  - Validates all HTML files for accessibility issues
  - Checks: skip links, main landmarks, alt text, h1 presence, lang attribute, etc.
  - Usage: `uv run python scripts/check_accessibility.py`

- **`improve_accessibility.py`** - Systematic accessibility enhancement
  - Adds skip-to-main-content links to all pages
  - Adds semantic `<main>` landmarks
  - Fixes empty links and missing titles
  - Usage: `uv run python scripts/improve_accessibility.py`

- **`check_heading_hierarchy.py`** - Heading structure validator
  - Checks for proper h1-h6 heading hierarchy
  - Identifies skipped heading levels and multiple h1 tags
  - Usage: `uv run python scripts/check_heading_hierarchy.py`

- **`validate-content.py`** - Content validation tool
  - Validates JSON data files
  - Checks for required fields and data integrity
  - Usage: `uv run python scripts/validate-content.py`

### SEO

- **`generate_sitemap.py`** - Sitemap generator
  - Creates XML sitemap from all HTML pages
  - Sets priority and lastmod dates
  - Usage: `uv run python scripts/generate_sitemap.py`
  - **Note:** May need updates for 11ty build structure

---

## Archived Scripts

See **`archive/README.md`** for information about:
- Migration scripts (11ty conversion)
- Image optimization scripts (initial setup)
- One-time fixes and updates

These scripts are preserved for reference but are no longer needed for regular maintenance.

---

## Python Environment

All scripts use `uv` for Python environment management:
```bash
# Run any script with:
uv run python scripts/<script_name>.py
```

## Notes

- All scripts are designed to be run from the repository root
- Scripts modify files in place - review changes before committing
- Use version control to track script-generated changes
- After 11ty migration, some scripts may need path updates (check `_site/` output)
