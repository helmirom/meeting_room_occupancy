from fastapi import FastAPI, Depends, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse

from sqlalchemy.orm import Session

from app.api import crud
from app.models import models, schemas
from app.db.database import engine, SessionLocal

description = """

## Webhook

* **Invoke webhook to register new records from sensors** .

## Sensors

The API allows:

* **Read sensors list** .
* **Read The occupancy of a specific room** .
* **Read The occupancy of a specific room at a specific instant** .
"""

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Meeting room occupancy API 🚀🚀",
    description=description
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def hello_world():

    return "Hello world"


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


@app.post("/api/webhook", response_model=schemas.RecordCreate)
def invoke_webhook(record: schemas.SensorRecord, db: Session = Depends(get_db)):

    try:
        return_object = crud.create_record(db=db, record=record)
        return return_object

    except:
        raise HTTPException(status_code=400, detail="Bad Request")


@app.get("/api/sensors/", response_model=schemas.Sensors)
def get_sensors_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_sensors(db)
    result_object = {
        "sensors": items
    }
    return result_object


@app.get("/api/sensors/{sensor}/occupancy", response_model=schemas.Occupancy)
def get_occupancy_for_sensor(sensor: str, db: Session = Depends(get_db)):
    try:
        occupancy = crud.get_occupancy(db, sensor=sensor)
        if not occupancy:
            raise HTTPException(status_code=400, detail="Bad Request")
        result_object = {
            "sensor": sensor,
            "inside": occupancy
        }
        return result_object

    except:
        raise HTTPException(status_code=404, detail="Not Found")
