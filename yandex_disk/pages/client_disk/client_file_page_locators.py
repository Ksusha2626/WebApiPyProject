from selenium.webdriver.common.by import By


class ClientPageLocators:
    FILE_ITEMS = (By.CLASS_NAME, 'clamped-text')
    FILENAMES = (By.CSS_SELECTOR, ".personal-info-login")
