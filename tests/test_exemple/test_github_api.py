from unittest.mock import Mock

import pytest

from exemple import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    avatar = "https://avatars.githubusercontent.com/u/44929191?v=4"
    resp_mock.json.return_value = {
        "avatar_url": avatar,
        "created_at": "2018-11-10T18:07:07Z",
        "updated_at": "2021-07-19T16:37:53Z"
    }
    get_mock = mocker.patch('exemple.github_api.requests.get')
    get_mock.return_value = resp_mock
    yield avatar


def test_search_avatar(avatar_url):
    url = github_api.search_avatar('Marco-25')
    assert avatar_url == url


def test_search_avatar_integration():
    url = github_api.search_avatar('Marco-25')
    assert 'https://avatars.githubusercontent.com/u/44929191?v=4' == url
