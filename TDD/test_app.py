import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_get_dummy_data(client):
    response = client.get('/')
    data = response.get_json()

    assert response.status_code == 200
    assert 'message' in data
    assert 'data' in data
