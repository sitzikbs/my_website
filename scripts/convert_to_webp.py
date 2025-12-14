#!/usr/bin/env python3
"""
Convert images to WebP format and generate responsive sizes.
Requires: pillow (PIL), pillow-avif-plugin (for AVIF support)
Install: uv pip install pillow pillow-avif-plugin
"""

import os
import json
from pathlib import Path
from PIL import Image
import concurrent.futures

# Configuration
INPUT_DIR = Path("assets/images")
WEBP_QUALITY = 85
SIZES = {
    "thumbnail": 200,
    "small": 400,
    "medium": 800,
    "large": 1200,
}

# Skip these extensions
SKIP_EXTENSIONS = {'.webp', '.svg', '.ico', '.gif'}

def convert_image_to_webp(image_path):
    """Convert a single image to WebP and generate responsive sizes"""
    try:
        # Skip if already WebP or unsupported format
        if image_path.suffix.lower() in SKIP_EXTENSIONS:
            return None
        
        # Skip if file doesn't exist
        if not image_path.exists():
            return None
        
        # Open image
        with Image.open(image_path) as img:
            # Convert RGBA to RGB if necessary
            if img.mode in ('RGBA', 'LA', 'P'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
                img = background
            elif img.mode not in ('RGB', 'L'):
                img = img.convert('RGB')
            
            # Get original dimensions
            orig_width, orig_height = img.size
            
            results = []
            
            # Generate responsive sizes
            for size_name, target_width in SIZES.items():
                # Skip if original is smaller than target
                if orig_width <= target_width and size_name != "thumbnail":
                    continue
                
                # Calculate new height maintaining aspect ratio
                aspect_ratio = orig_height / orig_width
                new_height = int(target_width * aspect_ratio)
                
                # Resize image
                resized = img.resize((target_width, new_height), Image.Resampling.LANCZOS)
                
                # Generate WebP filename
                webp_filename = f"{image_path.stem}-{target_width}.webp"
                webp_path = image_path.parent / webp_filename
                
                # Save as WebP
                resized.save(webp_path, 'WEBP', quality=WEBP_QUALITY, method=6)
                
                # Get file sizes
                original_size = image_path.stat().st_size if image_path.exists() else 0
                webp_size = webp_path.stat().st_size
                
                results.append({
                    'original': str(image_path),
                    'webp': str(webp_path),
                    'size': size_name,
                    'width': target_width,
                    'height': new_height,
                    'original_size': original_size,
                    'webp_size': webp_size,
                    'savings': original_size - webp_size if original_size > 0 else 0
                })
            
            return results
            
    except Exception as e:
        print(f"❌ Error converting {image_path}: {e}")
        return None

def get_all_images():
    """Get all image files from assets/images"""
    image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif'}
    images = []
    
    for ext in image_extensions:
        images.extend(INPUT_DIR.rglob(f"*{ext}"))
        images.extend(INPUT_DIR.rglob(f"*{ext.upper()}"))
    
    return images

def main():
    """Main execution"""
    print("🖼️  WebP Image Conversion Script")
    print("="*60)
    print(f"Quality: {WEBP_QUALITY}%")
    print(f"Sizes: {', '.join([f'{name}={width}px' for name, width in SIZES.items()])}")
    print("="*60)
    
    # Get all images
    images = get_all_images()
    print(f"\n📌 Found {len(images)} images to process\n")
    
    if not images:
        print("✅ No images to convert!")
        return
    
    # Process images in parallel
    all_results = []
    processed = 0
    skipped = 0
    errors = 0
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(convert_image_to_webp, img): img for img in images}
        
        for i, future in enumerate(concurrent.futures.as_completed(futures), 1):
            img_path = futures[future]
            print(f"[{i}/{len(images)}] Processing: {img_path.relative_to(INPUT_DIR)}")
            
            try:
                results = future.result()
                if results:
                    all_results.extend(results)
                    processed += 1
                    print(f"  ✅ Generated {len(results)} WebP versions")
                else:
                    skipped += 1
                    print(f"  ⏭️  Skipped")
            except Exception as e:
                errors += 1
                print(f"  ❌ Error: {e}")
    
    # Calculate statistics
    print("\n" + "="*60)
    print("📊 CONVERSION REPORT")
    print("="*60)
    
    if all_results:
        total_original_size = sum(r['original_size'] for r in all_results)
        total_webp_size = sum(r['webp_size'] for r in all_results)
        total_savings = total_original_size - total_webp_size
        savings_percent = (total_savings / total_original_size * 100) if total_original_size > 0 else 0
        
        print(f"Images processed:    {processed}")
        print(f"Images skipped:      {skipped}")
        print(f"Errors:              {errors}")
        print(f"WebP files created:  {len(all_results)}")
        print(f"\nOriginal size:       {total_original_size / (1024*1024):.2f} MB")
        print(f"WebP size:           {total_webp_size / (1024*1024):.2f} MB")
        print(f"Savings:             {total_savings / (1024*1024):.2f} MB ({savings_percent:.1f}%)")
        
        # Save conversion report
        report_file = Path("data/webp-conversion-report.json")
        report_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(report_file, 'w') as f:
            json.dump({
                'summary': {
                    'processed': processed,
                    'skipped': skipped,
                    'errors': errors,
                    'total_webp_files': len(all_results),
                    'total_original_size': total_original_size,
                    'total_webp_size': total_webp_size,
                    'total_savings': total_savings,
                    'savings_percent': savings_percent
                },
                'conversions': all_results
            }, f, indent=2)
        
        print(f"\n💾 Detailed report saved to: {report_file}")
    else:
        print("No images were converted.")
    
    print("="*60)
    print(f"\n✅ WebP conversion complete!")

if __name__ == "__main__":
    main()
