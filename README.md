# InsightFL
A basic template for building minimal flask applications.

### Introduction
InsightFL is a basic [Flask](http://flask.pocoo.org/) template to help those beginning

## Installation
### System Requirements
* [Python](https://www.python.org/downloads/) with [pip](http://pip.readthedocs.org/en/latest/installing.html) installed.
* [node and npm](https://gist.github.com/isaacs/579814)
*For a quick tutorial on how to install node and npm on Windows, Linux/Unix, or OSX visit this
 [site](http://www.joyent.com/blog/installing-node-and-npm/).*
* [bower](http://bower.io)

    ```
    npm install -g bower
    ```
### Environment Setup
1. Fork the [project](https://github.com/stormpython/insightfl/fork) and clone the repository.
2. Install Bower project dependencies.

  ```
  bower install
  ```

3. Install Python project dependencies.

  ```
  pip install -r requirements.txt
  ```

That's it! You are ready to start coding up your project.

## Getting Started
### Quick Start
Coming Soon!

### Tutorial
Coming Soon!

### Deploying to AWS
*Note: the setup script assumes you are deploying to an Ubuntu 12.04 Server*

1. Secure copy setup script to the remote host.

  ```
  scp /path/to/deployment/setup.sh user@remoteip:~/
  ```

2. SSH into the remote host and run the setup script.

  ```
  sudo chmod 755 setup.sh
  ./setup.sh
  ```

3. Clone your project's repo (using https).

  ```
  git clone https://github.com/<username>/insightfl.git
  ```

4. Change into the project directory and install dependencies.

  ```
  cd ~/insightfl
  bower install
  sudo pip install -r requirements.txt
  ```

5. Add your production settings to an environment variable.

  ```
  export PROD_CONFIG="/path/to/settings/production.cfg"
  ```

