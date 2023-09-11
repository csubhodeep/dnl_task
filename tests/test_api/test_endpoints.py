from __future__ import annotations

import pytest
from fastapi.testclient import TestClient
from webscraper.api.endpoints import app


@pytest.fixture(scope='session')
def client():
    test_client = TestClient(app)
    yield test_client
    del test_client


def test_import():
    # assert that the main function can be imported and that it does not throw an error
    try:
        from webscraper.api.endpoints import app
    except (ImportError, ModuleNotFoundError):
        pytest.fail('Could not import entrypoint module')


def test_read_main(client):

    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'msg': 'Hello World'}
