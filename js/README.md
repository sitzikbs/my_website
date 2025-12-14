# JavaScript Files

This directory contains all JavaScript files for the website.

## Files

### Analytics
- **`analytics.js`** - Google Analytics 4 configuration (development version)
  - Contains GA4 tracking code with Measurement ID: `G-EJRL17R9NE`
  - Privacy-compliant settings (anonymize_ip, secure cookies)
  - Same tracking ID as original WordPress site for data continuity
  
- **`analytics.min.js`** - Minified production version (359 bytes)
  - Used in all HTML files via `<script src="js/analytics.min.js"></script>`
  - Browser-cacheable for better performance

### Other Scripts
- **`main.js`** / **`main.min.js`** - Main site functionality
- **`blog.js`** / **`blog.min.js`** - Blog-specific features
- Additional minified scripts for various features

## Updating Analytics

To change the Google Analytics Measurement ID:

1. Edit `js/analytics.js`
2. Change the `GA4_MEASUREMENT_ID` constant
3. Regenerate minified version:
   ```bash
   npx terser js/analytics.js -o js/analytics.min.js -c -m
   ```
4. Commit and deploy

No need to modify any HTML files - they all reference the centralized script!

## Build Process

All JavaScript files should be minified before deployment:

```bash
# Minify a single file
npx terser js/filename.js -o js/filename.min.js -c -m

# Minify all JS files (from project root)
npm run minify:js
```

## Benefits of Centralized Analytics

✅ **Single source of truth** - Update GA4 ID in one place  
✅ **Smaller HTML files** - Reduced from ~15 lines to 1 line per page  
✅ **Better caching** - Browser caches the external script  
✅ **Easier maintenance** - No need to update 81 HTML files  
✅ **Version control** - Track analytics changes separately from content
