FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

RUN mkdir /src
RUN mkdir /src/app
WORKDIR /src/app
COPY ./src/app /src/app

RUN adduser -D applicationuser
USER applicationuser

