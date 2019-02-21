FROM python:3.7

WORKDIR /app

ADD . /app

RUN python setup.py develop

EXPOSE 8500