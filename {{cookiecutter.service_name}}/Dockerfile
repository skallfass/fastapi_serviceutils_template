FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY requirements.txt ./

RUN apt-get install libpq-dev && \
    pip install -r requirements.txt

COPY . /app
