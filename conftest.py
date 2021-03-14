import pytest

from utils.api.host_config import HostConfig
from utils.api.cluster_api import Cluster
from utils.web.selenium_session import SeleniumSession


def pytest_addoption(parser):
    parser.addoption(
        "--hostconf", action='store', help='full path to host_config.yml', default=None
    )


@pytest.fixture(scope='class', autouse=True)
def host_config(request):
    host_configuration = HostConfig(request.config.getoption("--hostconf"))
    return host_configuration.host_config


@pytest.fixture(scope='class')
def cluster(host_config):
    """A fixture to provide cluster config accordingly to given host_config.yaml and default"""
    cluster = Cluster(host_config)
    return cluster


@pytest.fixture(scope='class')
def app():
    session = SeleniumSession()
    yield session
    session.destroy()
