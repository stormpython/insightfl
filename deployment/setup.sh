#!/bin/sh

# Deployment Script for deploying to Ubuntu 12.04 Server

sudo apt-get update
sudo apt-get install python-pip mysql-server -y
sudo apt-get build-dep python-mysqldb

sudo pip install pip --upgrade
sudo pip install virtualenv

sudo apt-get install curl make gcc g++
echo 'export PATH=$HOME/local/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
mkdir ~/.local/
mkdir ~/node-latest-install
cd ~/node-latest-install
curl http://nodejs.org/dist/node-latest.tar.gz | tar xz --strip-components=1
./configure --prefix=~/local
make install
curl https://www.npmjs.org/install.sh | sh

sudo apt-get build-deps git-core
sudo apt-get install git-core
