from flask import Flask 
 
app = Flask(__name__)

POSTGRES = {
    'user': 'nbb',
    'pw': 'password',
    'db': 'nbb_db',
    'host': 'localhost',
    'port': '5432',
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

# import and register blueprints
from api.views import main
app.register_blueprint(main.mod)
