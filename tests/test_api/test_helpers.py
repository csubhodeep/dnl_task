from webscraper.api.helpers import build_query


def test_build_query():
    """Test that the query is built correctly."""
    expected = (
        "SELECT * "
        "FROM xyz "
        "WHERE LOWER(manufacturer) = 'test_manufacturer' "
        "AND LOWER(model) = 'test_model' "
        "AND LOWER(category) = 'test_category'"
    )

    actual = build_query(
        manufacturer="test_manufacturer",
        model="test_model",
        category="test_category",
        table_name="xyz",
    )

    assert actual == expected
