import os
import pathlib

BASE_URL = "https://www.urparts.com/index.cfm/page/catalogue"

DIALECT = "mysql"
DRIVER = "pymysql"
DB_USER = os.getenv("MYSQL_USER", "abcd")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD", "abcd")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("MYSQL_DATABASE", "urparts")


SQLALCHEMY_DATABASE_URL = (
    f"{DIALECT}+{DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

TABLE_NAME = "parts"

BASE_PATH = pathlib.Path(__file__).parent.parent.parent.parent

DATA_PATH = BASE_PATH / "data"
