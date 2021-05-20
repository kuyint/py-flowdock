
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

    def get_org(self, name=None, org_id=None):
        """
        Parameters:
        name (str):  parameterized_name of the org
        org_id (int): flowdock org id

        Get information about an organization using the parameterized name.
        The authenticated user must belong to the organization.
        """
        resp = {}
        if org_id:
            qdata = self.Configuration.organizations.get('find_org')
            qdata.update({'api':qdata['api'].format(id=org_id)})
            resp = self.ApiClient.client(qdata)
        else:
            qdata = self.Configuration.flow.get('get_org_name')
            qdata.update({'api':qdata['api'].format(org=name)})
            resp = self.ApiClient.client(qdata)
        return resp
