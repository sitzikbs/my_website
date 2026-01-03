const Image = require("@11ty/eleventy-img");
const path = require("path");

/**
 * Responsive image shortcode using Eleventy Image
 * Generates WebP + original format with multiple sizes
 * 
 * Usage in Nunjucks templates or markdown:
 * {% responsiveImage "assets/images/blog/image.jpg", "Alt text description" %}
 * 
 * Optional third parameter for sizes attribute:
 * {% responsiveImage "path.jpg", "Alt", "(min-width: 1200px) 1200px, 100vw" %}
 * 
 * Optional fourth parameter for loading strategy (default: "lazy"):
 * {% responsiveImage "path.jpg", "Alt", "(min-width: 800px) 800px, 100vw", "eager" %}
 * Use "eager" for above-the-fold images (especially LCP candidates) to improve performance
 */
async function responsiveImageShortcode(src, alt = "", sizes = "(min-width: 800px) 800px, 100vw", loading = "lazy") {
  // Handle relative paths
  let imagePath = src;
  
  // If path doesn't start with /, make it relative to project root
  if (!src.startsWith('/')) {
    imagePath = path.join(process.cwd(), src);
  } else {
    imagePath = path.join(process.cwd(), src.substring(1));
  }
  
  // Configure image processing
  let metadata = await Image(imagePath, {
    widths: [400, 800, 1200], // Responsive breakpoints
    formats: ["webp", null],   // Generate WebP + original format
    outputDir: "./assets/images/generated/", // Output directory (committed to git)
    urlPath: "/assets/images/generated/",    // URL path in HTML
    filenameFormat: function (id, src, width, format) {
      // Keep original filename structure with width and format
      const ext = path.extname(src);
      const name = path.basename(src, ext);
      return `${name}-${width}.${format}`;
    }
  });
  
  // Get lowest and highest resolution images
  let lowsrc = metadata.webp[0];
  let highsrc = metadata.webp[metadata.webp.length - 1];
  
  // Generate picture element with sources
  return `<picture>
    ${Object.values(metadata)
      // Generate source tags for each format
      .map(imageFormat => {
        return `  <source 
      type="${imageFormat[0].sourceType}" 
      srcset="${imageFormat.map(entry => entry.srcset).join(", ")}" 
      sizes="${sizes}">`;
      })
      .join("\n")}
    <img
      src="${lowsrc.url}"
      width="${highsrc.width}"
      height="${highsrc.height}"
      alt="${alt}"
      loading="${loading}"
      decoding="async"${loading === "eager" ? '\n      fetchpriority="high"' : ""}>
  </picture>`;
}

module.exports = responsiveImageShortcode;
