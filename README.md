# InsightFL
A basic template for building minimal web applications.

### Introduction
InsightFL is a basic [Flask](http://flask.pocoo.org/) template created specifically to help budding
data scientists in the [Insight Data Science](http://insightdatascience.com/) program get their web applications
off the ground quickly. As a former Insight fellow, I spent way too much time troubleshooting the ins and outs of
web development instead of focusing on what truly mattered, extracting insight from my data.

To get started building your web app, follow the instructions below to setup your development environment.

### Getting Started <a name="getting-started"></a>
#### System Requirements <a name="system-requirements"></a>
1. [Python](https://www.python.org/downloads/)(v2.7+) with [pip](http://pip.readthedocs.org/en/latest/installing.html) installed.

#### Setup <a name="environment-setup"></a>
1. Fork the [project](https://github.com/stormpython/insightfl/fork) and clone the repository.

  **Note:** It is helpful to change the repository name **before** cloning. In Github, click on `Settings` on the right-hand
  side of your screen. Within the Settings box at the top of the screen, rename the repository and click `Rename`.

  ```
  git clone git@github.com:<username>/<project>.git
  ```

2. **Recommended:** Install virtualenv and fire up a virtual environment.

  ```
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

That's it! You are ready to start coding your project.
