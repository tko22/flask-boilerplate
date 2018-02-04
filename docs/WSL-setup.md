# Setup for Windows Subsystem for Linux
Some prerequisites:
- Python 3
- pip 9.0 (this should come with your Python 3 installation)

Clone the repository and cd into it:
```
$ git clone https://github.com/tko22/flask-boilerplate.git
$ cd flask-boilerplate
```

Download and install PostgreSQL 10 from [here](https://www.openscg.com/bigsql/postgresql/installers.jsp/). Leave the default settings checked, and you don't need to install any of the additional components. Remember the password you set for your postgres user account. 

In your shell, install the necessary packages:
```
$ sudo apt-get update
$ sudo apt-get install postgresql-client-common postgresql-client
```

Verify that your Postgres installation worked:
```
$ psql -p 5432 -h localhost -U postgres
```

You should see the Postgres shell after the above command, and it should look like this:
```
postgres=#
```

Create a user 'testusr' with password 'password', and a database 'testdb'. Then, grant privileges to the newly created user:
```
postgres=# CREATE USER testusr WITH PASSWORD 'password';
postgres=# CREATE DATABASE testdb WITH OWNER testusr ENCODING 'utf-8';
postgres=# GRANT ALL PRIVILEGES ON DATABASE testdb TO testusr;
```

To quit out of the Postgres CLI:
```
postgres=# \q
```

Although not required, creating a virtual environment is strongly recommended. Install virtualenv with pip if you don't already have it, and create your virtual environment. ```venv``` can be renamed to whatever you want your virtual environment to be named:
```
$ pip3 install virtualenv
$ virtualenv -p python3 venv
```

Activate your virtual environment and you should see ```(venv)``` appear before your commands to indicate that you are in your virtual environment. You can install the Python package dependencies after activation:
```
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Run the server with your virtual environment still activated:
```
$ python manage.py runserver
```

Visit the API at http://127.0.0.1:5000/ to bask in the glory of your hard work.

To deactivate your virtual environment, just do:
```
$ deactivate
```
