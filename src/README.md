# Webscraper

This contains the Python application code for the two of three services. Those are:
1. The web scraper ETL service.
2. The web scraper read-only API service.

## Web scraper ETL service

This one lives under `etl` directory. Therein, the main entrypoint is `pipeline.py`. 
To run the ETL pipeline locally, run -

```bash
python -m webscraper.etl.pipeline
```

### Design

This service is further divided into three steps:
1. Extraction - this mainly involves scraping the web pages.
2. Transformation - this involves cleaning up the data and transforming it into a format that is suitable for loading into the database.
3. Loading - this involves loading the data into the database.


## Web scraper read-only API service

This one lives under `api` directory. Therein, the main entrypoint is `endpoints.py`.

To run the API service locally (in dev mode), run - 

```bash
uvicorn webscraper.api.endpoints:app --host 0.0.0.0 --port 8080 --reload
```

ALternatively,

```bash
python3 -m webscraper.api.endpoints
```

P.S. the `uvicorn` command would enable hot-reloading. The `python3` command would not. 