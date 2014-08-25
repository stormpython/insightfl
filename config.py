import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    DATABASE_HOST = "localhost"
    DATABASE_PORT = 3306
    DATABASE_USER = "root"
    DATABASE_PASSWORD = os.environ.get('DB_PASSWORD') or 'youllneverguess'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_DB = ""

class ProductionConfig(Config):
    DEBUG = False
    DATABASE_DB = ""

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
