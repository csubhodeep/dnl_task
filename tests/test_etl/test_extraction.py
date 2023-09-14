import pytest

from webscraper.etl.extraction import (
    open_page,
    parse_manufacturers,
    parse_categories,
    parse_models,
    parse_part_numbers,
    scrape,
)
from webscraper.utils.params import BASE_URL
from urllib.parse import urljoin, urlparse

# page fixtures to be used only in this module


@pytest.fixture(scope="module")
def base_html_page():
    yield open_page(BASE_URL)


@pytest.fixture(scope="module")
def category_html_page():
    cat_url = urljoin(f"{BASE_URL}/", "Ammann")
    yield open_page(cat_url)


@pytest.fixture(scope="module")
def model_html_page():
    mdl_url = urljoin(f"{BASE_URL}/", "Ammann/Roller%20Parts")
    yield open_page(mdl_url)


@pytest.fixture(scope="module")
def part_html_page():
    part_url = urljoin(f"{BASE_URL}/", "Ammann/Roller%20Parts/ASC100")
    yield open_page(part_url)


def test_parse_manufacturers(base_html_page):
    manufacturers = parse_manufacturers(base_html_page)
    assert isinstance(manufacturers, list)
    assert len(manufacturers) > 0
    assert "Ammann" in manufacturers
    assert manufacturers[0] not in ["", None]


def test_parse_models(model_html_page):
    models = parse_models(model_html_page)
    assert isinstance(models, list)
    assert len(models) > 0
    assert models[0] not in ["", None]


def test_parse_categories(category_html_page):
    categories = parse_categories(category_html_page)
    assert isinstance(categories, list)
    assert len(categories) > 0
    assert categories[0] not in ["", None]


def test_parse_part_numbers(part_html_page):
    part_numbers = parse_part_numbers(part_html_page)
    assert isinstance(part_numbers, list)
    assert len(part_numbers) > 0
    assert part_numbers[0] not in ["", None]


def test_scrape():
    res = scrape(BASE_URL, 1)
    assert isinstance(res, list)
    assert len(res) > 0
    assert isinstance(res[0], dict)
    url, parts = res[0].popitem()
    parsed_url = urlparse(url)
    assert all([parsed_url.netloc, parsed_url.scheme])
    assert parsed_url.netloc == urlparse(BASE_URL).netloc
    assert isinstance(parts, list)
