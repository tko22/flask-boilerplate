import configparser
import logging
from typing import Tuple, List

from werkzeug.local import LocalProxy
from flask import current_app, jsonify
from flask.wrappers import Response

# logger object for all views to use
logger = LocalProxy(lambda: current_app.logger)
core_logger = logging.getLogger("core")


class Mixin:
    """Utility Base Class for SQLAlchemy Models. 
    
    Adds `to_dict()` to easily serialize objects to dictionaries.
    """

    def to_dict(self) -> dict:
        d_out = dict((key, val) for key, val in self.__dict__.items())
        d_out.pop("_sa_instance_state", None)
        d_out["_id"] = d_out.pop("id", None)  # rename id key to interface with response
        return d_out


def create_response(
    data: dict = None, status: int = 200, message: str = ""
) -> Tuple[Response, int]:
    """Wraps response in a consistent format throughout the API.
    
    Format inspired by https://medium.com/@shazow/how-i-design-json-api-responses-71900f00f2db
    Modifications included:
    - make success a boolean since there's only 2 values
    - make message a single string since we will only use one message per response

    IMPORTANT: data must be a dictionary where:
    - the key is the name of the type of data
    - the value is the data itself

    :param data <str> optional data
    :param status <int> optional status code, defaults to 200
    :param message <str> optional message
    :returns tuple of Flask Response and int
    """
    if type(data) is not dict and data is not None:
        raise TypeError("Data should be a dictionary 😞")

    response = {"success": 200 <= status < 300, "message": message, "result": data}
    return jsonify(response), status


def serialize_list(items: List) -> List:
    """Serializes a list of SQLAlchemy Objects, exposing their attributes.
    
    :param items - List of Objects that inherit from Mixin
    :returns List of dictionaries
    """
    if not items or items is None:
        return []
    return [x.to_dict() for x in items]


# add specific Exception handlers before this, if needed
# More info at http://flask.pocoo.org/docs/1.0/patterns/apierrors/
def all_exception_handler(error: Exception) -> Tuple[Response, int]:
    """Catches and handles all exceptions, add more specific error Handlers.
    :param Exception
    :returns Tuple of a Flask Response and int
    """
    return create_response(message=str(error), status=500)


def get_pg_url(file: str = "creds.ini") -> str:
    """Gets Postgres URL including credentials from specified file.

    Example of File:
    ```
    [pg_creds]
    pg_url = postgresql://testusr:password@127.0.0.1:5432/testdb
    ```
    :param file name
    :returns str or None if exception failed
    """
    try:

        config = configparser.ConfigParser()
        config.read(file)

        mongo_section = config["pg_creds"]
        return mongo_section["pg_url"]
    except KeyError:
        print(
            f"Failed to retrieve postgres url. Check if {file} exists in the top directory and whether it follows the correct format. INGORE this message if you are not using {file} to store your credentials."
        )
        return None
