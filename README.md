# Daily Proverbs Bot for X

A Python-based bot that posts daily verses from the Book of Proverbs on X (formerly Twitter). This bot is designed to share wisdom and inspiration through automated tweets, helping users reflect on meaningful verses each day.

## Features

- **Daily Verse Posting**: Automatically posts a random verse from the Book of Proverbs at scheduled times.
- **Environment Variables**: Uses a `.env` file to securely manage API credentials.

## Configured Schedule

The bot runs via a GitHub Actions workflow (`.github/workflows/post-tweet.yml`) on the following cron schedule:

```
30 11,13,15,17,19,21,23 * * *
```

This means the bot posts **7 times a day at minute :30**, at the following UTC hours:

| UTC Time | EDT Time (UTC-4) | EST Time (UTC-5) |
|----------|-----------------|-----------------|
| 11:30    | 7:30 AM         | 6:30 AM         |
| 13:30    | 9:30 AM         | 8:30 AM         |
| 15:30    | 11:30 AM        | 10:30 AM        |
| 17:30    | 1:30 PM         | 12:30 PM        |
| 19:30    | 3:30 PM         | 2:30 PM         |
| 21:30    | 5:30 PM         | 4:30 PM         |
| 23:30    | 7:30 PM         | 6:30 PM         |

The workflow can also be triggered manually from the **Actions** tab on GitHub.

## Technologies Used

- **Python**: The primary programming language used for the bot.
- **Tweepy**: A Python library for accessing the X API.
- **Requests**: For fetching Proverbs verses from an external API.
- **bible-api.com**: A free JSON API for retrieving Bible verses and passages.
- **Schedule** (Optional): A Python library for scheduling tasks within the script.

## Getting Started

### Prerequisites

- Python 3.x
- X Developer Account (for API keys)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/daily-proverbs-bot.git
   cd daily-proverbs-bot
   ```

2. Create a virtual environment:
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate
    ```

3. Install the required packages:
    ```
    pip install tweepy requests python-dotenv
    ```

5. Create a .env file in the root directory and add your X API credentials:
    ```
    API_KEY=your_api_key
    API_SECRET=your_api_secret
    ACCESS_TOKEN=your_access_token
    ACCESS_TOKEN_SECRET=your_access_token_secret
    ```
    
6. To run the bot locally (one-time post), execute:
    ```
    python x_bot.py
    ```

7. For scheduled operation, the bot uses **GitHub Actions** (`.github/workflows/post-tweet.yml`):
    - The workflow runs automatically on the cron schedule documented in the **Configured Schedule** section above.
    - Add your API credentials as repository **Secrets** under *Settings → Secrets and variables → Actions*:
      - `ESV_API_KEY`
      - `API_KEY`
      - `API_SECRET`
      - `ACCESS_TOKEN`
      - `ACCESS_TOKEN_SECRET`
    - To trigger a run manually, go to the **Actions** tab and click **Run workflow**.
