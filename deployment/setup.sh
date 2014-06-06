#!/bin/sh

# Deployment Script for deploying to Ubuntu 14.04 Server

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
    # Default root MySQL password = 'root'
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

set_env_var () {
    local project_dir="$1"

    # sets the production settings path as an env variable
    echo export PRODUCTION_SETTINGS=$project_dir/app/settings/production.cfg >> $HOME/.bash_profile
    source $HOME/.bash_profile

    return
}

setup_nginx () {
    local project_dir="$1"

    # Replaces the nginx default file
    sudo rm /etc/nginx/sites-available/default
    sudo rm /etc/nginx/sites-enabled/default
    sudo touch /etc/nginx/sites-available/insightfl

    sudo bash -c 'cat > /etc/nginx/sites-available/insightfl <<- _EOF_
    server {
      listen 80;

      root '$project_dir';
      index index.html index.htm;

      server_name "";

      location / {
        proxy_pass http://127.0.0.1:8000;
      }
    }'

    # Creates a sudo link to sites-enabled
    sudo ln -s /etc/nginx/sites-available/insightfl /etc/nginx/sites-enabled/insightfl

    return
}

start_app () {
    local project_dir="$1"

    # Runs the app within a screen detached mode
    cd $project_dir
    screen -d -m gunicorn app:app

    # Starts nginx
    sudo service nginx start

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

    read -p $'\e[32m'"Enter your github username > "$'\e[0m' username

    if [[ ! -n "$username" ]]; then
        echo $'\e[31m'"Please enter a github username"$'\e[0m'
        main
    else
        read -p $'\e[32m'"Enter the github repository name [insightfl] > "$'\e[0m' project

        # Default project name is 'insightfl'
        project=${project:="insightfl"}
        project_dir=$HOME/$project
        status=$(curl -s -I "https://github.com/$username/$project" | head -n 1 | cut -d$' ' -f2)

        if [[ "$status" != 200 ]]; then
            echo $'\e[31m'"Status: $status"$'\e[0m'
            echo $'\e[31m'"You've entered an invalid username or Github repository"$'\e[0m'
            main
        else
            read -p $'\e[32m'"Would you like to install MySQL? [Y/n] > "$'\e[0m' mysql
            read -p $'\e[32m'"Would you like to install the SCIPY stack? [Y/n] > "$'\e[0m' scipy
            read -p $'\e[32m'"Would you like to install R? [Y/n] > "$'\e[0m' rcore

            # Default package options
            mysql=${mysql:="y"}
            scipy=${scipy:="y"}
            rcore=${rcore:="y"}

            mysql=$(echo $mysql | tr 'A-Z' 'a-z')
            scipy=$(echo $scipy | tr 'A-Z' 'a-z')
            rcore=$(echo $rcore | tr 'A-Z' 'a-z')

            install_global_dependencies

            if [[ "$mysql" == "y" ]]; then
                install_mysql_and_mysqldb
            fi

            if [[ "$scipy" == "y" ]]; then
                install_scipy
            fi

            if [[ "$rcore" == "y" ]]; then
                install_rcore
            fi

            # Clones project, installs dependencies, setups nginx, and starts app
            clone_project $username $project
            install_project_dependencies $project_dir
            set_env_var $project_dir
            setup_nginx $project_dir
            start_app $project_dir

            cd $HOME
        fi
    fi

    return
}

# Main function
main
