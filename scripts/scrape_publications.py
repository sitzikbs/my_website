import requests
from bs4 import BeautifulSoup
import json
import re
import os

def scrape_publications():
    url = "https://www.itzikbs.com/publications"
    print(f"Fetching {url}...")
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch page: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    
    publications = []
    
    # The structure is a bit loose based on the text representation.
    # We need to find the container for the full publication list.
    # Based on the fetch_webpage output, there is a header "Full Publication List (chronological order)"
    # We can look for that header and then process the following elements.
    
    # Find the header
    full_list_header = soup.find(lambda tag: tag.name in ['h1', 'h2', 'h3'] and "Full Publication List" in tag.text)
    
    if not full_list_header:
        print("Could not find 'Full Publication List' header.")
        return

    # The publications are in sections following the header.
    # We need to find the section containing the header, and then iterate over subsequent sections.
    # The header is inside a widget -> column -> section.
    
    header_section = full_list_header.find_parent('section')
    if not header_section:
        # Fallback if structure is different
        header_section = full_list_header.find_parent(class_='elementor-section')
        
    if not header_section:
        print("Could not find the section containing the header.")
        return

    # Get all subsequent sibling sections
    sections = header_section.find_next_siblings('section')
    
    for section in sections:
        # Check if we reached the end (e.g. "Keep in Touch" or "Additional Links")
        if "KEEP IN TOUCH" in section.get_text() or "Additional Links" in section.get_text():
            break
            
        # Each publication section usually has two columns: Image (33%) and Text (66%)
        # But sometimes it might be different. Let's look for the text editor widget.
        
        text_widget = section.find('div', class_='elementor-widget-text-editor')
        if not text_widget:
            continue
            
        # Extract text content
        # We need to preserve some structure to separate links from citation
        # But for now let's get the full text and parse it.
        full_text = text_widget.get_text(" ", strip=True)
        
        # Skip empty sections
        if not full_text:
            continue

        # Extract Title
        # Debug: print full text
        # print(f"Processing: {full_text[:50]}...")
        
        # Heuristic: Title is usually the first part, in quotes, followed by a comma.
        # We split by quote-comma combination.
        # Possible closing quotes: ", ”, “,
        
        # First, try to find the end of the title
        # It usually ends with ", or ”, or “,
        # The site seems to use Left Double Quote (\u201c) for both start and end sometimes?
        
        title_end_match = re.search(r'["”“\u201c\u201d],', full_text)
        if title_end_match:
            end_idx = title_end_match.start()
            title_raw = full_text[:end_idx]
            rest_of_text = full_text[title_end_match.end():].strip()
            
            # Clean title (remove opening quote)
            title = title_raw.strip()
            # Remove common quote characters from start
            title = re.sub(r'^["”“\u201c\u201d]\s*', '', title)
        else:
            # Fallback: try to find just a closing quote if comma is missing
            # But be careful not to match the opening quote if it's the same char
            # Assume title is at least 10 chars
            # We look for a quote that is followed by space and NOT at the start
            
            # Skip the first char if it is a quote
            start_offset = 0
            if full_text and full_text[0] in ['"', '”', '“', '\u201c', '\u201d']:
                start_offset = 1
                
            title_match = re.search(r'["”“\u201c\u201d]', full_text[start_offset:])
            if title_match:
                end_idx = start_offset + title_match.start()
                title = full_text[start_offset:end_idx].strip()
                rest_of_text = full_text[end_idx+1:].strip()
            else:
                # Last resort: take everything up to the first "., " or just everything?
                # Maybe split by "Yizhak" or known author?
                # Let's just take the whole text as title and mark as failed parse
                title = full_text
                rest_of_text = ""

        # Extract Links
        links_data = []
        links = text_widget.find_all('a')
        for link in links:
            link_text = link.get_text(strip=True)
            link_url = link.get('href')
            if link_url:
                # Clean link name
                name = link_text.replace('[', '').replace(']', '')
                if not name:
                    # If text is empty, maybe it's an image link or just brackets?
                    pass
                
                # If name is still empty, use a default or try to infer
                if not name:
                    if "arxiv" in link_url: name = "preprint"
                    elif "github" in link_url: name = "code"
                    elif "youtube" in link_url: name = "video"
                    else: name = "link"
                    
                links_data.append({"name": name, "url": link_url})

        # Extract Authors, Venue, Year from rest_of_text
        if rest_of_text:
            # ... (rest of the logic)
            
            # Clean up leading comma/dot
            if rest_of_text.startswith(',') or rest_of_text.startswith('.'):
                rest_of_text = rest_of_text[1:].strip()
                
            # Extract Year (last 4 digits)
            # We need to be careful about links text which might contain numbers
            # But we are parsing rest_of_text which comes from full_text
            # full_text includes links text like "[paper]"
            
            # Let's try to remove the links text from rest_of_text first?
            # It's hard because we don't know exactly where they are in the string representation.
            
            # Instead, let's look for the year pattern before the first "["
            citation_part = rest_of_text.split('[')[0].strip()
            
            year_match = re.search(r'(\d{4})', citation_part)
            if year_match:
                # Find the last occurrence of a year in the citation part
                all_years = re.findall(r'(\d{4})', citation_part)
                year = all_years[-1]
            else:
                year = "Unknown"
                
            # Venue is usually before the year
            if year != "Unknown":
                parts = citation_part.rsplit(year, 1)
                authors_venue = parts[0].strip()
                # Remove trailing comma/dot
                if authors_venue.endswith(',') or authors_venue.endswith('.'):
                    authors_venue = authors_venue[:-1].strip()
            else:
                authors_venue = citation_part

            # Split authors and venue
            # Usually separated by a comma or dot before the venue
            # But sometimes venue is just "CVPR" without comma.
            # Let's try to split by the last comma.
            if ',' in authors_venue:
                parts = authors_venue.rsplit(',', 1)
                venue = parts[1].strip()
                authors = parts[0].strip()
            elif '.' in authors_venue:
                 parts = authors_venue.rsplit('.', 1)
                 venue = parts[1].strip()
                 authors = parts[0].strip()
            else:
                authors = authors_venue
                venue = "Unknown"
        else:
            authors = ""
            venue = ""
            year = "Unknown"
            
        # Image
        image_url = ""
        img_widget = section.find('div', class_='elementor-widget-image')
        if img_widget:
            img = img_widget.find('img')
            if img:
                image_url = img.get('src')
                
        publications.append({
            "title": title,
            "authors": authors,
            "venue": venue,
            "year": year,
            "links": links_data,
            "image": image_url
        })

    print(f"Found {len(publications)} publications.")
    
    # Save to JSON
    output_path = 'data/publications.json'
    with open(output_path, 'w') as f:
        json.dump(publications, f, indent=4)
    print(f"Saved to {output_path}")

if __name__ == "__main__":
    scrape_publications()
