import pytest


def test_import():
    # assert that the main function can be imported and that it does not throw an error
    try:
        from webscraper.api.endpoints import app
    except (ImportError, ModuleNotFoundError):
        pytest.fail("Could not import entrypoint module")


def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
