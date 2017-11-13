from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from api import db, app
from api.models import Person

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)
@manager.command
def runserver():
    app.run(debug=True)
if __name__ == '__main__':
    manager.run()