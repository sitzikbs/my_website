const Image = require("@11ty/eleventy-img");
const path = require("path");

module.exports = async function responsiveImage(src, alt = "", sizes = "(min-width: 800px) 800px, 100vw") {
  // Handle relative paths from markdown files
  let imagePath;
  if (src.startsWith("http://") || src.startsWith("https://")) {
    imagePath = src;
  } else if (src.startsWith("/")) {
    imagePath = `.${src}`;
  } else if (src.startsWith("../") || src.startsWith("./")) {
    // Relative path with ../ or ./ - resolve from project root
    // Convert ../../assets/images/blog/image.jpg to assets/images/blog/image.jpg
    imagePath = path.normalize(src).replace(/^(\.\.\/)+/, "");
  } else {
    // Direct path like assets/images/blog/image.jpg
    imagePath = src;
  }

  const metadata = await Image(imagePath, {
    widths: [400, 800, 1200],
    formats: ["webp", null], // null = original format
    outputDir: "./_site/assets/images/generated/",
    urlPath: "/assets/images/generated/",
    filenameFormat: function (id, src, width, format, options) {
      const extension = format;
      const name = path.basename(src, path.extname(src));
      return `${name}-${width}.${extension}`;
    }
  });

  const imageAttributes = {
    alt,
    sizes,
    loading: "lazy",
    decoding: "async"
  };

  // Generate HTML with picture element
  return Image.generateHTML(metadata, imageAttributes);
};
