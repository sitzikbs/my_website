import requests
from bs4 import BeautifulSoup
import os

def scrape_page(url, output_filename, title):
    print(f"Fetching {url}...")
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch {url}: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract content
    # Usually in 'entry-content' or 'elementor-section-wrap'
    content_div = soup.find('div', class_='entry-content')
    if not content_div:
        content_div = soup.find('div', class_='elementor-section-wrap')
        
    if not content_div:
        # Try to find the main content area by looking for the header
        header = soup.find(lambda tag: tag.name in ['h1', 'h2'] and title in tag.text)
        if header:
            # If header is found, try to find the container that holds it and the content
            # Usually it's a section or column
            container = header.find_parent('section')
            if not container:
                container = header.find_parent(class_='elementor-section')
            
            if container:
                # Get all siblings of the header's section if the content is split across sections
                # Or just take the container content
                content_div = container.parent # Go up one level to capture multiple sections?
                
                # Better approach: Find the header, then iterate siblings until footer
                content_html = ""
                current = header.find_parent('section')
                if not current:
                     # Maybe the header is inside a widget inside a column inside a section
                     current = header.find_parent(class_='elementor-section')
                
                if current:
                    print(f"Found start section for {title}")
                    # Add this section and subsequent sections until footer
                    while current:
                        # print(f"Processing section: {current.get('class')}")
                        if "KEEP IN TOUCH" in current.get_text() or "Additional Links" in current.get_text():
                            print("Found footer, stopping.")
                            break
                        content_html += str(current)
                        current = current.find_next_sibling('section')
                    
                    # Create a dummy soup to hold the content
                    content_div = BeautifulSoup(content_html, 'html.parser')
                else:
                    print(f"Could not find parent section for header {title}")
            else:
                print(f"Could not find container for header {title}")
        else:
            print(f"Could not find header {title}")
            
    if not content_div:
        print(f"Could not extract content for {title}")
        return

    # Clean up
    for script in content_div(["script", "style"]):
        script.decompose()
        
    content_html = str(content_div)
    
    # Wrap in template
    template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Itzik Ben-Shabat</title>
    <link rel="stylesheet" href="css/style.css?v=4">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        .page-content {{ max-width: 800px; margin: 0 auto; padding: 2rem; }}
        .page-content img {{ max-width: 100%; height: auto; }}
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <div class="nav-brand">
                <a href="index.html">Home</a>
            </div>
            <button class="nav-toggle" aria-label="Toggle navigation">
                <span></span>
                <span></span>
                <span></span>
            </button>
            <ul class="nav-menu">
                <li><a href="index.html">About</a></li>
                <li><a href="publications.html">Publications</a></li>
                <li><a href="blog.html">Blog</a></li>
                <li><a href="contact.html">Contact</a></li>
            </ul>
        </div>
    </nav>

    <main>
        <section class="page-header">
            <div class="container">
                <h1>{title}</h1>
            </div>
        </section>

        <section class="page-content">
            <div class="container">
                {content}
            </div>
        </section>
    </main>
</body>
</html>"""

    full_html = template.format(title=title, content=content_html)
    
    with open(output_filename, 'w') as f:
        f.write(full_html)
    print(f"Saved {output_filename}")

def scrape_extras():
    scrape_page("https://www.itzikbs.com/awards", "awards.html", "Awards")
    scrape_page("https://www.itzikbs.com/code", "code.html", "Code")

if __name__ == "__main__":
    scrape_extras()
