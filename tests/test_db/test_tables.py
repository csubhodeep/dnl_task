from webscraper.db.tables import Base

from sqlalchemy.inspection import inspect


def test_create_table(db_engine):
    Base.metadata.create_all(db_engine)

    inspector = inspect(db_engine)

    assert inspector.has_table("parts")
