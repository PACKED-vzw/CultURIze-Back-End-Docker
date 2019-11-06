FROM python:3.8

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# pip install
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

# create unprivileged user (celery)
RUN adduser --disabled-password --gecos '' myuser
