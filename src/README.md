# Webscraper

This contains the application code for the two of three services. Those are:
1. The web scraper ETL service.
2. The web scraper read-only API service.

## Web scraper ETL service

This one lives under `etl` directory. Therein, the main entrypoint is `pipeline.py`. 
To run the ETL pipeline locally, run -

```bash
python -m webscraper.etl.pipeline
```


## Web scraper read-only API service

This one lives under `api` directory. Therein, the main entrypoint is `app.py`.

To run the API service locally (in dev mode), run - 

```bash
uvicorn webscraper.api.endpoints:app --host 0.0.0.0 --port 8080 --reload
```