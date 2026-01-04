# Scripts Directory

This directory contains utility scripts for maintaining and improving the website.

## 📁 Directory Structure

- **`/scripts/`** - Active, reusable maintenance scripts (5 scripts)
- **`/scripts/archive/`** - Archived 11ty migration scripts - see [archive/README.md](archive/README.md)
- **`/scripts/one-time/`** - One-time WordPress migration scripts - see [one-time/README.md](one-time/README.md)

---

## Active Utility Scripts

These 5 scripts are maintained for ongoing website maintenance:

### Accessibility & Quality

- **`check_accessibility.py`** - WCAG 2.1 AA compliance checker
  - Validates all HTML files for accessibility issues
  - Checks: skip links, main landmarks, alt text, h1 presence, lang attribute, etc.
  - Usage: `uv run python scripts/check_accessibility.py`

- **`check_heading_hierarchy.py`** - Heading structure validator
  - Checks for proper h1-h6 heading hierarchy
  - Identifies skipped heading levels and multiple h1 tags
  - Usage: `uv run python scripts/check_heading_hierarchy.py`

- **`validate-content.py`** - Content validation tool
  - Validates JSON data files (publications.json, blog-index.json)
  - Checks for required fields and data integrity
  - Usage: `uv run python scripts/validate-content.py`

### SEO

- **`generate_sitemap.py`** - Sitemap generator
  - Creates XML sitemap from all HTML pages
  - Sets priority and lastmod dates
  - Used in: `npm run build:sitemap`
  - Usage: `uv run python scripts/generate_sitemap.py`

---

## Historical Scripts

### One-Time WordPress Migration Scripts
See **`one-time/README.md`** for 30 scripts used during WordPress-to-static-site migration:
- WordPress URL fixing and content migration
- Initial image downloads from WordPress
- Image cleanup and consolidation
- Image quality upgrades and comparisons
- Content fixes and conversions

✅ **Migration complete** - These scripts are preserved for reference only.

### Archived 11ty Migration Scripts
See **`archive/README.md`** for 12 scripts from the 11ty conversion:
- Blog post migration to Markdown
- Responsive image fixes
- Styling updates
- WebP conversion

✅ **All completed** - These scripts have served their purpose.

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
