def test_occupancy_nok(client, endpoints):
    """
    Test occupancy for a specific sensor
    :param client:
    :return:
    """
    sensor = "meeting room RDC"
    endpoint = f"/api/sensors/{sensor}/occupancy"

    response_occupancy = client.get(endpoint)
    assert response_occupancy.status_code == 404
