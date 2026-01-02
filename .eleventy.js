module.exports = function(eleventyConfig) {
  
  // Ignore unnecessary directories and files
  eleventyConfig.ignores.add("blog/posts/**");
  eleventyConfig.ignores.add(".venv/**");
  eleventyConfig.ignores.add(".github/**");
  eleventyConfig.ignores.add("node_modules/**");
  eleventyConfig.ignores.add("scripts/**");
  eleventyConfig.ignores.add("docs/**");
  eleventyConfig.ignores.add("assets/README.md");
  eleventyConfig.ignores.add("blog/README.md");
  eleventyConfig.ignores.add("css/README.md");
  eleventyConfig.ignores.add("data/README.md");
  eleventyConfig.ignores.add("js/README.md");
  eleventyConfig.ignores.add("README.md");
  eleventyConfig.ignores.add("TODO.md");
  eleventyConfig.ignores.add("DEPLOYMENT.md");
  eleventyConfig.ignores.add("DESIGN_SYSTEM.md");
  eleventyConfig.ignores.add("AUDIT_2026-01-01.md");
  eleventyConfig.ignores.add("ISSUE_CLOSING_SUMMARIES.md");
  eleventyConfig.ignores.add("GITHUB_ISSUES_ACTIONS.md");
  
  // Copy static assets to output
  eleventyConfig.addPassthroughCopy("css");
  eleventyConfig.addPassthroughCopy("js");
  eleventyConfig.addPassthroughCopy("assets");
  eleventyConfig.addPassthroughCopy("data");
  eleventyConfig.addPassthroughCopy("blog/posts");  // Copy blog posts as-is for now
  eleventyConfig.addPassthroughCopy("favicon.ico");
  eleventyConfig.addPassthroughCopy("favicon-16x16.png");
  eleventyConfig.addPassthroughCopy("favicon-32x32.png");
  eleventyConfig.addPassthroughCopy("apple-touch-icon.png");
  eleventyConfig.addPassthroughCopy("android-chrome-192x192.png");
  eleventyConfig.addPassthroughCopy("android-chrome-512x512.png");
  eleventyConfig.addPassthroughCopy("site.webmanifest");
  eleventyConfig.addPassthroughCopy("robots.txt");
  eleventyConfig.addPassthroughCopy("sitemap.xml");

  // Watch for changes in CSS and JS during development
  eleventyConfig.addWatchTarget("./css/");
  eleventyConfig.addWatchTarget("./js/");

  // Set custom directories
  return {
    dir: {
      input: ".",           // Root directory for source files
      includes: "_includes", // Directory for layouts and partials
      data: "_data",        // Directory for global data files
      output: "_site"       // Output directory for built site
    },
    templateFormats: ["html", "njk", "11ty.js"],  // Removed "md" to prevent markdown processing
    htmlTemplateEngine: "njk",
    markdownTemplateEngine: "njk"
  };
};
