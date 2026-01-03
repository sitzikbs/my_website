#!/usr/bin/env python3
"""
Check color contrast ratios for WCAG 2.1 AA compliance.
AA requires 4.5:1 for normal text and 3:1 for large text (18pt+ or 14pt+ bold).
"""

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def relative_luminance(rgb):
    """Calculate relative luminance according to WCAG formula."""
    r, g, b = [x / 255.0 for x in rgb]
    
    # Apply gamma correction
    def adjust(channel):
        if channel <= 0.03928:
            return channel / 12.92
        else:
            return ((channel + 0.055) / 1.055) ** 2.4
    
    r, g, b = adjust(r), adjust(g), adjust(b)
    
    # Calculate luminance
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(color1, color2):
    """Calculate contrast ratio between two colors."""
    lum1 = relative_luminance(hex_to_rgb(color1))
    lum2 = relative_luminance(hex_to_rgb(color2))
    
    # Ensure lum1 is lighter
    if lum1 < lum2:
        lum1, lum2 = lum2, lum1
    
    return (lum1 + 0.05) / (lum2 + 0.05)


def main():
    """Check common color combinations used in the site."""
    print("=" * 80)
    print("COLOR CONTRAST AUDIT - WCAG 2.1 AA")
    print("=" * 80)
    print("\nRequirements:")
    print("  • Normal text (under 18pt): 4.5:1 minimum")
    print("  • Large text (18pt+ or 14pt+ bold): 3:1 minimum")
    print("  • UI components and graphics: 3:1 minimum")
    print("\n" + "=" * 80)
    
    # Define color combinations actually used in the site
    # Note: Only testing colors that are actually used for text/UI elements
    color_tests = [
        # Text colors (actual usage in CSS)
        ("Text on white", "#1a1a1a", "#ffffff", "normal"),  # gray-900 on white (body text)
        ("Primary links on white", "#2563eb", "#ffffff", "normal"),  # primary on white (links)
        ("Gray text on white", "#666666", "#ffffff", "normal"),  # gray-600 on white (secondary text)
        ("Dark gray on white", "#404040", "#ffffff", "normal"),  # gray-700 on white (nav links)
        
        # Button colors
        ("White on primary", "#ffffff", "#2563eb", "normal"),  # button text
        ("White on primary-dark", "#ffffff", "#1e40af", "normal"),  # hover button
        
        # Background colors
        ("Gray-900 on gray-50", "#1a1a1a", "#fafafa", "normal"),  # text on light bg
        ("Gray-800 on gray-100", "#2d2d2d", "#f5f5f5", "normal"),  # text on alt bg
    ]
    
    issues = []
    passes = []
    
    for name, fg, bg, text_type in color_tests:
        ratio = contrast_ratio(fg, bg)
        
        # Determine pass/fail based on text type
        if text_type == "large":
            threshold = 3.0
        else:
            threshold = 4.5
        
        status = "✅ PASS" if ratio >= threshold else "❌ FAIL"
        
        result = {
            'name': name,
            'fg': fg,
            'bg': bg,
            'ratio': ratio,
            'threshold': threshold,
            'status': status
        }
        
        if ratio >= threshold:
            passes.append(result)
        else:
            issues.append(result)
        
        print(f"\n{status} {name}")
        print(f"   Foreground: {fg}")
        print(f"   Background: {bg}")
        print(f"   Ratio: {ratio:.2f}:1 (minimum: {threshold}:1)")
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total tests: {len(color_tests)}")
    print(f"Passed: {len(passes)}")
    print(f"Failed: {len(issues)}")
    
    if issues:
        print("\n⚠️  CONTRAST ISSUES FOUND:")
        for issue in issues:
            print(f"   • {issue['name']}: {issue['ratio']:.2f}:1 (needs {issue['threshold']}:1)")
        print("\n💡 Recommendations:")
        print("   - Darken foreground colors or lighten backgrounds")
        print("   - Test with browser dev tools for precise values")
        print("   - Consider using darker grays for body text")
    else:
        print("\n✅ All color combinations meet WCAG 2.1 AA standards!")
    
    print("=" * 80)


if __name__ == "__main__":
    main()
