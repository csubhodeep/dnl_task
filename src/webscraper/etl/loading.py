import os

import pandas as pd
import sqlalchemy as sa
from loguru import logger
from webscraper.db.init_db import get_engine
from webscraper.db.tables import Base
from webscraper.utils.params import SQLALCHEMY_DATABASE_URL, TABLE_NAME


def load(data: pd.DataFrame):
    logger.info("Loading data to database...")
    url = os.getenv("SQLALCHEMY_DATABASE_URL", SQLALCHEMY_DATABASE_URL)
    db_engine = get_engine(url)

    inspector = sa.inspect(db_engine)
    if not inspector.has_table(TABLE_NAME):
        logger.info(f"Table '{TABLE_NAME}' does not exist, creating it...")
        Base.metadata.create_all(db_engine)
        assert inspector.has_table(TABLE_NAME), f"Table '{TABLE_NAME}' not created"

    data["load_timestamp_utc"] = pd.Timestamp.utcnow()
    data.to_sql(TABLE_NAME, db_engine, if_exists="append", index=False)
