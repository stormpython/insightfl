#!/bin/sh

# Deployment Script for deploying to Ubuntu 12.04 Server

install_global_dependencies () {
    # Installs git, git dependencies, pip, curl, nginx
    sudo apt-get update
    sudo apt-get build-dep -y git-core
    sudo apt-get install -y git-core python-pip curl nginx

    # Installs node and npm
    sudo apt-get install -y python-software-properties python g++ make
    sudo add-apt-repository -y ppa:chris-lea/node.js
    sudo apt-get update
    sudo apt-get install -y nodejs

    return
}

install_rcore () {
    # Installs R
    sudo apt-get install -y r-base-core

    return
}

install_scipy () {
    # Installs the scipy stack
    sudo apt-get install -y python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose

    return
}

install_mysql_and_mysqldb () {
    # Installs MySQL and MySQLdb
    # Creates the default root MySQL password to 'root'
    sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password root'
    sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password root'
    sudo apt-get install -y mysql-server
    sudo apt-get install -y python-mysqldb
    sudo pip install pip --upgrade

    return
}


clone_project () {
    local username="$1"
    local project="$2"

    # Clones the github repo
    git clone https://github.com/$username/$project.git

    return
}

install_project_dependencies () {
    local project_dir="$1"

    # Installs project dependencies
    cd $project_dir
    npm install
    sudo pip install -r requirements.txt

    return
}

setup_nginx () {
    local project_dir="$1"

    # Replaces the nginx default file
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

    # Creates a sudo link to sites-enabled
    sudo ln -s /etc/nginx/sites-available/insightfl /etc/nginx/sites-enabled/insightfl

    # Starts nginx
    sudo service nginx start

    return
}

start_app () {
    # Runs the app within a screen detached mode
    screen -d -m python production.py

    return
}

main () {
    local username
    local project
    local project_dir
    local status
    local mysql
    local scipy
    local rcore

    read -p "Enter your github username > " username

    if [[ ! -n "$username" ]]; then
        echo $'\e[31m'"Please enter a github username"$'\e[0m'
        main
    else
        read -p "Enter the github repository name [insightfl] > " project

        # Default project name is 'insightfl'
        project=${project:="insightfl"}
        project_dir=$HOME/$project
        status=$(curl -s -I "https://github.com/$username/$project" | head -n 1 | cut -d$' ' -f2)

        if [[ "$status" != 200 ]]; then
            echo $'\e[31m'"Status: $status"$'\e[0m'
            echo $'\e[31m'"You've entered an invalid username or Github repository"$'\e[0m'
            main
        else
            read -p "Would you like to install MySQL [Y/n] > " mysql
            read -p "Would you like to install the scipy stack [Y/n] > " scipy
            read -p "Would you like to install R [Y/n] >" rcore

            # Default package options
            mysql=${mysql:="Y" | tr '[:lower:]' '[:upper:]'}
            scipy=${scipy:="Y" | tr '[:lower:]' '[:upper:]'}
            rcore=${rcore:="Y" | tr '[:lower:]' '[:upper:]'}

            install_global_dependencies

            if [[ "$mysql" == "Y" ]]; then
                install_mysql_and_mysqldb
            fi

            if [[ "$scipy" == "Y" ]]; then
                install_scipy
            fi

            if [[ "$rcore" == "Y" ]]; then
                install_rcore
            fi

            # Clones project, installs dependencies, setups nginx, and starts app
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
