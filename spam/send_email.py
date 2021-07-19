from typing import Union

class SendEmail:
    def send(self, sender: str, to: str, subject_matter: str, body: str) -> Union[str, None]:
        """ Enviar email (quem vai enviar/ para quem vai enviar/ assunto / mensagem)
        abstração dos parametros"""
        if '@' not in sender:
            raise EmailInvalid(f'E-mail do remetente inválido {sender}')
        return sender


class EmailInvalid(Exception):
    pass
