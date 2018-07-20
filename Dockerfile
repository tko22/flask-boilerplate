FROM python:3.7
LABEL maintainer "Timothy Ko <tk2@illinois.edu>"

RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install pipenv
RUN pipenv install --system

EXPOSE 5000