import datetime


def test_occupancy_at_instant_sensors_empty(client, endpoints):
    """

    :param client:
    :return:
    """
    sensor = "meeting room rooftop"
    base_endpoint = f"sensors/{sensor}/occupancy"

    params = {"atInstant": ""}

    instant_1 = datetime.datetime.isoformat(datetime.datetime.now())
    params["atInstant"] = instant_1

    response_occupancy = client.get(base_endpoint, query_string=params)
    assert response_occupancy.status_code == 404
