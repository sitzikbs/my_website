# Data Directory

This directory contains structured data for the static website in JSON format.

## Files

### publications.json

Contains all publication data including papers, conference presentations, and journal articles.

**Schema:**
```json
{
  "publications": [
    {
      "id": "unique-identifier",
      "title": "Publication Title",
      "authors": ["Author 1", "Author 2"],
      "venue": "Conference/Journal Name",
      "venueType": "conference|journal|workshop|preprint",
      "year": 2024,
      "month": "Month name",
      "volume": "Volume number (for journals)",
      "issue": "Issue number (for journals)",
      "pages": "Page range",
      "abstract": "Full abstract text",
      "keywords": ["keyword1", "keyword2"],
      "links": {
        "paper": "/path/to/pdf",
        "project": "https://project-url",
        "code": "https://github.com/repo",
        "video": "https://youtube.com/...",
        "doi": "https://doi.org/...",
        "arxiv": "https://arxiv.org/abs/..."
      },
      "image": "/path/to/thumbnail",
      "bibtex": "BibTeX citation string",
      "featured": true|false,
      "awards": ["Award 1", "Award 2"],
      "tags": ["tag1", "tag2"]
    }
  ]
}
```

**Required fields:** id, title, authors, venue, year

### blog-index.json

Contains metadata for all blog posts, including categories and tags.

**Schema:**
```json
{
  "posts": [
    {
      "id": "YYYY-MM-DD-post-slug",
      "title": "Post Title",
      "date": "YYYY-MM-DD",
      "updated": "YYYY-MM-DD",
      "author": "Author Name",
      "excerpt": "Brief summary (2-3 sentences)",
      "content": "/blog/posts/YYYY-MM-DD-post-slug.html",
      "categories": ["Category1", "Category2"],
      "tags": ["tag1", "tag2"],
      "image": "/path/to/featured-image",
      "readingTime": 5,
      "featured": true|false,
      "status": "published|draft"
    }
  ],
  "categories": [
    {
      "name": "Category Name",
      "slug": "category-slug",
      "description": "Category description"
    }
  ],
  "tags": ["tag1", "tag2", "tag3"]
}
```

**Required fields:** id, title, date, author, excerpt, content

## Usage

These JSON files are loaded dynamically by JavaScript to populate the website content:

- `publications.js` loads `publications.json` to render the publications page
- `blog.js` loads `blog-index.json` to render the blog index page

## Validation

To validate the JSON files:

```bash
python3 scripts/validate-content.py
```

This will check:
- JSON syntax validity
- Required field presence
- Data type correctness
- Date format validity
- File path references

## Updating Content

### Adding a New Publication

1. Open `publications.json`
2. Add a new entry to the `publications` array following the schema
3. Ensure all required fields are present
4. Run validation: `python3 scripts/validate-content.py`
5. Add corresponding PDF and images to `assets/` directory

### Adding a New Blog Post

1. Create the blog post HTML file in `blog/posts/`
2. Open `blog-index.json`
3. Add a new entry to the `posts` array
4. Update `categories` and `tags` arrays if needed
5. Run validation: `python3 scripts/validate-content.py`
6. Add featured image to `assets/images/blog/`

## Migration from WordPress

See [MIGRATION_GUIDE.md](../MIGRATION_GUIDE.md) for detailed instructions on:
- Exporting WordPress content
- Converting posts to static format
- Populating these JSON files with real data
- Downloading and organizing media assets

## Current Status

- ✅ Directory structure created
- ✅ Schema defined with examples
- ✅ Validation script implemented
- ⏳ **Awaiting real WordPress data**

The example data in these files should be replaced with actual content from the WordPress site at https://itzikbs.com/
