from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from webscraper.db.init_db import Base


class Parts(Base):
    __tablename__ = "parts"

    id = Column(Integer, primary_key=True)
    timestamp_utc = Column(DateTime, default=datetime.utcnow())
    manufacturer = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    category = Column(String(50), nullable=False)
    part_number = Column(String(50), nullable=False)
