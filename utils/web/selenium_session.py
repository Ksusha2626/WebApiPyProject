from utils.web.webdrivers import driver


class SeleniumSession:
    def __init__(self):
        self._driver = driver()

    @property
    def driver(self):
        return self._driver

    def destroy(self):
        self._driver.quit()
