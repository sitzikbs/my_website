# Pre-Deployment Cleanup Plan

## Overview
Before deploying to Cloudflare Pages, we need to organize and remove unnecessary files to keep the repository clean and maintainable.

---

## 📋 Cleanup Tasks

### 1. **Root-Level Markdown Files** (Move to `docs/`)
These are project documentation files that clutter the root:

**Files to move:**
- `GITHUB_ISSUES_ACTIONS.md` → `docs/`
- `AUDIT_2026-01-01.md` → `docs/`
- `ISSUE_CLOSING_SUMMARIES.md` → `docs/`
- `DESIGN_SYSTEM.md` → `docs/`

**Files to keep in root:**
- `README.md` (primary documentation)
- `TODO.md` (active planning)
- `DEPLOYMENT.md` (deployment guide)

---

### 2. **Scripts Directory** (Archive old scripts)

**Current scripts (18 files):**
Many of these were one-time migration/optimization scripts.

**Recommendation:**
- Create `scripts/archive/` folder
- Move **completed one-time scripts** to archive:
  - `add_blog_hero_header.py` (one-time fix)
  - `fix_all_responsive_images.py` (one-time fix)
  - `fix_blog_post_styles.py` (one-time fix)
  - `fix_phd_post_images.py` (one-time fix)
  - `remove_old_blog_headers.py` (one-time fix)
  - `update_blog_hero_css.py` (one-time fix)
  - `update_talking_papers_logo.py` (one-time fix)
  - `quick_update_logo.sh` (one-time fix)
  - `migrate_blog_posts.py` (11ty migration - done!)
  - `download_images.py` (initial setup - done)
  - `convert_to_webp.py` (initial setup - done)

**Scripts to keep active:**
- `generate_sitemap.py` (may need to update sitemap)
- `validate-content.py` (useful for validation)
- `check_accessibility.py` (useful for audits)
- `check_heading_hierarchy.py` (useful for audits)
- `improve_accessibility.py` (may need again)
- `README.md` (documentation)

**Add to archive README:**
Document what each archived script did and why it's no longer needed.

---

### 3. **Hidden `.github/` Markdown Files** (Already good!)

Current files:
- `.github/copilot-instructions.md` ✅ Keep
- `.github/instructions/*.md` ✅ Keep
- `.github/11TY_MIGRATION_PLAN.md` → **Move to `docs/`** (completed plan)

---

### 4. **Assets Organization** (Already optimized!)

Current state:
- `assets/images/` - 73MB (optimized WebP + fallbacks) ✅
- No `-original` backups found ✅
- Well organized by category ✅

**Action:** No changes needed - already clean!

---

### 5. **Blog Posts** (Already clean!)

Current state:
- `blog/posts-md/` - 884KB (74 Markdown files) ✅
- No old HTML files remaining ✅

**Action:** No changes needed - migration cleanup already done!

---

### 6. **Update `.gitignore`** 

Add archive directories and ensure build artifacts ignored:

```gitignore
# Eleventy
_site/
node_modules/

# Archives
scripts/archive/
docs/archive/

# Build artifacts
*.min.css.map
*.min.js.map

# Editor files
.vscode/
.idea/

# OS files
.DS_Store
Thumbs.db

# Logs
npm-debug.log*
```

---

## 📊 Impact Summary

**Before cleanup:**
- 6 root MD files (only 3 should be there)
- 18 scripts (11 are one-time use)
- Unclear organization

**After cleanup:**
- 3 root MD files (clean!)
- 7 active scripts + 11 archived
- Clear organization
- Easier to navigate
- Better for new contributors

---

## 🔄 Execution Order

1. Create `scripts/archive/` directory
2. Move old scripts to archive
3. Create archive README
4. Create `docs/` directory (if not exists)
5. Move documentation files to `docs/`
6. Move 11ty migration plan to `docs/`
7. Update `.gitignore`
8. Update main README if needed (update paths)
9. Commit all changes
10. Push to main
11. **Ready to deploy!** 🚀

---

## ⚠️ Safety Notes

- Do NOT delete any files, only move/archive
- Keep all history (files may be referenced in git history)
- Test build after cleanup: `npm run build`
- Verify site still works: `npm run serve`

---

**Status:** Plan ready for execution  
**Next:** Execute cleanup and verify build
