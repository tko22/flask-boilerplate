import os

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from sqlalchemy_utils import create_database, database_exists

from api.config import config
from api.core import all_exception_handler


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

    # import and register blueprints
    from api.views import main

    app.register_blueprint(main.main)

    # register error Handler
    app.register_error_handler(Exception, all_exception_handler)

    return app
