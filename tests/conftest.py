import pytest

import sqlalchemy
from webscraper.db.init_db import get_engine
from webscraper.api.endpoints import app

from fastapi.testclient import TestClient


@pytest.fixture(scope="session")
def path_to_db(tmp_path_factory):
    return tmp_path_factory.mktemp("db_data").joinpath("mock_sqlite.db")


@pytest.fixture(scope="function")
def mock_env(monkeypatch, path_to_db):
    monkeypatch.setenv("SQLALCHEMY_DATABASE_URL", f"sqlite:///{path_to_db}")


@pytest.fixture(scope="session")
def db_engine(path_to_db) -> sqlalchemy.orm.session.Session:
    return get_engine(f"sqlite:///{path_to_db}")


@pytest.fixture(scope="function")
def client(mock_env):
    test_client = TestClient(app)
    yield test_client
    del test_client
