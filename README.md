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
1. The API service would only start after the ETL service has finished executing successfully. Ideally, the ETL service
usually takes 5-10 mins to finish.
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
source venv/bin/activate
```

3. (Optional) Make sure you have the correct version of `pip` installed:

```bash
pip3 install --upgrade pip==23.2.1
```

4. Install `pip-tools`:

```bash
pip3 install pip-tools==7.3.0
```

5. (Optional) Compile the consolidated dependency specification (`txt`) files:

```bash
pip-compile requirements/requirements.in && pip-compile requirements/requirements-dev.in
```

6. Install the dependencies:

```bash
pip-sync requirements/requirements-dev.txt
```

7. Install the pre-commit hooks:

```bash
pre-commit install
```

8. Check if everything works by running the tests (ideally all tests should pass):

```bash
pytest
```
Alternatively you could run the test with coverage:

```bash
pytest --cov=src
```

9. (Optional) For triggering a fresh build before running the containers locally:

```bash
docker compose up --build --no-cache
```

### Directory structure

The project is structured as follows:

```shell
.
├── compose.yaml
├── ops_utils
│   ├── dockerfiles
│   │   ├── api.Dockerfile
│   │   ├── db.Dockerfile
│   │   └── etl.Dockerfile
│   ├── run_api.mk
│   ├── run_etl.mk
│   └── setenv.mk
├── README.md
├── requirements
│   ├── requirements-dev.in
│   ├── requirements-dev.txt
│   ├── requirements.in
│   └── requirements.txt
├── src
│   ├── pyproject.toml
│   ├── README.md
│   └── webscraper
│       ├── api
│       │   ├── endpoints.py
│       │   ├── __init__.py
│       │   └── models.py
│       ├── db
│       │   ├── init_db.py
│       │   ├── __init__.py
│       │   └── tables.py
│       ├── etl
│       │   ├── extraction.py
│       │   ├── __init__.py
│       │   ├── loading.py
│       │   ├── pipeline.py
│       │   └── transformation.py
│       ├── __init__.py
│       └── utils
│           ├── __init__.py
│           └── params.py
└── tests
    ├── conftest.py
    ├── test_api
    │   └── test_endpoints.py
    ├── test_db
    │   └── test_tables.py
    └── test_etl
        ├── test_extraction.py
        ├── test_loading.py
        ├── test_pipeline.py
        └── test_transformation.py
```