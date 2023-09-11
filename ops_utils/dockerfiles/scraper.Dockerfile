FROM python:3.10-slim-bullseye

WORKDIR app

ADD ../requirements/requirements.txt ./requirements.txt

ADD ../../src ./src

ADD ../Makefile ./Makefile

RUN make
