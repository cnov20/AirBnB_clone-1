#!/usr/bin/env bash
# This script configures servers to deploy static content on the web
sudo apt-get update
sudo apt-get install -y nginx
sudo service nginx start
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test
echo -e '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' | sudo tee /data/web_static/releases/test/index.html
sudo ln -sfn /data/web_static/releases/test/ /data/web_static/current
sudo chown --recursive ubuntu:ubuntu /data/
sudo sed -i '38 i\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-enabled/default
sudo service nginx restart
