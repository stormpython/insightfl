# imports
from flask import Flask, request, redirect, url_for, \
    render_template
from flaskext.mysql import MySQL

# Creates our application.
app = Flask(__name__)

# CONFIGURATION SETTINGS
################################################################################
# Development settings - these are settings you'll use while developing
# your app.
# These settings should not be used in production.
app.config.from_pyfile('settings/development.cfg')

# You will need to set the following env variable for production settings.
# Run the following command in the terminal:
# export PROD_CONFIG="/path/to/settings/production.cfg"
app.config.from_envvar('PROD_CONFIG', silent=True)
################################################################################

# INITIALIZE MYSQL EXTENSION
################################################################################
mysql = MySQL()
mysql.init_app(app)

# Obtain a cursor
# cursor = mysql.get_db().cursor()
################################################################################

# ROUTING/VIEW FUNCTIONS
################################################################################
@app.route('/')
def index():
    # Renders index.html.
    return render_template('index.html')

@app.route('/about')
def about():
    # Renders about.html.
    return render_template('about.html')

@app.route('/contact')
def contact():
    # Renders contact.html.
    return render_template('contact.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
################################################################################

# Runs the app.
if __name__ == '__main__':
    app.run()