# Regular Setup 
This option should be secondary to the <a href='./docs/docker.md'>Docker</a> setup. 
### Pre-requisites:
- Python 3.x
- pip 9.0

For installations for Mac, [here](https://github.com/hack4impact-uiuc/wiki/wiki/Mac-Setup) are the steps for that.
Note: This doesn't have authentication yet. Coming soon! <br>
#### If your developing with Windows, ¯\\_(ツ)_/¯ <br> Check out the <a href='./WSL-setup.md'>Windows setup Doc</a>
Clone the Repository and cd into it
```
$ git clone https://github.com/tko22/flask-boilerplate.git
$ cd flask-boilerplate
```
To install Postgres with Homebrew([postgresapp](http://postgresapp.com/) also works). If you are using linux, use your linux distributon's package manager to install postgres:
```
$ brew install postgresql
$ brew link postgresql
```
This should start your postgres server(Ctrl-C to stop):
```
$ postgres -D /usr/local/var/postgres
```
It should say ```listening on IPv6 address "::1", port 5432``` If not, change the port. On a separate CLI, check whether you can access the database. Your postgres server must be on in-order for this to work:
```
$ createdb
$ psql -h localhost
# \q
```
We will be using [pipenv](https://docs.pipenv.org/), the officially recommended Python packaging tool from [Python](https://packaging.python.org/tutorials/managing-dependencies/#managing-dependencies). If prefer to use `pip` instead of `pipenv`, look below for instructions. Pipenv is very similar to npm and yarn in Javascript and it automatically creates/manages a virtualenv while adding/removing packages from your `Pipfile`. It also manages and autoloads environment variables and in general, helps developers setup a working environment. 





### Using Pip
Using pip would require a little bit more steps, since you would have to use pip and virtualenv separately. In addition, managing `requirements.txt` can be a pain. For more benefits `pipenv` solves, look at their [documentation](https://docs.pipenv.org/). I'd recommend using Pipenv but if you still haven't changed your mind, here are the instructions. 

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
After installing Postgres, create a user(with name 'testusr' and password 'password') and a database called 'testdb' then grant privileges. We will do this in your CLI:
```
$ psql
# create user testusr with password 'password';
# create database testdb owner testusr encoding 'utf-8';
# GRANT ALL PRIVILEGES ON DATABASE testdb TO testusr;
```
Note: Please replace the user name and password and database name to what you want in your own application. You must change those configurations in ```config.py``` and in ```.env```
## Running Development Server
To run the server, make sure you are in the root directory:
```
(venv)$ python manage.py runserver
```
The API should be at http://127.0.0.1:5000/ for you to experience its beauty LOL 
