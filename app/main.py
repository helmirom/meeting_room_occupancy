from fastapi import FastAPI

description = """

## Webhook

* **Invoke webhook to register new records from sensors** .

## Sensors

The API allows:

* **Read sensors list** .
* **Read The occupancy of a specific room** .
* **Read The occupancy of a specific room at a specific instant** .
"""

app = FastAPI(
    title="Meeting room occupancy API 🚀🚀",
    description=description
)


@app.get("/")
def hello_world():

    return "Hello world"
