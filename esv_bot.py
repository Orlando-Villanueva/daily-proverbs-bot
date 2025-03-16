import os
import random
import re
import requests
from dotenv import load_dotenv
from config import PROVERBS_VERSES

# Load environment variables
load_dotenv()

# ESV API settings
API_KEY = os.getenv("ESV_API_KEY")
API_URL = 'https://api.esv.org/v3/passage/text/'


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

    headers = {'Authorization': f'Token {API_KEY}'}

    # Make API request
    response = requests.get(API_URL, params=params, headers=headers)
    data = response.json()

    # Clean and format the text
    text = re.sub(r'\s+', ' ', data['passages'][0]).strip()
    return f"Proverbs {chapter}:{verse_num} (ESV)\n{text}"


if __name__ == "__main__":
    # Display the verse
    proverb = get_esv_proverb()
    print(proverb)
