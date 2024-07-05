#!/bin/bash

# Replace the placeholder with the environment variable
sed "s/{{HOST}}/$HOST/g" ./nginx.conf.template > /etc/nginx/nginx.conf

# Start Nginx
nginx -g "daemon off;" &

# Starting Flask app
/venv/bin/python3 app.py
