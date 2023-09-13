import pandas as pd


def transform(raw_data: list[dict[str, list[str]]]) -> pd.DataFrame:
    print("Transforming...")

    records = []
    # the below can be parallelized but skipping it for now
    for entry in raw_data:
        url, parts = entry.popitem()
        _, info = url.split("/catalogue/")
        manufacturer, category, model = info.split("/")
        # FIXME: this could be unsafe
        category = category.replace("%20", " ")
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
