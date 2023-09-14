from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import Index
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from webscraper.utils.params import TABLE_NAME


Base = declarative_base()


class Parts(Base):  # type: ignore
    __tablename__ = TABLE_NAME

    id = Column(Integer, primary_key=True, auto_increment=True)
    load_timestamp_utc = Column(DateTime, default=datetime.utcnow())
    manufacturer = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    category = Column(String(50), nullable=False)
    part_number = Column(String(50), nullable=False)

    # More indexes can be added here, if needed.
    __table_args__ = (Index("idx_manufacturer", "manufacturer"),)
