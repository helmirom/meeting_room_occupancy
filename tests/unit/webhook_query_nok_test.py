import datetime


def test_webhook_query_nok(client, endpoints):
    endpoint = endpoints["webhook"]

    sensor = "sensor_room_1"
    ts = datetime.datetime.isoformat(datetime.datetime.now())
    in_count = "a"
    out_count = 4

    data = {"sensor": sensor, "ts": ts, "in_count": in_count, "out": out_count}

    response = client.post(endpoint, json=data)
    assert response.status_code == 400
