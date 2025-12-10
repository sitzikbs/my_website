import json
import os
from bs4 import BeautifulSoup

def update_pages():
    # Load data
    with open('data/home_content.json', 'r') as f:
        data = json.load(f)
        
    # --- Update index.html ---
    with open('index.html', 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    # Update Profile Image
    if data.get('profile_image'):
        img = soup.find('div', class_='profile-image').find('img')
        if img:
            img['src'] = data['profile_image']
            
    # Update About Content
    if data.get('about'):
        about_div = soup.find('div', class_='about-content')
        if about_div:
            # Parse the about HTML from JSON
            about_soup = BeautifulSoup(data['about'], 'html.parser')
            # Replace content
            about_div.clear()
            about_div.append(about_soup)
            
    # Update News
    if data.get('news'):
        news_list = soup.find('ul', id='news-list')
        if news_list:
            news_list.clear()
            for item in data['news']:
                li = soup.new_tag('li')
                date_span = soup.new_tag('span', attrs={'class': 'news-date'})
                date_span.string = item['date']
                content_span = soup.new_tag('span', attrs={'class': 'news-content'})
                content_span.string = item['content']
                li.append(date_span)
                li.append(" ") # Space
                li.append(content_span)
                news_list.append(li)
                
    with open('index.html', 'w') as f:
        f.write(str(soup.prettify()))
        
    print("Updated index.html")
    
    # --- Update contact.html ---
    with open('contact.html', 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    # Update Email (if found, but it was empty in JSON)
    if data['contact'].get('email'):
        email_div = soup.find('div', class_='contact-item') # This is risky, need better selector
        # Let's look for the email link
        email_link = soup.find('a', href=lambda x: x and x.startswith('mailto:'))
        if email_link:
            email_link['href'] = f"mailto:{data['contact']['email']}"
            email_link.string = data['contact']['email']
            
    # Update Social Links
    # Find the container for social links. It might not exist in the template yet.
    # The template has contact-info div.
    contact_info = soup.find('div', class_='contact-info')
    if contact_info:
        # Check if social-links div exists
        social_div = contact_info.find('div', class_='social-links')
        if not social_div:
            social_div = soup.new_tag('div', attrs={'class': 'social-links', 'style': 'margin-top: 2rem; display: flex; justify-content: center; gap: 1.5rem;'})
            contact_info.append(social_div)
        else:
            social_div.clear()
            
        for link in data['contact']['social']:
            a = soup.new_tag('a', href=link['url'], target='_blank', attrs={'class': 'social-link', 'style': 'font-size: 1.5rem; color: var(--text-color);'})
            i = soup.new_tag('i', attrs={'class': link['icon']})
            a.append(i)
            social_div.append(a)
            
    with open('contact.html', 'w') as f:
        f.write(str(soup.prettify()))
        
    print("Updated contact.html")

if __name__ == "__main__":
    update_pages()
