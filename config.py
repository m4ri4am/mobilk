import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'ay habal'
    SQLALCHEMY_DATABASE_URI = "postgresql:///mobilk"


class ProductionConfig(Config):
    DEBUG = False
    
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:5432@localhost:5432/mobilk'


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
