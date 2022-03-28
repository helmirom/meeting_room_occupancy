import datetime


def test_occupancy_at_instant(client, endpoints):
    """

    :param client:
    :return:
    """
    sensor = "meeting room rooftop"
    base_endpoint = f"sensors/{sensor}/occupancy"

    params = {"atInstant": ""}
    # add a sensor and a record

    record = {
        "sensor": sensor,
        "ts": datetime.datetime.isoformat(datetime.datetime.now()),
        "in_count": 3,
        "out": 2,
    }
    response_post = client.post(endpoints["webhook"], json=record)
    assert response_post.status_code == 200

    instant_1 = datetime.datetime.isoformat(datetime.datetime.now())
    params["atInstant"] = instant_1

    response_occupancy = client.get(base_endpoint, params=params)
    assert response_occupancy.status_code == 200
    assert response_occupancy.json()["inside"] == 1
