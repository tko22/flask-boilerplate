# NBB Map Board 

Restful API using Flask 
Dependencies:
- Python 3.*
- pip 9.0

## Setup 
If your developing with Windows, ¯\_(ツ)_/¯
Install PostgreSQL–for MacOS, [postgresapp](http://postgresapp.com/) is a very simple one.
Always remember to be use the same virtual environement. This is a really good practice for any python development. First, install virtualenv, create and activate the environment called **venv**, and install the python package dependencies:
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
After installing Postgres, in your CLI create a user and database:
```
$ psql
$ create user nbb with password 'password';
$ create database nbb_db owner nbb encoding 'utf-8';
```

To run the server, make sure you are in the root directory:
```
python app.py
```

Also, if you're annoyed by the __pycache__ files 
```
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
```

Feel free to contact me for questions :) tk2@illinois.edu
