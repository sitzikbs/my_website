#!/bin/bash
# Quick update: Replace old Talking Papers logo with new one in all blog posts
find blog/posts -name "*.html" -exec sed -i 's|assets/images/publications/Talking_papers_cover-400\.webp|assets/images/icons/talking-papers-logo.webp|g' {} \;
echo "✅ Updated logo path in all blog posts"
