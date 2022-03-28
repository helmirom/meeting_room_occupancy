import datetime
import os

import requests
import streamlit as st

BACKEND_URL = os.getenv("API_URL")
endpoint = "/api/sensors"


def get_sensors():

    try:
        r = requests.get(url=BACKEND_URL + endpoint)
        return r.json()["sensors"]

    except Exception:
        return []


def invoke_webhook(sensor, in_count, out_count):
    PARAMS = {
        "sensor": sensor,
        "ts": datetime.datetime.isoformat(datetime.datetime.now()),
        "in": int(in_count),
        "out": int(out_count),
    }
    r = requests.post(url=BACKEND_URL + "/api/webhook", json=PARAMS)
    print(r.json())


def get_occupancy(sensor_id):
    try:
        r = requests.get(url=f"{BACKEND_URL}/api/sensors/{sensor_id}/occupancy")
        print(r.json())

        return r.json()["inside"]
    except LookupError:
        return 0


st.text(f"Sensors: {get_sensors()}")


form = st.form(key="my_form")


sensor = form.text_input(label="Sensor ID")
in_count = form.text_input(label="IN")
out_count = form.text_input(label="OUT")

submit_button = form.form_submit_button(label="Submit")

if submit_button:
    invoke_webhook(sensor=sensor, in_count=in_count, out_count=out_count)

option = st.selectbox("Select a Sensor", tuple(get_sensors()))


st.write("Occupancy :\n")

st.write(get_occupancy(option))
