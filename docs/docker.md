# Docker Setup
We will be utilizing Docker to provide the same development environment across your team. This will eliminate aggravating environment troubleshooting in different Operating Systems. We will not be using Docker in production since deployment using Heroku is easier.
## Prereqs
- [Docker](https://docs.docker.com/engine/installation/#time-based-release-schedule) – if you are running Linux, install the Server version and install [Docker-Compose](https://docs.docker.com/compose/install/#install-compose).
And that's it! For Mac, you will see a Docker icon on the top bar, indicating that docker is running. 
## Understanding Docker
Docker is a powerful tool that allows you to spin up containers(isolated and reproducible application environments), thus, allowing independence between applications and the infrastucture(ie your OS). 
For in-depth information, check out the [Docker Docs](https://docs.docker.com/get-started/)<br>
- **Docker Images**, what you get when you ```docker-compose build```. They are snapshots of your code at that certain time. This describes a container
- **Docker Containers** are instances of images. You can see the containers you are running with ```docker ps```
- **Docker Compose** is a tool for running multi-container applications with Docker. In our case, we use it to spin up ```app``` and ```postgres``` containers. 
## Our Docker Configuration
We have two Docker Images: 
- ```app```: Our Flask Application
- ```postgres```: Postgres Database<br>
Note: A new directory called ```postgres-data``` will be created. **DO NOT DELETE IT!!** It holds all your data in your database.
## Setup
Check if you have installed **Docker** and **Docker-Compose**(Installing Docker on Mac/Windows will automatically install Docker-Compose):
```
$ docker -v
Docker version 17.09.1-ce, build 19e2cf6
$ docker-compose -v
docker-compose version 1.17.1, build 6d101fb
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
Now go to ```http://localhost:5000``` and you should see the app running! Since it is in development configurations, any changes in your code will appear in the container and will auto-reload just like it would normally. 
## Running and Stopping Docker Containers
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
#### NOTE: Be careful to not run multiple containers of the same image. Check with ```docker ps``` and use ```docker-compose stop``` to stop all the containers if you are running multiple containers and restart. 
## Docker and Databases
Any commands, such as ```python manage.py db migrate``` **MUST** be performed inside the ```app``` Docker Container. If you need to access the postgres CLI, you MUST be inside the ```postgres``` Docker Container. <br>
#### Migrating the database
You must access the ```app``` container's bash. You will then see your app directory copied inside: 
```
$ docker-compose exec app bash
# ls
Dockerfile  Procfile   __pycache__  config.py		docs	   postgres-data     runtime.txt  venv
LICENSE     README.md  api	    docker-compose.yml	manage.py  requirements.txt  tests	  wait-for-postgres.sh
```
Then initalize migration files and migrate
```
# python manage.py db init
# python manage.py db migrate
# python manage.py db upgrade
# exit
```
#### Accessing Postgres CLI
You must access the ```postgres``` container's bash. 
```
$ docker-compose exec postgres bash
```
Then, you can ```psql``` inside and delete tables, databases, etc.
```
# su - postgres
$ psql
```

## Wiping all Docker Containers and Starting all over again
If you've given up trying to troubleshoot whatever is going wrong in Docker, here's a way to start all over. First, delete ```postgres-data```:
```
$ rm -rf postgres-data
```
Then delete all your related Docker Images and Containers
```
$ docker-compose stop
$ docker-compose rm
$ docker rmi $(docker images)
```
Now follow the setup steps again
## Common Docker commands
Stop the API and Postgres Containers
```
docker-compose stop
```
List all Containers:
```
$ docker ps
```
Stop all Containers:
```
$ docker stop $(docker ps -a)
```
Remove all images:
```
$ docker rmi $(docker images -q)
```
To get all images
```
$ docker images
```
Remove specific images:
```
$ docker rmi [IMAGE_ID]
```
Bash in a certain container, ie: ```api```
```
$ docker-compose run api bash
```
You can also run bash if you have the container's id. To get a container's id, do ```docker ps```
```
$ docker exec -it [CONTAINER_ID] /bin/bash
```
Or run a specific bash command, id: ```ls```
```
$ docker exec -it [CONTAINER_ID] ls
```
Remove 
- all stopped containers
- all volumes not used by at least one container
- all networks not used by at least one container
- all images without at least one container associated to them
```
$ docker system prune
```


