
DEBUG = False

SECRET_KEY = 'testkey'

POSTGRES = {
    'user': 'nbb',
    'pw': 'password',
    'db': 'nbb_db',
    'host': 'localhost',
    'port': '5432',
}

SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

SQLALCHEMY_TRACK_MODIFICATIONS = False