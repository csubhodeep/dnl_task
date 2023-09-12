# Refs - https://fastapi.tiangolo.com/deployment/docker/#dockerfile
FROM python:3.10-slim-bullseye

RUN apt-get update \
    && apt-get install -y make \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./requirements/requirements.txt /app/requirements/requirements.txt

COPY ./src /app/src

ADD ./ops_utils/setenv.mk /app/setenv.mk

ADD ./ops_utils/run_api.mk /app/run_api.mk

RUN make -f setenv.mk

CMD ["make", "-f", "run_api.mk"]