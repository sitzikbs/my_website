# Publications Inventory

**Document Purpose**: Detailed catalog of all research publications from WordPress site  
**Date**: 2025-11-17  
**Status**: 📝 Ready for Data Collection

---

## Instructions

This document should catalog every publication listed on the WordPress site. For each publication, document all available information including metadata, links, and media assets.

---

## Publication Template

Use this template for each publication:

```markdown
### Publication [#]

**ID**: [unique-identifier-slug]  
**Title**: [Full Publication Title]  
**Status**: Published / In Press / Preprint

#### Authors
1. [Author 1 Name] (Institution, role/position)
2. [Author 2 Name] (Institution, role/position)
3. [etc.]

#### Publication Details
- **Venue**: [Conference or Journal Name]
- **Venue Type**: Conference / Journal / Workshop / Preprint
- **Year**: [Publication Year]
- **Month**: [Publication Month]
- **Pages**: [Page numbers, if applicable]
- **Volume/Issue**: [Volume/Issue numbers, if applicable]

#### Abstract
```
[Full abstract text here]
```

#### Keywords/Tags
- [keyword1]
- [keyword2]
- [keyword3]

#### Media Assets
- **Thumbnail Image**:
  - Filename: [filename]
  - Current URL: [URL on WordPress]
  - Dimensions: [width x height]
  - Format: [JPG/PNG/etc.]
  - Alt text: [description]

- **Teaser/Figure Images**:
  - Image 1: [details]
  - Image 2: [details]

#### Links
- **Paper PDF**: [URL]
  - File size: [size]
  - Hosted: [Where - local/external]
  
- **Project Page**: [URL]
  - Type: [Local page / External site]
  
- **Code Repository**: [URL]
  - Platform: [GitHub/GitLab/etc.]
  
- **Video/Demo**: [URL]
  - Platform: [YouTube/Vimeo/Local]
  - Duration: [duration]
  
- **Supplementary Materials**: [URL]
  - Type: [Description]
  
- **DOI**: [DOI link]
- **arXiv**: [arXiv link]
- **Other Links**: [Any other relevant links]

#### BibTeX
```bibtex
@inproceedings{citationkey2024,
  title={Publication Title},
  author={Author1, First and Author2, First},
  booktitle={Conference/Journal Name},
  year={2024},
  pages={1--10}
}
```

#### Awards & Recognition
- [Award/Recognition 1]
- [Award/Recognition 2]

#### Additional Notes
- Featured publication: Yes / No
- Display priority: [Number - for ordering]
- Special formatting: [Any special display requirements]
- Related publications: [Links to related works]

---
```

## Publications List

### Publication 1

**ID**: [unique-identifier]  
**Title**: [Title]  
**Status**: [Status]

[Complete details using template above]

---

### Publication 2

**ID**: [unique-identifier]  
**Title**: [Title]  
**Status**: [Status]

[Complete details using template above]

---

### Publication 3

[Continue for all publications...]

---

## Publications by Year

### 2024
- [ ] Publication: [Title]
- [ ] Publication: [Title]

### 2023
- [ ] Publication: [Title]
- [ ] Publication: [Title]

### 2022
- [ ] Publication: [Title]

[Continue for all years...]

---

## Publications by Type

### Journal Articles
- [ ] [Publication Title] - [Journal] - [Year]
- [ ] [Publication Title] - [Journal] - [Year]

### Conference Papers
- [ ] [Publication Title] - [Conference] - [Year]
- [ ] [Publication Title] - [Conference] - [Year]

### Workshop Papers
- [ ] [Publication Title] - [Workshop] - [Year]

### Preprints
- [ ] [Publication Title] - [Platform] - [Year]

### Theses
- [ ] [Thesis Title] - [Degree] - [Year]

---

## Featured/Highlighted Publications

List any publications marked as "featured" or given special prominence:

1. [ ] [Publication Title] - [Year] - [Reason for featuring]
2. [ ] [Publication Title] - [Year] - [Reason for featuring]

---

## Publication Statistics

- **Total Publications**: [#]
- **Journal Articles**: [#]
- **Conference Papers**: [#]
- **Workshop Papers**: [#]
- **Preprints**: [#]
- **Years Span**: [First Year] - [Latest Year]
- **Total Authors Involved**: [#] (unique co-authors)
- **Publications with Code**: [#]
- **Publications with Video**: [#]
- **Publications with Project Pages**: [#]

---

## Media Assets Summary

### Images Required
| Publication | Thumbnail | Additional Images | Total Files |
|-------------|-----------|-------------------|-------------|
| [Pub 1] | ✓ | 2 | 3 |
| [Pub 2] | ✓ | 0 | 1 |
| [Total] | [#] | [#] | [#] |

### PDFs Required
| Publication | Main Paper | Supplementary | Total Size |
|-------------|------------|---------------|------------|
| [Pub 1] | 5MB | 2MB | 7MB |
| [Pub 2] | 3MB | - | 3MB |
| [Total] | [size] | [size] | [total] |

---

## Migration Checklist per Publication

For each publication, ensure:
- [ ] All metadata extracted
- [ ] BibTeX citation available
- [ ] All links documented and validated
- [ ] Images downloaded and organized
- [ ] PDF papers downloaded (if hosted locally)
- [ ] Video links verified
- [ ] Code repository links verified
- [ ] Abstract formatted properly
- [ ] Author names and affiliations recorded
- [ ] Publication year and venue confirmed

---

## Special Considerations

### Collaborative Publications
List any publications requiring special attribution or permission:
- [Publication]: [Notes about permissions/attribution]

### External Hosting
List publications with assets hosted externally:
- [Publication]: PDFs on [external site]
- [Publication]: Videos on [YouTube/Vimeo]

### Copyright Considerations
Note any copyright or licensing issues:
- [Publication]: [Copyright status]

---

## Conversion to JSON Format

Once all publications are documented, they should be converted to JSON format for `data/publications.json`. Example structure:

```json
{
  "publications": [
    {
      "id": "unique-id-2024",
      "title": "Example Publication Title",
      "authors": [
        "First Author",
        "Second Author"
      ],
      "venue": "Conference/Journal Name",
      "venueType": "conference",
      "year": 2024,
      "month": "June",
      "abstract": "Full abstract text here...",
      "links": {
        "paper": "/assets/documents/papers/paper-2024.pdf",
        "project": "https://project-page.com",
        "code": "https://github.com/user/repo",
        "video": "https://youtube.com/watch?v=xxxxx",
        "doi": "https://doi.org/xx.xxxx/xxxxx"
      },
      "image": "/assets/images/publications/pub-2024-thumbnail.jpg",
      "bibtex": "@inproceedings{...\n}",
      "featured": true,
      "awards": ["Best Paper Award"],
      "tags": ["computer vision", "3D reconstruction"]
    }
  ]
}
```

---

**Status**: 📝 Template Ready - Awaiting Data Entry  
**Next Step**: Visit WordPress site and begin cataloging each publication
