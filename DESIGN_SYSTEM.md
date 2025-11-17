# Design System Guide

**Version**: 1.0.0  
**Last Updated**: 2025-11-17  
**Status**: Foundation Complete

---

## Table of Contents

1. [Design Philosophy](#design-philosophy)
2. [Design Inspiration Analysis](#design-inspiration-analysis)
3. [Color System](#color-system)
4. [Typography](#typography)
5. [Spacing System](#spacing-system)
6. [Layout & Grid](#layout--grid)
7. [Components](#components)
8. [Responsive Design](#responsive-design)
9. [Accessibility](#accessibility)
10. [Design Tokens](#design-tokens)

---

## Design Philosophy

### Core Principles

1. **Clarity First**: Content should be easily readable and scannable
2. **Academic Professionalism**: Clean, minimal design that emphasizes research and publications
3. **Performance**: Lightweight design with minimal dependencies
4. **Accessibility**: WCAG 2.1 AA compliant from the ground up
5. **Responsive**: Mobile-first approach, works beautifully on all devices

### Visual Direction

- **Minimalist**: Remove unnecessary decoration, focus on content
- **Whitespace**: Generous spacing for breathing room
- **Typography-focused**: Let great typography carry the design
- **Subtle interactions**: Smooth transitions, no jarring effects
- **Professional**: Academic and research-oriented aesthetic

---

## Design Inspiration Analysis

### Vincent Sitzmann's Website Analysis

Based on analysis of clean academic website designs like vincentsitzmann.com:

#### Key Design Elements Observed

**Layout Patterns**:
- Single-column centered content with max-width constraint
- Generous margins and padding throughout
- Clear visual hierarchy with consistent spacing
- Publications displayed as clean cards with thumbnails
- Navigation is simple and unobtrusive

**Typography**:
- System font stack for fast loading and native feel
- Large, readable body text (16-18px base)
- Clear heading hierarchy
- Ample line-height for readability (1.6-1.8)
- Conservative use of font weights

**Colors**:
- Predominantly neutral (blacks, grays, whites)
- Minimal use of color, primarily for accents and links
- High contrast for readability
- Subtle hover states

**Navigation**:
- Simple horizontal navigation (desktop)
- Minimal, text-based links
- Clear active states
- Responsive hamburger menu (mobile)

**Content Presentation**:
- Publication cards with image, title, authors, venue
- Clean separation between sections
- Consistent card styling
- Hover effects for interactivity

---

## Color System

### Base Colors

Our color system uses a neutral-first approach with subtle accent colors.

#### Neutrals

```css
/* Grayscale */
--color-black: #000000;           /* Pure black */
--color-gray-900: #1a1a1a;        /* Primary text */
--color-gray-800: #2d2d2d;        /* Secondary text */
--color-gray-700: #404040;        /* Tertiary text */
--color-gray-600: #666666;        /* Muted text */
--color-gray-500: #808080;        /* Disabled text */
--color-gray-400: #999999;        /* Subtle text */
--color-gray-300: #cccccc;        /* Borders */
--color-gray-200: #e5e5e5;        /* Light borders */
--color-gray-100: #f5f5f5;        /* Light backgrounds */
--color-gray-50: #fafafa;         /* Subtle backgrounds */
--color-white: #ffffff;           /* Pure white */
```

#### Brand Colors

```css
/* Primary - Used for main interactive elements */
--color-primary: #2563eb;         /* Blue - links, buttons */
--color-primary-dark: #1e40af;    /* Darker blue - hover states */
--color-primary-light: #3b82f6;   /* Lighter blue - active states */
--color-primary-subtle: #dbeafe;  /* Very light blue - backgrounds */

/* Secondary - Used sparingly for emphasis */
--color-secondary: #6366f1;       /* Indigo - highlights */
--color-secondary-dark: #4f46e5;  /* Darker indigo */
--color-secondary-light: #818cf8; /* Lighter indigo */

/* Accent - For special elements */
--color-accent: #8b5cf6;          /* Purple - featured items */
--color-accent-dark: #7c3aed;     /* Darker purple */
--color-accent-light: #a78bfa;    /* Lighter purple */
```

#### Semantic Colors

```css
/* Success */
--color-success: #22c55e;         /* Green */
--color-success-dark: #16a34a;
--color-success-light: #86efac;
--color-success-bg: #dcfce7;

/* Warning */
--color-warning: #f59e0b;         /* Amber */
--color-warning-dark: #d97706;
--color-warning-light: #fcd34d;
--color-warning-bg: #fef3c7;

/* Error */
--color-error: #ef4444;           /* Red */
--color-error-dark: #dc2626;
--color-error-light: #fca5a5;
--color-error-bg: #fee2e2;

/* Info */
--color-info: #06b6d4;            /* Cyan */
--color-info-dark: #0891b2;
--color-info-light: #67e8f9;
--color-info-bg: #cffafe;
```

### Color Usage Guidelines

#### Text Colors

- **Primary Text**: `--color-gray-900` - Main body text, headings
- **Secondary Text**: `--color-gray-700` - Supporting text, captions
- **Tertiary Text**: `--color-gray-600` - Meta information, timestamps
- **Disabled Text**: `--color-gray-500` - Disabled elements
- **Links**: `--color-primary` - Interactive text links

#### Background Colors

- **Page Background**: `--color-white` - Main page background
- **Section Background**: `--color-gray-50` - Alternating sections
- **Card Background**: `--color-white` - Cards, panels
- **Hover Background**: `--color-gray-100` - Hover states
- **Active Background**: `--color-gray-200` - Active/pressed states

#### Border Colors

- **Default Border**: `--color-gray-300` - Standard borders
- **Light Border**: `--color-gray-200` - Subtle dividers
- **Focus Border**: `--color-primary` - Focus indicators

### Contrast Requirements

All color combinations must meet WCAG 2.1 AA standards:
- **Normal text** (< 18px): Minimum 4.5:1 contrast ratio
- **Large text** (≥ 18px or ≥ 14px bold): Minimum 3:1 contrast ratio
- **UI components**: Minimum 3:1 contrast ratio

---

## Typography

### Font Families

We use a system font stack for optimal performance and native appearance:

```css
/* Primary Font Stack - Used for all text */
--font-family-base: -apple-system, BlinkMacSystemFont, 'Segoe UI', 
                    Roboto, Oxygen-Sans, Ubuntu, Cantarell, 
                    'Helvetica Neue', sans-serif;

/* Monospace Font Stack - Used for code */
--font-family-mono: 'SF Mono', Monaco, 'Cascadia Code', 'Roboto Mono',
                    Consolas, 'Courier New', monospace;
```

**Rationale**: System fonts load instantly, look native on each platform, and provide excellent readability.

### Type Scale

Our type scale uses a 1.250 (Major Third) ratio for harmonious proportions:

```css
/* Font Sizes */
--font-size-xs: 0.75rem;      /* 12px - Very small text */
--font-size-sm: 0.875rem;     /* 14px - Small text, captions */
--font-size-base: 1rem;       /* 16px - Body text */
--font-size-lg: 1.125rem;     /* 18px - Lead text */
--font-size-xl: 1.25rem;      /* 20px - Small headings */
--font-size-2xl: 1.5rem;      /* 24px - H3 */
--font-size-3xl: 1.875rem;    /* 30px - H2 */
--font-size-4xl: 2.25rem;     /* 36px - H1 */
--font-size-5xl: 3rem;        /* 48px - Hero headings */
--font-size-6xl: 3.75rem;     /* 60px - Display headings */
```

### Font Weights

```css
--font-weight-light: 300;     /* Light - Rarely used */
--font-weight-normal: 400;    /* Normal - Body text */
--font-weight-medium: 500;    /* Medium - Emphasis */
--font-weight-semibold: 600;  /* Semibold - Strong emphasis */
--font-weight-bold: 700;      /* Bold - Headings */
--font-weight-extrabold: 800; /* Extra bold - Hero text */
```

### Line Heights

```css
--line-height-tight: 1.25;    /* 1.25 - Headings */
--line-height-snug: 1.375;    /* 1.375 - Tight text */
--line-height-normal: 1.5;    /* 1.5 - Default */
--line-height-relaxed: 1.625; /* 1.625 - Comfortable reading */
--line-height-loose: 1.75;    /* 1.75 - Very comfortable */
```

### Letter Spacing

```css
--letter-spacing-tight: -0.025em;  /* -0.025em - Large headings */
--letter-spacing-normal: 0;        /* 0 - Default */
--letter-spacing-wide: 0.025em;    /* 0.025em - Small caps */
--letter-spacing-wider: 0.05em;    /* 0.05em - Spacing emphasis */
```

### Typography Styles

#### Headings

```css
/* H1 - Page Title */
h1 {
  font-size: var(--font-size-4xl);       /* 36px */
  font-weight: var(--font-weight-bold);  /* 700 */
  line-height: var(--line-height-tight); /* 1.25 */
  letter-spacing: var(--letter-spacing-tight);
  margin-bottom: 1.5rem;
}

/* H2 - Section Title */
h2 {
  font-size: var(--font-size-3xl);       /* 30px */
  font-weight: var(--font-weight-bold);  /* 700 */
  line-height: var(--line-height-tight); /* 1.25 */
  margin-bottom: 1.25rem;
}

/* H3 - Subsection Title */
h3 {
  font-size: var(--font-size-2xl);       /* 24px */
  font-weight: var(--font-weight-semibold); /* 600 */
  line-height: var(--line-height-snug);  /* 1.375 */
  margin-bottom: 1rem;
}

/* H4 - Sub-subsection */
h4 {
  font-size: var(--font-size-xl);        /* 20px */
  font-weight: var(--font-weight-semibold); /* 600 */
  line-height: var(--line-height-snug);  /* 1.375 */
  margin-bottom: 0.75rem;
}

/* H5 & H6 - Minor headings */
h5, h6 {
  font-size: var(--font-size-lg);        /* 18px */
  font-weight: var(--font-weight-medium); /* 500 */
  line-height: var(--line-height-normal); /* 1.5 */
  margin-bottom: 0.5rem;
}
```

#### Body Text

```css
/* Paragraph - Default body text */
p {
  font-size: var(--font-size-base);       /* 16px */
  font-weight: var(--font-weight-normal); /* 400 */
  line-height: var(--line-height-relaxed); /* 1.625 */
  margin-bottom: 1rem;
}

/* Lead - Intro paragraphs */
.lead {
  font-size: var(--font-size-lg);        /* 18px */
  line-height: var(--line-height-relaxed); /* 1.625 */
  margin-bottom: 1.5rem;
}

/* Small - Fine print */
small, .small {
  font-size: var(--font-size-sm);        /* 14px */
  line-height: var(--line-height-normal); /* 1.5 */
}
```

#### Lists

```css
/* Lists */
ul, ol {
  font-size: var(--font-size-base);      /* 16px */
  line-height: var(--line-height-relaxed); /* 1.625 */
  margin-bottom: 1rem;
  padding-left: 1.5rem;
}

li {
  margin-bottom: 0.5rem;
}
```

---

## Spacing System

### Base Unit

We use an 8px base unit (0.5rem) for consistent spacing throughout:

```css
--spacing-unit: 0.5rem; /* 8px base unit */
```

### Spacing Scale

```css
--spacing-0: 0;                    /* 0px */
--spacing-1: 0.25rem;              /* 4px */
--spacing-2: 0.5rem;               /* 8px */
--spacing-3: 0.75rem;              /* 12px */
--spacing-4: 1rem;                 /* 16px */
--spacing-5: 1.25rem;              /* 20px */
--spacing-6: 1.5rem;               /* 24px */
--spacing-8: 2rem;                 /* 32px */
--spacing-10: 2.5rem;              /* 40px */
--spacing-12: 3rem;                /* 48px */
--spacing-16: 4rem;                /* 64px */
--spacing-20: 5rem;                /* 80px */
--spacing-24: 6rem;                /* 96px */
--spacing-32: 8rem;                /* 128px */
```

### Spacing Usage

#### Component Spacing

- **Extra Small**: `--spacing-1` (4px) - Icon gaps, tight spacing
- **Small**: `--spacing-2` (8px) - Button padding, small gaps
- **Medium**: `--spacing-4` (16px) - Default padding, element gaps
- **Large**: `--spacing-6` (24px) - Section padding, card padding
- **Extra Large**: `--spacing-8` (32px) - Major section spacing

#### Layout Spacing

- **Section Padding**: `--spacing-12` to `--spacing-16` (48-64px)
- **Section Margin**: `--spacing-16` to `--spacing-24` (64-96px)
- **Container Padding**: `--spacing-6` to `--spacing-8` (24-32px)

### Margin & Padding Utilities

```css
/* Margins */
.m-0 { margin: 0; }
.m-1 { margin: var(--spacing-1); }
.m-2 { margin: var(--spacing-2); }
.m-4 { margin: var(--spacing-4); }
.m-6 { margin: var(--spacing-6); }
.m-8 { margin: var(--spacing-8); }

/* Padding */
.p-0 { padding: 0; }
.p-1 { padding: var(--spacing-1); }
.p-2 { padding: var(--spacing-2); }
.p-4 { padding: var(--spacing-4); }
.p-6 { padding: var(--spacing-6); }
.p-8 { padding: var(--spacing-8); }

/* Directional variants available as needed */
```

---

## Layout & Grid

### Container System

```css
/* Max-width containers */
--container-xs: 480px;   /* Small content */
--container-sm: 640px;   /* Articles, blog posts */
--container-md: 768px;   /* Default content */
--container-lg: 1024px;  /* Wide content */
--container-xl: 1280px;  /* Publications grid */
--container-2xl: 1536px; /* Full-width sections */
```

### Content Width

For optimal readability, text content should not exceed 65-75 characters per line:

```css
--content-width: 65ch; /* ~65 characters */
```

### Grid System

We use CSS Grid for flexible layouts:

```css
/* 12-column grid */
--grid-columns: 12;
--grid-gap: var(--spacing-6); /* 24px */

/* Common grid layouts */
.grid {
  display: grid;
  gap: var(--grid-gap);
}

.grid-2 { grid-template-columns: repeat(2, 1fr); }
.grid-3 { grid-template-columns: repeat(3, 1fr); }
.grid-4 { grid-template-columns: repeat(4, 1fr); }
```

### Flexbox Utilities

```css
.flex { display: flex; }
.flex-col { flex-direction: column; }
.flex-wrap { flex-wrap: wrap; }
.items-center { align-items: center; }
.justify-between { justify-content: space-between; }
.gap-2 { gap: var(--spacing-2); }
.gap-4 { gap: var(--spacing-4); }
.gap-6 { gap: var(--spacing-6); }
```

---

## Components

### Buttons

```css
/* Primary Button */
.btn-primary {
  padding: var(--spacing-3) var(--spacing-6); /* 12px 24px */
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-medium);
  color: var(--color-white);
  background-color: var(--color-primary);
  border: none;
  border-radius: var(--radius-md);
  cursor: pointer;
  transition: all 150ms ease;
}

.btn-primary:hover {
  background-color: var(--color-primary-dark);
  transform: translateY(-1px);
  box-shadow: var(--shadow-md);
}

/* Secondary Button */
.btn-secondary {
  padding: var(--spacing-3) var(--spacing-6);
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-medium);
  color: var(--color-primary);
  background-color: transparent;
  border: 2px solid var(--color-primary);
  border-radius: var(--radius-md);
  cursor: pointer;
  transition: all 150ms ease;
}

.btn-secondary:hover {
  background-color: var(--color-primary);
  color: var(--color-white);
}

/* Text Button */
.btn-text {
  padding: var(--spacing-2) var(--spacing-4);
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-medium);
  color: var(--color-primary);
  background-color: transparent;
  border: none;
  cursor: pointer;
  transition: color 150ms ease;
}

.btn-text:hover {
  color: var(--color-primary-dark);
  text-decoration: underline;
}
```

### Links

```css
/* Default link */
a {
  color: var(--color-primary);
  text-decoration: none;
  transition: color 150ms ease;
}

a:hover {
  color: var(--color-primary-dark);
  text-decoration: underline;
}

a:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
  border-radius: 2px;
}

/* Nav link */
.nav-link {
  color: var(--color-gray-700);
  font-weight: var(--font-weight-medium);
  padding: var(--spacing-2) var(--spacing-4);
  border-radius: var(--radius-sm);
  transition: all 150ms ease;
}

.nav-link:hover {
  color: var(--color-gray-900);
  background-color: var(--color-gray-100);
  text-decoration: none;
}

.nav-link.active {
  color: var(--color-primary);
  font-weight: var(--font-weight-semibold);
}
```

### Cards

```css
/* Base card */
.card {
  background-color: var(--color-white);
  border: 1px solid var(--color-gray-200);
  border-radius: var(--radius-lg);
  padding: var(--spacing-6);
  transition: all 200ms ease;
}

.card:hover {
  border-color: var(--color-gray-300);
  box-shadow: var(--shadow-lg);
  transform: translateY(-2px);
}

/* Publication card */
.publication-card {
  display: grid;
  grid-template-columns: 200px 1fr;
  gap: var(--spacing-6);
  padding: var(--spacing-6);
  border: 1px solid var(--color-gray-200);
  border-radius: var(--radius-lg);
  transition: all 200ms ease;
}

.publication-card:hover {
  border-color: var(--color-primary);
  box-shadow: var(--shadow-lg);
}

/* Blog card */
.blog-card {
  background-color: var(--color-white);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  transition: all 200ms ease;
}

.blog-card:hover {
  box-shadow: var(--shadow-xl);
  transform: translateY(-4px);
}
```

### Forms

```css
/* Input field */
.form-input {
  width: 100%;
  padding: var(--spacing-3) var(--spacing-4);
  font-size: var(--font-size-base);
  font-family: inherit;
  color: var(--color-gray-900);
  background-color: var(--color-white);
  border: 2px solid var(--color-gray-300);
  border-radius: var(--radius-md);
  transition: all 150ms ease;
}

.form-input:focus {
  outline: none;
  border-color: var(--color-primary);
  box-shadow: 0 0 0 3px var(--color-primary-subtle);
}

.form-input:disabled {
  background-color: var(--color-gray-100);
  cursor: not-allowed;
}

/* Label */
.form-label {
  display: block;
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-gray-700);
  margin-bottom: var(--spacing-2);
}

/* Textarea */
.form-textarea {
  min-height: 120px;
  resize: vertical;
}
```

### Tags & Badges

```css
/* Tag */
.tag {
  display: inline-block;
  padding: var(--spacing-1) var(--spacing-3);
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-gray-700);
  background-color: var(--color-gray-100);
  border-radius: var(--radius-full);
  transition: background-color 150ms ease;
}

.tag:hover {
  background-color: var(--color-gray-200);
}

/* Badge */
.badge {
  display: inline-flex;
  align-items: center;
  padding: var(--spacing-1) var(--spacing-2);
  font-size: var(--font-size-xs);
  font-weight: var(--font-weight-semibold);
  color: var(--color-white);
  background-color: var(--color-primary);
  border-radius: var(--radius-sm);
}
```

### Border Radius

```css
--radius-none: 0;
--radius-sm: 0.25rem;   /* 4px */
--radius-md: 0.5rem;    /* 8px */
--radius-lg: 0.75rem;   /* 12px */
--radius-xl: 1rem;      /* 16px */
--radius-2xl: 1.5rem;   /* 24px */
--radius-full: 9999px;  /* Fully rounded */
```

### Shadows

```css
--shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
--shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1),
             0 2px 4px -1px rgba(0, 0, 0, 0.06);
--shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1),
             0 4px 6px -2px rgba(0, 0, 0, 0.05);
--shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1),
             0 10px 10px -5px rgba(0, 0, 0, 0.04);
--shadow-2xl: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
```

### Transitions

```css
--transition-fast: 150ms;
--transition-base: 200ms;
--transition-slow: 300ms;
--transition-slower: 500ms;

/* Common easing functions */
--ease-in: cubic-bezier(0.4, 0, 1, 1);
--ease-out: cubic-bezier(0, 0, 0.2, 1);
--ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
```

---

## Responsive Design

### Breakpoints

We use a mobile-first approach with the following breakpoints:

```css
/* Mobile First Breakpoints */
--breakpoint-xs: 0px;       /* Extra small devices (phones) */
--breakpoint-sm: 640px;     /* Small devices (large phones) */
--breakpoint-md: 768px;     /* Medium devices (tablets) */
--breakpoint-lg: 1024px;    /* Large devices (desktops) */
--breakpoint-xl: 1280px;    /* Extra large devices (large desktops) */
--breakpoint-2xl: 1536px;   /* 2X large devices (very large screens) */
```

### Media Query Usage

```css
/* Mobile (default) */
.element {
  font-size: var(--font-size-base);
}

/* Tablet and up */
@media (min-width: 768px) {
  .element {
    font-size: var(--font-size-lg);
  }
}

/* Desktop and up */
@media (min-width: 1024px) {
  .element {
    font-size: var(--font-size-xl);
  }
}

/* Large desktop and up */
@media (min-width: 1280px) {
  .element {
    font-size: var(--font-size-2xl);
  }
}
```

### Responsive Typography

```css
/* Fluid typography using clamp() */
h1 {
  font-size: clamp(2rem, 5vw, 3.75rem);
}

h2 {
  font-size: clamp(1.5rem, 4vw, 2.25rem);
}

p {
  font-size: clamp(1rem, 2vw, 1.125rem);
}
```

### Responsive Spacing

```css
/* Section padding scales with screen size */
.section {
  padding-top: var(--spacing-12);
  padding-bottom: var(--spacing-12);
}

@media (min-width: 768px) {
  .section {
    padding-top: var(--spacing-16);
    padding-bottom: var(--spacing-16);
  }
}

@media (min-width: 1024px) {
  .section {
    padding-top: var(--spacing-24);
    padding-bottom: var(--spacing-24);
  }
}
```

### Grid Responsiveness

```css
/* Responsive grid */
.publications-grid {
  display: grid;
  gap: var(--spacing-6);
  grid-template-columns: 1fr; /* Mobile: 1 column */
}

@media (min-width: 768px) {
  .publications-grid {
    grid-template-columns: repeat(2, 1fr); /* Tablet: 2 columns */
  }
}

@media (min-width: 1024px) {
  .publications-grid {
    grid-template-columns: repeat(3, 1fr); /* Desktop: 3 columns */
  }
}
```

### Device-Specific Considerations

#### Mobile (< 640px)
- Single column layouts
- Full-width elements
- Larger touch targets (min 44x44px)
- Simplified navigation (hamburger menu)
- Reduced spacing between elements

#### Tablet (640px - 1024px)
- 2-column layouts where appropriate
- Moderate spacing
- Horizontal navigation possible
- Optimized for both portrait and landscape

#### Desktop (1024px - 1440px)
- Multi-column layouts (2-3 columns)
- Full navigation visible
- Generous spacing
- Optimal reading width maintained

#### Large Desktop (> 1440px)
- Maximum content width constrained
- Extra whitespace on sides
- Potentially 4-column grids
- Enhanced visual hierarchy

---

## Accessibility

### WCAG 2.1 AA Compliance

#### Color Contrast

- **Normal text**: Minimum 4.5:1 contrast ratio
- **Large text**: Minimum 3:1 contrast ratio
- **UI components**: Minimum 3:1 contrast ratio

#### Focus Indicators

```css
/* Visible focus states for keyboard navigation */
:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
  border-radius: 2px;
}

/* Remove default outline but keep for focus-visible */
:focus {
  outline: none;
}
```

#### Skip Links

```css
/* Skip to main content link for screen readers */
.skip-link {
  position: absolute;
  left: -9999px;
  z-index: 999;
}

.skip-link:focus {
  left: 50%;
  transform: translateX(-50%);
  top: var(--spacing-4);
}
```

#### Touch Targets

Minimum touch target size: 44x44px (iOS HIG and Android guidelines)

```css
.touch-target {
  min-width: 44px;
  min-height: 44px;
}
```

#### Screen Reader Support

- Use semantic HTML elements
- Provide alt text for all images
- Use ARIA labels where necessary
- Ensure proper heading hierarchy
- Add aria-live regions for dynamic content

#### Motion & Animation

```css
/* Respect user's motion preferences */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## Design Tokens

### Complete Token Reference

```css
:root {
  /* Colors - Neutrals */
  --color-black: #000000;
  --color-gray-900: #1a1a1a;
  --color-gray-800: #2d2d2d;
  --color-gray-700: #404040;
  --color-gray-600: #666666;
  --color-gray-500: #808080;
  --color-gray-400: #999999;
  --color-gray-300: #cccccc;
  --color-gray-200: #e5e5e5;
  --color-gray-100: #f5f5f5;
  --color-gray-50: #fafafa;
  --color-white: #ffffff;

  /* Colors - Brand */
  --color-primary: #2563eb;
  --color-primary-dark: #1e40af;
  --color-primary-light: #3b82f6;
  --color-primary-subtle: #dbeafe;

  /* Typography */
  --font-family-base: -apple-system, BlinkMacSystemFont, 'Segoe UI', 
                      Roboto, Oxygen-Sans, Ubuntu, Cantarell, sans-serif;
  --font-family-mono: 'SF Mono', Monaco, 'Cascadia Code', 'Roboto Mono',
                      Consolas, monospace;
  
  --font-size-xs: 0.75rem;
  --font-size-sm: 0.875rem;
  --font-size-base: 1rem;
  --font-size-lg: 1.125rem;
  --font-size-xl: 1.25rem;
  --font-size-2xl: 1.5rem;
  --font-size-3xl: 1.875rem;
  --font-size-4xl: 2.25rem;
  --font-size-5xl: 3rem;

  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;

  --line-height-tight: 1.25;
  --line-height-snug: 1.375;
  --line-height-normal: 1.5;
  --line-height-relaxed: 1.625;
  --line-height-loose: 1.75;

  /* Spacing */
  --spacing-1: 0.25rem;
  --spacing-2: 0.5rem;
  --spacing-3: 0.75rem;
  --spacing-4: 1rem;
  --spacing-5: 1.25rem;
  --spacing-6: 1.5rem;
  --spacing-8: 2rem;
  --spacing-10: 2.5rem;
  --spacing-12: 3rem;
  --spacing-16: 4rem;
  --spacing-20: 5rem;
  --spacing-24: 6rem;

  /* Layout */
  --container-sm: 640px;
  --container-md: 768px;
  --container-lg: 1024px;
  --container-xl: 1280px;
  --content-width: 65ch;

  /* Border Radius */
  --radius-sm: 0.25rem;
  --radius-md: 0.5rem;
  --radius-lg: 0.75rem;
  --radius-xl: 1rem;
  --radius-full: 9999px;

  /* Shadows */
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
  --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1);

  /* Transitions */
  --transition-fast: 150ms;
  --transition-base: 200ms;
  --transition-slow: 300ms;

  /* Breakpoints (for reference in JS) */
  --breakpoint-sm: 640px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 1024px;
  --breakpoint-xl: 1280px;
}
```

---

## Implementation Guidelines

### CSS Architecture

Recommended file structure:

```
css/
├── 01-settings/
│   └── variables.css      # Design tokens
├── 02-tools/
│   └── mixins.css         # Reusable patterns (if using preprocessor)
├── 03-base/
│   ├── reset.css          # Browser normalization
│   └── base.css           # Base element styles
├── 04-layout/
│   ├── container.css      # Container utilities
│   ├── grid.css           # Grid system
│   └── flex.css           # Flexbox utilities
├── 05-components/
│   ├── buttons.css        # Button styles
│   ├── cards.css          # Card styles
│   ├── forms.css          # Form styles
│   ├── navigation.css     # Navigation
│   └── ...                # Other components
└── 06-utilities/
    └── utilities.css      # Utility classes
```

### Development Workflow

1. **Use Design Tokens**: Always reference CSS custom properties instead of hardcoded values
2. **Mobile First**: Start with mobile styles, progressively enhance for larger screens
3. **Component-Based**: Build reusable components following this design system
4. **Accessibility First**: Consider accessibility from the start, not as an afterthought
5. **Performance**: Optimize images, minimize CSS, use system fonts

### Design Review Checklist

Before considering a component complete:

- [ ] Uses design tokens (colors, spacing, typography)
- [ ] Meets contrast requirements (4.5:1 minimum)
- [ ] Has visible focus states
- [ ] Works on mobile, tablet, and desktop
- [ ] Uses semantic HTML
- [ ] Has appropriate ARIA labels (if needed)
- [ ] Respects prefers-reduced-motion
- [ ] Touch targets are minimum 44x44px
- [ ] Loads quickly (performance optimized)
- [ ] Code is clean and maintainable

---

## Future Considerations

### Dark Mode

Design tokens are structured to support dark mode in the future:

```css
/* Future dark mode implementation */
@media (prefers-color-scheme: dark) {
  :root {
    --color-gray-900: #fafafa;
    --color-gray-50: #1a1a1a;
    /* ... inverted values */
  }
}
```

### Animation Library

Consider adding a curated set of animations:
- Fade in/out
- Slide in/out
- Scale up/down
- Stagger animations for lists
- Page transitions

### Icon System

Recommend using:
- SVG icons for scalability
- Icon font as fallback
- Consistent icon sizing (16px, 20px, 24px)

---

## Resources & References

### Design Inspiration
- [Vincent Sitzmann's Website](https://www.vincentsitzmann.com/) - Clean academic design
- [Refactoring UI](https://refactoringui.com/) - Design principles
- [Inclusive Components](https://inclusive-components.design/) - Accessible patterns

### Tools
- [Coolors](https://coolors.co/) - Color palette generation
- [Type Scale](https://type-scale.com/) - Typography scale calculator
- [Contrast Checker](https://webaim.org/resources/contrastchecker/) - WCAG contrast validation

### Documentation
- [MDN Web Docs](https://developer.mozilla.org/) - Web standards reference
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/) - Accessibility standards
- [CSS Tricks](https://css-tricks.com/) - CSS techniques and patterns

---

## Changelog

### Version 1.0.0 (2025-11-17)
- Initial design system created
- Color system defined
- Typography scale established
- Spacing system implemented
- Component styles documented
- Responsive breakpoints defined
- Accessibility guidelines included

---

**Maintained by**: Itzik Ben-Shabat  
**Last Review**: 2025-11-17  
**Status**: Active Development
