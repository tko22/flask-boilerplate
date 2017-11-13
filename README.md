# Flask Boilerplate

Restful API using Flask <br>
Dependencies:
- Python 3.6.x
- pip 9.0
- PostgreSQL 

## Setup 
If your developing with Windows, ¯\\_(ツ)_/¯ <br>
To install Postgres with Homebrew([postgresapp](http://postgresapp.com/) also works):
```
$ brew install postgresql
$ brew link postgresql
```
This should start your postgres server(Ctrl-C to stop):
```
$ postgres -D /usr/local/var/postgres
```
It should say ```listening on IPv6 address "::1", port 5432``` If not, change the port. On a separate CLI:
```
$ createdb
$ psql -h localhost
```
Always remember to use the same virtual environement!!!! This is a good practice for any python development. <br>
First, install virtualenv, create and activate the environment called **venv**, and install the python package dependencies:
```bash
$ pip3 install virtualenv
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
To deactivate when you're using it:
```
$ deactivate venv
```
After installing Postgres, in your CLI create a user named "testuser" and database and grant privileges:
```
$ psql
# create user testuser with password 'password';
# create database test_db owner nbb encoding 'utf-8';
# GRANT ALL PRIVILEGES ON DATABASE test_db TO testuser;
```

## Run Development Server
To run the server, make sure you are in the root directory:
```
python run.py
```
The API should be at http://127.0.0.1:5000/ for you to experience its beauty

## Database Schema Changes
The Database Schema is described in ```models.py```. For any changes you make, you need to let everyone know about it. 
You will need to intialize the configurations for migrations once:
```
$ python manage.py db init
```
Everytime you change the schema, create migration files for your changes:
```
$ python manage.py db migrate 
```
This will be reflected in ```/migrations```. Don't worry about what is added, but you must add and commit those files for everyone else to use. Then, upgrade the database and let everyone know to do to.
```
$ python manage.py db upgrade
```

## MISC
If you're annoyed by the __pycache__ files 
```
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
```

Feel free to contact me for questions :) 
