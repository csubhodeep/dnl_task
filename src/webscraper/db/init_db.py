from __future__ import annotations

import sqlalchemy
from sqlalchemy import create_engine


def get_engine(url: str) -> sqlalchemy.engine.Engine:
    """This function returns an sqlalchemy engine.
    :param url: The database url - this could point to an sqlite file or a MySQL database.
    :return: An sqlalchemy engine.
    """
    return create_engine(url)
