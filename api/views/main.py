from api import app
from flask import Blueprint, request
from api.models import PointsOfInterest

mod = Blueprint('main', __name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

# this doesnt work 
@app.route('/name')
def name():
    return PointsOfInterest.query.filter_by(id=id)

