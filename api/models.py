from api import db
from sqlalchemy.dialects.postgresql import JSON
from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

class Person(db.Model):
    """Person"""
    __tablename__ = "person"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<name {}>'.format(self.name)
