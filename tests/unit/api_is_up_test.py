def test_home_page(client):
    """
    Test if api is UP and responding
    :param client:
    :return:
    """
    response = client.get("/")
    assert response.status_code == 200
