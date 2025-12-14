# Scripts Directory

This directory contains utility scripts for maintaining and improving the website.

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

### Performance
- **`convert_to_webp.py`** - Image optimization
  - Converts JPEG/PNG images to WebP format
  - Reduces file sizes while maintaining quality
  - Usage: `uv run python scripts/convert_to_webp.py`

- **`download_images.py`** - Asset management
  - Downloads images from remote URLs
  - Organizes assets in local directory structure
  - Usage: `uv run python scripts/download_images.py`

### SEO
- **`generate_sitemap.py`** - Sitemap generator
  - Creates XML sitemap from all HTML pages
  - Sets priority and lastmod dates
  - Usage: `uv run python scripts/generate_sitemap.py`

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
