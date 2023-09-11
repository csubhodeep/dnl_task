from __future__ import annotations

from fastapi import Depends
from fastapi import FastAPI
from sqlalchemy.orm import Session
from webscraper.db.init_db import Base
from webscraper.db.init_db import get_session
from webscraper.utils.params import SQLALCHEMY_DATABASE_URL

app = FastAPI()

# Base.metadata.create_all(bind=get_session(SQLALCHEMY_DATABASE_URL).get_bind())


# Dependency
def get_db_sess():
    db = get_session(SQLALCHEMY_DATABASE_URL)
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def read_root(db_sess: Session = Depends(get_db_sess)):
    return {'msg': 'Hello World'}
