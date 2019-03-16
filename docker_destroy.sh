#!/bin/bash

docker_ps_out=$(docker ps | grep 'postgres')
read -ra docker_args <<< $docker_ps_out
docker_id=${docker_args[0]}
docker stop $docker_id
docker container rm $docker_id
docker volume rm flask-app-db
