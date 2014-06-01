# InsightFL
A basic template for building minimal web applications.

### Introduction
InsightFL is a basic [Flask](http://flask.pocoo.org/) template created specifically to help budding
data scientists in the [Insight Data Science](http://insightdatascience.com/) program get their web applications
off the ground quickly. As a former Insight fellow, I spent way too much time troubleshooting the ins and outs of
web development instead of focusing on what truly mattered, extracting insight from my data.

InsightFL comes with all the necessary tools you'll need to create your web app quickly:

  1. [Twitter Bootstrap](http://getbootstrap.com/) for designing your web pages.
  2. [Bower](http://bower.io/) to easily install third party libraries.
  3. [Reveal.js](http://lab.hakim.se/reveal-js/#/) for creating amazing presentations in HTML.
  4. And its already in version control from the [Git](http://git-scm.com/) go!

To get started building your web app, follow the instructions below to setup your development and production
environments.

### Getting Started <a name="getting-started"></a>
#### System Requirements <a name="system-requirements"></a>
1. [Python](https://www.python.org/downloads/)(v2.7+) with [pip](http://pip.readthedocs.org/en/latest/installing.html) installed.
2. [node](http://nodejs.org/)(v0.10.26+) - make sure to install the packages with [npm](https://www.npmjs.org/): Windows: *.msi*, MacOSX: *.pkg*

#### Dev Environment Setup <a name="environment-setup"></a>
1. Fork the [project](https://github.com/stormpython/insightfl/fork) and clone the repository.

  **Note:** It is helpful to change the repository name **before** cloning. In Github, click on `Settings` on the right-hand
  side of your screen. Within the Settings box at the top of the screen, rename the repository and click `Rename`.

  ```
  git clone git@github.com:<username>/<project>.git
  ```

2. Change into the project directory and install node project dependencies.

  ```
  cd /path/to/project/directory
  npm install
  ```

3. Install virtualenv and fire up a virtual environment.

  ```
  sudo pip install virtualenv
  virtualenv venv
  source venv/bin/activate
  ```

4. Install Python project dependencies.

  ```
  pip install -r requirements.txt
  ```

5. To test your application, run the server.py file: `python server.py`, and open your web browser to
`localhost:5000`.

That's it! You are ready to start coding your project.

### Deploying to AWS

*Note: the setup script assumes you are deploying to an Ubuntu **14.04** Server*

1. Secure copy the setup script (located in the deployment directory) to the remote host.

  ```
  scp -i mykey.pem /path/to/setup.sh ubuntu@ec2-12-345-67-89.us-west-2.compute.amazonaws.com:~
  ```

2. SSH into the remote host and run the setup script. Answer the questions when prompted and wait for
the downloads to finish.

  ```
  ssh -i mykey.pem ubuntu@ec2-12-345-67-89.us-west-2.compute.amazonaws.com
  source setup.sh
  ```

3. Open up a web browser and enter your public DNS: `ec2-12-345-67-89.us-west-2.compute.amazonaws.com`

That's it, you should now have a fully functioning web app!
