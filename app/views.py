from flask import render_template
from app import app


# ROUTING/VIEW FUNCTIONS
@app.route('/')
@app.route('/index')
def index():
    # Renders index.html.
    return render_template('index.html')

@app.route('/author')
def author():
    # Renders author.html.
    return render_template('author.html')
