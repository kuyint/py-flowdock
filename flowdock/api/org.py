
"""Org api module for py-flowdock."""
#from flowdock.exceptions import FlowdockException
from flowdock.api import Configuration
from flowdock.api_client import ApiClient

class Org():
    """Org api class for py-flowdock."""
    def __init__(self):
        """Org api module for py-flowdock."""
        self.Configuration = Configuration
        self.ApiClient = ApiClient(Configuration)

    def list_org(self):
        """
        List organizations of the authenticated user.
        """
        return self.ApiClient.client(self.Configuration.organizations.get('list_org'))

    def get_org(self, org_id):
        """
        Parameters:
        org_id (int): flowdock org id.

        Get information about an organization using the parameterized name.
        The authenticated user must belong to the organization.
        """
        qdata = self.Configuration.organizations.get('find_org')
        qdata.update({'api':qdata['api'].format(id=org_id)})
        return self.ApiClient.client(qdata)
