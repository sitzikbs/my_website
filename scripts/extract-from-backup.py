#!/usr/bin/env python3
"""
Extract specific WordPress images from backup tar.gz archive.
This script extracts the original high-resolution images that were uploaded to WordPress.
"""

import tarfile
import os
from pathlib import Path

# Path to the backup archive (in Windows filesystem via WSL)
BACKUP_PATH = "/mnt/c/Users/sitzi/Downloads/download_havrakon_1767420934_64223.tar.gz"

# Images we want to extract (without any size suffixes - the originals)
TARGET_IMAGES = {
    "IMG_20190619_194012.jpg": "backup/homedir/sites/itzikbs.com/wp-content/uploads/2019/06/IMG_20190619_194012.jpg",
    "nyu_v2_1.png": "backup/homedir/sites/itzikbs.com/wp-content/uploads/2019/04/nyu_v2_1.png",
    "boya_by_m1_microphone.jpg": "backup/homedir/sites/itzikbs.com/wp-content/uploads/2020/11/boya_by_m1_microphone.jpg",
}

# Destination directory
DEST_DIR = Path("assets/images/blog")

def main():
    print(f"Opening archive: {BACKUP_PATH}")
    print(f"Destination: {DEST_DIR}")
    print()
    
    try:
        with tarfile.open(BACKUP_PATH, 'r:gz') as tar:
            for filename, archive_path in TARGET_IMAGES.items():
                dest_path = DEST_DIR / filename
                
                print(f"Extracting {filename}...")
                print(f"  From: {archive_path}")
                print(f"  To: {dest_path}")
                
                try:
                    # Extract the file
                    member = tar.getmember(archive_path)
                    
                    # Read the file content
                    file_obj = tar.extractfile(member)
                    if file_obj:
                        # Write to destination
                        with open(dest_path, 'wb') as f:
                            f.write(file_obj.read())
                        
                        # Get file size
                        size_kb = dest_path.stat().st_size / 1024
                        print(f"  ✓ Extracted successfully ({size_kb:.1f} KB)")
                        
                        # Check dimensions if it's an image
                        import subprocess
                        try:
                            result = subprocess.run(
                                ['identify', '-format', '%wx%h', str(dest_path)],
                                capture_output=True,
                                text=True,
                                check=True
                            )
                            dimensions = result.stdout.strip()
                            print(f"  Dimensions: {dimensions}")
                        except:
                            pass
                    else:
                        print(f"  ✗ Could not read file content")
                        
                except KeyError:
                    print(f"  ✗ File not found in archive")
                except Exception as e:
                    print(f"  ✗ Error: {e}")
                
                print()
                
    except FileNotFoundError:
        print(f"ERROR: Archive not found at {BACKUP_PATH}")
        return 1
    except Exception as e:
        print(f"ERROR: Failed to open archive: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
