# imports
from flask import Flask
from config import config

def create_app(config_name):

    # Creates our application.
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # DATABASE SETTINGS
    host = app.config["DATABASE_HOST"]
    port = app.config["DATABASE_PORT"]
    user = app.config["DATABASE_USER"]
    passwd = app.config["DATABASE_PASSWORD"]
    db = app.config["DATABASE_DB"]

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
