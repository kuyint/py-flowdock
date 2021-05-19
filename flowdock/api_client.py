"""api client module for py-flowdock"""
import requests
from flowdock.exceptions import ApiException
class ApiClient():
    """api client module for py-flowdock"""
    def __init__(self, config):
        """api client module for py-flowdock
        Parameters:
        config (class): config module

        """
        self.base_url = config.base_url
        self.ssl_verify = config.ssl_verify
        self.proxy = config.proxy
        self.auth = config.auth
        self.user_agent = {'User-Agent': 'py-flowdock client 1.0'}
        self.client_header = {'Content-Type': 'application/json'}
        self.client_header.update(self.user_agent)
        self.client_header = None
        print(self.client_header)

    def get(self, url, headers=None):
        """
        flowdock client get request method
        """
        return requests.get(url, auth=self.auth, headers=headers,
                            verify=self.ssl_verify, proxies=self.proxy)

    def put(self, url, headers=None,  data=None):
        """
        flowdock client put request method
        """
        return requests.put(url, auth=self.auth, headers=headers,
                            verify=self.ssl_verify, proxies=self.proxy, data=data)

    def post(self, url, headers=None, data=None):
        """
        flowdock client post request method
        """
        return requests.post(url, auth=self.auth, headers=headers,
                            verify=self.ssl_verify, proxies=self.proxy, data=data)

    def delete(self, url, headers=None, data=None):
        """
        flowdock client delete request method
        """
        return requests.delete(url, auth=self.auth, headers=headers,
                            verify=self.ssl_verify, proxies=self.proxy, data=data)

    def client(self, query_data):
        """
        Parameters:
        query_data (dict): api and request data

        flowdock client to sent api request
        """
        response = None

        url = self.base_url + query_data.get('api')
        if query_data.get('method') == 'GET':
            response = self.get(url, self.client_header)
        if query_data.get('method') == 'POST':
            response = self.post(url, self.client_header, data=query_data.get('payload'))
        if query_data.get('method') == 'DELETE':
            response = self.delete(url, self.client_header)
        if query_data.get('method') == 'PUT':
            response = self.put(url, self.client_header, data=query_data.get('payload'))
        if response.status_code not in [ 200, 201 ]:
            raise ApiException(response=response)
        return response.json()
