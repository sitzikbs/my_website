#!/usr/bin/env python3
"""
Update HTML files to use:
1. Minified CSS and JS assets
2. Local WebP images with <picture> elements and lazy loading
3. Proper width/height attributes to prevent CLS
"""

import json
import os
import re
from pathlib import Path
from typing import Dict, Set
from urllib.parse import urlparse
from PIL import Image


def load_image_mapping() -> Dict[str, str]:
    """Load the WordPress CDN URL to local path mapping."""
    mapping_file = Path("data/image-mapping.json")
    if not mapping_file.exists():
        return {}
    
    with open(mapping_file) as f:
        return json.load(f)


def get_image_dimensions(image_path: str) -> tuple:
    """Get width and height of an image."""
    try:
        with Image.open(image_path) as img:
            return img.size
    except Exception as e:
        print(f"Warning: Could not get dimensions for {image_path}: {e}")
        return None, None


def update_css_js_references(content: str) -> str:
    """Update CSS and JS references to use minified versions."""
    # Update CSS references (handle various path patterns and query strings)
    # Matches: href="css/style.css", href="../../css/style.css", href="css/style.css?v=5", etc.
    content = re.sub(
        r'href="([\.\/]*css/style)\.css(\?[^"]*)?(")',
        r'href="\1.min.css\2\3',
        content
    )
    
    # Update JS references (handle various path patterns)
    js_files = [
        'main.js',
        'navigation.js',
        'data-loader.js',
        'publications-loader.js',
        'blog-loader.js',
        'podcast-loader.js'
    ]
    
    for js_file in js_files:
        min_file = js_file.replace('.js', '.min.js')
        # Match with relative paths: src="js/main.js", src="../../js/main.js", etc.
        content = re.sub(
            f'src="([\.\/]*js/{re.escape(js_file)})"',
            f'src="\\1".replace(".js", ".min.js")',
            content
        )
        # Simpler version that actually works
        content = content.replace(f'js/{js_file}"', f'js/{min_file}"')
    
    return content


def create_picture_element(wordpress_url: str, local_path: str, alt_text: str = "", 
                           class_attr: str = "", style_attr: str = "") -> str:
    """
    Create a <picture> element with WebP sources and fallback.
    
    Args:
        wordpress_url: Original WordPress CDN URL
        local_path: Path to local image file
        alt_text: Alt text for the image
        class_attr: CSS class attribute
        style_attr: Inline style attribute
    
    Returns:
        HTML <picture> element string
    """
    # Get base filename without extension
    path_obj = Path(local_path)
    base_name = path_obj.stem
    directory = path_obj.parent
    
    # Get image dimensions from original
    width, height = get_image_dimensions(local_path)
    dimension_attrs = ""
    if width and height:
        dimension_attrs = f' width="{width}" height="{height}"'
    
    # Check which WebP sizes exist
    webp_sizes = []
    for size in [1200, 800, 400, 200]:
        webp_path = directory / f"{base_name}-{size}.webp"
        if webp_path.exists():
            webp_sizes.append((size, str(webp_path)))
    
    # If no WebP files found, just return regular img tag
    if not webp_sizes:
        attrs = f' class="{class_attr}"' if class_attr else ''
        attrs += f' style="{style_attr}"' if style_attr else ''
        attrs += dimension_attrs
        return f'<img src="{local_path}" alt="{alt_text}"{attrs} loading="lazy">'
    
    # Build <picture> element
    picture_html = '<picture>\n'
    
    # Add WebP sources in descending order (largest first)
    webp_sizes.sort(reverse=True)
    for size, webp_path in webp_sizes:
        picture_html += f'  <source srcset="{webp_path}" type="image/webp" media="(min-width: {size}px)">\n'
    
    # Add fallback img tag
    attrs = f' class="{class_attr}"' if class_attr else ''
    attrs += f' style="{style_attr}"' if style_attr else ''
    attrs += dimension_attrs
    picture_html += f'  <img src="{local_path}" alt="{alt_text}"{attrs} loading="lazy">\n'
    picture_html += '</picture>'
    
    return picture_html


def normalize_wp_cdn_url(url: str) -> str:
    """
    Normalize WordPress CDN URLs by converting i1, i2, i3.wp.com to i0.wp.com
    and removing query parameters for matching purposes.
    """
    # Replace i1.wp.com, i2.wp.com, etc. with i0.wp.com
    normalized = re.sub(r'i[0-9]\.wp\.com', 'i0.wp.com', url)
    # Remove query parameters for matching (keep the base URL)
    normalized = normalized.split('?')[0]
    return normalized


