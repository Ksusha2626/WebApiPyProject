from selenium.webdriver.support.wait import WebDriverWait
from utils.web.base_element import BaseElement
from utils.web.base_page import BasePage
from utils.web.constants import DEFAULT_TIMEOUT
from .login_page_locators import LoginPageLocators as Locators


class LoginPage(BasePage):
    def __init__(self, session, config):
        self.service_name = 'yandex_passport'
        self.host = config[self.service_name]['host']
        super().__init__(session=session,
                         service_name=self.service_name,
                         service_url='/auth',
                         host=self.host)

    def auth(self, email, password):
        self.driver.find_element(*Locators.LOGIN_INPUT).send_keys(email)
        self.driver.find_element(*Locators.SUBMIT_BUTTON).click()
        WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            method=lambda _driver: _driver.find_element(*Locators.PASSWORD_INPUT)
        ).send_keys(password)
        self.driver.find_element(*Locators.SUBMIT_BUTTON).click()
        BaseElement(self.driver).element_is_exist(Locators.CHECK_AUTH)
