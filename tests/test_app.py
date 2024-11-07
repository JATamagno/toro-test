from http import HTTPStatus
from toro_test.schemas import UserPublic


def test_root_must_return_ok_and_hello_world(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World'}


def test_create_user(client):
    response = client.post(
        '/users',
        json={
            'username': 'julia',
            'email': 'julia@tamagno.com.br',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'julia',
        'email': 'julia@tamagno.com.br',
        'id': 1,
    }

def test_read_users(client):
    response = client.get('/users')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}

def test_read_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.json() == {'users': [user_schema]}

def test_update_user(client, user):
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

def test_update_integrity_error(client, user):
    client.post(
        '/users',
        json={
            'username': 'joao',
            'email': 'joao@example.com',
            'password': 'passwordsecret',
        },
    )

    response_update = client.put(
        f'/users/{user.id}',
        json={
            'username': 'joao',
            'email': 'maria@test.com',
            'password': 'passwordsecret',
        },
    )


def test_delete_user(client, user):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}
