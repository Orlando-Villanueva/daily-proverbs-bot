
import os
import tweepy
from dotenv import load_dotenv

# Load environment variables
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

# Announcement text
announcement = """📢 Exciting update! Daily Proverbs Bot is now sharing wisdom SIX times daily (7am, 10am, 1pm, 4pm, 7pm & 10pm EST)! More biblical wisdom throughout your day. Follow for regular doses of Proverbs wisdom from the KJV Bible. #DailyProverbs #Bible #Wisdom"""

# Post the announcement
try:
    tweet = client.create_tweet(text=announcement)
    print(f"Announcement posted successfully: {tweet.data['id']}")
    print(f"Tweet content: {announcement}")
except Exception as e:
    print(f"Error posting announcement: {e}")

if __name__ == "__main__":
    print("Posting announcement tweet...")
