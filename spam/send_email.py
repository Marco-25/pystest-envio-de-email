

class SendEmail:
    def __init__(self) -> None:
        self.__qtd_email_sent: int = 0

    @property
    def qtd_email_sent(self) -> int:
        return self.__qtd_email_sent

    @qtd_email_sent.setter
    def qtd_email_sent(self, value: int) -> None:
        self.__qtd_email_sent = value

    @staticmethod
    def send(self, sender: str, to: str, subject_matter: str, body: str) -> str:
        """ Função estatic*
        Enviar email (quem vai enviar/ para quem vai enviar/ assunto / mensagem)
        abstração dos parametros"""
        if '@' not in sender:
            raise EmailInvalid(f'E-mail do remetente inválido {sender}')
        self.qtd_email_sent += 1
        return sender


class EmailInvalid(Exception):
    pass
