from flask import Blueprint
from api.models import Person
from api.utils import create_response, serialize_list
from api.core import logger

main = Blueprint("main", __name__)


# function that is called when you visit /
@main.route("/")
def index():
    # access the logger with the logger from api.core and uses the standard logging module
    logger.info("Hello World!")
    return "<h1>Hello World!</h1>"


# function that is called when you visit /persons
@main.route("/persons")
def name():
    persons = Person.query.all()
    return create_response(data={"persons": serialize_list(persons)})
