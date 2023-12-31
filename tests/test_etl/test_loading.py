from webscraper.etl.loading import load
from webscraper.utils.params import TABLE_NAME


def test_insert_records(db_engine, test_data_df, mock_env):
    # test if all data can be loaded into the database
    load(test_data_df)

    assert db_engine.execute(f"SELECT COUNT(*) FROM {TABLE_NAME}").fetchone()[0] == len(
        test_data_df
    )
