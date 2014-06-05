from flask import render_template
from app import app, host, port, user, passwd, db
from app.helpers.database import con_db


# To create a database connection, add the following
# within your view functions:
# con = con_db(host, port, user, passwd, db)


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

@app.route('/slides')
def about():
    # Renders slides.html.
    return render_template('slides.html')

@app.route('/author')
def contact():
    # Renders author.html.
    return render_template('author.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
