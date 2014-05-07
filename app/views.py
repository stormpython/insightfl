from flask import render_template
from app import app
from app.helpers.database import con_db

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
# cur = con.cursor()
################################################################################


# ROUTING/VIEW FUNCTIONS
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

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
