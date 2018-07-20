from api import app
from flask import Blueprint
from api.models import Person
from api.utils import create_response, serialize_list

mod = Blueprint("main", __name__)


# function that is called when you visit /
@app.route("/")
def index():
    # access the logger with `app.logger` and uses the standard logging module
    app.logger.info("Hello World!")
    return "<h1>Hello World!</h1>"


# function that is called when you visit /persons
@app.route("/persons")
def name():
    persons = Person.query.all()
    persons_list = serialize_list(persons)

    return create_response(data={"persons": persons_list})
