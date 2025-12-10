import requests
from bs4 import BeautifulSoup
import json
import os
import re

def scrape_home_and_contact():
    url = "https://www.itzikbs.com/"
    print(f"Fetching {url}...")
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch home page: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    
    # --- Scrape About Me ---
    about_section = soup.find(lambda tag: tag.name in ['h1', 'h2', 'h3'] and "About Me" in tag.text)
    about_text = ""
    if about_section:
        # Get paragraphs following the header
        # The structure seems to be header -> text editor widget -> paragraphs
        # Or header is inside a widget, and text is in another widget.
        
        # Let's look for the text editor widget in the same section or column
        parent_col = about_section.find_parent(class_='elementor-column')
        if parent_col:
            # Get all text editor widgets in this column
            text_widgets = parent_col.find_all(class_='elementor-widget-text-editor')
            for widget in text_widgets:
                # Check if this widget contains the header? No, header is separate usually.
                # Just get all text from widgets that are NOT the header widget
                if widget.find(lambda tag: tag.name in ['h1', 'h2', 'h3'] and "About Me" in tag.text):
                    continue
                about_text += str(widget.find('div', class_='elementor-widget-container'))
        else:
            # Fallback
            about_text = "<p>Could not extract About Me content automatically.</p>"
    
    # Clean up about text (remove elementor classes if needed, but keeping HTML is good)
    
    # --- Scrape News ---
    # Look for "News:" text
    news_items = []
    # The news seems to be in a text block starting with "News:"
    # It might be in the same column as the profile image or intro.
    
    # Let's search for the string "News:"
    news_header = soup.find(string=re.compile("News:"))
    if news_header:
        # It's likely inside a p tag or div
        news_container = news_header.find_parent('div') or news_header.find_parent('p')
        if news_container:
            # The news items are likely lines following "News:"
            # Or separate paragraphs.
            # Based on previous fetch, it looked like:
            # News:
            # 07/25: ...
            # 10/24: ...
            
            text_content = news_container.get_text(separator="\n")
            lines = text_content.split('\n')
            capture = False
            for line in lines:
                if "News:" in line:
                    capture = True
                    continue # Skip the "News:" line itself if it's just that
                
                if capture:
                    line = line.strip()
                    if not line: continue
                    
                    # Check if it looks like a date "MM/YY:"
                    date_match = re.match(r'(\d{2}/\d{2}):', line)
                    if date_match:
                        date = date_match.group(1)
                        content = line[len(date)+1:].strip()
                        news_items.append({"date": date, "content": content})
                    elif news_items:
                        # Append to previous item if it's a continuation
                        news_items[-1]["content"] += " " + line
    
    # --- Scrape Profile Image ---
    profile_img_url = ""
    # Look for an image with alt "Itzik Ben Shabat" or similar
    img = soup.find('img', alt=re.compile("Itzik Ben Shabat", re.I))
    if img:
        profile_img_url = img.get('src')
    
    # --- Scrape Contact Info ---
    # Check footer or contact page
    contact_url = "https://www.itzikbs.com/contact"
    print(f"Fetching {contact_url}...")
    contact_response = requests.get(contact_url)
    email = ""
    social_links = []
    
    if contact_response.status_code == 200:
        contact_soup = BeautifulSoup(contact_response.content, 'html.parser')
        # Look for mailto link
        mailto = contact_soup.find('a', href=re.compile(r'^mailto:'))
        if mailto:
            email = mailto['href'].replace('mailto:', '')
            
        # Look for social links
        # Twitter, LinkedIn, Github, Youtube
        social_map = {
            "twitter.com": "Twitter",
            "linkedin.com": "LinkedIn",
            "github.com": "GitHub",
            "youtube.com": "YouTube"
        }
        
        for link in contact_soup.find_all('a', href=True):
            href = link['href']
            for domain, name in social_map.items():
                if domain in href:
                    # Avoid duplicates
                    if not any(l['name'] == name for l in social_links):
                        social_links.append({"name": name, "url": href, "icon": f"fab fa-{name.lower()}"})

    # Save Data
    data = {
        "about": about_text,
        "news": news_items,
        "profile_image": profile_img_url,
        "contact": {
            "email": email,
            "social": social_links
        }
    }
    
    with open('data/home_content.json', 'w') as f:
        json.dump(data, f, indent=4)
        
    print("Saved home content to data/home_content.json")

if __name__ == "__main__":
    scrape_home_and_contact()
