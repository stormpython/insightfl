from app import app
import logging
from logging.handlers import SMTPHandler

# Production configuration settings
app.config.from_pyfile('settings/production.cfg')

# Error emails
admins = app.config["ADMINS"]
mail_handler = SMTPHandler('127.0.0.1',
                           'server-error@example.com',
                           admins, 'YourApplication Failed')
mail_handler.setLevel(logging.ERROR)
app.logger.addHandler(mail_handler)

app.run(debug=False)