import os
import random
import re
import tweepy
import requests
from dotenv import load_dotenv
from config import PROVERBS_VERSES

# Load environment variables
load_dotenv()

# ESV API settings
ESV_API_KEY = os.getenv("ESV_API_KEY")
API_URL = 'https://api.esv.org/v3/passage/text/'

# X API credentials
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate with X
client = tweepy.Client(consumer_key=API_KEY,
                       consumer_secret=API_SECRET,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_TOKEN_SECRET)


def get_esv_proverb():
    # Select a random chapter and verse
    chapter, verse_num = random.choice(PROVERBS_VERSES)
    passage = f"Proverbs {chapter}:{verse_num}"

    # Configure API parameters
    params = {
        'q': passage,
        'indent-poetry': False,
        'include-headings': False,
        'include-footnotes': False,
        'include-verse-numbers': False,
        'include-short-copyright': False,
        'include-passage-references': False
    }

    headers = {'Authorization': f'Token {ESV_API_KEY}'}

    # Make API request
    response = requests.get(API_URL, params=params, headers=headers)
    data = response.json()

    # Clean and format the text
    text = re.sub(r'\s+', ' ', data['passages'][0]).strip()
    return f"Proverbs {chapter}:{verse_num} (ESV)\n{text}"


def post_tweet():
    proverb = get_esv_proverb()
    try:
        tweet = client.create_tweet(text=proverb)
        print(f"Tweet posted successfully: {tweet.data['id']}")
        print(f"Tweet content: {proverb}")
        return proverb
    except Exception as e:
        print(f"Error posting tweet: {e}")


if __name__ == "__main__":
    # Always run once and exit - scheduling is handled by Replit Scheduled Deployments
    tweet = post_tweet()
    print("Tweet posted. Job complete.")
    print(tweet)
