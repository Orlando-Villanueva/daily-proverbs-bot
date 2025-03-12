import random
import requests
from config import PROVERBS_VERSES


def get_esv_proverb():
    # Select a random chapter and verse
    chapter, verse_num = random.choice(PROVERBS_VERSES)

    # Fetch only the selected verse using ASV translation
    url = f"https://bible-api.com/proverbs+{chapter}:{verse_num}?translation=asv"
    response = requests.get(url)
    data = response.json()

    verse_text = data['text'].replace('\n', ' ').replace('  ', ' ').strip()
    return f"Proverbs {chapter}:{verse_num} (ASV)\n{verse_text}"


if __name__ == "__main__":
    # Display the verse
    proverb = get_esv_proverb()
    print(proverb)
