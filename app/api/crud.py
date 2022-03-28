from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models import models, schemas


def create_record(db: Session, record: schemas.SensorRecord):
    db_record = models.SensorRecords(sensor=record.sensor, ts=record.ts, in_count=record.in_count, out=record.out)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return {"message": "OK"}


def get_sensors(db: Session):
    query = db.query(models.SensorRecords.sensor).group_by(models.SensorRecords.sensor).all()
    sensors = [sensor[0] for sensor in query]

    return sensors


def get_occupancy(db: Session, sensor: str):

    try:
        occupancy = db.query(func.sum(models.SensorRecords.in_count - models.SensorRecords.out)).filter(models.SensorRecords.sensor == sensor).first()[0]
        return occupancy
    except:
        raise


