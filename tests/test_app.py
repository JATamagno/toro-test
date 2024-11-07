from http import HTTPStatus

from fastapi.testclient import TestClient

from toro_test.app import app


def test_root_must_return_ok_and_hello_world(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'julia',
            'email': 'julia@tamagno.com.br',
            'password': 'secretpassword',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'julia',
        'email': 'julia@tamagno.com.br',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'julia',
                'email': 'julia@tamagno.com.br',
                'id': 1,
            }
        ]
    }

def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'maria',
            'email': 'maria@test.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'maria',
        'email': 'maria@test.com',
        'id': 1,
    }

def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}
