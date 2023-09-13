import pytest
import pandas as pd
from webscraper.etl.transformation import transform


@pytest.fixture(scope="function")
def raw_data() -> list[dict[str, list[str]]]:
    return [
        {
            "https://www.urparts.com/index.cfm/page/catalogue/Ammann/Roller%20Parts/ASC100": [
                "ND0710",
                "ND011758",
            ]
        },
        {
            "https://www.urparts.com/index.cfm/page/catalogue/Ammann/Roller%20Parts/ASC120": [
                "ND011710",
                "ND011758",
            ]
        },
        {
            "https://www.urparts.com/index.cfm/page/catalogue/Volvo/Parts/ASC102": [
                "ND0110",
                "ND011753",
            ]
        },
        {
            "https://www.urparts.com/index.cfm/page/catalogue/Volvo/Roller/ASC101": [
                "ND011710",
                "ND0758",
            ]
        },
    ]


def test_transform(raw_data):
    df = transform(raw_data)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert df.shape == (8, 4)
    assert set(df.columns) == {"manufacturer", "part_number", "model", "category"}
    assert set(df["manufacturer"]) == {"Ammann", "Volvo"}
    assert set(df["category"]) == {"Roller Parts", "Roller", "Parts"}
    assert set(df["model"]) == {"ASC102", "ASC101", "ASC120", "ASC100"}
    assert set(df["part_number"]) == {
        "ND0710",
        "ND011758",
        "ND011710",
        "ND0110",
        "ND0758",
        "ND011753",
    }
