#!/usr/bin/env python3
"""
Download remaining IKEA images from markdown file URLs (with query parameters).
"""

import urllib.request
import ssl
import os

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

def is_valid_image(file_path):
    """Check if file is a valid image."""
    if not os.path.exists(file_path):
        return False
    try:
        with open(file_path, 'rb') as f:
            header = f.read(16)
            if len(header) < 2:
                return False
            if header.startswith(b'<!DO') or header.startswith(b'<htm'):
                return False
            return header[:2] == b'\xff\xd8' or header[:8] == b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'
    except:
        return False

def download(url, path):
    """Download file from URL."""
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        request = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0'
        })
        with urllib.request.urlopen(request, context=ssl_context, timeout=30) as response:
            content = response.read()
        temp = path + '.tmp'
        with open(temp, 'wb') as f:
            f.write(content)
        if is_valid_image(temp):
            os.rename(temp, path)
            return True, len(content)
        os.remove(temp)
        return False, "Invalid"
    except Exception as e:
        return False, str(e)

# IKEA images from markdown file - use high-res CDN URLs
images = [
    ("https://i2.wp.com/www.itzikbs.com/wp-content/uploads/2020/08/IMG_8418-scaled.jpg?fit=2560%2C1707&ssl=1", "assets/images/blog/IMG_8418-scaled.jpg"),
    ("https://i2.wp.com/www.itzikbs.com/wp-content/uploads/2020/08/IMG_8432-1-scaled.jpg?fit=2560%2C1707&ssl=1", "assets/images/blog/IMG_8432-1-scaled.jpg"),
    ("https://i2.wp.com/www.itzikbs.com/wp-content/uploads/2020/08/IMG_8508-scaled.jpg?fit=2560%2C1707&ssl=1", "assets/images/blog/IMG_8508-scaled.jpg"),
    ("https://i0.wp.com/www.itzikbs.com/wp-content/uploads/2020/08/pose_example.jpg?fit=1920%2C1080&ssl=1", "assets/images/blog/pose_example.jpg"),
    ("https://i0.wp.com/www.itzikbs.com/wp-content/uploads/2020/08/segmentation_example.jpg?fit=1920%2C1080&ssl=1", "assets/images/blog/segmentation_example.jpg"),
]

print(f"Downloading {len(images)} IKEA dataset images...\n")

for i, (url, path) in enumerate(images, 1):
    filename = os.path.basename(path)
    print(f"[{i}/{len(images)}] {filename}...", end=' ')
    
    if is_valid_image(path):
        print("✓ Already exists")
        continue
    
    result, info = download(url, path)
    if result:
        print(f"✅ {info:,} bytes")
    else:
        print(f"❌ {info}")

print("\nDone!")
