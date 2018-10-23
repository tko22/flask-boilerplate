import os
from api.core import get_pg_url


class Config:
    SECRET_KEY = "testkey"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_FILE = "api.log"


class DevelopmentConfig(Config):
    url = (
        get_pg_url()
        if get_pg_url()
        else "postgresql://testusr:password@127.0.0.1:5432/testdb"  # TODO set the URI to get_pg_url() once you have `creds.ini` setup
    )
    SQLALCHEMY_DATABASE_URI = url
    DEBUG = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    )  # you may do the same as the development config
    DEBUG = False


class DockerDevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://testusr:password@postgres/testdb"
    DEBUG = True


config = {"dev": DevelopmentConfig, "prod": ProductionConfig, "docker": DockerDevConfig}
