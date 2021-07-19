from spam.models import User


def test_save_user(session):
    user = User(name='Marco', email="marco@test.com")
    session.save(user)
    assert isinstance(user.id, int)


def test_list_all_user(session):
    users = [
        User(name='Marco', email="marco@test.com"),
        User(name='Marcia', email="marcia@test.com")
    ]
    for user in users:
        session.save(user)
    assert users == session.list_all()


# estrutura de um teste com conexão com banco de dados
# def test_save_user():  # teste exemplo
#     connect = Connect()  # classe conexao
#     session = connect.generate_session()  # gerar uma sessao no banco de dados
#     user = User(name='Marco')  # criar objeto
#     session.save(user)  # salvar objeto no banco dados atraves da sessao
#     assert isinstance(user.id, int)  # auto explicativo
#     session.roll_back()  # desfazer alterações no banco de dados
#     session.close()  # fechar sessao no banco de dados
#     connect.close()  # fechar conexao no banco de dados


