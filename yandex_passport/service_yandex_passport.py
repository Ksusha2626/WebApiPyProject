from utils.api.base_service import BaseService


class ServiceYandexPassport(BaseService):
    def __init__(self, config, name='yandex_passport'):
        super().__init__(config, name)
        self.host = self.host
