import pytest
import sqlalchemy
from webscraper.db.init_db import Base
from webscraper.db.init_db import get_session


@pytest.fixture(scope="session")
def path_to_db(tmp_path_factory):
    return tmp_path_factory.mktemp("db_data").joinpath("mock_sqlite.db")


@pytest.fixture(scope="session")
def db_session(path_to_db) -> sqlalchemy.orm.session.Session:
    return get_session(f"sqlite:///{path_to_db}")


def test_create_table(db_session):
    db_session.autocommit = True
    Base.metadata.create_all(bind=db_session.get_bind())

    with db_session:
        assert db_session.get_bind().has_table("parts")
