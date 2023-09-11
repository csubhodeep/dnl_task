# Task description

## Web scraping
Do data extraction of a static website:
1. Scrape a static website.
2. Look at https://www.urparts.com/index.cfm/page/catalogue.
3. Check for a manufacturer, then look into the categories, then the models and the result-set where you find the part number before ‘ - ‘ and the part category.
4. Scrape the whole catalog from the website and load it into a database.
5. Containerize the scraper and database.

## Develop an API
1. Implement the API as a web service using the FastAPI framework.
2. Write an endpoint to expose the data.
3. Add query-parameters to the endpoint, e.g. ?manufacturer=Ammann .
4. Enable and configure Swagger in FastAPI.
5. Containerize the web service.

# Instructions

## For running the application

This application is made of 3 micro-services:
1. A web scraper service that scrapes the data from the website and stores it in a database.
2. A database service that stores the scraped data.
3. A web service that exposes the scraped data stored in the database through an API endpoint.

Hence, to start the application we need to start all the 3 services.
This should be done using [`docker-compose`](https://docs.docker.com/compose/) as following:
```bash
docker-compose up
```

## For setting up the dev environment

This section outline how to initialize the runtime environment of the project that are required to run application
on Docker. This is important for local development and testing purposes.

This project is built on **Python-3.10.12**. It manages its dependencies using [`pip-tools`](https://pip-tools.readthedocs.io/en/latest/).

Follow the steps below to set up the environment (assuming you have `python3` and `python3-venv` installed):

1. We set up the virtual environment and install the dependencies. To do this, run the following commands from the root of the project:

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

4. Compile the consolidated dependency specification (`txt`) files:

```bash
pip-compile requirements/requirements.in && pip-compile requirements/requirements-dev.in
```

4. Install the dependencies:

```bash
pip-sync requirements/requirements-dev.txt
```

5. Install the pre-commit hooks:

```bash
pre-commit install
```

6. Check if everything works by running the tests (from the root of the project):

```bash
pytest
```
