from pydantic import BaseModel


class RecordCreate(BaseModel):
    message: str


class SensorRecord(BaseModel):
    sensor: str
    ts: str
    in_count: int
    out: int


class Sensors(BaseModel):
    sensors: list


class Occupancy(BaseModel):
    sensor: str
    inside: int


class OccupancyAtInstant(BaseModel):
    inside: int
