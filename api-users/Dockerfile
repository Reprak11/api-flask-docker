# syntax=docker/dockerfile:1
FROM python:3.9-alpine

WORKDIR /code

ENV FLASK_APP="entrypoint:app"
ENV FLASK_RUN_HOST=0.0.0.0
ENV APP_SETTINGS_MODULE="config.default"
ENV password="root11"

RUN apk add --no-cache gcc musl-dev linux-headers
RUN apk update && apk add --virtual build-dependencies

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

EXPOSE $PORT

COPY . /code
CMD ["flask", "run"]