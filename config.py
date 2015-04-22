import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('APP_SECRET')
    ROOT_DIR = os.environ.get('ROOT_DIR')

    @staticmethod
    def init_app(app):
        pass


class TestingConfig(Config):
    TESTING = True
    MONGODB_SETTINGS = {
        "DB": 'testing',
        "USERNAME": '',
        "PASSWORD": '',
        "HOST": 'localhost',
        "PORT": 27017
    }


class DevelopmentConfig(Config):
    ROOT_DIR = os.environ.get('ROOT_DIR')
    DEBUG = True
    # MONGODB_DB = os.environ.get('MONGODB_DEV_DATABASE')
    # MONGODB_USERNAME = os.environ.get('MONGODB_DEV_USER')
    # MONGODB_PASSWORD = os.environ.get('MONGODB_DEV_PASSWORD')
    # MONGODB_HOST = os.environ.get('MONGODB_DEV_HOST')
    # MONGODB_PORT = int(os.environ.get('MONGODB_DEV_PORT'))
    MONGODB_SETTINGS = {
        "db": os.environ.get('MONGODB_DEV_DATABASE'),
        "username": os.environ.get('MONGODB_DEV_USER'),
        "password": os.environ.get('MONGODB_DEV_PASSWORD'),
        "host": os.environ.get('MONGODB_DEV_HOST'),
        "port": int(os.environ.get('MONGODB_DEV_PORT'))
    }

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
    'testing': TestingConfig
}
