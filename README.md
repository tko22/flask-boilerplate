# Flask Boilerplate 
This Boilerplate is meant for building out simple REST APIs deployed using Heroku and developed using Docker containers. This app is written in Python 3.6 with Postgres 10 as the chosen data persistance. You can deploy it with another service, like AWS, Google Cloud, and DigitalOcean with Gunicorn and Nginx, but instructions for that are not provided. Included are simple examples to help you get started. For development, the default way is to use Docker for ease of setup. However, there is documentation for setup without docker <a href='./docs/regular-setup.md'>here.</a> I've also written a <a href="https://medium.freecodecamp.org/docker-development-workflow-a-guide-with-flask-and-postgres-db1a1843044a">blog post</a> about using Docker based on this repository.<br> 

## Docs
Please Please **PLEASE** read documentation if you dont understand something
- <a href='./docs/conventions.md'>Conventions</a>
- <a href='./docs/databases.md'>Database Interactions & Troubleshooting</a>
- <a href='./docs/heroku.md'>Heroku Deployment</a>
- <a href='./docs/docker.md'>Docker</a>
- <a href='./docs/regular-setup.md'>Regular setup if you hate Docker</a>

### Repository Contents
* ```api/views/``` - Holds files that define your endpoints
* ```api/models.py``` - Defines your database schema
* ```api/__init__.py``` - What is initially ran when you start your application
* ```tests/``` - Folder holding tests
#### Others
* ```config.py``` - Provides Configuration for the application. There are two configurations: one for development and one for production using Heroku. 
* ```manage.py``` - Command line interface that allows you to perform common functions with a command
* ```requirements.txt``` - A list of python package dependencies the application requires
* ```runtime.txt``` & ```Procfile``` - configuration for Heroku
* ```Dockerfile``` - instructions for Docker to build the Flask app
* ```docker-compose.yml``` - config to setup this Flask app and a Database
* ```postgres-data/``` - Postgres Docker Container data - doesnt exist until you build your docker images and start your containers
* ```migrations/``` - Holds migration files – doesn't exist until you ```python manage.py db init``` if you decide to not use docker

## Prereqs
We will be utilizing Docker to provide the same development environment across your team. This will eliminate aggravating environment troubleshooting in different Operating Systems. We will not be using Docker in production since deployment using Heroku is easier. Check out this <a href="https://medium.freecodecamp.org/docker-development-workflow-a-guide-with-flask-and-postgres-db1a1843044a">blog post</a> I wrote for more information.
- [Docker](https://docs.docker.com/engine/installation/#time-based-release-schedule) – if you are running Linux, install the Server version and install [Docker-Compose](https://docs.docker.com/compose/install/#install-compose).
And that's it! For Mac, you will see a Docker icon on the top bar, indicating that docker is running.
## Our Docker Configuration
We have two Docker Images: 
* ```app```: Our Flask Application
* ```postgres```: Postgres Database<br>

## Setup
First, clone the repo:
```
git clone https://github.com/tko22/flask-boilerplate.git
```
Check if you have installed **Docker** and **Docker-Compose**(Installing [Docker](https://docs.docker.com/engine/installation/#time-based-release-schedule) on Mac/Windows will automatically install Docker-Compose):
```
$ docker -v
Docker version 17.09.1-ce, build 19e2cf6
$ docker-compose -v
docker-compose version 1.17.1, build 6d101fb
```
If it doesn't work, try resetting your shell:
```
$ reset
```
Now build the Docker images(the flask app and postgres database) and setup the database:
```
$ docker-compose build
$ docker-compose up -d
$ docker-compose exec app python manage.py recreate_db
```
Check if your Docker Containers are running:
```
$ docker ps
```
Now go to http://localhost:5000/ and you should see the app running! Since it is in development configurations, any changes in your code will appear in the container and will auto-reload just like it would normally. ```docker-compose up -d``` will build and start it. You will not be using that to start the container after this setup step. Look at the next section for instructions. <br> 
Now stop the container:
``` 
$ docker-compose stop
```
#### Note: A new directory called ```postgres-data``` will be created. **DO NOT DELETE IT!!** It holds all your data in your database.
## Running and Stopping Docker Containers - these are the instructions you run after the Setup!
To start your Postgres and your flask api:
```
$ docker-compose start
```
To stop them:
``` 
$ docker-compose stop
```
To view your logs for the api:
```
$ docker-compose logs app
```
If you need to rebuild your containers, delete the previous containers and rebuild
```
$ docker-compose rm -f
$ docker-compose up -d
```
#### NOTE: Be careful to not run multiple containers of the same image. Check with ```docker ps``` and use ```docker-compose stop``` to stop all the containers if you are running multiple containers and then restart with ```docker-compose start```. 
## MISC
If you would prefer to setup your application environment instead of using Docker, follow this doc - <a href='./docs/regular-setup.md'>Regular Setup</a>
If you're annoyed by the __pycache__ files 
```
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
```
### Additional Documentation
* [Flask](http://flask.pocoo.org/) - Flask Documentation 
* [Flask SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) - the ORM for the database
* [Heroku](https://devcenter.heroku.com/articles/getting-started-with-python#introduction) - Deployment using Heroku
* [Learn Python](https://www.learnpython.org/) - Learning Python3
* [Relational Databases](https://www.ntu.edu.sg/home/ehchua/programming/sql/Relational_Database_Design.html) - Designing a database schema
* [REST API](http://www.restapitutorial.com/lessons/restquicktips.html) - tips on making an API Restful
* [Docker Docs](https://docs.docker.com/get-started/) - Docker docs

Feel free to contact me for questions :) <br>
tk2@illinois.edu
