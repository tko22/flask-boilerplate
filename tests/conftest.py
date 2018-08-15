# conftest.py is used by pytest to share fixtures
# https://docs.pytest.org/en/latest/fixture.html#conftest-py-sharing-fixture-functions
import os
import tempfile
import time
from unittest import mock

import pytest
import sqlalchemy
from flask_migrate import Migrate

from api import create_app

SQLITE_FILE_PATH = f"{os.getcwd()}/test.db"


# testing using sqlite, which may
# not be the same as testing with
# postgres but for unit tests, this will do
@pytest.fixture(scope="session")
def client():
    config_dict = {
        "SQLALCHEMY_DATABASE_URI": f"sqlite:///{SQLITE_FILE_PATH}",
        "DEBUG": True,
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    }
    app = create_app(config_dict)
    app.app_context().push()

    # wait for sqlite file to be created
    time.sleep(2)
    from api.models import db

    db.create_all()
    # for test client api reference
    # http://flask.pocoo.org/docs/1.0/api/#test-client
    client = app.test_client()
    yield client

    # remove the file
    os.remove(SQLITE_FILE_PATH)
