
import os
import random
import tweepy
import requests
import schedule
import time
from dotenv import load_dotenv
from config import PROVERBS_VERSES, TRANSLATION

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
    # Select a random chapter and verse
    chapter, verse_num = random.choice(PROVERBS_VERSES)
    
    try:
        # Fetch only the selected verse
        url = f"https://bible-api.com/proverbs+{chapter}:{verse_num}?translation={TRANSLATION}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        data = response.json()
        verse_text = data['text'].replace('\n', ' ').replace('  ', ' ').strip()
        return f"Proverbs {chapter}:{verse_num} ({TRANSLATION})\n{verse_text}"
    except requests.exceptions.RequestException as e:
        print(f"API request error: {e}")
        return None
    except (KeyError, ValueError) as e:
        print(f"Data parsing error: {e}")
        return None

def post_tweet():
    proverb = get_proverb()
    if not proverb:
        print("Failed to get proverb. Skipping tweet.")
        return
    
    try:
        tweet = client.create_tweet(text=proverb)
        print(f"Tweet posted successfully: {tweet.data['id']}")
        print(f"Tweet content: {proverb}")
    except tweepy.TweepyException as e:
        print(f"Twitter API error: {e}")
    except Exception as e:
        print(f"Unexpected error posting tweet: {e}")

def run_scheduled_job():
    print(f"Running scheduled job at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    post_tweet()

if __name__ == "__main__":
    # Post immediately on startup
    post_tweet()
    
    # Schedule daily posts at 8:00 AM
    schedule.every().day.at("08:00").do(run_scheduled_job)
    
    print("Bot started. Scheduled to post daily at 08:00.")
    
    # Keep the script running
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute
