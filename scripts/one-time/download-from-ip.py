#!/usr/bin/env python3
"""
Download missing images directly from IP address 185.56.72.227
Focuses on critical IKEA images and other missing files.
"""

import json
import urllib.request
import urllib.error
import ssl
import os
from pathlib import Path

# Create SSL context that doesn't verify certificates
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

def is_valid_file(file_path, expected_type='image'):
    """Check if file is valid by reading its signature."""
    if not os.path.exists(file_path):
        return False
    
    try:
        with open(file_path, 'rb') as f:
            header = f.read(16)
            if len(header) < 4:
                return False
            
            # Check for HTML (common for 404 pages)
            if header.startswith(b'<!DO') or header.startswith(b'<htm') or header.startswith(b'<HTM'):
                return False
            
            if expected_type == 'image':
                # JPEG
                if header[:2] == b'\xff\xd8':
                    return True
                # PNG
                if header[:8] == b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a':
                    return True
                # GIF
                if header[:3] == b'GIF':
                    return True
                # WebP
                if header[:4] == b'RIFF' and header[8:12] == b'WEBP':
                    return True
                return False
            elif expected_type == 'pdf':
                return header[:4] == b'%PDF'
            elif expected_type == 'zip':
                return header[:2] == b'PK'
            
    except Exception as e:
        print(f"Error checking file {file_path}: {e}")
        return False
    
    return False

def download_file(url, local_path, expected_type='image'):
    """Download a file from URL to local path."""
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        
        # Try to download
        request = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
        with urllib.request.urlopen(request, context=ssl_context, timeout=30) as response:
            content = response.read()
            
            # Save to temp file first
            temp_path = local_path + '.tmp'
            with open(temp_path, 'wb') as f:
                f.write(content)
            
            # Verify it's valid
            if is_valid_file(temp_path, expected_type):
                os.rename(temp_path, local_path)
                return True, len(content)
            else:
                os.remove(temp_path)
                return False, 0
                
    except Exception as e:
        return False, str(e)

def main():
    """Download critical missing files."""
    
    # Critical files to download with IP-based URLs
    files_to_download = [
        # IKEA images - try non-scaled versions first
        {
            'urls': [
                'http://185.56.72.227/wp-content/uploads/2020/08/IMG_8418.jpg',
                'http://185.56.72.227/wp-content/uploads/2020/08/IMG_8418-scaled.jpg',
            ],
            'local': 'assets/images/blog/IMG_8418-scaled.jpg',
            'type': 'image'
        },
        {
            'urls': [
                'http://185.56.72.227/wp-content/uploads/2020/08/IMG_8432-1.jpg',
                'http://185.56.72.227/wp-content/uploads/2020/08/IMG_8432-1-scaled.jpg',
            ],
            'local': 'assets/images/blog/IMG_8432-1-scaled.jpg',
            'type': 'image'
        },
        {
            'urls': [
                'http://185.56.72.227/wp-content/uploads/2020/08/IMG_8435-1.jpg',
                'http://185.56.72.227/wp-content/uploads/2020/08/IMG_8435-1-scaled.jpg',
            ],
            'local': 'assets/images/blog/IMG_8435-1-scaled.jpg',
            'type': 'image'
        },
        {
            'urls': [
                'http://185.56.72.227/wp-content/uploads/2020/08/IMG_8508.jpg',
                'http://185.56.72.227/wp-content/uploads/2020/08/IMG_8508-scaled.jpg',
            ],
            'local': 'assets/images/blog/IMG_8508-scaled.jpg',
            'type': 'image'
        },
        # Dataset examples
        {
            'urls': [
                'http://185.56.72.227/wp-content/uploads/2020/08/pose_example.jpg',
            ],
            'local': 'assets/images/blog/pose_example.jpg',
            'type': 'image'
        },
        {
            'urls': [
                'http://185.56.72.227/wp-content/uploads/2020/08/segmentation_example.jpg',
            ],
            'local': 'assets/images/blog/segmentation_example.jpg',
            'type': 'image'
        },
        # Other missing files
        {
            'urls': [
                'http://185.56.72.227/wp-content/uploads/2020/07/AI_teaser.jpg',
            ],
            'local': 'assets/images/blog/AI_teaser.jpg',
            'type': 'image'
        },
        {
            'urls': [
                'http://185.56.72.227/wp-content/uploads/2021/03/Itzik-Ben-Shabat.gif',
            ],
            'local': 'assets/images/blog/Itzik-Ben-Shabat.gif',
            'type': 'image'
        },
        # Corrupted PDFs/ZIPs
        {
            'urls': [
                'http://185.56.72.227/wp-content/uploads/2017/11/LaTeX-General-Template.zip',
            ],
            'local': 'assets/images/blog/LaTeX-General-Template.zip',
            'type': 'zip'
        },
        {
            'urls': [
                'http://185.56.72.227/wp-content/uploads/2017/08/Part-Validation-Dan-and-Raz.pdf',
            ],
            'local': 'assets/images/blog/Part-Validation-Dan-and-Raz.pdf',
            'type': 'pdf'
        },
        {
            'urls': [
                'http://185.56.72.227/wp-content/uploads/2017/08/Poster-raz-and-dan.pdf',
            ],
            'local': 'assets/images/blog/Poster-raz-and-dan.pdf',
            'type': 'pdf'
        },
        {
            'urls': [
                'http://185.56.72.227/wp-content/uploads/2019/06/Nesti-Net_poster.pdf',
            ],
            'local': 'assets/images/blog/Nesti-Net_poster.pdf',
            'type': 'pdf'
        },
        {
            'urls': [
                'http://185.56.72.227/wp-content/uploads/2017/08/PartsValidator.zip',
            ],
            'local': 'assets/images/blog/PartsValidator.zip',
            'type': 'zip'
        },
        {
            'urls': [
                'http://185.56.72.227/wp-content/uploads/2017/01/ItzikAfro.jpg',
            ],
            'local': 'assets/images/blog/ItzikAfro.jpg',
            'type': 'image'
        },
    ]
    
    print(f"Attempting to download {len(files_to_download)} files from IP 185.56.72.227...")
    print()
    
    successful = 0
    failed = 0
    
    for i, file_info in enumerate(files_to_download, 1):
        local_path = file_info['local']
        file_type = file_info['type']
        filename = os.path.basename(local_path)
        
        print(f"[{i}/{len(files_to_download)}] {filename}...", end=' ')
        
        # Skip if already exists and valid
        if is_valid_file(local_path, file_type):
            print(f"✓ Already exists")
            successful += 1
            continue
        
        # Try each URL
        downloaded = False
        for url in file_info['urls']:
            result, size = download_file(url, local_path, file_type)
            if result:
                print(f"✅ Downloaded ({size:,} bytes) from {url}")
                downloaded = True
                successful += 1
                break
        
        if not downloaded:
            print(f"❌ Failed all URLs")
            failed += 1
    
    print()
    print("="*80)
    print(f"Download complete: {successful} successful, {failed} failed")
    print("="*80)

if __name__ == "__main__":
    main()
