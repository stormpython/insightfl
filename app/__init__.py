# imports
from flask import Flask

# Creates our application.
app = Flask(__name__)

# Development configuration settings
app.config.from_pyfile('settings/development.cfg')

from app import views
