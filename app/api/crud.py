from sqlalchemy.orm import Session

from app.models import models, schemas


def create_record(db: Session, record: schemas.SensorRecord):
    db_record = models.SensorRecords(sensor=record.sensor, ts=record.ts, in_count=record.in_count, out=record.out)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return {"message": "OK"}
