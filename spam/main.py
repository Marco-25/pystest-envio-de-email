from spam.db import Section
from spam.send_email import SendEmail


class SenderSpam:
    def __init__(self, session_obj: Section, send: SendEmail) -> None:
        self.session: Section = session_obj
        self.send_email_obj: SendEmail = send

    def send_email(self, to_user_email: str, subject: str, body_obj: str) -> None:
        """Envia um e-mail ou varios e-mails"""
        for user in self.session.list_all():
            self.send_email_obj.send(
                to_user_email,
                user.email,
                subject,
                body_obj
            )
