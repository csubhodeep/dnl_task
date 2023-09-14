import os
import sqlalchemy

from webscraper.db.init_db import get_engine
from webscraper.utils.params import SQLALCHEMY_DATABASE_URL, TABLE_NAME


def get_db_engine() -> sqlalchemy.engine.Engine:
    """This function returns a database engine.
    :return: A database engine.
    """
    # inject config during runtime
    url = os.getenv("SQLALCHEMY_DATABASE_URL", SQLALCHEMY_DATABASE_URL)
    db_engine = get_engine(url)
    yield db_engine


def build_query(
    manufacturer: str | None = None,
    model: str | None = None,
    category: str | None = None,
    table_name: str = TABLE_NAME,
    n_results: int = 5,
) -> str:
    """This function builds a SQL query.
    :param manufacturer: The manufacturer of the parts.
    :param model: The model of the parts.
    :param category: The category of the parts.
    :return: A SQL query.
    """
    where_conditions = []
    if manufacturer:
        where_conditions.append(f"LOWER(manufacturer) = '{manufacturer.lower()}'")
    if model:
        where_conditions.append(f"LOWER(model) = '{model.lower()}'")
    if category:
        where_conditions.append(f"LOWER(category) = '{category.lower()}'")

    if n_results:
        limit_query = f"LIMIT {n_results}"
    else:
        limit_query = ""

    if not where_conditions:
        query = f"SELECT * FROM {table_name} {limit_query}"
    else:
        where_conditions = " AND ".join(where_conditions)
        query = f"SELECT * FROM {table_name} WHERE {where_conditions} {limit_query}"

    return query
