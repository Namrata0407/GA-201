import pytest
from app import app, weather_data

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_create_weather(client):
    response = client.post('/weather', json={'city': 'Chicago', 'temperature': 25, 'weather': 'Sunny'})
    assert response.status_code == 201
    assert response.data == b'Weather data created successfully'

def test_create_weather_invalid_request(client):
    response = client.post('/weather', json={'temperature': 25, 'weather': 'Sunny'})
    assert response.status_code == 400
    assert response.data == b'Invalid request data'

def test_update_weather(client):
    response = client.put('/weather/Seattle', json={'temperature': 15})
    assert response.status_code == 200
    assert response.data == b'Weather data updated successfully'
    assert weather_data['Seattle']['temperature'] == 15

def test_update_weather_nonexistent_city(client):
    response = client.put('/weather/India', json={'temperature': 25})
    assert response.status_code == 404
    assert response.data == b'Weather data not found for India'

def test_delete_weather(client):
    response = client.delete('/weather/San Francisco')
    assert response.status_code == 200
    assert response.data == b'Weather data deleted successfully'
    assert 'San Francisco' not in weather_data

def test_delete_weather_nonexistent_city(client):
    response = client.delete('/weather/India')
    assert response.status_code == 404
    assert response.data == b'Weather data not found for India'