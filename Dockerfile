# syntax=docker/dockerfile:1

FROM python:3-alpine3.15

WORKDIR /app3

COPY . /app3

RUN pip install -r requirements.txt

EXPOSE 3000

CMD  python ./main.py