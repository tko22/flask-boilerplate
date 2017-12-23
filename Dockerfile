
FROM python:3.6
LABEL Name=flask-boilerplate Version=0.0.1 

LABEL maintainer "Timothy Ko <tk2@illinois.edu>"

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
EXPOSE 5000

ENTRYPOINT ["python", "manage.py", "runserver"]