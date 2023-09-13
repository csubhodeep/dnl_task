from webscraper.utils.params import TABLE_NAME
from webscraper.etl.loading import load


def test_insert_records(db_engine, test_data_df, mock_env):
    load(test_data_df)

    assert db_engine.execute(f"SELECT COUNT(*) FROM {TABLE_NAME}").fetchone()[0] == len(
        test_data_df
    )
