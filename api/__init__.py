from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

CORS(app)
env = os.environ.get('FLASK_ENV', 'dev')
app.config.from_object(config[env])

db = SQLAlchemy(app)
db.create_all()

# import and register blueprints
from api.views import main
app.register_blueprint(main.mod)
