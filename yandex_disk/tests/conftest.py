import pytest

from yandex_disk.pages.client_disk.client_file_page import ClientPage
from yandex_passport.web.login.login_page import LoginPage


@pytest.fixture(scope='class')
def yandex_fixture(app, host_config):
    lp = LoginPage(app, host_config)
    cp = ClientPage(app, host_config)
    yield {'login_page': lp, 'client_page': cp}
