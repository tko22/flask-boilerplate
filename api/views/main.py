from api import app
from flask import Blueprint, request
from api.models import Person
import json
from flask import jsonify

mod = Blueprint('main', __name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

# this doesnt work 
@app.route('/persons')
def name():
    return jsonify(Person.query.all())

