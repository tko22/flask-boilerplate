# Flask Boilerplate 
This Boilerplate meant for building out simple REST APIs meant to be deployed using Heroku. You can deploy it with anything else but instructions for that are not provided. Included are simple examples to help you get started. <br>

## Docs
<a href='./docs/conventions.md'>Conventions</a>
<a href='./docs/database.md'>Database Interactions & Troubleshooting</a>
<a href='./docs/git_flow.md'>Heroku Deployment</a>

### Repository Contents
* ```/api/views/``` - Holds files that define your endpoints
* ```/api/models.py``` - Defines your database schema
* ```/api/__init__.py``` - What is ran initially when you start your application
#### Others
* ```config.py``` - Provides Configuration for the application. There are two configurations: one for development and one for production using Heroku. 
* ```manage.py``` - Command line interface that allows you to perform common functions with a command
* ```requirements.txt``` - A list of python package dependencies the application requires
* ```runtime.txt``` & ```Procfile``` - configuration for Heroku

## Setup 
### Pre-requisites:
- Python 3.x
- pip 9.0
- PostgreSQL <br>
Note: This doesn't have authentication yet. Coming soon! <br>
#### If your developing with Windows, ¯\\_(ツ)_/¯ <br>
Clone the Repository and cd into it
```
$ git clone https://github.com/tko22/flask-boilerplate.git
$ cd flask-boilerplate
```
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
Always remember to use the ***same virtual environement***!!!! This is a good practice for any python development. <br>
First, install virtualenv, create and activate the environment called **venv**:
```bash
$ pip3 install virtualenv
$ virtualenv -p python3 venv
$ source venv/bin/activate
```
You will then have a ```(venv)``` before the ```$```, meaning that you are now in your virtual environment. Then, install the python package dependencies, which include Flask.
```
(venv)$ pip install -r requirements.txt
```
To deactivate when you're using it:
```
(venv)$ deactivate venv
```
After installing Postgres, create a user and a database then grant privileges. We will do this in your CLI:
```
$ psql
# create user nbb with password 'password';
# create database nbb_db owner nbb encoding 'utf-8';
# GRANT ALL PRIVILEGES ON DATABASE nbb_db TO nbb;
```
## Running Development Server
To run the server, make sure you are in the root directory:
```
(venv)$ python manage.py runserver
```
The API should be at http://127.0.0.1:5000/ for you to experience its beauty LOL 

## MISC

If you're annoyed by the __pycache__ files 
```
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
```

Feel free to contact me for questions :) 
tk2@illinois.edu
