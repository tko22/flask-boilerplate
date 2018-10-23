FROM python:3.7-alpine as build
LABEL maintainer "Timothy Ko <tk2@illinois.edu>"

COPY Pipfile Pipfile.lock ./
RUN apk update && \
    apk add --virtual build-deps gcc musl-dev && \
    apk add postgresql-dev && \
    rm -rf /var/cache/apk/*

RUN pip install pipenv
RUN pipenv install --system

RUN apk del build-deps gcc musl-dev && pip uninstall -y pipenv
COPY . /app
WORKDIR /app
ENV FLASK_ENV=prod
EXPOSE 5000
ENTRYPOINT [ "gunicorn", "-b", "0.0.0.0:5000", "--log-level", "INFO", "manage:app" ]

# configured to deploy with zeit now