# Assets Directory

This directory contains all static assets for the website including images, documents, and videos.

## Directory Structure

```
assets/
├── images/
│   ├── profile/          # Profile photos and headshots
│   ├── publications/     # Publication thumbnails and figures
│   ├── blog/            # Blog post images (featured and inline)
│   ├── general/         # Site-wide images (logo, backgrounds, etc.)
│   └── icons/           # Icons and small graphics
├── documents/
│   ├── cv/              # CV and resume files
│   └── papers/          # Publication PDFs and supplementary materials
└── videos/              # Video files (if hosted locally)
```

## File Naming Conventions

### Profile Images
- `profile-large.jpg` - Large profile photo (800x800px)
- `profile-medium.jpg` - Medium profile photo (400x400px)
- `profile-thumb.jpg` - Small thumbnail (200x200px)
- `headshot.jpg` - Professional headshot

### Publications
- Thumbnails: `[publication-id]-thumb.jpg`
- Figures: `[publication-id]-fig1.png`, `[publication-id]-fig2.png`
- Papers: `[publication-id]-paper.pdf`
- Supplementary: `[publication-id]-supplementary.pdf`

### Blog Posts
- Featured images: `YYYY-MM-DD-[post-slug]-featured.jpg`
- Inline images: `YYYY-MM-DD-[post-slug]-img-1.jpg`

### General Site Assets
- `logo.png` - Site logo
- `logo-small.png` - Small version for mobile
- `favicon.ico` - Browser favicon
- `og-image.jpg` - Default Open Graph image for social sharing

## Image Optimization Guidelines

Before adding images to this directory:

1. **Resize appropriately:**
   - Profile photos: Max 800x800px
   - Publication thumbnails: Max 1200x600px
   - Blog featured images: Max 1600x900px
   - Blog inline images: Max 1200px width

2. **Compress images:**
   - Use tools like TinyPNG, ImageOptim, or Squoosh
   - Target: < 500KB per image for most images
   - Target: < 200KB for thumbnails

3. **Use appropriate formats:**
   - Photos: JPG (quality 85%)
   - Graphics with transparency: PNG
   - Simple icons: SVG (preferred)
   - Consider WebP with fallbacks for better compression

4. **Add alt text:**
   - Ensure all images have descriptive alt text in HTML/JSON

## Image Optimization Tools

### Command-line
```bash
# Using ImageMagick
mogrify -resize 1600x1600\> -quality 85 *.jpg

# Using OptiPNG
optipng -o7 *.png

# Using cwebp (WebP conversion)
cwebp -q 85 input.jpg -o output.webp
```

### Online Tools
- [TinyPNG](https://tinypng.com/) - PNG and JPG compression
- [Squoosh](https://squoosh.app/) - Advanced image compression
- [SVGOMG](https://jakearchibald.github.io/svgomg/) - SVG optimization

### Desktop Apps
- **ImageOptim** (Mac) - Drag-and-drop image optimization
- **FileOptimizer** (Windows) - Multi-format optimizer
- **Trimage** (Linux) - Lossless image optimizer

## WordPress Media Migration

When migrating from WordPress:

### Download Media Files

```bash
# Option 1: SFTP/FTP
sftp user@itzikbs.com
get -r /wp-content/uploads/ ./wordpress-media/

# Option 2: Using WP-CLI
wp media export --dir=./media-export/
```

### Organize Downloaded Files

1. **Sort by type:**
   - Identify profile photos → `images/profile/`
   - Identify publication images → `images/publications/`
   - Identify blog images → `images/blog/`
   - Identify PDFs → `documents/papers/` or `documents/cv/`

2. **Rename consistently:**
   - Follow naming conventions above
   - Remove WordPress date prefixes (e.g., `2024/03/image.jpg` → `blog/2024-03-15-post-img.jpg`)

3. **Update references:**
   - Update all image paths in HTML files
   - Update paths in JSON data files
   - Test all images load correctly

## Current Status

- ✅ Directory structure created
- ⏳ **Awaiting WordPress media download**

## Next Steps

1. Download all media from WordPress site
2. Organize files into appropriate directories
3. Rename files following conventions
4. Optimize all images
5. Update file paths in content
6. Verify all images load correctly

See [MIGRATION_GUIDE.md](../MIGRATION_GUIDE.md) for detailed migration instructions.
