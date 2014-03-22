# InsightFL
A basic template for building minimal flask applications.

### Introduction
InsightFL is a basic [Flask](http://flask.pocoo.org/) template created specifically to help budding
data scientists in the [Insight Data Science](http://insightdatascience.com/) program get their web applications
off the ground quickly. As a former Insight fellow, I spent way too much time troubleshooting the ins and outs of
web development instead of focusing on what truly mattered, extracting insight from my data.

InsightFL comes with all the necessary tools you'll need to create your web app:

  1. Twitter Bootstrap for designing your web pages
  2. Bower to easily install third party libraries
  3. Reveal.js for creating amazing presentations in HTML
  4. And its already in version control from the [git](http://git-scm.com/) go!

To get started building your web app, follow the instructions below to setup your development and production
environments.

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

1. Secure copy the setup script (located in the deployment directory) to the remote host.

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

6. You should now be able to run your app!

  ```
  python app.py
  ```

