from app import db
from sqlalchemy.dialects.postgresql import JSON
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# this doesn't work 
class PointsOfInterest(db.Model):
    """Points of Interest"""
    __tablename__ = "points_of_interests"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<name {}'.format(self.name)
