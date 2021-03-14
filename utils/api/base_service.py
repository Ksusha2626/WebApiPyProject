class BaseService:
    def __init__(self, config: dict, name):
        self.config = config
        self.service_name = name
        self.host = self.config['host']

    class BearerToken:
        def __init__(self, token, auth_name='Authorization', token_type='Bearer', **kwargs):
            self.token_type = token_type
            self._token = token
            self._new_header_params = kwargs
            self._auth_name = auth_name

        def __call__(self, r):
            r.headers[self._auth_name] = self.token_type + ' ' + self._token
            r.headers.update(self._new_header_params)
            return r
