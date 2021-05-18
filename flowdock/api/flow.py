"""flow api module for py-flowdock."""
#from flowdock.exceptions import FlowdockException
from flowdock.api import Configuration
from flowdock.api_client import ApiClient

class Flow():
    """flow api class for py-flowdock."""
    def __init__(self):
        """flow api module for py-flowdock."""
        self.Configuration = Configuration
        self.ApiClient = ApiClient(Configuration)
    def list_flows(self):
        """
        Lists the flows that the authenticated user is a member of.
        """
        return self.ApiClient.client(self.Configuration.flow.get('list'))
    def list_all_flows(self):
        """
        Lists the flows that the authenticated user has access to or can join.
        """
        return self.ApiClient.client(self.Configuration.flow.get('list_all'))

    def get_flow(self, name=None, flow_id=None):
        """
        Parameters:
        name (str): flowdock flow name.
        flow_id (int): flowdock flow id

        Get a single flow.
        Single flow information always includes the flow’s user list.
        """
        resp = {}
        if flow_id:
            qdata = self.Configuration.flow.get('get_flow_id')
            qdata.update({'api':qdata['api'].format(flow=flow_id)})
            resp = self.ApiClient.client(qdata)
        else:
            qdata = self.Configuration.flow.get('get_flow_name_org')
            qdata.update({'api':qdata['api'].format(flow=name)})
            resp = self.ApiClient.client(qdata)
        return resp

    def create_flow(self, name):
        """
        Parameters:
        name (str): flowdock flow name.

        Create a flow for the specified organization.
        """
        qdata = self.Configuration.flow.get('create_flow')
        qdata.update({'payload': {'name': name} })
        return self.ApiClient.client(qdata)

    # def update_flow(self, name, disabled=False, access_mode='organization', open=True):
    #     """
    #     Parameters:
    #     name	(str): New name of the flow (max. 100 characters)
    #     open	(bool): Boolean value (true or false). \
    #         If set to true and the user has not previously joined the flow, \
    #         the user will automatically be added to the flow.
    #     disabled (bool): Boolean value (true or false). \
    #         When set to true, the flow will disappear from users, \
    #         users will no longer be able to send messages to it \
    #         and users will not be able to join the flow. \
    #         The flow can be considered to be archived.
    #     access_mode	(str): How users see and access the flow. \
    #         Possible values are invitation (the flow is invite-only – \
    #         new members have to be explicitly invited or added by existing members),\
    #         link (anyone can join the flow by using the join_url) or organization \
    #         (in addition to using the link, anyone in the organization can join the flow.

    #     Update flow information.
    #     Only adminstrators can modify certain parts of the flow metadata.
    #     """
    #     qdata = self.Configuration.flow.get('create_flow_org')
    #     qdata.update({'payload': {'name': name} })
