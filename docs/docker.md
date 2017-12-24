# Docker Setup
We will be using Docker to provide the same development environment across the team and eliminate aggravating environment troubleshooting in different OS. 
## Prereqs
- Install [Docker](https://docs.docker.com/engine/installation/#time-based-release-schedule)–if you are running Linux, install the Server version and install [Docker-Compose](https://docs.docker.com/compose/install/#install-compose)
That's it!
## Setup
Check if you have installed Docker and Docker-Compose(Installing Docker on Mac/Windows will automatically install Docker-Compose)
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
$ docker-compose exec api python manage.py recreate_db
```
```
Stop the API and Postgres Containers
```
docker-compose stop
```
List all Containers
```
docker ps
```
Stop all Containers
```
docker stop $(docker ps -a)
```
Remove all images
```
docker rmi $(docker images -q)
```
Bash in a certain container, ie: ```api```
```
docker-compose run api bash
```
You can also run bash if you have the container's id. To get a container's id, do ```docker ps```
```
docker exec -it [CONTAINER_ID] /bin/bash
```
Or run a specific bash command, id: ```ls```
```
docker exec -it [CONTAINER_ID] ls
```
Docker Images, what you get when you ```docker-compose build``` are snapshots of your code at that certain time
Docker Containers are .....



