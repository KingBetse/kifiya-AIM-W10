import os
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')
print(API_KEY)

def fetch_news_data(start_date, end_date, keyword="Brent oil"):
    url = f'http://api.mediastack.com/v1/news'
    params = {
        'access_key': API_KEY,
        'keywords': keyword,
        'date': f'{start_date},{end_date}',
        'languages': 'en',  # English articles
        'limit': 100  # Max results per request (consider API limits)
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json().get('data', [])
        articles = [{
            'Date': article['published_at'],
            'Title': article['title'],
            'Description': article['description'],
            'Source': article['source'],
            'URL': article['url']
        } for article in data]
        return articles
    else:
        print(f"Error: {response.status_code}")
        return []

# Define date range
start_date = '1987-05-20'
end_date = '2024-09-30'

# Fetch articles
articles = fetch_news_data(start_date, end_date)

# Check if any articles were returned
if articles:
    # Convert to DataFrame and save to CSV
    df = pd.DataFrame(articles)
    df.to_csv('historical_news_events.csv', index=False)
    print("Scraping completed and saved to historical_news_events.csv.")
else:
    print("No articles found for the given date range and keyword.")