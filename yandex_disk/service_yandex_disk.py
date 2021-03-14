from utils.api.api_request import ApiRequest
from utils.api.base_service import BaseService

PREFIX = '/v1/disk'


class ServiceYandexDisk(BaseService):
    def __init__(self, config, name='yandex_disk'):
        super().__init__(config, name)
        self.host_api = self.config['host_api'] + PREFIX

    def get_user_files(self, token):
        response = ApiRequest(
            url='/resources/files',
            service_url=self.host_api,
            method='GET',
            auth=self.BearerToken(token, token_type='OAuth'),
        ).perform()
        return response
