import os

from fastapi import Depends
from fastapi import FastAPI
import sqlalchemy
from webscraper.db.init_db import Base
from webscraper.db.init_db import get_engine
from webscraper.utils.params import SQLALCHEMY_DATABASE_URL

app = FastAPI()


# Dependency
def get_db_engine() -> sqlalchemy.engine.Engine:
    # inject config during runtime
    url = os.getenv("SQLALCHEMY_DATABASE_URL", SQLALCHEMY_DATABASE_URL)
    db_engine = get_engine(url)
    Base.metadata.create_all(bind=db_engine)
    yield db_engine


@app.get("/")
def read_root(db_session: sqlalchemy.engine.Engine = Depends(get_db_engine)):
    return {"msg": "Hello World"}