def update_images_in_html(content: str, image_mapping: Dict[str, str]) -> tuple:
    """
    Replace WordPress CDN image URLs with local WebP <picture> elements.
    
    Returns:
        tuple: (updated_content, number_of_replacements)
    """
    replacements = 0
    
    # Create normalized mapping for faster lookup
    normalized_mapping = {}
    for key, value in image_mapping.items():
        normalized_key = normalize_wp_cdn_url(key)
        normalized_mapping[normalized_key] = value
    
    # Match <img> tags with WordPress CDN URLs
    # Pattern matches: <img [attributes] src="https://i[0-9].wp.com/..." [more attributes]>
    img_pattern = r'<img\s+([^>]*?)\s*src=["\']([^"\']+i[0-9]\.wp\.com[^"\']+)["\']([^>]*?)>'
    
    def replace_img(match):
        nonlocal replacements
        before_src = match.group(1)
        src_url = match.group(2)
        after_src = match.group(3)
        
        # Normalize the URL for lookup
        normalized_url = normalize_wp_cdn_url(src_url)
        
        # Check if this URL is in our normalized mapping
        if normalized_url in normalized_mapping:
            local_path = normalized_mapping[normalized_url]
            
            # Extract alt text
            alt_match = re.search(r'alt=["\']([^"\']*)["\']', before_src + after_src)
            alt_text = alt_match.group(1) if alt_match else ""
            
            # Extract class
            class_match = re.search(r'class=["\']([^"\']*)["\']', before_src + after_src)
            class_attr = class_match.group(1) if class_match else ""
            
            # Extract style
            style_match = re.search(r'style=["\']([^"\']*)["\']', before_src + after_src)
            style_attr = style_match.group(1) if style_match else ""
            
            # Create picture element
            picture_html = create_picture_element(
                src_url, local_path, alt_text, class_attr, style_attr
            )
            
            replacements += 1
            return picture_html
        
        # If not in mapping, return original
        return match.group(0)
    
    updated_content = re.sub(img_pattern, replace_img, content)
    return updated_content, replacements


def update_html_file(html_file: Path, image_mapping: Dict[str, str]) -> Dict:
    """
    Update a single HTML file with minified assets and WebP images.
    
    Returns:
        dict: Statistics about the updates
    """
    print(f"Processing {html_file}...")
    
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Update CSS/JS references
    content = update_css_js_references(content)
    
    # Update images
    content, img_replacements = update_images_in_html(content, image_mapping)
    
    # Only write if changes were made
    if content != original_content:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return {
            'file': str(html_file),
            'updated': True,
            'image_replacements': img_replacements
        }
    
    return {
        'file': str(html_file),
        'updated': False,
        'image_replacements': 0
    }


def main():
    """Main function to update all HTML files."""
    # Load image mapping
    print("Loading image mapping...")
    image_mapping = load_image_mapping()
    print(f"Loaded {len(image_mapping)} image mappings")
    
    # Find all HTML files (root and blog posts)
    html_files = []
    
    # Root HTML files
    for html_file in Path('.').glob('*.html'):
        html_files.append(html_file)
    
    # Blog post HTML files
    blog_dir = Path('blog/posts')
    if blog_dir.exists():
        html_files.extend(blog_dir.glob('*.html'))
    
    print(f"\nFound {len(html_files)} HTML files to process\n")
    
    # Update each file
    results = []
    for html_file in sorted(html_files):
        result = update_html_file(html_file, image_mapping)
        results.append(result)
    
    # Print summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    
    updated_count = sum(1 for r in results if r['updated'])
    total_img_replacements = sum(r['image_replacements'] for r in results)
    
    print(f"Total files processed: {len(results)}")
    print(f"Files updated: {updated_count}")
    print(f"Total image replacements: {total_img_replacements}")
    
    # Show files with most replacements
    print("\nFiles with most image replacements:")
    top_files = sorted(
        [r for r in results if r['image_replacements'] > 0],
        key=lambda x: x['image_replacements'],
        reverse=True
    )[:10]
    
    for r in top_files:
        print(f"  {r['file']}: {r['image_replacements']} images")
    
    # Save detailed report
    report_file = Path('data/html-update-report.json')
    with open(report_file, 'w') as f:
        json.dump({
            'summary': {
                'total_files': len(results),
                'files_updated': updated_count,
                'total_image_replacements': total_img_replacements
            },
            'details': results
        }, f, indent=2)
    
    print(f"\nDetailed report saved to: {report_file}")


if __name__ == '__main__':
    main()
