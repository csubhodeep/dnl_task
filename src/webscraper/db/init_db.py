from __future__ import annotations

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


Base = declarative_base()


def get_engine(url: str) -> sqlalchemy.engine.Engine:
    return create_engine(url)
