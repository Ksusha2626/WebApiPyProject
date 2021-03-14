from selenium.common.exceptions import WebDriverException, TimeoutException
from utils.web.constants import DEFAULT_TIMEOUT
from selenium.webdriver.support.wait import WebDriverWait


class BaseElement:
    def __init__(self, driver):
        self.wd = driver

    def click_js(self, locator):
        """Click using JS"""
        self.wd.execute_script(f"""document.querySelector({locator}).click()""")

    def element_is_exist(self, locator, retry_count=2):
        for count in range(retry_count):
            try:
                WebDriverWait(self.wd, DEFAULT_TIMEOUT).until(
                    method=lambda _driver: _driver.find_element(*locator))
                return True
            except WebDriverException as error:
                if isinstance(error, TimeoutException):
                    return False
                if count == retry_count - 1:
                    raise error
        return False
