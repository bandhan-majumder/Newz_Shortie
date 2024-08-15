from flask import Flask, render_template, jsonify, request, redirect, Response
import os
import requests
import json
from randomNiche import random_niches
import random
from datetime import datetime, timedelta
from prometheus_client import generate_latest, REGISTRY, Counter, Gauge, Summary
from werkzeug.serving import run_simple

my_news_api_key = os.environ["NEWS_API_KEY"] # get api key 
app = Flask(__name__)  # turn this file into flask application

# Define the Prometheus metrics
request_counter = Counter('http_requests_total', 'Total number of HTTP requests.')
active_users = Gauge('active_users', 'Current number of active users')
request_duration = Summary('request_duration_seconds', 'Request duration in seconds')

# My common niche types
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

# Custom 404 error handler
@app.errorhandler(404)
def page_not_found(error):
    request_counter.inc()
    return render_template('404.html'), 404

# registering a route
@app.route("/")
@request_duration.time()
def hello_world():
    request_counter.inc()
    active_users.inc()
    fields = ['Technology', 'Sports', 'Weather', 'Finance']
    return render_template('home.html', common_niches=common_niches, fields=fields)

@app.route("/niche/<url_param>", methods=["GET"])
@request_duration.time()
def news_type(url_param):
    request_counter.inc()
    news_data = get_news(url_param)
    return render_template('recent_news.html', news=news_data)

@app.route("/niche", methods=["POST", "GET"])
@request_duration.time()
def news_niche():
    request_counter.inc()
    # if it's a "get" request, do the things
    if request.method == "GET":
        if not request.args.get("search"):  # if the search field is empty
            return render_template('recent_news.html', news="")
        niche = request.args.get("search")
        news_data = get_news(niche)
        return render_template('recent_news.html', news=news_data)
    # else it's a "post" request
    return "Post request"

@app.route("/random", methods=["GET"])
@request_duration.time()
def random_news():
    request_counter.inc()
    i = random.randint(0, 149)
    niche = random_niches[i]
    news_data = get_news(niche)
    return render_template('recent_news.html', news=news_data)

@app.route("/about", methods=["GET"])
@request_duration.time()
def about():
    request_counter.inc()
    return render_template('about.html')

@app.route('/metrics')
def metrics():
    return Response(generate_latest(REGISTRY), mimetype='text/plain')

if __name__ == '__main__':
    run_simple('localhost', 5000, app, use_reloader=True, threaded=True)

