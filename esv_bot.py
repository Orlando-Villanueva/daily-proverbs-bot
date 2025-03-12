
import random
import requests
from config import PROVERBS_VERSES

def get_proverb_in_translations():
    # Select a random chapter and verse
    chapter, verse_num = random.choice(PROVERBS_VERSES)
    
    # Dictionary to store verse text for each translation
    verses = {}
    
    # Fetch KJV translation
    kjv_url = f"https://bible-api.com/proverbs+{chapter}:{verse_num}?translation=kjv"
    kjv_response = requests.get(kjv_url)
    kjv_data = kjv_response.json()
    kjv_text = kjv_data['text'].replace('\n', ' ').replace('  ', ' ').strip()
    verses["KJV"] = kjv_text
    
    # Fetch ASV translation
    asv_url = f"https://bible-api.com/proverbs+{chapter}:{verse_num}?translation=asv"
    asv_response = requests.get(asv_url)
    asv_data = asv_response.json()
    asv_text = asv_data['text'].replace('\n', ' ').replace('  ', ' ').strip()
    verses["ASV"] = asv_text
    
    # Format the output
    output = f"Proverbs {chapter}:{verse_num}\n"
    output += f"KJV: {verses['KJV']}\n"
    output += f"ASV: {verses['ASV']}"
    
    return output

if __name__ == "__main__":
    # Display the verses in both translations
    proverb = get_proverb_in_translations()
    print(proverb)
