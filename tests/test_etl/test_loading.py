from webscraper.utils.params import TABLE_NAME


def test_insert_records(db_engine, test_data_df):
    test_data_df.to_sql(TABLE_NAME, db_engine, if_exists="append", index=False)

    assert db_engine.execute("SELECT COUNT(*) FROM parts").fetchone()[0] == len(
        test_data_df
    )
