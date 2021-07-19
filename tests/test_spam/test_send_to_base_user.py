from unittest.mock import Mock

import pytest

from spam.main import SenderSpam
from spam.models import User


@pytest.mark.parametrize(
    'users',
    [
        [
            User(name='Marco', email="marco@test.com"),
            User(name='Marcia', email="marcia@test.com")
        ],
        [
            User(name='Marco', email="marco@test.com"),
        ]
    ]
)
def test_send_spam(session, users):
    for user in users:
        session.save(user)
    email = Mock()
    sender_spam = SenderSpam(session, email)
    sender_spam.send_email(
        'remetente@teste.com',
        'assunto do email',
        'corpo do email (mensagem do email)'
    )
    assert len(users) == email.send.call_count


def test_parameters_send_spam(session):
    user = User(name='Marco', email="marco@test.com")
    session.save(user)
    email = Mock()
    sender_spam = SenderSpam(session, email)
    sender_spam.send_email(
        'remetente_teste@teste.com',
        'assunto do email',
        'corpo do email (mensagem do email)'
    )
    email.send.assert_called_once_with(
        'remetente_teste@teste.com',
        'marco@test.com',
        'assunto do email',
        'corpo do email (mensagem do email)'
    )
