import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "secret!")


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False
