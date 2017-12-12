# Database Interactions
## SQLAlchemy Examples
Here are some ways to use SQLAlchemy to query, add, and delete from your database. <br>
Note: this example is specific to what is initially described in ```models.py```–A Table called Person with an attribute called "name"(String).
```python
# import Person and db
>>> from api.models import Person
>>> from api import db

# add a Person with name "Tim" and another with name "Tim2"– yes, I'm that narcissistic haha
>>> person1 = Person(name="Tim")
>>> person2 = Person(name="Tim2")
>>> db.session.add(person1)
>>> db.session.add(person2)
>>> db.session.commit()

# get Person with id 1
>>> person1 = Person.query.get(1)
>>> person1.name # person1 is a Python object so you can access its attributes like python class variables!
Tim

# get all Persons
>>> Person.query.all()
[<Person Tim>,<Person Tim2>] # this depends on how __repr__() is defined for Person, but it will be a list of Person

# filter based on certain attributes
>>> Person.query.filter(Person.name=="Tim") # returns list of Person that has a name "Tim"
[<Person Tim>]

# deleting a Person
>>> p = Person.query.get(1) # get the object you want to delete
>>> db.session.delete(obj   # delete it
>>> db.session.commit()        
>>> Person.query.all()
[<Person Tim2>]
# If you had any Foreign Keys linked to Person, you must set make sure to define whether you want
# it to cascade or SET NULL when you define your model

# Relationships – say there was an Email Table with a foreign key in Email with "email"(String) attribute
# that was linked to Person and Person had an attribute "emails = db.relationship('Email', backref='person')"
>>> email1 = Email(email="tim@gmail.com")
>>> email2 = Email(email="tim.ko@gmail.com")
>>> p = Person.query.get(2)
>>> p.emails.append(email1)
>>> p.emails.append(email2)
>>> p.emails
[<email tim@gmail.com>,<email tim.ko@gmail.com>]
```
### Adding Dummy data 
Eventually, you would want to make POST requests to certain endpoints that would add entries to the database. You can add dummy data through the python CLI. Make sure you're in the right virtualenv. 
```
(venv)$ python
```
You will be at the head directory. Import the Objects you need from ```models.py``` and your database
```python
>>> from api.models import Person
>>> from api import db
```
Then, make a new Person Object and add it to the database.
```python
>>> p = Person(name="Tim")
>>> db.session.add(p)
```
Once you add it, you need save(commit) the change
```python
>>> db.session.commit()
```


## Database Schema Changes
The Database Schema is described in ```models.py```. For any changes you make, you MUST let everyone know about it. First, create migration files for your changes:
```
$ python manage.py db migrate 
```
This will be reflected in ```/migrations```. Then, upgrade the database and let everyone know to do to.
```
$ python manage.py db upgrade
```
Everyone will have to follow this same process whenever someone pushes new changes to ```models.py```. Migration files will not be pushed into the main repo due to versioning complaints. <br>
### Versioning errors
If you are getting errors when you migrate, remove the migrations folder, go into the postgres CLI, connect to the database, and Drop the ```alembic_version``` table.
```
$ rm -rf migrations/
$ psql
# \connect nbb_db
# DROP TABLE alembic_version;
# \q
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
```