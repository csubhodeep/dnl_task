import pytest


def test_import():
    # assert that the main function can be imported and that it does not throw an error
    try:
        from webscraper.etl.pipeline import run_pipeline
    except (ImportError, ModuleNotFoundError):
        pytest.fail("Could not import entrypoint module")
