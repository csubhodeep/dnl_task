from __future__ import annotations

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


def get_session(url: str) -> sqlalchemy.orm.session.Session:
    engine = create_engine(url)
    SessionLocal = sessionmaker(autocommit=False, bind=engine, autoflush=False)
    return SessionLocal()
