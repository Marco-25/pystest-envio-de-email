import pytest

from spam.db import Connect


# abstração [conceito de setup do unittest]
# Ao passar um scope(module) a conexao com bd é feita somente uma vez
# Ao passar um scope(session) a conexao com bd é feita somente uma vez durante a sessao
@pytest.fixture(scope='session')
def connection():
    """Metodo de setup e teardown, roda uma conexao antes de rodar um teste e,
    logo apos fecha a conexão
    Ex:
        conexao
            bloco de teste
        fecha conexao
    """
    # setup
    connect_obj = Connect()
    yield connect_obj
    # apos o yield executa um teardown
    connect_obj.close()


# abstração [conceito de setup do unittest]
@pytest.fixture
def session(connection):
    """inicia uma sessao fazendo manipulações no banco de dados como [save/list/update/delete]"""
    session_obj = connection.generate_session()
    yield session_obj
    session_obj.roll_back()
    session_obj.close()
