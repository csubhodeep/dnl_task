import pandas as pd
import pytest

import datetime

from webscraper.db.init_db import Base
from webscraper.db.tables import Parts  # noqa


def test_create_table(db_engine):
    Base.metadata.create_all(db_engine)

    assert db_engine.has_table("parts")


@pytest.fixture(scope="module")
def test_data_df():
    return pd.DataFrame(
        {
            "load_timestamp_utc": [
                datetime.datetime.utcnow(),
                datetime.datetime.utcnow(),
            ],
            "manufacturer": ["aa", "xx"],
            "model": ["bb", "yy"],
            "category": ["cc", "zz"],
            "part_number": ["dd", "ww"],
        }
    )


def test_insert_table(db_engine, test_data_df):
    Base.metadata.create_all(db_engine)

    # insert a dummy row into the table
    with db_engine.connect() as conn:
        test_data_df.to_sql("parts", conn, if_exists="append", index=False)


def test_read_table(db_engine, test_data_df):
    with db_engine.connect() as conn:
        df = pd.read_sql_table("parts", conn)

    pd.testing.assert_frame_equal(df.drop(columns="id"), test_data_df)
