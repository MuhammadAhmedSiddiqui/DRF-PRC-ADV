FROM python:3.7-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create and activate virtual environment
RUN python3 -m venv rapid_env

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .temp-build-deps \
     gcc libc-dev linux-headers postgresql-dev
RUN /rapid_env/bin/pip install -r requirements.txt

RUN mkdir /src
RUN mkdir /src/app
WORKDIR /src/app
COPY ./src/app /src/app

EXPOSE 8000


RUN adduser -D applicationuser
USER applicationuser

