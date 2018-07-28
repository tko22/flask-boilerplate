import os
import logging

from flask import Flask, request
from flask_cors import CORS
from flask_migrate import Migrate
from sqlalchemy_utils import create_database, database_exists

from api.config import config
from api.core import all_exception_handler


class RequestFormatter(logging.Formatter):
    def format(self, record):
        record.url = request.url
        record.remote_addr = request.remote_addr
        return super().format(record)


def create_app(test_config=None):
    app = Flask(__name__)

    CORS(app)  # add CORS
    if test_config:
        app.config.from_mapping(**test_config)
    else:
        # check environment variables to see which config to load
        env = os.environ.get("FLASK_ENV", "dev")
        app.config.from_object(config[env])

    # decide whether to create database
    if env != "prod":
        db_url = config[env].SQLALCHEMY_DATABASE_URI
        if not database_exists(db_url):
            print("Database doesn't exist. Creating now...")
            create_database(db_url)

    # register sqlalchemy to this app
    from api.models import db

    db.init_app(app)
    Migrate(app, db)

    # logging
    formatter = RequestFormatter(
        "%(asctime)s %(remote_addr)s: requested %(url)s: %(levelname)s in [%(module)s: %(lineno)d]: %(message)s"
    )
    fh = logging.FileHandler(app.config["LOG_FILE"])
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)

    strm = logging.StreamHandler()
    strm.setLevel(logging.DEBUG)
    strm.setFormatter(formatter)

    app.logger.addHandler(fh)
    app.logger.addHandler(strm)
    app.logger.setLevel(logging.DEBUG)

    # import and register blueprints
    from api.views import main

    app.register_blueprint(main.main)

    # register error Handler
    app.register_error_handler(Exception, all_exception_handler)

    return app
