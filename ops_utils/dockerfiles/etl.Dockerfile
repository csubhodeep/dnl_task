FROM python:3.10-slim-bullseye

RUN apt-get update \
    && apt-get install -y make \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app

ADD ./requirements/requirements.txt /app/requirements/requirements.txt

ADD ./src /app/src

ADD ./ops_utils/setenv.mk /app/setenv.mk

ADD ./ops_utils/run_etl.mk /app/run_etl.mk

RUN make -f setenv.mk

CMD ["make", "-f", "run_etl.mk"]