import os
import random
import re
import tweepy
import requests
from dotenv import load_dotenv
from config import PROVERBS_VERSES
from config import CHAPTER_VERSES

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


def get_complete_passage(chapter, start_verse):
    # First, check if we need to look backwards
    current_verse = start_verse

    # Get initial verse to check capitalization
    passage = f"Proverbs {chapter}:{start_verse}"
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
    response = requests.get(API_URL, params=params, headers=headers)
    data = response.json()
    text = re.sub(r'\s+', ' ', data['passages'][0]).strip()

    # If verse starts with lowercase, look backwards
    if text[0].islower() and start_verse > 1:
        original_verse = current_verse
        start_verse -= 1
        while start_verse >= 1:
            passage = f"Proverbs {chapter}:{start_verse}-{original_verse}"
            params['q'] = passage
            response = requests.get(API_URL, params=params, headers=headers)
            data = response.json()
            text = re.sub(r'\s+', ' ', data['passages'][0]).strip()
            if text[0].isupper():
                break
            start_verse -= 1

    # Now look forward for the end of the sentence
    current_verse = original_verse if 'original_verse' in locals(
    ) else start_verse
    complete_text = ""
    reference = f"Proverbs {chapter}:{start_verse}"

    while current_verse <= CHAPTER_VERSES.get(chapter, 0):
        passage = f"Proverbs {chapter}:{start_verse}-{current_verse}"

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
        response = requests.get(API_URL, params=params, headers=headers)
        data = response.json()

        text = re.sub(r'\s+', ' ', data['passages'][0]).strip()

        if text.endswith('.') or text.endswith('?') or text.endswith('!'):

            complete_text = text
            if current_verse > start_verse:
                reference = f"Proverbs {chapter}:{start_verse}-{current_verse}"
            break

        current_verse += 1
        if current_verse > CHAPTER_VERSES.get(chapter, 0):
            # If we reach the end of the chapter, use what we have
            complete_text = text
            break

    return f"{reference} (ESV)\n{complete_text}"


def get_esv_proverb():
    # Select a random chapter and verse
    chapter, verse_num = random.choice(PROVERBS_VERSES)
    print(f"Initially selected: Proverbs {chapter}:{verse_num}")
    final_passage = get_complete_passage(chapter, verse_num)
    print(f"Final passage reference: {final_passage.split('\n')[0]}")
    return final_passage


def post_tweet():
    proverb = get_esv_proverb()
    try:
        #tweet = client.create_tweet(text=proverb)
        #print(f"Tweet posted successfully: {tweet.data['id']}")
        print(f"Tweet content: {proverb}")
    except Exception as e:
        print(f"Error posting tweet: {e}")


if __name__ == "__main__":
    # Always run once and exit - scheduling is handled by Replit Scheduled Deployments
    post_tweet()
