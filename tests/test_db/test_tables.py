import pandas as pd

from webscraper.db.tables import Base


def test_create_table(db_engine):
    Base.metadata.create_all(db_engine)

    assert db_engine.has_table("parts")
