from spam.send_email import SendEmail
from tests.test_spam.conftest import session


class SenderSpam:
    def __init__(self, session_obj: session, send: SendEmail) -> None:
        self.session: session = session_obj
        self.send_email: SendEmail = send

    def send_email(self, to_user_email: str, subject: str, body_obj: str) -> None:
        """Envia um e-mail ou varios e-mails"""
        for user in self.session.list_all():
            self.send_email.send(
                to_user_email,
                user.email,
                subject,
                body_obj
            )
