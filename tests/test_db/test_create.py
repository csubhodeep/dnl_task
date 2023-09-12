from webscraper.db.init_db import Base
from webscraper.db.tables import Parts  # noqa


def test_create_table(db_engine):
    Base.metadata.create_all(db_engine)

    assert db_engine.has_table("parts")
