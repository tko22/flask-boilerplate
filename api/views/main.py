from flask import Blueprint, request
from api.models import db, Person, Email
from api.core import create_response, serialize_list, logger
from sqlalchemy import inspect

main = Blueprint("main", __name__)  # initialize blueprint


# function that is called when you visit /
@main.route("/")
def index():
    # you are now in the current application context with the main.route decorator
    # access the logger with the logger from api.core and uses the standard logging module
    # try using ipdb here :) you can inject yourself
    logger.info("Hello World!")
    return "<h1>Hello World!</h1>"


# function that is called when you visit /persons
@main.route("/persons", methods=["GET"])
def get_persons():
    persons = Person.query.all()
    return create_response(data={"persons": serialize_list(persons)})


# POST request for /persons
@main.route("/persons", methods=["POST"])
def create_person():
    data = request.get_json()

    logger.info("Data recieved: %s", data)
    if "name" not in data:
        msg = "No name provided for person."
        logger.info(msg)
        return create_response(status=422, message=msg)
    if "email" not in data:
        msg = "No email provided for person."
        logger.info(msg)
        return create_response(status=422, message=msg)

    # create SQLAlchemy Objects
    new_person = Person(name=data["name"])
    email = Email(email=data["email"])
    new_person.emails.append(email)

    # commit it to database
    db.session.add_all([new_person, email])
    db.session.commit()
    return create_response(
        message=f"Successfully created person {new_person.name} with id: {new_person._id}"
    )
