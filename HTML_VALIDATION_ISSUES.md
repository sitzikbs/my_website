# HTML Validation Issues Summary

Generated from workflow run #20735489532

**Total Issues**: 88 (54 errors, 34 warnings)

---

## Issue #1: Deprecated `frameborder` Attributes on Iframes (34 warnings)

**Severity**: Low (Warning)  
**Rule**: `no-deprecated-attr`  
**Impact**: Standards compliance, future compatibility

### Description
34 blog posts contain deprecated `frameborder="0"` attribute on `<iframe>` elements (mostly YouTube embeds).

### Affected Files (Sample)
- `blog/posts/2018-10-01-3d-point-cloud-classification-a-summary-of-useful-links.html`
- `blog/posts/2019-02-10-robotic-vision-summer-school-rvss-2019.html`
- `blog/posts/2020-07-27-surface-fitting-for-3d-point-cloud-deepfit.html`
- `blog/posts/2021-03-10-nesti-net-normal-estimation-for-3d-point-clouds.html`
- `blog/posts/2022-02-05-deep-declarative-networks.html`
- And 29 more...

### Recommended Fix
**Replace**: `<iframe frameborder="0" ...>`  
**With**: `<iframe style="border: none;" ...>` or add CSS rule: `iframe { border: none; }`

### Labels
`P3`, `bug`, `html`, `accessibility`

---

## Issue #2: Anchor Links Missing Descriptive Text (13 errors)

**Severity**: High (Error)  
**Rule**: `wcag/h30`  
**Impact**: Accessibility (WCAG 2.1 AA), Screen reader users

### Description
13 anchor (`<a>`) links lack descriptive text, making them inaccessible to screen reader users.

### Affected Files
- `contact/index.html` (4 instances - lines 157, 161, 165, 169 - social media icons)
- `blog/posts/2021-03-10-part-validation-dan-and-raz.html` (1 instance - line 236)
- `blog/posts/2022-08-09-bacon.html` (1 instance - line 199)
- `blog/posts/2022-10-19-keypointnerf.html` (2 instances - lines 199, 624)
- `blog/posts/2022-12-14-random-walks-for-adversarial-meshes.html` (4 instances - lines 208)

### Example Problem
```html
<!-- BAD: Empty link -->
<a href="https://twitter.com/username"></a>

<!-- BAD: Icon-only link without text -->
<a href="https://twitter.com/username"><i class="fab fa-twitter"></i></a>
```

### Recommended Fix
```html
<!-- GOOD: Add descriptive text -->
<a href="https://twitter.com/username">Follow me on Twitter</a>

<!-- GOOD: Add aria-label for icon-only links -->
<a href="https://twitter.com/username" aria-label="Follow me on Twitter">
  <i class="fab fa-twitter"></i>
</a>

<!-- GOOD: Add visually-hidden text -->
<a href="https://twitter.com/username">
  <i class="fab fa-twitter"></i>
  <span class="sr-only">Follow me on Twitter</span>
</a>
```

### Labels
`P1`, `bug`, `accessibility`, `wcag-aa`

---

## Issue #3: Deprecated `<center>` Tags (4 errors)

**Severity**: Medium (Error)  
**Rule**: `deprecated`, `element-permitted-content`  
**Impact**: Standards compliance, invalid HTML structure

### Description
4 blog posts use deprecated `<center>` tags for centering content.

### Affected Files
- `blog/posts/2017-01-30-helping-out-a-friend-with-processing.html` (2 instances - lines 201, 223)
- `blog/posts/2019-02-10-robotic-vision-summer-school-rvss-2019.html` (1 instance - line 222)

### Recommended Fix
**Replace**: `<center>...</center>`  
**With**: `<div style="text-align: center;">...</div>` or CSS class

### Labels
`P2`, `bug`, `html`

---

## Issue #4: Malformed HTML Structure (37 errors)

**Severity**: High (Error)  
**Rules**: `no-implicit-close`, `element-permitted-content`, `close-order`, `void-content`  
**Impact**: Browser rendering, accessibility, standards compliance

### Description
Multiple structural HTML errors across blog posts including:
- `<p>` elements not permitted inside `<code>` or `<pre>` tags
- Stray end tags (`</p>`)
- Elements implicitly closed by siblings
- Self-closing syntax on void elements (`<img></img>`)
- Invalid nesting (`<p>` inside `<p>`, `<a>` inside `<a>`)

### Affected Files by Error Type

