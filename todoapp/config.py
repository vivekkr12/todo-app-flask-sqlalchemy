import os


class Config:
    __basedir__ = os.getcwd()
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(__basedir__, 'db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///memory'


class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ''
