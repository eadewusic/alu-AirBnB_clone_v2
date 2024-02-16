#!/usr/bin/env bash
# Script that sets up web servers for the deployment of web_static

# Install Nginx if it is not already installed
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

# Create necessary folders if they don't already exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create or recreate symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve content
sudo sed -i '/hbnb_static/ s/^#//' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart

exit 0
