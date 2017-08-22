#!/usr/bin/env bash
# Bash script that sets up web server deployment

sudo apt-get update

sudo apt-get install -y nginx

sudo service nginx start

sudo mkdir -p /data/web_static/releases/test

echo "<!DOCTYPE html><html><head></head><body>test html</body></html>" > /data/web_static/releases_test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sed -i '31 i \location /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx restart
