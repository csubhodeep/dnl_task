import pandas as pd
from loguru import logger


def transform(raw_data: list[dict[str, list[str]]]) -> pd.DataFrame:
    """This function transforms the raw data into a dataframe.
    :param raw_data: list of dictionaries containing the raw data
    :return: dataframe containing the transformed data
    """
    logger.info("Transforming raw data...")

    records = []
    # the below can be parallelized but skipping it for now
    for entry in raw_data:
        url, parts = entry.popitem()
        _, info = url.split("/catalogue/")
        manufacturer, category, *model = info.split("/")
        # FIXME: these could be unsafe
        manufacturer = manufacturer.replace("%20", " ")
        category = category.replace("%20", " ")
        model = "/".join(model).replace("%20", " ")
        for part in parts:
            records.append(
                {
                    "manufacturer": manufacturer,
                    "category": category,
                    "model": model,
                    "part_number": part,
                }
            )

    return pd.DataFrame(records)
