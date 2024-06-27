import os

# Print all environment variables for debugging
print(os.environ)

# Fetch the API key from GitHub secret
my_news_api_key = os.getenv('NEWS_API_KEY')

if my_news_api_key is None:
    raise ValueError("NEWS_API_KEY not found in environment variables. Please set it in GitHub secrets.")
    

