#!/usr/bin/env python3
"""Script to add highlighted field to publications and add missing DiGS publication"""

import json

# Titles of publications to highlight
HIGHLIGHTED_TITLES = {
    "VI3NR: Variance Informed Initialization for Implicit Neural Representations",
    "Neural Experts: Mixture of Experts for Implicit Neural Representations",
    "3DInAction: Understanding Human Actions in 3D Point Clouds",
    "IKEA Ego 3D Dataset: Understanding furniture assembly actions from ego-view 3D Point Clouds",
    "DiGS: Divergence Guided Shape Implicit Neural Representation for Unoriented Point Clouds",
    "The IKEA ASM Dataset: Understanding People Assembling Furniture through Actions, Objects and Pose",
    "DeepFit: 3D Surface Fitting via Neural Network Weighted Least Squares",
    "Nesti-Net: Normal Estimation for Unstructured 3D Point Clouds using Convolutional Neural Networks",
    "3DmFV: 3D Point Cloud Classification in Real-Time using Convolutional Neural Networks"
}

# DiGS publication to add (insert after CloudWalker in 2022)
DIGS_PUBLICATION = {
    "title": "DiGS: Divergence Guided Shape Implicit Neural Representation for Unoriented Point Clouds",
    "authors": "Yizhak Ben-Shabat*, Chamin Hewa Koneputugodage*, Stephen Gould",
    "venue": "CVPR",
    "year": "2022",
    "links": [
        {
            "name": "paper",
            "url": "https://openaccess.thecvf.com/content/CVPR2022/html/Ben-Shabat_DiGS_Divergence_Guided_Shape_Implicit_Neural_Representation_for_Unoriented_Point_CVPR_2022_paper.html"
        },
        {
            "name": "preprint",
            "url": "https://arxiv.org/abs/2106.10811"
        },
        {
            "name": "project website",
            "url": "https://chumbyte.github.io/DiGS-Site/"
        },
        {
            "name": "full video",
            "url": "https://www.youtube.com/watch?v=bQWpRyM9wYM&list=PLD-7XrNHCcFLDQ6KH7w2xFLe0JWvalYfr&index=4&ab_channel=anucvml"
        },
        {
            "name": "code",
            "url": "https://github.com/Chumbyte/DiGS"
        },
        {
            "name": "podcast",
            "url": "https://www.itzikbs.com/digs"
        }
    ],
    "image": "",
    "highlighted": True
}

def main():
    # Read the publications file
    with open('/home/sitzikbs/dev/my_website/data/publications.json', 'r') as f:
        publications = json.load(f)
    
    # Filter out the invalid "If you found this interesting" entry
    publications = [p for p in publications if p.get('title') and p['title'].startswith("If you found") == False]
    
    # Add highlighted field to all publications
    updated_pubs = []
    digs_inserted = False
    
    for pub in publications:
        # Add highlighted field
        pub['highlighted'] = pub['title'] in HIGHLIGHTED_TITLES
        updated_pubs.append(pub)
        
        # Insert DiGS after CloudWalker (both from 2022)
        if not digs_inserted and pub['title'] == "CloudWalker: Random walks for 3D point cloud shape analysis":
            updated_pubs.append(DIGS_PUBLICATION)
            digs_inserted = True
    
    # Write back to file with nice formatting
    with open('/home/sitzikbs/dev/my_website/data/publications.json', 'w') as f:
        json.dump(updated_pubs, f, indent=4, ensure_ascii=False)
    
    # Print summary
    highlighted_count = sum(1 for p in updated_pubs if p.get('highlighted'))
    print(f"✓ Updated {len(updated_pubs)} publications")
    print(f"✓ {highlighted_count} publications marked as highlighted")
    print(f"✓ DiGS publication {'added' if digs_inserted else 'already exists'}")
    print("\nHighlighted publications:")
    for pub in updated_pubs:
        if pub.get('highlighted'):
            print(f"  - {pub['title']} ({pub['year']})")

if __name__ == "__main__":
    main()
