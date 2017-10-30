# NBB Map Board 

Restful API using Flask <br>
Dependencies:
- Python 3.*
- pip 9.0
- PostgreSQL – for MacOS, [postgresapp](http://postgresapp.com/) is a very simple one. <br>

## Setup 
If your developing with Windows, ¯\_(ツ)_/¯ <br>
Always remember to be use the same virtual environement. This is a really good practice for any python development. <br>
First, install virtualenv, create and activate the environment called **venv**, and install the python package dependencies:
```
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
To deactivate when you're using it:
```
$ deactivate venv
```
After installing Postgres, in your CLI create a user and database and grant privileges:
```
$ psql
$ create user nbb with password 'password';
$ create database nbb_db owner nbb encoding 'utf-8';
GRANT ALL PRIVILEGES ON DATABASE nbb_db TO nbb;
```


## Run Development Server
To run the server, make sure you are in the root directory:
```
python run.py
```

The API should be at http://127.0.0.1:5000/ for you to experience its beauty LOL 

## Conventions
- **Controllers**, which describe API endpoints will be defined under ``api/views/*``. We will be using [Flask Blueprints](http://flask.pocoo.org/docs/0.12/blueprints/) for easier collaborations in view controllers. Be sure to know how to use them. <br>
- The **Database** Structure will be defined under ``api/models.py``

## MISC

If you're annoyed by the __pycache__ files 
```
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
```

Feel free to contact me for questions :) 
