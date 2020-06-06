import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'ay habal'
    SQLALCHEMY_DATABASE_URI = "postgresql:///DbName"


class ProductionConfig(Config):
    DEBUG = False
    
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:passwprd@localhost:5432/DbName'


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
