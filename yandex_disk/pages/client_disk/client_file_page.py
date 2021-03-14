from utils.web.base_page import BasePage
from utils.web.base_element import BaseElement
from .client_file_page_locators import ClientPageLocators as Locators


class ClientPage(BasePage):
    def __init__(self, session, config):
        self.service_name = 'yandex_disk'
        self.host = config[self.service_name]['host']
        super().__init__(session=session,
                         service_name=self.service_name,
                         service_url='/client/disk',
                         host=self.host)

    def get_all_filenames(self):
        names = []
        elements = self.driver.find_elements(*Locators.FILE_ITEMS)
        [names.append(el.text) for el in elements if el.text != 'Корзина']
        return sorted(names)

