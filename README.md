# InsightFL
A basic template for building minimal web applications.

### Introduction
InsightFL is a basic [Flask](http://flask.pocoo.org/) template created specifically to help budding
data scientists in the [Insight Data Science](http://insightdatascience.com/) program. It comes with a very basic 
[Bootstrap](http://getbootstrap.com/) template to help Insight fellows get started building their web application.
If you are new to Flask and/or web development, take a look at the
[resources](https://github.com/stormpython/insightfl#resources) below.

To get started building your web app, follow the instructions below to setup your development environment.

**Note**: This assumes you are comfortable with the Terminal and have some familiarity with Unix/Linux commands. If this
is not the case, take a look at this [guide](http://www.ee.surrey.ac.uk/Teaching/Unix/).

### Getting Started <a name="getting-started"></a>
#### System Requirements <a name="system-requirements"></a>
1. [Python](https://www.python.org/downloads/)(v2.7+) with [pip](http://pip.readthedocs.org/en/latest/installing.html) installed.

#### Setup <a name="environment-setup"></a>
1. [Fork](https://github.com/stormpython/insightfl/fork) the project and clone the repository.

  **Note:** It is helpful to change the repository name **before** cloning. In Github, click on `Settings` on the right-hand
  side of your screen. Within the Settings box at the top of the screen, rename the repository and click `Rename`.

  ```
  git clone git@github.com:<username>/<project>.git
  ```

2. **Recommended:** Install virtualenv and fire up a virtual environment.

  ```
  # cd into your InsightFL project folder
  # Install virtualenv
  sudo pip install virtualenv

  # Create virtualenv folder `venv`
  virtualenv venv

  # Activate the virtual environment
  source venv/bin/activate
  ```

3. Install Python project dependencies.

  ```
  pip install -r requirements.txt
  ```

4. To test your application, run the manage.py file: `python manage.py runserver`, and open your web browser to
`localhost:5000`.

![Home Page](https://dl.dropboxusercontent.com/u/30620269/insightfl.png)

That's it! You are ready to start building your web application.

**Note**: *`manage.py` uses the builtin server for development. You should not use the builtin development server
in production (i.e. when you're launching your web application). To run in production, use `gunicorn manage:app` at
the command line.*

### Application Structure
#### Philosophy
InsightFL's project layout mimics that of large Flask applications. This is done intentionally. Despite the
fact that most Insight projects are small applications, utilizing this structure allows you to separate your development 
concerns more effectively. Instead of having all your web app code in one file, it can be broken up into separate, 
smaller chunks, which makes for cleaner code and easier debugging.

#### Project Layout
- **[app](app)** - Where your Flask web application lives. This is where you'll spend the majority of your time
- **.gitignore** - [Git ignore file](https://help.github.com/articles/ignoring-files)
- **config.py** - Project configuration file for storing sensitive or dynamic settings, e.g. database settings 
- **LICENSE.md** - Project license
- **manage.py** - Entry point to your Flask application during development, click [here](http://flask-script.readthedocs.org/en/latest/) for more info.
- **README.md** - You're looking at it! :)
- **requirements.txt** - Tracks all your Python dependencies using [pip](http://pip.readthedocs.org/en/latest/user_guide.html#requirements-files)
- **schema.sql** - Your SQL database schemas

### Resources
1. **Documentation**
    - [Flask QuickStart](http://flask.pocoo.org/docs/0.10/quickstart/#a-minimal-application)
    - [Flask, pip, and virtualenv](http://flask.pocoo.org/docs/0.10/installation/)
    - [Getting started with pip](http://pip.readthedocs.org/en/latest/user_guide.html)
    - [Setup Git](https://help.github.com/articles/set-up-git)

2. **Interactive Tutorials**
    - [Learning HTML, CSS](http://www.codecademy.com/tracks/web)
    - [Learning jQuery](http://www.codecademy.com/tracks/jquery)
    - [Learning Python](http://www.codecademy.com/tracks/python)
    - [Learning Git](https://try.github.io/levels/1/challenges/1)

3. **Books**
    - [Flask](http://www.amazon.com/Flask-Web-Development-Developing-Applications/dp/1449372627/ref=sr_1_1?s=books&ie=UTF8&qid=1411598577&sr=1-1&keywords=flask)
    - [MySQL](http://www.amazon.com/MySQL-Crash-Course-Ben-Forta/dp/0672327120/ref=sr_1_5?s=books&ie=UTF8&qid=1411598459&sr=1-5&keywords=mysql)
