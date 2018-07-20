from typing import Tuple

from werkzeug.local import LocalProxy
from flask import current_app
from flask.wrappers import Response

from api.utils import create_response

# logger object for all views to use
logger = LocalProxy(lambda: current_app.logger)

# add specific Exception handlers before this, if needed
def all_exception_handler(error: Exception) -> Tuple[Response, int]:
    """Catches and handles all exceptions, add more specific error Handlers.
    :param Exception
    :returns Tuple of a Flask Response and int
    """
    return create_response(message=str(error), status=500)
