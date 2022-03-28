from fastapi import FastAPI
from app.models import models
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
