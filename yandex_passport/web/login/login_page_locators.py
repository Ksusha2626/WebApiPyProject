from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_INPUT = (By.XPATH, "//input[@id='passp-field-login']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='passp-field-passwd']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    CHECK_AUTH = (By.CSS_SELECTOR, ".personal-info-login")
