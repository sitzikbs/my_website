# HTML Validation Workflow Testing Guide

This document provides information on testing the HTML validation workflow.

## Automated Testing (GitHub Actions)

The HTML validation workflow will automatically run:
- When you open or update a pull request to the `main` branch
- When you push commits to the `main` branch
- When you manually trigger it from the Actions tab

### Manual Trigger
1. Go to the repository on GitHub
2. Click on the "Actions" tab
3. Select "HTML Validation" workflow from the left sidebar
4. Click "Run workflow" button
5. Select the branch and click "Run workflow"

## Local Testing

Before pushing changes, you can test HTML validation locally:

### Prerequisites
```bash
# Install dependencies (if not already installed)
npm install
```

### Build and Validate
```bash
# Build the site
npm run build

# Run HTML validation
npm run test:html
```

### Expected Output
- **Success**: No output or "0 errors found" message
- **Failure**: Detailed error messages with file paths and line numbers

### Common Validation Rules
The workflow validates:
- ✅ HTML5 syntax correctness
- ✅ Proper element nesting
- ✅ Required attributes presence
- ✅ Double-quoted attributes
- ✅ Basic WCAG accessibility rules (h30, h32, h36, h37, h67, h71)

### Configuration
Edit `.htmlvalidate.json` to customize validation rules:
- `"error"` - Fails validation
- `"warn"` - Shows warning but doesn't fail
- `"off"` - Disables the rule

## Viewing Results in GitHub Actions

1. Navigate to the "Actions" tab in the repository
2. Click on a workflow run
3. Click on the "Validate HTML and Accessibility" job
4. Expand the steps to see detailed output:
   - "Validate HTML files" - Shows HTML validation results
   - "Run accessibility checks with pa11y" - Shows accessibility check results
   - "Validation summary" - Shows overall pass/fail status

## Troubleshooting

### Workflow Fails Locally But Not in CI
- Ensure you're using the same Node.js version (20.x)
- Clean your `_site` directory and rebuild: `rm -rf _site && npm run build`
- Check that all dependencies are installed: `npm ci`

### Common HTML Validation Errors
1. **Unclosed tags**: Make sure all HTML tags are properly closed
2. **Missing required attributes**: Check that elements like `<img>` have `alt` attributes
3. **Invalid nesting**: Ensure elements are nested correctly (e.g., no `<div>` inside `<p>`)
4. **Incorrect attribute quotes**: Use double quotes for all attributes

### Need Help?
- Check the workflow file: `.github/workflows/html-validate.yml`
- Review the configuration: `.htmlvalidate.json`
- See the README.md for more information
