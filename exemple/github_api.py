import requests


def search_avatar(user: str) -> str:
    """ Busca o avatar de um usuario no GitHub """
    url: str = f'https://api.github.com/users/{user}'
    response = requests.get(url)
    return response.json()['avatar_url']


if __name__ == '__main__':
    print(search_avatar('Marco-25'))
