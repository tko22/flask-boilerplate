# Database Interactions
This doc was written before Docker was implemented in. Check out the <a href="./docker.md">Docker doc<a> before looking through this. 
## Caveats
* If you are using Docker, always remember to be in the correct container before running these commands
* If you are in the regular setup, always remember to be in your virtual environment
## SQLAlchemy Examples
Here are some ways to use SQLAlchemy to query, add, and delete from your database. <br>
Note: this example is specific to what is initially described in ```models.py```

– A Table called Person with an attribute called "name"(String) and one-to-many relationship to the table Emails. Another Table called Email has an attribute called "email"(String) and a Foreign Key to Person. 
```python
# import Person and db
>>> from api.models import Person, Email
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

# Relationships
# In our current schema, we see that a Person has an attribute "emails".
# This is represented by a python list, which would be initially empty
>>> email1 = Email(email="tim@gmail.com") # create an Email
>>> email2 = Email(email="tim.ko@gmail.com")
>>> p = Person.query.get(2) # query the person who has the email
>>> p.emails.append(email1) # add the email to that person 
# Note: You must add an Email object
>>> p.emails.append(email2)
>>> p.emails
[<email tim@gmail.com>,<email tim.ko@gmail.com>]
```
### Adding Dummy data 
Eventually, you would want to make POST requests to certain endpoints that would add entries to the database. You can add dummy data through the python CLI. Make sure you're in the right virtualenv. <br> 

**Note:** For Docker, go into the ```app``` container with ```docker-compose exec app bash``` beforehand.
```
$ python
```
You will be at the head directory. Import the Objects you need from ```models.py``` and your database
```python
>>> from api.models import Person, Email
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
You can also write scripts to do this. Or you can also write scripts in the frontend, where you will make POST requests to your "adding resources" endpoint


## Database Schema Changes
The Database Schema is described in ```models.py```. For any changes you make, you MUST let everyone know about it. First, create migration files for your changes:<br> 

**Note:** For Docker, be sure to be inside the ```app``` container with ```docker-compose exec app bash``` beforehand.<br>
For regular setup, make sure you're in the right virtualenv.
```
$ python manage.py db migrate 
```
This will be reflected in ```/migrations```. Then, upgrade the database and let everyone know to do to.
```
$ python manage.py db upgrade
```
Everyone will have to follow this same process whenever someone pushes new changes to ```models.py```. Migration files will not be pushed into the main repo due to versioning complaints. <br>
### Versioning errors
If you are getting errors when you migrate, remove the migrations folder, go into the postgres CLI, connect to the database, and Drop the ```alembic_version``` table.<br>

**Note:** For Docker, make sure to be inside the ```app``` container with ```docker-compose exec app bash``` beforehand.
```
$ rm -rf migrations/
$ exit
```
Now, for Docker, access bash for the ```postgres``` container to edit the database. Skip if you aren't using Docker
```
$ docker-compose exec postgres bash
# su - postgres
```
Then, for both Docker and Regular setup,
```
$ psql
# \connect testdb
# DROP TABLE alembic_version;
# \q
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
```
### Random errors
Sometimes you might run into weird errors. Since you most likely will run into these errors in the beginning(when your schema keeps changing) and, thus, will not have important data inside your database, you can just delete the database and start all over.<br>

**Note:** For docker, you must be in the ```postgres``` container
```
$ psql
# DROP DATABASE testdb;
# create database testdb owner testusr encoding 'utf-8';
# GRANT ALL PRIVILEGES ON DATABASE testdb TO testusr;
# \q
```
Another way that might works is(for docker, you must be in the ```app``` container:
```
$ python manage.py recreate_db
```
