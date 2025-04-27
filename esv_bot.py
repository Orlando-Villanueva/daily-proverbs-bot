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


def search_forwards(chapter, start_verse, current_verse):
    text = fetch_passage(f"Proverbs {chapter}:{start_verse}-{current_verse}")

    while not text.endswith(('.', '?', '!', '!"', '."')):
        current_verse += 1
        try:
            passage = f"Proverbs {chapter}:{start_verse}-{current_verse}"
            text = fetch_passage(passage)
        except:
            # If we hit an invalid verse, return the last valid text
            return text, current_verse - 1

    return text, current_verse


def build_reference(chapter, start_verse, end_verse=None):
    if end_verse and end_verse > start_verse:
        return f"Proverbs {chapter}:{start_verse}-{end_verse}"
    return f"Proverbs {chapter}:{start_verse}"


def handle_special_cases(chapter, start_verse):
    special_cases = {
        25: {
            6: ("Proverbs 25:6-7a (ESV)", 
                "Do not put yourself forward in the king's presence or stand in the place of the great, for it is better to be told, \"Come up here,\" than to be put lower in the presence of a noble."),
            7: ("Proverbs 25:7b-8 (ESV)",
                "What your eyes have seen do not hastily bring into court, for what will you do in the end, when your neighbor puts you to shame?")
        }
        # Add more special cases here as needed:
        # chapter_num: {
        #     verse_num: ("Reference", "Text")
        # }
    }

    if chapter in special_cases and start_verse in special_cases[chapter]:
        reference, text = special_cases[chapter][start_verse]
        return f"{reference}\n{text}"
    return None

def get_esv_proverb():
    while True:
        # Select a random chapter and verse
        chapter, verse_num = random.choice(PROVERBS_VERSES)
        # Get initial verse and check if it starts with capital letter
        verse_text = get_initial_verse(chapter, verse_num)
        # Check first actual character after any whitespace
        first_char = next(c for c in verse_text if not c.isspace())
        if not first_char.isupper():
            continue

        # First check if it's a special case
        special_case = handle_special_cases(chapter, verse_num)
        if special_case:
            return special_case

        # Check if verse is complete (ends with punctuation)
        if verse_text.endswith(('.', '?', '!', '!"', '."')):
            return f"Proverbs {chapter}:{verse_num} (ESV)\n{verse_text}"

        # If not complete, try to find the complete passage
        text, end_verse = search_forwards(chapter, verse_num, verse_num)
        if text.endswith(('.', '?', '!', '!"', '."')):
            return f"Proverbs {chapter}:{verse_num}-{end_verse} (ESV)\n{text}"


def post_tweet():
    proverb = get_esv_proverb()
    try:
        client = tweepy.Client(consumer_key=API_KEY,
                             consumer_secret=API_SECRET,
                             access_token=ACCESS_TOKEN,
                             access_token_secret=ACCESS_TOKEN_SECRET)
        tweet = client.create_tweet(text=proverb)
        print(f"Tweet posted successfully: {tweet.data['id']}")
        print(f"Tweet content: {proverb}")
    except Exception as e:
        print(f"Error posting tweet: {e}")


if __name__ == "__main__":
    # Always run once and exit - scheduling is handled by Replit Scheduled Deployments
    post_tweet()