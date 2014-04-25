#!/bin/sh

# Deployment Script for deploying to Ubuntu 12.04 Server

install_global_dependencies () {
    # Installing git, git dependencies, pip, curl, nginx
    sudo apt-get update
    sudo apt-get build-dep -y git-core
    sudo apt-get install -y git-core python-pip curl nginx

    # Installing R
    sudo apt-get install -y r-base-core

    # Installing the scipy stack
    sudo apt-get install -y python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose

    # Installing MySQL and MySQLdb
    # Creates the default root MySQL password to 'root'
    sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password root'
    sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password root'
    sudo apt-get install -y mysql-server
    sudo apt-get install -y python-mysqldb
    sudo pip install pip --upgrade

    # Installing node and npm
    sudo apt-get install -y python-software-properties python g++ make
    sudo add-apt-repository -y ppa:chris-lea/node.js
    sudo apt-get update
    sudo apt-get install -y nodejs

    return
}

clone_project () {
    local username="$1"
    local project="$2"

    # Cloning the github repo
    git clone https://github.com/$username/$project.git

    return
}

install_project_dependencies () {
    local project_dir="$1"

    # Installing project dependencies
    cd $project_dir
    npm install
    sudo pip install -r requirements.txt

    return
}

setup_nginx () {
    local project_dir="$1"

    # Replacing the nginx default file
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

    # Start nginx
    sudo service nginx start

    return
}

start_app () {
    # Running the app within screen detached mode
    screen -d -m python server.py

    return
}

main () {
    local username
    local project
    local project_dir
    local status

    read -p "Enter your github username > " username

    if [[ ! -n "$username" ]]; then
        echo $'\e[31m'"Please enter a username"$'\e[0m'
        main
    else
        read -p "Enter the github repository name [insightfl] > " project

        # Default project name is 'insightfl'
        project=${project:="insightfl"}
        project_dir=$HOME/$project
        status=$(curl -s -I "https://github.com/$username/$project" | head -n 1 | cut -d$' ' -f2)

        if [[ "$status" != 200 ]]; then
            echo $'\e[31m'"$status"$'\e[0m'
            echo $'\e[31m'"You've entered an invalid username or Github repository"$'\e[0m'
            main
        else
            install_global_dependencies
            clone_project $username $project
            install_project_dependencies $project_dir
            setup_nginx $project_dir
            start_app
            cd $HOME
        fi
    fi

    return
}

# Main function
main
