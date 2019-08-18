import os


class Config:
    __basedir__ = os.path.abspath(os.path.dirname(__file__))
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(__basedir__, 'db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestConfig(Config):
    __basedir__ = os.path.abspath(os.path.dirname(__file__))
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///memory'


class ProdConfig(Config):
    __basedir__ = os.path.abspath(os.path.dirname(__file__))
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ''
