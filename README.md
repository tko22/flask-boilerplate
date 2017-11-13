# Flask Boilerplate

Restful API using Flask <br>
Dependencies:
- Python 3.x
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
