import os


class Config:

    SECRET_KEY = 'testkey'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://testusr:password@127.0.0.1:5432/testdb'
    # SQLALCHEMY_DATABASE_URI = 'postgres://127.0.0.1:5432'
    DEBUG = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    DEBUG = False


class DockerDevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://testusr:password@postgres/testdb'
    DEBUG = True


config = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig,
    'docker': DockerDevConfig
}
