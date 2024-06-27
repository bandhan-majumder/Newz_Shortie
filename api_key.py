import os

# Fetch the API key from GitHub secret
news_api_key = os.getenv('NEWS_API_KEY')

if news_api_key is None:
    raise ValueError("NEWS_API_KEY not found in environment variables. Please set it in GitHub secrets.")

