#!/bin/sh

# Deployment Script for deploying to Ubuntu 12.04 Server

# Installing git and git dependencies, pip, and curl
sudo apt-get update
sudo apt-get build-dep git-core -y
sudo apt-get install git-core python-pip curl -y
sudo pip install pip --upgrade

# Installing node, npm, and bower
echo 'export PATH=$HOME/local/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
mkdir ~/.local/
mkdir ~/node-latest-install
cd ~/node-latest-install
curl http://nodejs.org/dist/node-latest.tar.gz | tar xz --strip-components=1
./configure --prefix=~/local
make install
curl https://www.npmjs.org/install.sh | sh
npm install -g bower

# Change into home directory
cd ~
