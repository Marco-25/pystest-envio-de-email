import pytest
from typing import List

from spam.main import SenderSpam
from spam.models import User
from spam.send_email import SendEmail


class SendEmailMock(SendEmail):
    """SendEmailMocke classe que simula a classe SendEmail
    O conceito de mock é trocar um objecto por outro
    """
    def __init__(self) -> None:
        super().__init__()
        self.__parameters_send: List[str] = []
        self.__qtd_email_sent: int = 0

    @property
    def parameters_send(self):
        return self.__parameters_send

    @parameters_send.setter
    def parameters_send(self, params: List[str]) -> None:
        self.__parameters_send = params

    @property
    def qtd_email_sent(self) -> int:
        return self.__qtd_email_sent

    @qtd_email_sent.setter
    def qtd_email_sent(self, value: int) -> None:
        self.__qtd_email_sent = value

    def send(self, sender: str, to: str, subject_matter: str, body: str) -> None:
        self.parameters_send = (sender, to, subject_matter, body)
        self.qtd_email_sent += 1


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
    email = SendEmailMock()
    sender_spam = SenderSpam(session, email)
    sender_spam.send_email(
        'remetente@teste.com',
        'assunto do email',
        'corpo do email (mensagem do email)'
    )
    assert len(users) == email.qtd_email_sent


def test_parameters_send_spam(session):
    user = User(name='Marco', email="marco@test.com")
    session.save(user)
    email = SendEmailMock()
    sender_spam = SenderSpam(session, email)
    sender_spam.send_email(
        'remetente_teste@teste.com',
        'assunto do email',
        'corpo do email (mensagem do email)'
    )
    assert email.parameters_send == (
        'remetente_teste@teste.com',
        'marco@test.com',
        'assunto do email',
        'corpo do email (mensagem do email)'
    )
