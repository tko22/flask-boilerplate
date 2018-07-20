from flask_sqlalchemy import SQLAlchemy
from api.utils import Mixin

# instantiate database object
db = SQLAlchemy()


class Person(Mixin, db.Model):
    """Person Table."""

    __tablename__ = "person"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String, nullable=False)
    emails = db.relationship("Email", backref="emails")

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return "<Person {}>".format(self.name)


class Email(Mixin, db.Model):
    """Email Table."""

    __tablename__ = "email"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    email = db.Column(db.String, nullable=False)
    person = db.Column(
        db.Integer, db.ForeignKey("person.id", ondelete="SET NULL"), nullable=True
    )

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return "<Email {}>".format(self.email)
