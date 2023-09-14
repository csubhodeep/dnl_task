from typing import Any

import pandas as pd
import sqlalchemy
import uvicorn
from fastapi import Depends
from fastapi import FastAPI
from webscraper.api.models import Part
from webscraper.api.helpers import build_query, get_db_engine


app = FastAPI()


@app.get("/", response_model=list[Part])
async def read_data(
    db_engine: sqlalchemy.engine.Engine = Depends(get_db_engine),
    manufacturer: str | None = None,
    model: str | None = None,
    category: str | None = None,
) -> Any:
    """This endpoint returns a list of parts from the database.
    :param db_engine: The database engine.
    :param manufacturer: The manufacturer of the parts.
    :param model: The model of the parts.
    :param category: The category of the parts.
    :return: A list of parts in the form of
        [
            {
                "manufacturer": str,
                "model": str,
                "category": str",
                "part_number": str,
            },
            ...
        ]
    """
    query = build_query(manufacturer, model, category)

    df = pd.read_sql(query, db_engine)

    return df.to_dict(orient="records")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
