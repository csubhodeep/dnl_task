import pandas as pd

import os

from webscraper.db.init_db import get_engine
from webscraper.utils.params import SQLALCHEMY_DATABASE_URL, TABLE_NAME


def load(data: pd.DataFrame):
    print("Loading data to database...")
    url = os.getenv("SQLALCHEMY_DATABASE_URL", SQLALCHEMY_DATABASE_URL)
    db_engine = get_engine(url)
    data.to_sql(TABLE_NAME, db_engine, if_exists="append", index=False)
