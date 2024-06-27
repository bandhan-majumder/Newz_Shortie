from flask import Flask, render_template, jsonify, request, redirect
import os
import requests
import json
from randomNiche import random_niches
import random
from datetime import datetime, timedelta

my_news_api_key = os.environ["my_news_api_key"]
app = Flask(__name__)  # turn this file into flask application

common_niches = [{
    "id":
        1,
    "title":
        "Technology",
    "description":
        "Stay up-to-date with the latest tech innovations and advancements.",
}, {
    "id":
        2,
    "title":
        "Sports",
    "description":
        "Catch up on the latest scores, highlights, and stories from the world of sports.",
}, {
    "id":
        3,
    "title":
        "Weather",
    "description":
        "Get forecasts, weather updates, and climate news for your local area and beyond.",
}, {
    "id":
        4,
    "title":
        "Finance",
    "description":
        "Stay informed about market trends, investment opportunities, and financial news.",
}]


# Function to get yesterday's date
def get_yesterdays_date():
    yesterday = datetime.now() - timedelta(days=2)
    return yesterday.strftime('%Y-%m-%d')


# Function to fetch news data
def get_news(interest):
    api_key = my_news_api_key  # Your News API key
    yesterday_date = get_yesterdays_date()
    response = requests.get(
        f"https://newsapi.org/v2/everything?q={interest}&language=en&pagesize=15&from={yesterday_date}&sortBy=publishedAt&apiKey={api_key}"
    )
    news_data = json.loads(response.text)
    return news_data.get("articles", [])

# registering a route (a html route)
@app.route("/")  
def hello_world():
    fields = ['Technology', 'Sports', 'Weather', 'Finance']
    return render_template('home.html', common_niches=common_niches, fields=fields)


@app.route("/niche/<url_param>", methods=["GET"])
def news_type(url_param):
    news_data = get_news(url_param)
    return render_template('recent_news.html', news=news_data)


# Inside <form>, the submit button at the bottom of home.html has action="/niche" and method is "GET"
@app.route("/niche", methods=["POST", "GET"])
def news_niche():
    # if it's a "get" request, do the things
    if request.method == "GET":
        if not request.args.get("search"):  # if the search field is empty
            return render_template('recent_news.html', news="")
        niche = request.args.get("search")  # default niche is toys
        news_data = get_news(niche)
        return render_template('recent_news.html', news=news_data)  # news=news_data , key=value
    # else it's a "post" request
    return "Post request"


@app.route("/random", methods=["GET"])
def random_news():
    i = random.randint(0, 149)
    niche = random_niches[i]
    news_data = get_news(niche)
    return render_template('recent_news.html', news=news_data)


@app.route("/about", methods=["GET"])
def about():
    return render_template('about.html')


if __name__ == "__main__":  # if the file is run directly / invoked via fle name (python app.py)
    app.run(host='0.0.0.0',
            debug=True)  # debug=True enables reloading the changes while running
