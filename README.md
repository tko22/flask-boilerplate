# Flask Boilerplate 
This is an minimal but opinionated boilerplate meant for building out simple REST APIs deployed with Heroku primarily used at [Hack4Impact UIUC](https://github.com/hack4impact-uiuc). This app is written in Python 3.6 with Postgres 10 as the chosen data persistance. You can deploy it with another service, like AWS, Google Cloud, or DigitalOcean with Gunicorn and Nginx, but instructions for that are not provided. Included are simple examples and instructions developing with or without Docker are provided. I've also written a <a href="https://medium.freecodecamp.org/docker-development-workflow-a-guide-with-flask-and-postgres-db1a1843044a">blog post</a> about using Docker based on this repository.<br> 

The goal of this boilerplate is to allow developers to quickly write their API structured to best practices while giving them flexibility to easily add/change features. Here are the problems this is trying to solve:
1. **Flask is too flexible.** With Flask, you can write your application in any structure you like, even in one file. There are also a lot of different tutorials and guides providing different instructions to setup a Flask app with a database, confusing many newcomers. This Boilerplate's structure is inspired by Django's structure and is based on the hitchiker's guide to Python and described below.

2. **Django and other Flask boilerplates are too heavy.** Sometimes, I don't need a fully featured admin portal with Redis and an Email manager nor do I need templates. Many APIs and applications require the use of a database though. Thus, I've chosen Postgres because it is a battle-tested and reliable database used in many companies and we know that 99% of applications can easily be designed to use SQL databases (especially the ones used at Hack4Impact).

3. **Other boilerplates don't provide enough instructions to setup everything.** This includes downloading and installing the databases, connecting them to Flask, etc.

![](../master/docs/flask.gif)

## Docs
Please Please **PLEASE** read documentation if you dont understand something
- <a href='./docs/conventions.md'>Conventions + Utility Functions/Classes</a>
- <a href='./docs/databases.md'>Database Interactions & Troubleshooting</a>
- <a href='./docs/heroku.md'>Heroku Deployment</a>
- <a href='./docs/docker.md'>Docker</a>
- <a href='./docs/WSL-setup.md'>Windows subsystem for Linux setup</a>
- <a href='./docs/regular-setup.md'>Regular setup</a>

### Repository Contents
* ```api/views/``` - Holds files that define your endpoints
* ```api/models.py``` - Defines your database schema
* ```api/__init__.py``` - What is initially ran when you start your application
* ```api/utils.py``` - utility functions and classes - explained [here](./docs/conventions.md)
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
