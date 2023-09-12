from __future__ import annotations

from webscraper.etl.extraction import scrape
from webscraper.etl.loading import load
from webscraper.etl.transformation import transform
from webscraper.utils.params import BASE_URL


def run_pipeline():
    data = scrape(BASE_URL)
    df = transform(data)
    load(df)


if __name__ == "__main__":
    run_pipeline()
