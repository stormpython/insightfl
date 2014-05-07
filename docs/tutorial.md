
## Checking System Requirements
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

## Root Directory Structure
1. `app/`
2. `deployment/` - contains example files and bash scripts to aid in deploying to Amazon AWS (Ubuntu 12.04)
3. `docs/` - project documentation
4. `.bowerrc` - Bower configuration file
5. `.gitignore` - [Git ignore file](https://help.github.com/articles/ignoring-files)
6. `bower.json`
7. `development.py`
8. `LICENSE.md`
9. `package.json`
10. `production.py`
11. `README.md`
12. `requirements.txt`
13. `schema.sql`
