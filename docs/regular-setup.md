# Regular Setup 
This option should be secondary to the <a href='./docs/docker.md'>Docker</a> setup. 
### Pre-requisites:
- Python 3.x
- pip 9.0

For installations for Mac, [here](https://github.com/hack4impact-uiuc/wiki/wiki/Mac-Setup) are the steps for that.

Note: This doesn't have authentication yet. Coming soon! <br>
#### If your developing with Windows, ¯\\_(ツ)_/¯  Check out the <a href='./WSL-setup.md'>Windows setup Doc</a>

## Mac
If you have a Mac, run this script and everything should be setup. 
```
$ ./mac_setup.sh
```
## Running Development Server
To run the server, make sure you are in the root directory. Then, startup the virtual environment and run the server:
```
$ pipenv shell  # startup virtual environment
(flask-boilerplate-_rcP-Rlt) bash-3.2$ python manage.py runserver
```
If you are using pipenv, you may also run commands without being inside your virtual environment:
```
$ pipenv run python manage.py runserver # pipenv run [command]
```
The API should be at http://127.0.0.1:5000/ for you to experience its beauty LOL

## Step-by-Step Instructions
If you prefer to go through step-by-step instructions to understand what's going on, you're at the right place!

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
This should start your postgres server:
```
$ brew services start postgresql
```
To stop:
```
$ brew services stop postgresql
```
On a separate CLI, check whether you can access the database. Your postgres server must be on in order for this to work:
```
$ createdb
$ psql -h localhost
# \q
```
After installing Postgres, create a user(with name 'testusr' and password 'password') and a database called 'testdb' then grant privileges. We will do this in your CLI:
```
$ psql
# create user testusr with password 'password';
# create database testdb owner testusr encoding 'utf-8';
# GRANT ALL PRIVILEGES ON DATABASE testdb TO testusr;
```
Note: Please replace the user name and password and database name to what you want in your own application. You must change those configurations in ```config.py``` and in ```.env```

We will be using [pipenv](https://docs.pipenv.org/), the officially recommended Python packaging tool from [Python](https://packaging.python.org/tutorials/managing-dependencies/#managing-dependencies). If prefer to use `pip` instead of `pipenv`, look below for instructions. Pipenv is very similar to npm and yarn in Javascript and it automatically creates/manages a virtualenv while adding/removing packages from your `Pipfile`. It also manages and autoloads environment variables and in general, helps developers setup a working environment. 

First, install pipenv. If you are on MacOS, use homebrew:
```
brew install pipenv
```
If you're using Linux or Windows, I'd just use pip:
```
pip install pipenv
```

Then, setup pipenv for flask-boilerplate:
```
pipenv --python 3.6
```
That's it! All your dependencies will be installed in your virtualenv. Virtualenv is a tool to create isolated Python environments, which will prevent dependency conflicts with your python projects.

To start your virtualenv, run:
```
pipenv shell
```
Now, any python command you run will be ran inside this virtual environment. You should get something that looks like this:
```
(flask-boilerplate-_rcP-Rlt) bash-3.2 $
```
To deactivate, type `exit`:
```
(flask-boilerplate-_rcP-Rlt) bash-3.2 $ exit
```
For more instructions, see the [official documentation](https://docs.pipenv.org) for pipenv.
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
If you are using pip, your command line will have `(venv)$` in front instead of the `(flask......) bash-3.2$` Now look above for instructions to run the server.
