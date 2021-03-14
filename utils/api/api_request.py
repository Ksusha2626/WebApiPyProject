import logging
import sys

from pprint import pprint
from jsonmodels.models import Base
from requests import ReadTimeout, Session, Request
from utils.api.constants import DEFAULT_HEADER


class ApiRequest(Request):
    def __init__(self, url, service_url=None, method='POST', **kwargs):
        self.url = service_url + url

        if 'json' in kwargs.keys():
            if isinstance(kwargs['json'], Base):
                kwargs['json'] = kwargs['json'].to_struct()

        if 'headers' not in kwargs.keys():
            headers = DEFAULT_HEADER
        else:
            headers = kwargs['headers']
            del kwargs['headers']
        super(ApiRequest, self).__init__(url=self.url, method=method, headers=headers, **kwargs)

        self.prepared_request = self.prepare()
        self.session = Session()
        self.response = None

    def perform(self, check_ok=True, timeout=10):
        try:
            self.response = self.session.send(self.prepared_request, timeout=timeout)
        except ReadTimeout as e:
            logging.error(f"Failed to get answer for {e.request.method} to {e.request.path_url}")
            logging.error(f"Request header:\n {e.request.headers} \n")
            logging.error(f"Request body: \n {e.request.body} \n")
            raise e

        if len(self.response.content) > 0:
            try:
                self.response.decoded_body = self.response.json()
            except Exception as e:
                logging.warning(f"Can't decode JSON body\n{e}\n")
        if check_ok:
            try:
                assert self.response.ok
            except AssertionError:
                pprint(self.prepared_request.headers, stream=sys.stderr)
                pprint(self.response.headers, stream=sys.stderr)
                pprint(self.response.text, stream=sys.stderr)
        return self.response
