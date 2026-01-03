#!/usr/bin/env python3
"""
Create placeholder images for missing IKEA images using IMG_8505-scaled.jpg
"""

import shutil
import os
from pathlib import Path

def main():
    base_dir = Path("/home/sitzikbs/dev/my_website")
    source_image = base_dir / "assets/images/blog/IMG_8505-scaled.jpg"
    
    # Missing IKEA images that need placeholders
    missing_images = [
        "IMG_8418-scaled.jpg",
        "IMG_8432-1-scaled.jpg",
        "IMG_8435-1-scaled.jpg",
        "IMG_8508-scaled.jpg",
    ]
    
    if not source_image.exists():
        print(f"❌ Source image not found: {source_image}")
        return
    
    print(f"Creating placeholders using {source_image.name}")
    print()
    
    for img_name in missing_images:
        dest_path = base_dir / "assets/images/blog" / img_name
        
        if dest_path.exists():
            print(f"⏭️  {img_name} already exists")
            continue
        
        try:
            shutil.copy2(source_image, dest_path)
            print(f"✅ Created {img_name}")
        except Exception as e:
            print(f"❌ Failed to create {img_name}: {e}")
    
    print()
    print("=" * 80)
    print("Placeholder creation complete")
    print("=" * 80)
    print()
    print("Note: These are placeholder images. The original IKEA images are no longer")
    print("available from the WordPress server. All 4 images now use IMG_8505-scaled.jpg")
    print("as a temporary substitute showing similar IKEA assembly content.")

if __name__ == "__main__":
    main()
