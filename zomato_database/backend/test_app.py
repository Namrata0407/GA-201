import pytest
from app import app
from bson import ObjectId

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

# Test for GET '/data'
def test_get_data(client):
    response = client.get('/data')
    assert response.status_code == 200
    data = response.get_json()
    # Add more specific tests here based on the expected response data

# Test for POST '/data'
def test_add_data(client):
    data = {
        'dish_name': 'New Dish',
        'price': 10.99,
        'availability': True
    }
    response = client.post('/data', json=data)
    assert response.status_code == 200
    result = response.get_json()
    assert 'id' in result
    # Optionally, check the database to verify that the document was added

# Test for PUT '/data/<id>'
def test_update_data(client):
    data = {
        'dish_name': 'Updated Dish',
        'price': 15.99,
        'availability': False
    }
    # Generate a valid ObjectId for testing
    valid_id = str(ObjectId())
    response = client.put(f'/data/{valid_id}', json=data)
    assert response.status_code == 200
    result = response.get_json()
    assert 'message' in result
    # Optionally, check the database to verify that the document was updated

# Test for DELETE '/data/<id>'
def test_delete_data(client):
    # Generate a valid ObjectId for testing
    valid_id = str(ObjectId())
    response = client.delete(f'/data/{valid_id}')
    assert response.status_code == 200
    result = response.get_json()
    assert 'message' in result
    # Optionally, check the database to verify that the document was deleted

# Test for POST '/order'
def test_order_data(client):
    data = {
        'dish_name': 'Ordered Dish',
        'price': 20.99,
        'username': 'user123'
    }
    response = client.post('/order', json=data)
    assert response.status_code == 200
    result = response.get_json()
    assert 'id' in result
    # Optionally, check the database to verify that the order was added

# Test for GET '/order'
def test_get_order(client):
    response = client.get('/order')
    assert response.status_code == 200
    data = response.get_json()
    # Add more specific tests here based on the expected response data

if __name__ == '__main__':
    pytest.main()
