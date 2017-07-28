#!/usr/bin/env bash
# This script configures servers to deploy static content on the web
sudo apt-get update
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test
echo -e '<html>
  <head>
    <title>Test File</title>
  </head>
  <body>
    Holberton School
  </body>
</html>' | sudo tee /data/web_static/releases/test/index.html
sudo ln -sfn /data/web_static/releases/test/ /data/web_static/current
sudo chown --recursive ubuntu:ubuntu /data/
sudo sed -i '80 i\\n\tserver {\n\t\tlocation /hbnb_static {\n\t\t\talias /data/web_static/current/;\n\t\t} \n\t}' /etc/nginx/nginx.conf
sudo service nginx restart
