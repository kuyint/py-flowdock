"""User api module for py-flowdock."""
#from flowdock.exceptions import FlowdockException
from flowdock.api import Configuration
from flowdock.api_client import ApiClient

class User():
    """user api module for py-flowdock."""
    def __init__(self):
        """user api module for py-flowdock."""
        self.Configuration = Configuration
        self.ApiClient = ApiClient(Configuration)

    def list_users(self):
        """
        List all users visible to the authenticated user
        """
        return self.ApiClient.client(self.Configuration.user.get('list'))

    def list_flow_users(self, flow):
        """
        Parameters:
        flow (str): flowdock user id

        List the users of a flow. \
            The user must belong to the organization and have access to the flow
        """
        qdata = self.Configuration.user.get('list_flow_users')
        qdata.update({'api':qdata['api'].format(flow=flow)})
        return self.ApiClient.client(qdata)

    def org_users(self):
        """
        List the users of an organization.
        """
        return self.ApiClient.client(self.Configuration.user.get('list_org_users'))

    def get_user(self, user_id):
        """
        Parameters:
        user_id (int): flowdock user id

        Get information about a single user.
        The requesting user must be belong to same organization as the target user.
        """
        qdata = self.Configuration.user.get('get_user')
        qdata.update({'api':qdata['api'].format(id=user_id)})
        return self.ApiClient.client(qdata)

    def remove_users(self, user_id):
        """
        Parameters:
        user_id (int): flowdock user id

        To remove a user from an organization,\
            you will need to have administrator rights to the organization.
        """
        qdata = self.Configuration.user.get('remove_users_org')
        qdata.update({'api':qdata['api'].format(id=user_id)})
        return self.ApiClient.client(qdata)

    def add_user_flow(self, flow, user_id):
        """
        Parameters:
        flow (int): flowdock flow name
        user_id (int): flowdock user id

        Add a user to a flow.
        The authenticated user and the target user must be members of the organization.
        """
        qdata = self.Configuration.user.get('add_user_flow')
        qdata.update({'api':qdata['api'].format(flow=flow)})
        qdata.update({'payload': {'id': user_id}})
        return self.ApiClient.client(qdata)
