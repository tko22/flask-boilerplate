FROM python:3.6
LABEL maintainer "Timothy Ko <tk2@illinois.edu>"

RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install pipenv
RUN pipenv install --system
# RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000