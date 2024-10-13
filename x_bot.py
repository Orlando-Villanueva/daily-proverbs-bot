import os
import random
import tweepy
import requests
from dotenv import load_dotenv

load_dotenv()

# X API credentials
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
    # Get a random Proverbs chapter (1-31)
    chapter = random.randint(1, 31)
    TRANSLATION = "KJV"
    url = f"https://bible-api.com/proverbs+{chapter}?translation={TRANSLATION}"
    response = requests.get(url)
    data = response.json()
    
    # Get a random verse from the chapter
    verses = data['verses']
    verse = random.choice(verses)
    verse['text'] = verse['text'].replace('\n', ' ').strip()  # Remove newlines and extra spaces
    
    return f"Proverbs {chapter}:{verse['verse']} ({TRANSLATION})\n{verse['text']}"

def post_tweet():
    proverb = get_proverb()
    try:
        tweet = client.create_tweet(text=proverb)
        print(f"Tweet posted successfully: {tweet.data['id']}")
        print(f"Tweet content: {proverb}")
    except Exception as e:
        print(f"Error posting tweet: {e}")

if __name__ == "__main__":
    post_tweet()