from dataclasses import asdict

from sqlalchemy import select

from toro_test.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time: 
        new_user = User(
            username='julia', password='secretpassword', email='julia@tamagno.com.br'
        )
        session.add(new_user)
        session.commit()

    user = session.scalar(select(User).where(User.username == 'julia'))

    assert asdict(user) == { 
        'id': 1,
        'username': 'julia',
        'password': 'secretpassword',
        'email': 'julia@tamagno.com.br',
        'created_at': time,  
    }
