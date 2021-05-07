"""Messages api module for py-flowdock."""
#from flowdock.exceptions import FlowdockException
from flowdock.api import Configuration
from flowdock.api_client import ApiClient

class Messages():
    """Messages api module for py-flowdock."""
    def __init__(self):
        """Messages api module for py-flowdock."""
        self.Configuration = Configuration
        self.ApiClient = ApiClient(Configuration)

    def list_msg(self):
        """ to do """
        return self.Configuration

    def list_msg_all(self):
        """ to do """
        return self.Configuration