#### 4.1: `<p>` Elements in Code Blocks (14 errors)
- `blog/posts/2017-02-16-tensorflow-deep-mnist-experts-tutorial.html` (3 errors)
- `blog/posts/2018-02-11-first-steps-deep-learning-using-tensorflow.html` (13 errors)
- `blog/posts/2021-03-10-gaussian-mixture-model-gmm-3d-point-cloud-classification-primer.html` (2 errors)

**Fix**: Remove `<p>` tags from within `<code>` and `<pre>` blocks. Use line breaks or proper code formatting.

#### 4.2: Stray End Tags (8 errors)
Multiple files with unclosed or mismatched tags causing stray `</p>` tags.

**Fix**: Ensure proper opening/closing tag pairs and valid nesting.

#### 4.3: Invalid Element Nesting (8 errors)
- `<center>` inside `<p>` (deprecated + invalid nesting)
- `<p>` inside `<p>` 
- `<a>` inside `<a>` (line 199 in keypointnerf post)

**Fix**: Restructure HTML to follow content model rules.

#### 4.4: Void Element Closing Tags (3 errors)
- `blog/posts/2020-11-29-how-to-improve-your-online-content-creation-quality-for-academics.html` (`</img>`)
- `blog/posts/2021-03-10-fisher-vector-for-3d-point-clouds-classification-primer.html` (`</img>`)
- `blog/posts/2021-03-10-gaussian-mixture-model-gmm-3d-point-cloud-classification-primer.html` (`</img>`)

**Fix**: Remove closing tags from void elements like `<img>`, `<br>`, `<input>`.

#### 4.5: Prefer Native Button Element (6 errors)
- `blog/posts/2020-08-24-the-story-behind-the-ikea-assembly-dataset-paper.html` (6 instances)

**Fix**: Replace clickable divs with role="button" with actual `<button>` elements.

### Labels
`P1`, `bug`, `html`, `accessibility`

---

## Issue #5: Empty Headings (2 warnings)

**Severity**: Low (Warning)  
**Rule**: `empty-heading`  
**Impact**: Accessibility, SEO

### Affected Files
- `blog/posts/2018-10-19-reasearch-visit-in-germany.html` (2 instances - lines 199, 233)

### Recommended Fix
Either add text content to `<h2>` tags or remove them if not needed.

### Labels
`P3`, `bug`, `html`, `accessibility`

---

## Issue #6: Deprecated Align Attributes (3 warnings)

**Severity**: Low (Warning)  
**Rule**: `no-deprecated-attr`  
**Impact**: Standards compliance

### Affected Files
- `blog/posts/2018-10-19-reasearch-visit-in-germany.html` (`align` on `<div>` - lines 254, 260)
- `blog/posts/2019-05-02-israel-machine-vision-conference-imvc-2019.html` (`align` on `<p>` - line 202)

### Recommended Fix
Replace `align` attribute with CSS `text-align` property.

### Labels
`P3`, `bug`, `html`

---

## Issue #7: Misused aria-label Attribute (1 warning)

**Severity**: Low (Warning)  
**Rule**: `aria-label-misuse`  
**Impact**: Accessibility

### Affected Files
- `contact/index.html` (line 123:74)

### Description
`aria-label` is being used on an element where it's not allowed or not effective.

### Recommended Fix
Review the element and use appropriate ARIA attributes or alternative accessible labeling methods.

### Labels
`P2`, `bug`, `accessibility`, `aria`

---

## Priority Recommendations

### High Priority (P1)
1. **Fix anchor links missing descriptive text** (13 errors) - Critical for accessibility
2. **Fix malformed HTML structure** (37 errors) - Affects rendering and accessibility

### Medium Priority (P2)
1. **Replace deprecated `<center>` tags** (4 errors) - Invalid HTML
2. **Fix aria-label misuse** (1 warning) - Accessibility improvement

### Low Priority (P3)
1. **Remove deprecated `frameborder` attributes** (34 warnings) - Standards compliance
2. **Fix empty headings** (2 warnings) - Minor accessibility/SEO issue
3. **Replace deprecated align attributes** (3 warnings) - Standards compliance

---

## How to Test Locally

```bash
# Build the site
npm run build

# Run HTML validation
npm run validate:html

# Check specific file
npx html-validate "_site/contact/index.html"
```

## Configuration Files
- `.htmlvalidate.json` - Validation rules (HTML5 + WCAG 2.1 AA)
- `.htmlvalidateignore` - Files excluded from validation
- `.github/workflows/html-validate.yml` - CI workflow

## References
- HTML-validate documentation: https://html-validate.org/
- WCAG 2.1 Guidelines: https://www.w3.org/WAI/WCAG21/quickref/
- Workflow run: https://github.com/sitzikbs/my_website/actions/runs/20735489532
