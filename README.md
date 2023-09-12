# Task description

## Web scraping
Do data extraction of a static website:
1. Scrape a static website.
2. Look at https://www.urparts.com/index.cfm/page/catalogue.
3. Check for a manufacturer, then look into the categories, then the models and the result-set where you find the part number before ‘ - ‘ and the part category.
4. Scrape the whole catalog from the website and load it into a database.
6. Scraper should run as fast as possible through the whole page.

# Instructions

## For running the application

This application is made of 3 micro-services:
1. A web scraper service that scrapes the data from the website and stores it in a database.
2. A database service that stores the data scraped by the scraper service.
3. A web service that exposes the scraped data stored in the database through a queryable API endpoint.

Hence, to start the application we need to start all the 3 services.
This should be done using [`docker-compose`](https://docs.docker.com/compose/) as following:
```bash
docker-compose up
```

## For setting up the dev environment

This section outline how to initialize the development environment of the project that are required to run the applications
on Docker.

This project is built on **Python-3.10.12**. It manages its dependencies using [`pip-tools`](https://pip-tools.readthedocs.io/en/latest/).

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

4. Install the dependencies:

```bash
pip-sync requirements/requirements-dev.txt
```

5. Install the pre-commit hooks:

```bash
pre-commit install
```

6. Check if everything works by running the tests:

```bash
pytest
```
