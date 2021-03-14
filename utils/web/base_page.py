from utils.web.selenium_session import SeleniumSession


class BasePage:

    def __init__(self, session: 'SeleniumSession', service_name, service_url, host):
        self._driver = session.driver
        self._session = session
        self.host = host
        self.service_url = service_url
        self.service_name = service_name
        self.full_url = self.host + self.service_url

    @property
    def session(self):
        return self._session

    @property
    def driver(self):
        return self._driver

    def refresh(self):
        self.driver.refresh()

    def open_host(self):
        self.driver.get(self.host)

    def open_full_url(self):
        self.driver.get(self.full_url)
