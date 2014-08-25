import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    DATABASE_HOST = 'localhost'
    DATABASE_PORT = 3306
    DATABASE_USER = None
    DATABASE_PASSWORD = None
    DATABASE_DB = None
    DATABASE_CHARSET = 'utf8'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
