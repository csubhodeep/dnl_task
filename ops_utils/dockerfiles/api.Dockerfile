# Refs - https://fastapi.tiangolo.com/deployment/docker/#dockerfile
FROM python:3.9

WORKDIR /code

COPY ../../requirements/requirements.txt /code/requirements.txt

COPY ../setenv.mk /code/setenv.mk

RUN make -f setenv.mk

CMD ["uvicorn", "webscraper.api.endpoints:app", "--host", "0.0.0.0", "--port", "80"]
