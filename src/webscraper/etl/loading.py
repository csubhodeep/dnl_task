import logging
import os

import pandas as pd
import sqlalchemy as sa
from loguru import logger
from webscraper.db.init_db import get_engine
from webscraper.db.tables import Base
from webscraper.utils.params import SQLALCHEMY_DATABASE_URL, TABLE_NAME


def load(data: pd.DataFrame):
    """This function loads the data to the database.
    :param data: A pandas DataFrame containing the data to be loaded
    :return:
    """
    # inject config during runtime
    url = os.getenv("SQLALCHEMY_DATABASE_URL", SQLALCHEMY_DATABASE_URL)
    logging.info(f"Connecting to database at {url}...")
    db_engine = get_engine(url)

    inspector = sa.inspect(db_engine)
    if not inspector.has_table(TABLE_NAME):
        logger.info(f"Table '{TABLE_NAME}' does not exist, creating it...")
        Base.metadata.create_all(db_engine)
        assert inspector.has_table(TABLE_NAME), f"Table '{TABLE_NAME}' not created"

    data["load_timestamp_utc"] = pd.Timestamp.utcnow()
    logger.info("Loading data to database...")
    data.to_sql(
        TABLE_NAME,
        db_engine,
        if_exists="append",
        index=False,
        # bigger chunksize or setting this to None -> faster but leads to memory usage and OOM
        chunksize=20_000,
    )
