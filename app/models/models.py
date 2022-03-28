from sqlalchemy import Column, Integer, String

from app.db.database import Base


class SensorRecords(Base):
    __tablename__ = "records"
    id = Column(Integer, primary_key=True)
    sensor = Column(String)
    ts = Column(String)
    in_count = Column(Integer)
    out = Column(Integer)
