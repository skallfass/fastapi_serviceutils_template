FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7-alpine3.8

COPY requirements.txt ./

RUN apk update && \
    apk add --no-cache --virtual .build-deps build-base postgresql-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del .build-deps

COPY . /app
