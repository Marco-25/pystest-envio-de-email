from time import sleep
from typing import List

from spam.models import User


class Section:
    count: int = 0
    users: List[User] = []

    def save(self, user: User) -> None:
        """Salva um usuario em vetor"""
        Section.count += 1
        user.id = Section.count
        self.users.append(user)

    def list_all(self) -> List[User]:
        """Lista todos os usuarios no vetor"""
        return self.users

    def roll_back(self) -> None:
        """Limpa todos os usuario do vetor"""
        self.users.clear()

    def close(self) -> None:
        """Simula fechamento da conexão com banco de dados"""
        pass


class Connect:

    def __init__(self) -> None:
        sleep(1)

    @staticmethod
    def generate_session() -> Section:
        """Função estatica para gerar uma sessão"""
        return Section()

    def close(self) -> None:
        """Simula fechamento da conexão com banco de dados"""
        pass
