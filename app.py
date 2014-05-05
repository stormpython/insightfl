# imports
from flask import Flask, request, redirect, url_for, render_template
from helpers.database import con_db

# Creates our application.
app = Flask(__name__)

# CONFIGURATION SETTINGS
################################################################################
# Development settings - settings you'll use while developing your app.
# These settings should not be used in production.
app.config.from_pyfile('settings/development.cfg')
################################################################################

# DATABASE SETTINGS
################################################################################
host = app.config["DATABASE_HOST"]
port = app.config["DATABASE_PORT"]
user = app.config["DATABASE_USER"]
passwd = app.config["DATABASE_PASSWORD"]
db = app.config["DATABASE_DB"]

# Connect to database
con = con_db(host, port, user, passwd, db)
# Fetch database cursor
cur = con.cursor()
################################################################################

# ROUTING/VIEW FUNCTIONS
################################################################################
@app.route('/')
@app.route('/index')
def index():
    # Renders index.html.
    return render_template('index.html')

@app.route('/home')
def home():
    # Renders home.html.
    return render_template('home.html')

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
    app.run(debug=True)
