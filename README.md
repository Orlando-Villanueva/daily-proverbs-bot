# Daily Proverbs Bot

A Python-based bot that posts daily verses from the Book of Proverbs on X (formerly Twitter). This bot is designed to share wisdom and inspiration through automated tweets, helping users reflect on meaningful verses each day.

## Features

- **Daily Verse Posting**: Automatically posts a random verse from the Book of Proverbs at scheduled times.
- **Customizable Schedule**: Easily modify the posting schedule to fit your needs.
- **Environment Variables**: Uses a `.env` file to securely manage API credentials.
- **Error Handling**: Includes error handling to manage potential issues with posting.

## Technologies Used

- **Python**: The primary programming language used for the bot.
- **Tweepy**: A Python library for accessing the X API.
- **Requests**: For fetching Proverbs verses from an external API.
- **Schedule**: A Python library for scheduling tasks.
- **PythonAnywhere**: Hosting platform for running the bot continuously.

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
    pip install -r requirements.txt
    ```

5. Create a .env file in the root directory and add your X API credentials:
    ```
    API_KEY=your_api_key
    API_SECRET=your_api_secret
    ACCESS_TOKEN=your_access_token
    ACCESS_TOKEN_SECRET=your_access_token_secret
    ```
    
6. To run the bot locally, execute:
    ```
    python x_bot.py
    ```
