import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    client = TestClient(app)
    return client


@pytest.fixture
def endpoints():
    _endpoints_t = {"webhook": "/api/webhook", "sensors": "/api/sensors"}
    return _endpoints_t
