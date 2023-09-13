from sqlalchemy.inspection import inspect
from webscraper.db.tables import Base
from webscraper.utils.params import TABLE_NAME


def test_create_table(db_engine):
    Base.metadata.create_all(db_engine)

    inspector = inspect(db_engine)

    assert inspector.has_table(TABLE_NAME)
