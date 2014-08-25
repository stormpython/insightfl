from . import main
from flask import render_template
#from main.helpers.database import con_db


# To create a database connection, add the following
# within your view functions:
# con = con_db(host, port, user, passwd, db)


# ROUTING/VIEW FUNCTIONS
@main.route('/')
@main.route('/index')
def index():
    # Renders index.html.
    return render_template('index.html')

@main.route('/presentation')
def about():
    # Renders presentation.html.
    return render_template('presentation.html')

@main.route('/author')
def contact():
    # Renders author.html.
    return render_template('author.html')
