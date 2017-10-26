from api import app
from flask import Blueprint, request

mod = Blueprint('main',__name__)

 
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

