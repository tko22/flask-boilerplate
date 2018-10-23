# this dockerfile is used for product deployments
FROM python:3.7-alpine
LABEL maintainer "Timothy Ko <tk2@illinois.edu>"

COPY Pipfile Pipfile.lock ./
RUN apk update && \
    apk add --virtual build-deps gcc musl-dev && \
    apk add postgresql-dev && \
    rm -rf /var/cache/apk/*

RUN pip install pipenv
RUN pipenv install --system

# delete dependencies required to install certain python packages 
# so the docker image size is low enough for Zeit now
RUN apk del build-deps gcc musl-dev && pip uninstall -y pipenv

COPY . /app
WORKDIR /app

# for the flask config
ENV FLASK_ENV=prod

EXPOSE 5000
ENTRYPOINT [ "gunicorn", "-b", "0.0.0.0:5000", "--log-level", "INFO", "manage:app" ]