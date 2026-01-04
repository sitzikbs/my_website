# One-Time Scripts

This directory contains scripts that were created for one-time operations during the WordPress-to-static-site migration and initial setup. These scripts are kept for historical reference but are not intended for regular use.

## Migration Complete

All WordPress migration, image optimization, and content consolidation tasks have been completed. The site is now fully operational as a static site deployed on Cloudflare Pages.

---

## WordPress Migration & URL Fixing Scripts

Scripts used to migrate from WordPress to static Markdown site and fix URL references:

- **analyze-wordpress-urls.py** - Analyzed WordPress URLs during migration planning
- **fix-wordpress-urls.py** - Fixed WordPress URL references in HTML content
- **replace-wordpress-urls.py** - Replaced WordPress URLs with local paths
- **replace-markdown-wordpress-urls.py** - Replaced WordPress URLs in Markdown files
- **remove-wordpress-duplicates.py** - Removed duplicate files from WordPress export
- **missing-wordpress-urls.md** - Report listing 87 missing URLs from migration

---

## Image Download Scripts

Scripts used for initial download of images from WordPress site:

- **download-all-blog-images.py** - Downloaded all blog post images
- **download-missing-images.py** - Downloaded images that were initially missed
- **download-from-ip.py** - Downloaded images from direct IP address
- **download-with-params.py** - Downloaded images with query parameters
- **download-ikea-images.py** - Downloaded IKEA dataset images

---

## Image Cleanup & Consolidation Scripts

Scripts used to clean up and consolidate images after migration:

- **cleanup-duplicate-images.py** - Removed duplicate image files
- **cleanup-generated-variants.py** - Removed automatically generated image variants
- **consolidate-blog-images.py** - Consolidated blog images into organized structure
- **remove-scaled-duplicates.py** - Removed WordPress `-scaled` duplicate images

---

## Image Upgrade & Comparison Scripts

Scripts used to upgrade image quality and compare with backup versions:

- **auto-upgrade-images.py** - Automatically upgraded images from backup
- **compare-all-images-with-backup.py** - Compared all images with backup versions
- **compare-and-upgrade-all-images.py** - Combined comparison and upgrade operations
- **compare-with-extracted-backup.py** - Compared with extracted backup archive
- **upgrade-small-images.py** - Upgraded images with small resolutions
- **upgrade-twitter-images.py** - Upgraded Twitter card images
- **upgrade-wordpress-images.py** - Upgraded WordPress-sourced images
- **quick-scan-backup.py** - Quick utility to scan backup directory

---

## Content Fixing Scripts

Scripts used for one-time content fixes and conversions:

- **fix-date-specific-images.py** - Fixed date-specific image path references
- **fix-image-references.py** - Fixed image reference paths in content
- **fix-image-refs.py** - Alternative image reference fixing script
- **convert-images-to-shortcode.py** - Converted image tags to 11ty shortcode format
- **create-image-placeholders.py** - Created placeholder images for missing files

---

## Accessibility Improvements

- **improve_accessibility.py** - One-time accessibility improvements to content

---

## Backup Operations

- **extract-from-backup.py** - Extracted files from backup archive

---

## Status

✅ **All operations complete** - These scripts have served their purpose and are archived for historical reference only.

**Last Updated:** January 4, 2026
