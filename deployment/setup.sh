#!/bin/sh

# Deployment Script for deploying to Ubuntu 12.04 Server

# Installing git, git dependencies, pip, curl, nginx, MySQL, and MySQLdb
sudo apt-get update
sudo apt-get build-dep git-core -y
sudo apt-get install git-core python-pip curl nginx mysql-server python-mysqldb -y
sudo pip install pip --upgrade

# Installing node and npm
sudo apt-get install python-software-properties python g++ make -y
sudo add-apt-repository ppa:chris-lea/node.js -y
sudo apt-get update
sudo apt-get install nodejs -y

# Change into home directory
cd ~
