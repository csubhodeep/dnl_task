import pandas as pd

from webscraper.db.tables import Base


def test_create_table(db_engine):
    Base.metadata.create_all(db_engine)

    assert db_engine.has_table("parts")


def test_insert_table(db_engine, test_data_df):
    Base.metadata.create_all(db_engine)

    test_data_df.to_sql("parts", db_engine, if_exists="append", index=False)

    assert db_engine.execute("SELECT COUNT(*) FROM parts").fetchone()[0] == len(
        test_data_df
    )


def test_read_table(db_engine, test_data_df, populated_db):
    df = pd.read_sql_table("parts", db_engine)

    pd.testing.assert_frame_equal(df, test_data_df)
