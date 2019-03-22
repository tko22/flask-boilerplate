
mac_setup:
	./mac_setup

setup: start_dev_db
	pip3 install virtualenv
	virtualenv venv
	venv/bin/pip install -r requirements.txt -r requirements-dev.txt
	venv/bin/python manage.py recreate_db

run_server:
	venv/bin/python manage.py runserver

start_dev_db:
	echo "creating docker postgres DB"
	docker run -e POSTGRES_USER=testusr -e POSTGRES_PASSWORD=password -e POSTGRES_DB=testdb -p 5432:5432 -v flask-app-db:/var/lib/postgresql/data -d postgres:10

recreate_db:
	./scripts/docker_destroy.sh
	start_dev_db
	sleep 2
	venv/bin/python manage.py recreate_db


destroy:
	./scripts/docker_destroy.sh

up: 
	docker-compose up

compose_destroy:
	docker-compose stop
	docker-compose rm -f
	docker volume rm flask-app-db

make compose_start:
	docker-compose start

heroku_setup:
	python manage.py recreate_db
	