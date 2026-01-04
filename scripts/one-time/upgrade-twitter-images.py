#!/usr/bin/env python3
"""
Download full-resolution versions of Twitter/X images that are currently thumbnails.
"""

import os
import subprocess
from pathlib import Path
import time

BLOG_DIR = Path("assets/images/blog")

# Twitter image IDs from the CVPR 2024 post (and potentially others)
# Format: filename -> Twitter media ID
TWITTER_IMAGES = {
    "GQYJnJja8AAmF5L.jpg": "GQYJnJja8AAmF5L",
    "GQXi2XXbAAAMP5T.jpg": "GQXi2XXbAAAMP5T",
    "GQXhtIrbgAAgVrS.jpg": "GQXhtIrbgAAgVrS",
    "GQX_keoaIAIqBAP.jpg": "GQX_keoaIAIqBAP",
    "GQYNemQaIAUTC8O-1.jpg": "GQYNemQaIAUTC8O",
    "GQZk0VVbgAArrqk.jpg": "GQZk0VVbgAArrqk",
    "GQZgR7racAAKyB1.jpg": "GQZgR7racAAKyB1",
    "GQcn5ltaIAEMKDC.jpg": "GQcn5ltaIAEMKDC",
    "GQcn5lybQAAKmax.jpg": "GQcn5lybQAAKmax",
    "GQcn5oHa4AAfCqd.jpg": "GQcn5oHa4AAfCqd",
    "GQcn5oIagAEWvso.jpg": "GQcn5oIagAEWvso",
    "GQcoA93aIAUnCgY.jpg": "GQcoA93aIAUnCgY",
    "GQcoIf8bsAAx3Oc.jpg": "GQcoIf8bsAAx3Oc",
    "GQcoTDmaIAI6lUU.jpg": "GQcoTDmaIAI6lUU",
    "GQcpEheaAAAa9Kp.jpg": "GQcpEheaAAAa9Kp",
    "GQcpEheawAAwYMx.jpg": "GQcpEheawAAwYMx",
    "GQcpEi3aoAAy_AS.jpg": "GQcpEi3aoAAy_AS",
    "GQcpEjTaIAM99A0.jpg": "GQcpEjTaIAM99A0",
    "GQcpJ2-awAAP-cX.jpg": "GQcpJ2-awAAP-cX",
    "GQcpJ2HaIAMtqnl.jpg": "GQcpJ2HaIAMtqnl",
    "GQcpJ5LaIAAPkj6.jpg": "GQcpJ5LaIAAPkj6",
    "GQcpJ5faoAAfJSz.jpg": "GQcpJ5faoAAfJSz",
    "GQcpP3yaIAIVyCn.jpg": "GQcpP3yaIAIVyCn",
    "GQcpP4paIAIyI_E.jpg": "GQcpP4paIAIyI_E",
    "GQcpP5qaIAMtk8d.jpg": "GQcpP5qaIAMtk8d",
    "GQcpxl_bMAAmI31.jpg": "GQcpxl_bMAAmI31",
    "GQcpxmMawAAI8vu.jpg": "GQcpxmMawAAI8vu",
    "GQcpxn-aIAAJOYp.jpg": "GQcpxn-aIAAJOYp",
    "GQcpxqzaIAIMG5C.jpg": "GQcpxqzaIAIMG5C",
    "GQcpzXvaMAASvpT.jpg": "GQcpzXvaMAASvpT",
    "GQctM1kaIAEbKj5.jpg": "GQctM1kaIAEbKj5",
    "GQdsw4baIAQIeZq.jpg": "GQdsw4baIAQIeZq",
    "GQeMqrpaMAA96u_.jpeg": "GQeMqrpaMAA96u_",
    "GQh5m-la8AAEP_B-1.jpg": "GQh5m-la8AAEP_B",
    "GQi5gAyakAIEzDs.jpg": "GQi5gAyakAIEzDs",
    "GQiwOPuakAIBSN9.jpg": "GQiwOPuakAIBSN9",
    "GQiwOPybcAAcSnE.jpg": "GQiwOPybcAAcSnE",
    "GQnCrcMbwAAsM-M.jpeg": "GQnCrcMbwAAsM-M",
    "GQnMvmYakAIXR4M.jpeg": "GQnMvmYakAIXR4M",
    "GQnyld0akAUiigf.jpeg": "GQnyld0akAUiigf",
    "GQnyle6akAURUVw.jpeg": "GQnyle6akAURUVw",
    "GQnyle7akAMA5eT.jpeg": "GQnyle7akAMA5eT",
    "GQoOOGVakAUIBzi.jpeg": "GQoOOGVakAUIBzi",
}

def get_image_dimensions(image_path):
    """Get dimensions of an image file."""
    try:
        result = subprocess.run(
            ["identify", "-format", "%wx%h", str(image_path)],
            capture_output=True,
            text=True,
            check=True
        )
        width, height = map(int, result.stdout.strip().split('x'))
        return width, height
    except Exception:
        return None, None

def download_twitter_image(media_id, output_path):
    """Download a Twitter image in large format."""
    url = f"https://pbs.twimg.com/media/{media_id}?format=jpg&name=large"
    
    try:
        result = subprocess.run(
            ["curl", "-s", "-L", "-f", url, "-o", str(output_path)],
            capture_output=True,
            check=True
        )
        return True
    except subprocess.CalledProcessError:
        print(f"  ❌ Failed to download from Twitter")
        return False

def main():
    print("Upgrading Twitter/X images to full resolution...")
    print("=" * 80)
    
    upgraded = 0
    skipped = 0
    failed = 0
    
    for filename, media_id in TWITTER_IMAGES.items():
        image_path = BLOG_DIR / filename
        
        if not image_path.exists():
            print(f"⏭️  {filename}: File not found, skipping")
            skipped += 1
            continue
        
        # Check current dimensions
        width, height = get_image_dimensions(image_path)
        if not width:
            print(f"⚠️  {filename}: Cannot read dimensions, skipping")
            skipped += 1
            continue
        
        if width >= 1024:
            print(f"✓  {filename}: Already high-res ({width}x{height}), skipping")
            skipped += 1
            continue
        
        print(f"📥 {filename}: Upgrading from {width}x{height}...")
        
        # Download from Twitter
        temp_path = image_path.with_suffix('.tmp' + image_path.suffix)
        if download_twitter_image(media_id, temp_path):
            new_width, new_height = get_image_dimensions(temp_path)
            if new_width and new_width > width:
                # Replace the old file
                temp_path.replace(image_path)
                print(f"  ✅ Upgraded to {new_width}x{new_height}")
                upgraded += 1
            else:
                temp_path.unlink()
                print(f"  ⚠️  Downloaded image not better quality")
                failed += 1
        else:
            failed += 1
        
        # Be nice to Twitter's servers
        time.sleep(0.5)
    
    print("\n" + "=" * 80)
    print(f"Summary: {upgraded} upgraded, {skipped} skipped, {failed} failed")

if __name__ == "__main__":
    main()
