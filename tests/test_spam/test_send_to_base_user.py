import pytest

from spam.main import SenderSpam
from spam.models import User
from spam.send_email import SendEmail


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
    email = SendEmail()
    sender_spam = SenderSpam(session, email)
    sender_spam.send_email(
        'remetente@teste.com',
        'assunto do email',
        'corpo do email (mensagem do email)'
    )
    assert len(users) == email.qtd_email_sent
