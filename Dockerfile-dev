# Our docker-compose file uses Dockerfile-dev instead of Dockerfile
FROM python:3.7
LABEL maintainer "Timothy Ko <tk2@illinois.edu>"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

ENV FLASK_ENV=docker
EXPOSE 5000