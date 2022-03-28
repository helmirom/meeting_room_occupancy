import datetime


def test_occupancy(client, endpoints):
    """
    Test occupancy for a specific sensor
    :param client:
    :return:
    """
    sensor = "meeting room RDC"
    endpoint = f"/api/sensors/{sensor}/occupancy"

    # add a sensor and a record

    record = {
        "sensor": sensor,
        "ts": datetime.datetime.isoformat(datetime.datetime.now()),
        "in_count": 3,
        "out": 2,
    }
    response_post = client.post(endpoints["webhook"], json=record)
    assert response_post.status_code == 200

    response_occupancy = client.get(endpoint)
    assert response_occupancy.status_code == 200
    assert response_occupancy.json["sensor"] == sensor
    assert response_occupancy.json["inside"] == 1
