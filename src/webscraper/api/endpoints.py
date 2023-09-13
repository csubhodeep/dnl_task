import os
from typing import Any

import pandas as pd
import sqlalchemy
from fastapi import Depends
from fastapi import FastAPI
from webscraper.api.models import Part
from webscraper.db.init_db import get_engine
from webscraper.utils.params import SQLALCHEMY_DATABASE_URL


app = FastAPI()


# Dependency
def get_db_engine() -> sqlalchemy.engine.Engine:
    # inject config during runtime
    url = os.getenv("SQLALCHEMY_DATABASE_URL", SQLALCHEMY_DATABASE_URL)
    db_engine = get_engine(url)
    yield db_engine


@app.get("/", response_model=list[Part])
async def read_data(
    db_engine: sqlalchemy.engine.Engine = Depends(get_db_engine),
    manufacturer: str | None = None,
) -> Any:
    if manufacturer is None:
        query = "SELECT * FROM parts LIMIT 5"
    else:
        query = f"SELECT * FROM parts WHERE manufacturer = '{manufacturer}'"
    df = pd.read_sql(query, db_engine)

    return df.to_dict(orient="records")
