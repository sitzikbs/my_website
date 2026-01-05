# Assets Directory

This directory contains all static assets for the website including images, documents, and videos.

## Image Storage

**All image files in this directory are stored as binary files in the git repository.**

- Image files (`.jpg`, `.jpeg`, `.png`, `.webp`, `.gif`) are committed directly to git
- Eleventy's `@11ty/eleventy-img` plugin generates optimized responsive variants during build
- Generated images are output to `_site/assets/images/generated/` (gitignored)
assets/
├── images/
│   ├── profile/          # Profile photos and headshots
│   ├── publications/     # Publication thumbnails and figures
│   ├── blog/            # Blog post images (source images only)
│   ├── general/         # Site-wide images (logo, backgrounds, etc.)
│   ├── icons/           # Icons and small graphics
│   └── generated/       # Responsive image variants (build-time generated, gitignored)
├── documents/
│   ├── cv/              # CV and resume files
│   └── papers/          # Publication PDFs and supplementary materials
└── videos/              # Video files (if hosted locally)
```

## Image Workflow

### Source Images (Committed to Git via LFS)
- Store only **source/original** images in `assets/images/[category]/`
- These are tracked by Git LFS and committed to the repository
- Keep images optimized (target < 500KB where possible)

### Generated Variants (Not Committed)
- Responsive image variants are **auto-generated at build time** by `@11ty/eleventy-img`
- Generated files are stored in `assets/images/generated/` (gitignored)
- Variants include multiple sizes (400px, 800px, 1200px) and formats (WebP + fallback)
- Never commit files in the `generated/` directory

### Using Images in Blog Posts

Use the `{% responsiveImage %}` shortcode in Markdown:

```markdown
{% responsiveImage "assets/images/blog/my-photo.jpg", "Alt text description" %}
```

This automatically:
- Generates responsive sizes (400px, 800px, 1200px widths)
- Creates WebP versions with fallbacks
- Outputs proper `<picture>` element with srcset
- Lazy loads images for performance

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
