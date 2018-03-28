from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import config
import os
from sqlalchemy_utils import create_database, database_exists


app = Flask(__name__)

CORS(app)
env = os.environ.get('FLASK_ENV', 'dev')
app.config.from_object(config[env])

db = SQLAlchemy(app)
db_url = config[env].SQLALCHEMY_DATABASE_URI
if not database_exists(db_url):
    print("Database doesn't exist. Creating now...")
    create_database(db_url)
    db.create_all()
    db.session.commit()

# import and register blueprints
from api.views import main
app.register_blueprint(main.mod)
