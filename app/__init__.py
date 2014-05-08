# imports
from flask import Flask
from app.helpers.database import con_db

# Creates our application.
app = Flask(__name__)

# Development configuration settings
app.config.from_pyfile('settings/development.cfg')

# DATABASE SETTINGS
host = app.config["DATABASE_HOST"]
port = app.config["DATABASE_PORT"]
user = app.config["DATABASE_USER"]
passwd = app.config["DATABASE_PASSWORD"]
db = app.config["DATABASE_DB"]

# Connect to database
con = con_db(host, port, user, passwd, db)

from app import views
