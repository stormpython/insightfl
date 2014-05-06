# imports
from flask import Flask

# Creates our application.
app = Flask(__name__)

# CONFIGURATION SETTINGS
# Development settings - settings you'll use while developing your app.
app.config.from_pyfile('settings/development.cfg')

from app import views
