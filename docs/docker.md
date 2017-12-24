
docker-compose build
docker-compose up -d
docker-compose exec api python manage.py recreate_db

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



