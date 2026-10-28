
# Flask API Tests
# This file tests the GET and POST endpoints
# to make sure they return the correct results.

import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


# Test the hello endpoint with a name
def test_hello_with_name(client):
    response = client.get('/hello?name=Nia')

    assert response.status_code == 200
    assert response.get_json() == {'message': 'Hello, Nia!'}


# Test the hello endpoint without a name
def test_hello_without_name(client):
    response = client.get('/hello')

    assert response.status_code == 200
    assert response.get_json() == {'message': 'Hello, World!'}


# Test the sum endpoint with valid numbers
def test_sum_valid(client):
    response = client.post('/sum', json={'numbers': [1, 2, 3]})

    assert response.status_code == 200
    assert response.get_json() == {'sum': 6}


# Test the sum endpoint with a missing field
def test_sum_missing_numbers(client):
    response = client.post('/sum', json={})

    assert response.status_code == 400
    assert 'error' in response.get_json()


# Test the sum endpoint with invalid data
def test_sum_invalid_numbers(client):
    response = client.post('/sum', json={'numbers': [1, 'hello', 3]})

    assert response.status_code == 400
    assert 'error' in response.get_json()


# Test the sum endpoint with an incorrect data type
def test_sum_not_a_list(client):
    response = client.post('/sum', json={'numbers': '123'})

    assert response.status_code == 400
    assert 'error' in response.get_json()


# Test the sum endpoint with malformed JSON
def test_sum_malformed_json(client):
    response = client.post(
        '/sum',
        data='{"numbers": [1, 2,',
        content_type='application/json'
    )

    assert response.status_code == 400
    assert 'error' in response.get_json()
