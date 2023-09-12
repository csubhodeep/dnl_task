from __future__ import annotations

import os

BASE_URL = "https://www.urparts.com/index.cfm/page/catalogue"

DIALECT = "pymysql"
DRIVER = "mysql"
DB_USER = os.getenv("DB_USER", "abcd")
DB_PASSWORD = os.getenv("DB_PASSWORD", "abcd")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "urparts")


SQLALCHEMY_DATABASE_URL = (
    f"{DRIVER}+{DIALECT}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
)
