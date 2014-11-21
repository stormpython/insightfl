import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # Flask Application Key (optional)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    # MySQL Database Settings
    MYSQL_DATABASE_HOST = 'localhost'
    MYSQL_DATABASE_PORT = 3306
    MYSQL_DATABASE_USER = os.environ.get('MYSQL_DATABASE_USER') or None
    MYSQL_DATABASE_PASSWORD = os.environ.get('MYSQL_DATABASE_PASSWORD') or None
    MYSQL_DATABASE_DB = None
    MYSQL_DATABASE_CHARSET = 'utf8'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    # Add settings for development here.
    DEBUG = True


class ProductionConfig(Config):
    # Add settings for production here.
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
