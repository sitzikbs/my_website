# Archived Scripts

This directory contains one-time scripts that were used during website development, migration, and optimization. They are archived here for reference but are no longer needed for regular maintenance.

---

## Migration Scripts

### `migrate_blog_posts.py`
**Purpose:** Converted 74 HTML blog posts to Markdown for Eleventy (11ty) migration  
**Used:** January 2026 (Phase 4 of 11ty migration)  
**Status:** ✅ Complete - All blog posts successfully migrated  
**Why archived:** Migration is complete; all posts are now in Markdown

---

## Image Optimization Scripts

### `download_images.py`
**Purpose:** Downloaded and organized images from WordPress site  
**Used:** December 2025 (Initial setup)  
**Status:** ✅ Complete - All images downloaded  
**Why archived:** Initial setup task, no longer needed

### `convert_to_webp.py`
**Purpose:** Converted images to WebP format with fallbacks  
**Used:** December 2025 (Performance optimization)  
**Status:** ✅ Complete - 78.3% size reduction achieved  
**Why archived:** All images already converted

---

## One-Time Fixes

### `add_blog_hero_header.py`
**Purpose:** Added hero sections to blog post pages  
**Used:** December 2025  
**Status:** ✅ Complete  
**Why archived:** Now handled by 11ty blog-post.njk template

### `fix_all_responsive_images.py`
**Purpose:** Made images responsive with srcset  
**Used:** December 2025  
**Status:** ✅ Complete  
**Why archived:** All images already fixed

### `fix_blog_post_styles.py`
**Purpose:** Fixed CSS styling issues in blog posts  
**Used:** December 2025  
**Status:** ✅ Complete  
**Why archived:** Styling now handled by 11ty templates

### `fix_phd_post_images.py`
**Purpose:** Fixed image paths in PhD-related blog posts  
**Used:** December 2025  
**Status:** ✅ Complete  
**Why archived:** One-time fix, already applied

### `remove_old_blog_headers.py`
**Purpose:** Removed duplicate headers from blog posts  
**Used:** December 2025  
**Status:** ✅ Complete  
**Why archived:** One-time cleanup, already applied

### `update_blog_hero_css.py`
**Purpose:** Updated hero section CSS styling  
**Used:** December 2025  
**Status:** ✅ Complete  
**Why archived:** Now handled by main CSS file

### `update_talking_papers_logo.py`
**Purpose:** Updated Talking Papers podcast logo  
**Used:** December 2025  
**Status:** ✅ Complete  
**Why archived:** One-time update, already applied

### `quick_update_logo.sh`
**Purpose:** Quick shell script to update logo files  
**Used:** December 2025  
**Status:** ✅ Complete  
**Why archived:** One-time update, already applied

---

## Notes

- **Do not delete these files** - They may be referenced in git history
- These scripts are kept for reference in case similar tasks are needed in the future
- If you need to run any of these, review the code first as paths may have changed
- For active maintenance scripts, see the parent `scripts/` directory

---

**Archived:** January 2, 2026  
**Reason:** Pre-deployment cleanup after 11ty migration completion
