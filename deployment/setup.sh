#!/bin/sh

# Deployment Script for deploying to Ubuntu 12.04 Server
read -p "Enter your github username > " username
read -p "Enter the github repository name [insightfl] > " project

# Default project name is 'insightfl'
project=${project:="insightfl"}
project_dir=$HOME/$project

if [[ username && project ]]; then
  # Installing git, git dependencies, pip, curl, nginx, MySQL, and MySQLdb
  sudo apt-get update
  sudo apt-get build-dep -y git-core
  sudo apt-get install -y git-core python-pip curl nginx mysql-server python-mysqldb
  sudo pip install pip --upgrade

  # Installing node and npm
  sudo apt-get install -y python-software-properties python g++ make
  sudo add-apt-repository -y ppa:chris-lea/node.js
  sudo apt-get update
  sudo apt-get install -y nodejs

  # Cloning the github repo
  git clone https://github.com/$username/$project.git

  # Installing project dependencies
  cd $project_dir
  npm install
  sudo pip install -r requirements.txt

  # Setting up nginx
  sudo rm /etc/nginx/sites-available/default
  sudo touch /etc/nginx/sites-available/insightfl

  sudo bash -c 'cat > /etc/nginx/sites-available/insightfl <<- _EOF_
  server {
    listen 80;

    root '$project_dir';
    index index.html index.htm;

    server_name "";

    location / {
      proxy_pass http://127.0.0.1:5000;
    }
  }'

  # Creating sudo link to sites-enabled & starting nginx
  sudo ln -s /etc/nginx/sites-available/insightfl /etc/nginx/sites-enabled/insightfl
  sudo service nginx start

  # Starting the app
  screen -d -m python app.py

  # Change into home directory
  cd $HOME
else
  if [[ !username ]]; then
    echo "Please enter a username"
    exit 1
  fi
fi



