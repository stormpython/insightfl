# Imports
from flask import Flask, request, redirect, url_for, \
    render_template
import mysqldb

# Creates our application
app = Flask(__name__)

# CONFIGURATION SETTINGS
################################################################################
# Development settings - these are settings you'll use while developing
# your app.
# These settings should not be used in production.
app.config.from_object('settings')

# You will need to set the following env variable for production settings.
# Run the following command in the terminal:
# export PROD_CONFIG="/home/stormpython/myapp/prod_settings.py"
app.config.from_envvar('PROD_CONFIG', silent=True)
################################################################################

# ROUTING/VIEW FUNCTIONS
################################################################################
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
################################################################################

#
if __name__ == '__main__':
    app.run()
