import os
from typing import Any

import pandas as pd
import sqlalchemy
from fastapi import Depends
from fastapi import FastAPI
from webscraper.api.models import Part
from webscraper.db.init_db import get_engine
from webscraper.utils.params import SQLALCHEMY_DATABASE_URL, TABLE_NAME


app = FastAPI()


# Dependency
def get_db_engine() -> sqlalchemy.engine.Engine:
    """This function returns a database engine.
    :return: A database engine.
    """
    # inject config during runtime
    url = os.getenv("SQLALCHEMY_DATABASE_URL", SQLALCHEMY_DATABASE_URL)
    db_engine = get_engine(url)
    yield db_engine


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
    if manufacturer is None:
        query = f"SELECT * FROM {TABLE_NAME} LIMIT 5"
    else:
        query = f"""
            SELECT * 
            FROM {TABLE_NAME} 
            WHERE manufacturer = '{manufacturer}'
                AND model = '{model}'
                AND category = '{category}'
        """
    df = pd.read_sql(query, db_engine)

    return df.to_dict(orient="records")
