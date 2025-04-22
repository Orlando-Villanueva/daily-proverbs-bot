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


def fetch_passage(passage, params=None):
    default_params = {
        'q': passage,
        'indent-poetry': False,
        'include-headings': False,
        'include-footnotes': False,
        'include-verse-numbers': False,
        'include-short-copyright': False,
        'include-passage-references': False
    }
    if params:
        default_params.update(params)

    headers = {'Authorization': f'Token {ESV_API_KEY}'}
    response = requests.get(API_URL, params=default_params, headers=headers)
    data = response.json()
    return re.sub(r'\s+', ' ', data['passages'][0]).strip()


def get_initial_verse(chapter, verse):
    passage = f"Proverbs {chapter}:{verse}"
    return fetch_passage(passage)


def search_backwards(chapter, start_verse, original_verse):
    current_verse = start_verse
    while current_verse >= 1:
        passage = f"Proverbs {chapter}:{current_verse}-{original_verse}"
        text = fetch_passage(passage)
        if text[0].isupper():
            return text, current_verse
        current_verse -= 1
    return text, current_verse


def search_forwards(chapter, start_verse, current_verse):
    text = fetch_passage(f"Proverbs {chapter}:{start_verse}-{current_verse}")

    while not text.endswith(
        ('.', '?', '!', '!"')) and current_verse < CHAPTER_VERSES.get(
            chapter, 0):
        current_verse += 1
        passage = f"Proverbs {chapter}:{start_verse}-{current_verse}"
        text = fetch_passage(passage)

    return text, current_verse


def build_reference(chapter, start_verse, end_verse=None):
    if end_verse and end_verse > start_verse:
        return f"Proverbs {chapter}:{start_verse}-{end_verse}"
    return f"Proverbs {chapter}:{start_verse}"


def get_complete_passage(chapter, start_verse):
    # Get initial verse
    text = get_initial_verse(chapter, start_verse)
    original_verse = start_verse

    # Handle lowercase start
    if text[0].islower() and start_verse > 1:
        text, new_start = search_backwards(chapter, start_verse - 1,
                                         original_verse)
        if new_start >= 1:  # Only update if valid verse found
            start_verse = new_start

    # Check if complete sentence
    if text.endswith(('.', '?', '!', '!"')):
        reference = build_reference(chapter, start_verse, original_verse)
        return f"{reference} (ESV)\n{text}"

    # Search forwards if needed
    text, end_verse = search_forwards(chapter, start_verse, start_verse)

    reference = build_reference(chapter, start_verse, end_verse)
    return f"{reference} (ESV)\n{text}"


def get_esv_proverb():
    # Select a random chapter and verse
    #chapter, verse_num = random.choice(PROVERBS_VERSES)
    chapter, verse_num = 24, 22
    print(f"Initially selected: Proverbs {chapter}:{verse_num}")
    final_passage = get_complete_passage(chapter, verse_num)
    print(f"Final passage reference: {final_passage.split('\n')[0]}")
    return final_passage


def post_tweet():
    proverb = get_esv_proverb()
    try:
        # X API credentials (moved here)
        client = tweepy.Client(consumer_key=API_KEY,
                               consumer_secret=API_SECRET,
                               access_token=ACCESS_TOKEN,
                               access_token_secret=ACCESS_TOKEN_SECRET)
        #tweet = client.create_tweet(text=proverb)
        #print(f"Tweet posted successfully: {tweet.data['id']}")
        print(f"Tweet content: {proverb}")
    except Exception as e:
        print(f"Error posting tweet: {e}")


if __name__ == "__main__":
    # Always run once and exit - scheduling is handled by Replit Scheduled Deployments
    post_tweet()
