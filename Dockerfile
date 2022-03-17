FROM python:3.7-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create and activate virtual environment
RUN python3 -m venv rapid_env

COPY ./requirements.txt /requirements.txt

RUN /rapid_env/bin/pip install -r requirements.txt

RUN mkdir /src
RUN mkdir /src/app
WORKDIR /src/app
COPY ./src/app /src/app

EXPOSE 8000

CMD ["/rapid_env/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]

RUN adduser -D applicationuser
USER applicationuser

