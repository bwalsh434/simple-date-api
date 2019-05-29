import pytest

import app as appl


@pytest.fixture
def client():
    appl.app.config["TESTING"] = True
    client = appl.app.test_client()
    yield client


def test_index_endpoint(client):
    result = client.get("/")
    assert b'index!' in result.data


def test_date_endpoint_default(client):
    result = client.get("/date")
    print(result)
    assert b'timestamp' in result.data
