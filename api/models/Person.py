from api.core import Mixin
from .base import db


class Person(Mixin, db.Model):
    """Person Table."""

    __tablename__ = "person"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String, nullable=False)
    emails = db.relationship("Email", backref="emails")

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"<Person {self.name}>"
