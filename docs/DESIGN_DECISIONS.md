# Design Decisions & Rationale

**Version**: 1.0.0  
**Date**: 2025-11-17  
**Status**: Foundation Complete

---

## Overview

This document explains the reasoning behind key design decisions made for the personal academic website. It serves as a reference for future changes and helps maintain design consistency.

---

## Table of Contents

1. [Design Philosophy](#design-philosophy)
2. [Color Choices](#color-choices)
3. [Typography Decisions](#typography-decisions)
4. [Layout Approach](#layout-approach)
5. [Component Design](#component-design)
6. [Responsive Strategy](#responsive-strategy)
7. [Performance Considerations](#performance-considerations)
8. [Accessibility Choices](#accessibility-choices)

---

## Design Philosophy

### Why Minimalism?

**Decision**: Adopt a clean, minimal design aesthetic.

**Rationale**:
- **Content Focus**: Research and publications should be the star, not the design
- **Professionalism**: Academic websites benefit from understated, professional aesthetics
- **Performance**: Minimal design = less code = faster loading
- **Timelessness**: Simple designs age better than trendy ones
- **Accessibility**: Simpler interfaces are easier to navigate for all users

**Inspiration**: Academic websites like Vincent Sitzmann's demonstrate that minimal design can be both beautiful and functional.

### Why No Framework?

**Decision**: Use vanilla HTML, CSS, and JavaScript instead of frameworks.

**Rationale**:
- **Performance**: No framework overhead (React, Vue, etc. add ~100KB+)
- **Simplicity**: Easier to maintain and understand for future contributors
- **Control**: Full control over every aspect of the design
- **Learning**: Better demonstrates web fundamentals
- **Longevity**: Less likely to become outdated or deprecated

---

## Color Choices

### Neutral-First Palette

**Decision**: Use predominantly grayscale colors with blue accents.

**Rationale**:
- **Professionalism**: Neutral colors convey academic seriousness
- **Readability**: High contrast black text on white background is most readable
- **Versatility**: Neutral base allows accent colors to stand out
- **Accessibility**: Easy to maintain WCAG contrast requirements
- **Print-Friendly**: Grayscale designs print well

### Blue as Primary Color

**Decision**: Use blue (#2563eb) as the primary interactive color.

**Rationale**:
- **Trust**: Blue conveys trust, intelligence, and professionalism
- **Convention**: Blue is universally understood as the color for links
- **Accessibility**: Blue provides good contrast against white backgrounds
- **Gender-Neutral**: Appeals broadly without gender bias
- **Scientific**: Associated with technology and academia

### Subtle Color Usage

**Decision**: Use color sparingly, primarily for interactive elements.

**Rationale**:
- **Focus**: Draws attention to important interactive elements
- **Clarity**: Reduces visual noise and cognitive load
- **Elegance**: Restraint in color usage appears more sophisticated
- **Consistency**: Easier to maintain consistent color application

---

## Typography Decisions

### System Font Stack

**Decision**: Use system fonts rather than web fonts.

**Rationale**:
- **Performance**: Zero network requests, instant rendering
- **Familiarity**: Users are accustomed to their system fonts
- **Quality**: System fonts are professionally designed and optimized
- **Consistency**: Matches the user's operating system aesthetic
- **Accessibility**: Better rendering for users with reading difficulties

### Type Scale (1.250 Major Third)

**Decision**: Use a 1.250 ratio for the type scale.

**Rationale**:
- **Harmony**: Creates visually harmonious size relationships
- **Readability**: Provides clear distinction between heading levels
- **Moderation**: Not too aggressive (1.5) or too subtle (1.125)
- **Standard**: Widely used ratio in professional typography

### Line Height (1.625 for Body)

**Decision**: Use 1.625 line height for body text.

**Rationale**:
- **Readability**: Optimal for comfortable reading of longer texts
- **Research-Backed**: Studies show 1.5-1.7 is ideal for body text
- **Accessibility**: Helps users with dyslexia or vision impairments
- **Balance**: Not too tight (claustrophobic) or too loose (disjointed)

---

## Responsive Strategy

### Mobile-First Approach

**Decision**: Design for mobile first, then enhance for larger screens.

**Rationale**:
- **Progressive Enhancement**: Ensures core functionality works everywhere
- **Performance**: Mobile CSS is loaded by default, desktop adds enhancements
- **Focus**: Forces prioritization of essential content
- **Modern Best Practice**: Industry standard approach
- **Mobile Traffic**: Increasing percentage of users on mobile devices

### Breakpoint Choices

**Decision**: Use breakpoints at 640px, 768px, 1024px, and 1280px.

**Rationale**:
- **Device Coverage**: Aligns with common device sizes
- **Standards**: Matches frameworks like Tailwind CSS
- **Flexibility**: Provides granular control without being excessive
- **Future-Proof**: Works with emerging device sizes

---

## Performance Considerations

### No External Dependencies

**Decision**: Avoid external libraries and frameworks where possible.

**Rationale**:
- **Speed**: Eliminates network requests for dependencies
- **Reliability**: No dependency on third-party CDNs
- **Size**: Dramatically reduces page weight
- **Control**: Full control over code and no version conflicts
- **Privacy**: No tracking from external services

### CSS Custom Properties

**Decision**: Use CSS custom properties for design tokens.

**Rationale**:
- **Performance**: Native browser feature, no preprocessing needed
- **Dynamic**: Can be changed with JavaScript if needed
- **Inheritance**: Leverages CSS cascade naturally
- **Debugging**: Visible in browser DevTools
- **Modern**: Widely supported in all modern browsers

---

## Accessibility Choices

### WCAG 2.1 AA Target

**Decision**: Target WCAG 2.1 Level AA compliance.

**Rationale**:
- **Legal**: Required by many institutions and countries
- **Inclusive**: Makes site usable by people with disabilities
- **Ethical**: Right thing to do for all users
- **SEO**: Accessibility improvements often improve SEO
- **Quality**: Forces better overall design decisions

### Semantic HTML

**Decision**: Use semantic HTML5 elements throughout.

**Rationale**:
- **Accessibility**: Screen readers rely on semantic structure
- **SEO**: Search engines understand content better
- **Maintainability**: Code is more readable and maintainable
- **Standards**: Following web standards best practices
- **Future-Proof**: More likely to work with future technologies

---

## Trade-offs & Compromises

### No Dark Mode (Initially)

**Decision**: Launch without dark mode support.

**Rationale**:
- **Scope**: Reduces initial development complexity
- **Testing**: Simpler to test and debug single theme
- **Future**: Can be added later without breaking changes
- **Design System**: Tokens are structured to support it later

---

## References

### Research & Articles

- [Butterick's Practical Typography](https://practicaltypography.com/)
- [Inclusive Design Principles](https://inclusivedesignprinciples.org/)
- [Material Design Guidelines](https://material.io/design)

### Tools Used

- [Coolors](https://coolors.co/) - Color palette generation
- [Type Scale](https://type-scale.com/) - Typography scale calculation
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)

---

**Document Owner**: Itzik Ben-Shabat  
**Last Updated**: 2025-11-17  
**Status**: Active
