def test_get_sensor_list(client, endpoints):
    """
    Test get list of sensors
    :param client: from pytest.fixture
    :param endpoints: from pytest.fixture
    :return:
    """
    endpoint = endpoints["sensors"]
    response = client.get(endpoint)
    assert response.status_code == 200
