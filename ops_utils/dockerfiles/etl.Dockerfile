FROM python:3.10-slim-bullseye

WORKDIR /app

ADD ../../requirements/requirements.txt /app/requirements.txt

ADD ../../src /app/src

ADD ../setenv.mk /code/setenv.mk

RUN make -f setenv.mk

CMD ["python", "-m", "webscraper.etl.pipeline"]
