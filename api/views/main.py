from api import app
from flask import Blueprint, request
from api.models import Person
import json
from flask import jsonify
import utils

mod = Blueprint('main', __name__)

# function that is called when you visit /
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

# function that is called when you visit /persons
@app.route('/persons')
def name():
    return jsonify({'Status':'Success','Data':Person.query.all()}) # returns all elements in Person