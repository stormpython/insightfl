# imports
from app import app

# Production configuration settings
app.config.from_pyfile('settings/production.cfg')

app.run(debug=False)