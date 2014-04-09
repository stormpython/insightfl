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
### System Requirements <a name="system-requirements"></a>
* [Python](https://www.python.org/downloads/) with [pip](http://pip.readthedocs.org/en/latest/installing.html) installed.
* [node and npm](https://gist.github.com/isaacs/579814)

  *For a quick tutorial on how to install node and npm on Windows, Linux/Unix, or OSX visit this
  [site](http://www.joyent.com/blog/installing-node-and-npm/).*

* [bower](http://bower.io)

    ```
    npm install -g bower
    ```

### Environment Setup <a name="environment-setup"></a>
1. Fork the [project](https://github.com/stormpython/insightfl/fork) and clone the repository.
2. Install Bower and the project dependencies.

  ```
  npm install
  ```

3. Install Python project dependencies.

  ```
  pip install -r requirements.txt
  ```

That's it! You are ready to start coding up your project.

## Getting Started <a name="getting-started"></a>
### Directory Structure
1. `deployment/` - contains bash script for deploying to Amazon AWS (Ubuntu 12.04)
2. `helpers/` - stores your python helper scripts
3. `settings/` - contains your app configuration files, e.g. development and production settings
4. `static/` - contains all the css, images, javascript, and third party libraries
5. `templates/` - contains all of your html files
6. `.bowerrc` - bower configuration file (defines the directory where bower saves dependencies)
7. `.gitignore` - git ignore file
9. `app.py` - main flask/application script for rendering views
10. `bower.json` - keeps track of your bower dependencies along with other project metadata
11. `requirements.txt` - keeps track of your python dependencies
12. `schema.sql` - SQL schema definitions

### Tutorial
In this tutorial, we will create a data application. We will use the Twitter API to visualize
tweets of [Flight MH370](http://en.wikipedia.org/wiki/Malaysia_Airlines_Flight_370) over time.

For the purposes of this tutorial, I will assume that you are familiar with the command line,
and that you know enough html, css, javascript, and python to get by. You do not need to be an
expert. You just need to know enough to understand what the code is doing. If you are new to any
of these things, a great place to learn or hone your skills is [Codecademy](http://www.codecademy.com/).
You will also need a [Github](https://github.com) account. If you do not have one, please create one now.
We will be developing our applications on our local machines.

So, the first thing you will need to do is make sure you have Python, pip, node, npm, and bower installed.
For instructions on how to install these for your system, visit their respective links in the
[system requirements](https://github.com/stormpython/insightfl#system-requirements) section. You can test
that any one of these is installed by running `which` followed by the item you wish to test. For example:

```
which pip
```

This should return the full path for pip.

```
/usr/local/bin/pip
```

If is does not return anything, it means that it is not installed on your system and you will need to install it.

Once all of the requirements are installed, fork the [InsightFL](https://github.com/stormpython/insightfl/fork)
project on Github and clone the repo to your computer.

```
git clone git@github.com:<username>/insightfl.git
```

Before we install anything else, lets go ahead and install
[virtualenv](http://www.virtualenv.org/en/latest/virtualenv.html). Virtualenv is a tool to create isolated Python
environments. Its good practice to use virtual environments when dealing with python and web development. To
install virtualenv:

```
sudo pip install virtualenv
```

Now lets activate a new isolated environment for our data application. Change into your project folder and create
a virtual environment directory with virtualenv.

```
cd path/to/insightfl
virtualenv venv
```

Here, we have created a new isolated python environment. Now lets activate our new virtual environment.

```
source venv/bin/activate
```

You should now see `(venv)` prepended to your command prompt. For example:

```
(venv)Stormpythons-MacBook-Pro:insightfl stormpython$
```

We can follow the rest of the [environment setup guide](https://github.com/stormpython/insightfl#environment-setup).
Since we have already forked and cloned our repo, we can skip step one. The next steps would be to install
the bower and python dependencies.

```
bower install
pip install -r requirements.txt
```

Now lets check to make sure our application runs ok. At the command line within the root or the project directory,
type:

```
python app.py
```

You should see something similar to this returned:

```
 * Running on http://127.0.0.1:5000/
 * Restarting with reloader
 ```

Open up a browser, and paste in `http://127.0.0.1:5000/`. You should see the InsightFL index page.
Great! With that out of the way, we are ready to begin creating our data application.

## Deploying to AWS

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
  npm install
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

