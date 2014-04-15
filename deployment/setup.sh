#!/bin/sh

# Deployment Script for deploying to Ubuntu 12.04 Server

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

# Change into home directory
cd $HOME

if [[ $1 ]]; then
  PROJECT_DIR=$HOME/$1
else


