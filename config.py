import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USER_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://kitsao:kitsao@localhost/myblog'

    DEBUG = True

class TestConfig(Config):
    '''
    child test configuration class
    '''
    pass

config_options = {
'development':DevConfig,
'production':ProdConfig,
 'test':TestConfig
}