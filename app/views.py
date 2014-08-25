from flask import render_template
from app import app, host, port, user, passwd, db
from app.helpers.database import con_db

# To create a database connection, add the following
# within your view functions:
con = con_db(host, port, user, passwd, db)


# ROUTING/VIEW FUNCTIONS
@app.route('/')
@app.route('/index')
def index():
    # Renders index.html.
    return render_template('index.html')


@app.route('/presentation')
def about():
    # Renders presentation.html.
    return render_template('presentation.html')


@app.route('/author')
def contact():
    # Renders author.html.
    return render_template('author.html')
