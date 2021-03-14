import pytest

from common.users_info import TEST_LOGIN_YANDEX, TEST_PASSWORD_YANDEX

TEST_TOKEN = 'AgAAAABSDLD8AADLW-6snFdEfU8PqPO0Ei8p2tA'


@pytest.mark.yandex
class TestYaDisk:

    def test_get_and_rename_file(self, yandex_fixture, cluster):
        lp = yandex_fixture['login_page']
        cp = yandex_fixture['client_page']
        lp.open_full_url()
        lp.auth(TEST_LOGIN_YANDEX, TEST_PASSWORD_YANDEX)
        files = cluster.yandex_disk.get_user_files(token=TEST_TOKEN).decoded_body['items']
        filenames = sorted([el['name'] for el in files])
        cp.open_full_url()
        assert cp.get_all_filenames() == filenames
        # a = cp.get_all_filenames()
        # a = 'f'

