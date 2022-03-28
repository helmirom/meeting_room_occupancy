from pydantic import BaseModel


class RecordCreate(BaseModel):
    message: str


class SensorRecord(BaseModel):
    sensor: str
    ts: str
    in_count: int
    out: int

