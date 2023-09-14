# Web scraper
This is a basic webscraper application made of 3 micro-services:
1. A web scraper service that scrapes the data from the website and stores it in a database.
2. A database service that stores the data scraped by the scraper service.
3. A web service that exposes the scraped data stored in the database through a queryable API endpoint.

# Instructions

## For running the application

To start the application we need to start all the 3 services.
This should be done using [`docker-compose`](https://docs.docker.com/compose/) as following 
```bash
docker compose up
```
(it is assumed that you have `docker` (engine and CLI) and `docker-compose` installed)


A few points regarding the design of the application:
1. The API service would only start after the ETL service has finished executing successfully.
2. The ETL and API service both depend on the DB service, so they would only start after the DB service has started.

After the API service is live you should be able to check the Swagger docs and try out querying the endpoint
under [`http://localhost:8080/docs`](http://localhost:8080/docs).

Additionally, the DB service is also exposed at `localhost:3306`. One could also check the contents of the DB
using a DB client (like MySQL Workbench or Jetbrains DataGrip). 

To establish a connection please refer to the `compose.yaml` file for credentials.

## For setting up the dev environment

This section outline how to initialize the development environment of the project that are required to run the applications
on Docker.

This project is built on **Python-3.10** and it manages its dependencies using [`pip-tools`](https://pip-tools.readthedocs.io/en/latest/).

Follow the steps below and run the accompanying code snippets from the root of the project to set up the environment 
(assuming you have `python3` and `python3-venv` installed):

1. Set up the virtual environment and install the dependencies.

```bash
python3 -m venv ./venv
```

2. Activate the virtual environment:

```bash
source ven/bin/activate
```

3. Install `pip-tools`:

```bash
pip3 install pip-tools==7.3.0
```

4. (Optional) Compile the consolidated dependency specification (`txt`) files:

```bash
pip-compile requirements/requirements.in && pip-compile requirements/requirements-dev.in
```

5. Install the dependencies:

```bash
pip-sync requirements/requirements-dev.txt
```

6. Install the pre-commit hooks:

```bash
pre-commit install
```

7. Check if everything works by running the tests (ideally all tests should pass):

```bash
pytest
```

8. (Optional) For triggering a fresh build before running the containers locally:

```bash
docker compose up --build --no-cache
```