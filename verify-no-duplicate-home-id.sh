#!/bin/bash
# Verification script for duplicate ID 'home' issue
# Run this to verify that no duplicate ID 'home' exists

echo "======================================"
echo "Duplicate ID 'home' Verification Script"
echo "======================================"
echo ""

# Build the site
echo "Step 1: Building site..."
npm run build > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✅ Build successful"
else
    echo "❌ Build failed"
    exit 1
fi
echo ""

# Search for id="home" in source files
echo "Step 2: Searching source files for id=\"home\"..."
SOURCE_MATCHES=$(grep -r 'id="home"' --include="*.html" --include="*.njk" . 2>/dev/null | grep -v "_site" | grep -v "node_modules" | wc -l)
if [ "$SOURCE_MATCHES" -eq 0 ]; then
    echo "✅ No id=\"home\" found in source files"
else
    echo "⚠️  Found $SOURCE_MATCHES instances in source files:"
    grep -r 'id="home"' --include="*.html" --include="*.njk" . 2>/dev/null | grep -v "_site" | grep -v "node_modules"
fi
echo ""

# Search for id='home' in source files  
echo "Step 3: Searching source files for id='home'..."
SOURCE_MATCHES_SINGLE=$(grep -r "id='home'" --include="*.html" --include="*.njk" . 2>/dev/null | grep -v "_site" | grep -v "node_modules" | wc -l)
if [ "$SOURCE_MATCHES_SINGLE" -eq 0 ]; then
    echo "✅ No id='home' found in source files"
else
    echo "⚠️  Found $SOURCE_MATCHES_SINGLE instances in source files:"
    grep -r "id='home'" --include="*.html" --include="*.njk" . 2>/dev/null | grep -v "_site" | grep -v "node_modules"
fi
echo ""

# Search compiled HTML
echo "Step 4: Searching compiled HTML for id=\"home\"..."
COMPILED_MATCHES=$(grep -r 'id="home"' _site --include="*.html" 2>/dev/null | wc -l)
if [ "$COMPILED_MATCHES" -eq 0 ]; then
    echo "✅ No id=\"home\" found in compiled HTML"
else
    echo "⚠️  Found $COMPILED_MATCHES instances in compiled HTML:"
    grep -r 'id="home"' _site --include="*.html" 2>/dev/null
fi
echo ""

# Check specific pages
echo "Step 5: Checking specific pages mentioned in issue..."
PAGES=("_site/index.html" "_site/about/index.html" "_site/blog/index.html" "_site/code/index.html" "_site/contact/index.html" "_site/podcast/index.html" "_site/publications/index.html")
ISSUES_FOUND=0

for page in "${PAGES[@]}"; do
    if [ -f "$page" ]; then
        COUNT=$(grep 'id="home"' "$page" 2>/dev/null | wc -l)
        COUNT_SINGLE=$(grep "id='home'" "$page" 2>/dev/null | wc -l)
        TOTAL=$((COUNT + COUNT_SINGLE))
        
        if [ "$TOTAL" -gt 0 ]; then
            echo "⚠️  $page: Found $TOTAL instances"
            ISSUES_FOUND=$((ISSUES_FOUND + 1))
        else
            echo "✅ $page: No 'home' ID found"
        fi
    else
        echo "⚠️  $page: File not found"
    fi
done
echo ""

# Run HTML validation
echo "Step 6: Running HTML validation..."
VALIDATION_OUTPUT=$(npm run validate:html 2>&1)
DUP_ID_ERRORS=$(echo "$VALIDATION_OUTPUT" | grep -i "duplicate.*id.*home" | wc -l)

if [ "$DUP_ID_ERRORS" -eq 0 ]; then
    echo "✅ HTML validation: No duplicate ID 'home' errors"
else
    echo "⚠️  HTML validation found duplicate ID errors:"
    echo "$VALIDATION_OUTPUT" | grep -i "duplicate.*id.*home"
fi
echo ""

# Final summary
echo "======================================"
echo "SUMMARY"
echo "======================================"
if [ "$SOURCE_MATCHES" -eq 0 ] && [ "$SOURCE_MATCHES_SINGLE" -eq 0 ] && [ "$COMPILED_MATCHES" -eq 0 ] && [ "$ISSUES_FOUND" -eq 0 ] && [ "$DUP_ID_ERRORS" -eq 0 ]; then
    echo "✅ PASS: No duplicate ID 'home' found"
    echo ""
    echo "The issue does not exist in the current codebase."
    exit 0
else
    echo "❌ FAIL: Duplicate ID 'home' detected"
    echo ""
    echo "Found issues in the following checks:"
    [ "$SOURCE_MATCHES" -gt 0 ] && echo "- Source files (double quotes)"
    [ "$SOURCE_MATCHES_SINGLE" -gt 0 ] && echo "- Source files (single quotes)"
    [ "$COMPILED_MATCHES" -gt 0 ] && echo "- Compiled HTML"
    [ "$ISSUES_FOUND" -gt 0 ] && echo "- Specific pages"
    [ "$DUP_ID_ERRORS" -gt 0 ] && echo "- HTML validation"
    exit 1
fi
