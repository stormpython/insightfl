#!/bin/sh

# Update script
cd /home/ubuntu/insightfl

# Pulls down the latest changes
git pull origin master

# Installs project dependencies
npm install
sudo pip install -r requirements.txt

# terminates the running screen and restarts
screen -X quit
screen -d -m python production.py
