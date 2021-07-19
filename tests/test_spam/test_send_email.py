import pytest

from spam.send_email import SendEmail, EmailInvalid


def test_create_sender_email():
    send_email = SendEmail()
    assert send_email is not None


@pytest.mark.parametrize(
    'sender',
    ['marco@teste.com.br', 'foo@bar.com.br']
)
def test_sender(sender):
    send_email = SendEmail()
    # noinspection PyArgumentList
    result = send_email.send(
        sender,
        'marcoantn020@gmail.com',
        'Assunto teste',
        'Não sei exatamente o que colocar aqui.'
    )
    assert sender in result


@pytest.mark.parametrize(
    'sender',
    ['', 'foo']
)
def test_sender_invalid(sender):
    send_email = SendEmail()
    with pytest.raises(EmailInvalid):
        # noinspection PyArgumentList
        send_email.send(
            sender,
            'marcoantn020@gmail.com',
            'Assunto teste',
            'Não sei exatamente o que colocar aqui.'
        )

