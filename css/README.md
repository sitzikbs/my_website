# CSS Architecture

This directory contains the modular CSS architecture for the website, following a mobile-first responsive design approach.

## File Structure

The CSS is organized into modular files following a clear separation of concerns:

```
css/
├── reset.css       - Browser normalization
├── variables.css   - Design tokens (CSS custom properties)
├── base.css        - Global styles and typography
├── layout.css      - Layout utilities and grid system
├── components.css  - Reusable component styles
└── responsive.css  - Media queries for responsive design
```

## Loading Order

For optimal cascade and specificity management, load the CSS files in this order:

```html
<!-- 1. Reset - Browser normalization -->
<link rel="stylesheet" href="css/reset.css">

<!-- 2. Variables - Design tokens -->
<link rel="stylesheet" href="css/variables.css">

<!-- 3. Base - Global styles -->
<link rel="stylesheet" href="css/base.css">

<!-- 4. Layout - Layout utilities -->
<link rel="stylesheet" href="css/layout.css">

<!-- 5. Components - Component styles -->
<link rel="stylesheet" href="css/components.css">

<!-- 6. Responsive - Media queries -->
<link rel="stylesheet" href="css/responsive.css">
```

## File Descriptions

### reset.css
- Modern CSS reset based on current best practices
- Ensures consistent baseline across all browsers
- Removes default margins, paddings, and browser-specific styles
- Includes accessibility features like reduced motion support

### variables.css
- CSS custom properties (design tokens) for the entire design system
- Colors (neutrals, brand, semantic)
- Typography (font families, sizes, weights, line heights)
- Spacing scale (based on 8px unit)
- Layout values (container widths, grid settings)
- Border radius, shadows, transitions
- Breakpoint values (for reference)

### base.css
- Global element styles
- Typography styles for headings, paragraphs, lists
- Link styles with hover and focus states
- Code and blockquote styles
- Table styles
- Accessibility utilities (skip links, screen reader only)
- Text selection styles

### layout.css
- Container system with responsive widths
- Section spacing utilities
- CSS Grid system with column utilities
- Flexbox utilities (direction, alignment, justify)
- Spacing utilities (margin, padding)
- Display, position, and text alignment utilities

### components.css
- Reusable component patterns
- Buttons (primary, secondary, text, sizes)
- Navigation links and navbar
- Cards (base, publication, blog)
- Forms (inputs, textareas, labels)
- Tags and badges
- Alert messages
- Avatars
- Dividers

### responsive.css
- Mobile-first media queries
- Breakpoints: 640px (sm), 768px (md), 1024px (lg), 1280px (xl), 1536px (2xl)
- Responsive typography scaling
- Responsive grid column utilities
- Responsive display and flex utilities
- Touch device optimizations
- Print styles
- High contrast mode support
- Dark mode placeholder (for future implementation)

## Design Philosophy

### Mobile-First Approach
All styles are written mobile-first, with progressive enhancement for larger screens:
- Base styles target mobile devices
- Media queries use `min-width` to add styles for larger screens
- This ensures optimal performance on mobile devices

### CSS Custom Properties
The system uses CSS custom properties extensively for:
- Easy theming and customization
- Consistent design system implementation
- Better maintainability
- Future dark mode support

### Cascade & Specificity
Files are ordered to manage specificity naturally:
1. Reset removes browser defaults
2. Variables define tokens (no specificity)
3. Base styles elements directly (low specificity)
4. Layout provides utilities (moderate specificity)
5. Components target classes (moderate specificity)
6. Responsive overrides when needed (higher specificity via media queries)

### Accessibility
- WCAG 2.1 AA compliant color contrast
- Visible focus states for keyboard navigation
- Skip links for screen reader users
- Minimum 44px touch targets
- Respect for reduced motion preferences
- Semantic HTML encouraged

## Usage Examples

### Using the Grid System
```html
<!-- Mobile: 1 column, Tablet: 2 columns, Desktop: 3 columns -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
  <div class="card">Card 1</div>
  <div class="card">Card 2</div>
  <div class="card">Card 3</div>
</div>
```

### Using Flexbox Utilities
```html
<div class="flex flex-col md:flex-row justify-between items-center gap-4">
  <div>Content 1</div>
  <div>Content 2</div>
</div>
```

### Using Components
```html
<!-- Button -->
<button class="btn btn-primary">Click Me</button>

<!-- Card -->
<div class="card">
  <h3 class="card-title">Card Title</h3>
  <p class="card-text">Card content goes here.</p>
</div>

<!-- Publication Card -->
<article class="publication-card">
  <img src="image.jpg" alt="" class="publication-card-image">
  <div class="publication-card-content">
    <h3 class="publication-card-title">Paper Title</h3>
    <p class="publication-card-authors">Author Names</p>
    <p class="publication-card-venue">Conference/Journal</p>
  </div>
</article>
```

### Using Spacing Utilities
```html
<div class="mt-8 mb-6 p-4">
  Content with custom spacing
</div>
```

## Browser Support

This CSS architecture supports:
- Modern evergreen browsers (Chrome, Firefox, Safari, Edge)
- iOS Safari 12+
- Android Chrome 90+

Features used:
- CSS Custom Properties
- CSS Grid
- Flexbox
- Modern CSS selectors
- Media queries

## Performance

- No CSS preprocessor required (pure CSS)
- Uses system fonts for instant loading
- Modular structure allows for selective loading
- Custom properties reduce file size
- No JavaScript dependencies

## Future Enhancements

- Dark mode implementation (structure ready)
- Additional component patterns as needed
- Animation library
- Icon system integration
- CSS custom properties for dynamic theming

## References

- Based on the comprehensive Design System documented in `DESIGN_SYSTEM.md`
- Follows BEM-like naming conventions for components
- Utility-first approach for layout and spacing
- Semantic component classes for common patterns

## Testing

Test the CSS implementation across:
- [ ] Mobile devices (< 640px)
- [ ] Tablets (640px - 1024px)
- [ ] Desktops (1024px+)
- [ ] Chrome, Firefox, Safari, Edge
- [ ] Keyboard navigation (focus states)
- [ ] Screen readers
- [ ] Reduced motion preferences
- [ ] High contrast mode
- [ ] Print layout

---

**Version**: 1.0.0  
**Last Updated**: 2025-11-17  
**Maintained by**: Itzik Ben-Shabat
