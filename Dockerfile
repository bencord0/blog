FROM python:3.6.1

ADD . /app
WORKDIR /app

RUN pip install -e .
