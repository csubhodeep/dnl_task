import pandas as pd
import pytest
import sqlalchemy
from fastapi.testclient import TestClient
from webscraper.api.endpoints import app
from webscraper.db.init_db import get_engine


@pytest.fixture(scope="function")
def path_to_db(tmp_path_factory):
    return tmp_path_factory.mktemp("db_data").joinpath("mock_sqlite.db")


@pytest.fixture(scope="function")
def mock_env(monkeypatch, path_to_db):
    monkeypatch.setenv("SQLALCHEMY_DATABASE_URL", f"sqlite:///{path_to_db}")


@pytest.fixture(scope="function")
def db_engine(path_to_db):
    yield get_engine(f"sqlite:///{path_to_db}")


@pytest.fixture(scope="function")
def client(mock_env):
    test_client = TestClient(app)
    yield test_client
    del test_client


@pytest.fixture(scope="function")
def test_data_df():
    return pd.DataFrame(
        {
            "manufacturer": ["aa", "xx"],
            "model": ["bb", "yy"],
            "category": ["cc", "zz"],
            "part_number": ["dd", "ww"],
        }
    )


@pytest.fixture(scope="function")
def populated_db(db_engine, test_data_df):
    test_data_df.to_sql("parts", db_engine, if_exists="append", index=False)
