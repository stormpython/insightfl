#!/bin/sh

# Update script
cd /home/ubuntu/insightfl
git pull origin master
npm install
sudo pip install -r requirements.txt
