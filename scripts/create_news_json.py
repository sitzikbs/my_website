import json

def create_news_json():
    with open('data/home_content.json', 'r') as f:
        data = json.load(f)
        
    news = data.get('news', [])
    
    with open('data/news.json', 'w') as f:
        json.dump(news, f, indent=4)
        
    print("Created data/news.json")

if __name__ == "__main__":
    create_news_json()
