# imports
from flask import Flask

# Creates our application.
app = Flask(__name__)

# Development configuration settings
app.config.from_pyfile('settings/development.cfg')

# Sends an error email to admins upon errors in production
admins = app.config["ADMINS"]

if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    mail_handler = SMTPHandler('127.0.0.1',
                               'server-error@example.com',
                               admins, 'YourApplication Failed')
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)

from app import views
