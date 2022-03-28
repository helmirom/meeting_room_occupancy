import datetime


def test_scenario(client, endpoints):
    """
    Test functional scenario
    :param client: from pytest.fixture
    :param endpoints: from pytest.fixture
    :return:
    """

    # Test @ startup sensor list is empty
    response = client.get(endpoints["sensors"])
    assert response.status_code == 200
    assert response.json["sensors"] == []

    # Invoke webhook and check sensor is added, and record is fine
    sensor = "sensor_room_baby_boy"
    ts = datetime.datetime.isoformat(datetime.datetime.now())
    in_count = 6
    out_count = 3

    data = {"sensor": sensor, "ts": ts, "in": in_count, "out": out_count}

    response_webhook = client.post(endpoints["webhook"], json=data)
    assert response_webhook.status_code == 201

    instant_1 = datetime.datetime.isoformat(datetime.datetime.now())

    # Test occupancy
    endpoint_occupancy = f"/api/sensors/{sensor}/occupancy"
    response_occupancy = client.get(endpoint_occupancy)
    assert response_occupancy.status_code == 200
    assert response_occupancy.json["sensor"] == sensor
    assert response_occupancy.json["inside"] == 3

    # Invoke webhook with new record for previous sensor, and add new sensor

    data_it2_sensor1 = {
        "sensor": sensor,
        "ts": datetime.datetime.isoformat(datetime.datetime.now()),
        "in": 1,
        "out": 3,
    }
    response_webhook = client.post(endpoints["webhook"], json=data_it2_sensor1)
    assert response_webhook.status_code == 201

    sensor_2 = "sensor_room_baby_girl"
    data_sensor_2 = {
        "sensor": sensor_2,
        "ts": datetime.datetime.isoformat(datetime.datetime.now()),
        "in": 2,
        "out": 1,
    }
    response_webhook = client.post(endpoints["webhook"], json=data_sensor_2)
    assert response_webhook.status_code == 201

    # Test Occupancy at instant_1 for sensor_1 and check it
    endpoint_occupancy_at_instant = f"sensors/{sensor}/occupancy"
    params = {"atInstant": instant_1}
    response_occupancy = client.get(endpoint_occupancy_at_instant, query_string=params)
    assert response_occupancy.status_code == 200
    assert response_occupancy.json["inside"] == 3

    # Test Occupancy at instant_2 for sensor_1 and check it
    instant_2 = datetime.datetime.isoformat(datetime.datetime.now())
    endpoint_occupancy_at_instant = f"sensors/{sensor}/occupancy"
    params = {"atInstant": instant_2}
    response_occupancy = client.get(endpoint_occupancy_at_instant, query_string=params)
    assert response_occupancy.status_code == 200
    assert response_occupancy.json["inside"] == 1
