# Conventions
- **Controllers**, which describe API endpoints will be defined under ``api/views/*``. We will be using [Flask Blueprints](http://flask.pocoo.org/docs/0.12/blueprints/) for easier collaborations in view controllers. Be sure to know how to use them. <br>
... Blueprints simplify the application by splitting it under relevant components. To register a Blueprint, you must import it and register it under ```__init__.py```.
```
from api.views import main
app.register_blueprint(main.mod)
```
- The **Database** Structure will be defined under ``api/models.py``. Look at the Database Schema Section to know how to update your database. We are using [SQLAlchemy](http://docs.sqlalchemy.org/en/latest/) as our ORM, which allows us to create, query, and filter through the database easily. 