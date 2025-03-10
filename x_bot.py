import os
import random
import tweepy
import requests
from dotenv import load_dotenv
from config import PROVERBS_VERSES, TRANSLATION

# Load environment variables (for local testing)
load_dotenv()

# X API credentials (from Deployment secrets)
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate with X
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

def get_proverb():
    # Select a random chapter and verse
    chapter, verse_num = random.choice(PROVERBS_VERSES)
    
    # Fetch only the selected verse
    url = f"https://bible-api.com/proverbs+{chapter}:{verse_num}?translation={TRANSLATION}"
    response = requests.get(url)
    data = response.json()
    
    verse_text = data['text'].replace('\n', ' ').replace('  ', ' ').strip()
    return f"Proverbs {chapter}:{verse_num} ({TRANSLATION})\n{verse_text}"

def post_tweet():
    proverb = get_proverb()
    try:
        tweet = client.create_tweet(text=proverb)
        print(f"Tweet posted successfully: {tweet.data['id']}")
        print(f"Tweet content: {proverb}")
    except Exception as e:
        print(f"Error posting tweet: {e}")

if __name__ == "__main__":
    # Debug credentials
    print(f"API_KEY exists: {API_KEY is not None}")
    print(f"API_SECRET exists: {API_SECRET is not None}")  
    print(f"ACCESS_TOKEN exists: {ACCESS_TOKEN is not None}")
    print(f"ACCESS_TOKEN_SECRET exists: {ACCESS_TOKEN_SECRET is not None}")
    
    # Always run once and exit - scheduling is handled by Replit Scheduled Deployments
    post_tweet()
    print("Tweet posted. Job complete.")