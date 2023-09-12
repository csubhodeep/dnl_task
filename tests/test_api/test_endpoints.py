import pytest


def test_import():
    # assert that the main function can be imported and that it does not throw an error
    try:
        from webscraper.api.endpoints import app
    except (ImportError, ModuleNotFoundError):
        pytest.fail("Could not import entrypoint module")


def test_read_root(client, populated_db, test_data_df):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == test_data_df.to_dict(orient="records")
