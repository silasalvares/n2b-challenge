FROM python:3.8.1-slim-buster

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENV NAME wine-reviews-service