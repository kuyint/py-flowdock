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
        name (str):  parameterized_name of the flow
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
        name (str):  parameterized_name of the flow

        Create a flow for the specified organization.
        """
        qdata = self.Configuration.flow.get('create_flow')
        qdata.update({'payload': {'name': name} })
        return self.ApiClient.client(qdata)

    def rename_flow(self, current_flow_name, new_flow_name):
        """
        Parameters:
        current_flow_name (str): parameterized_name of the flow
        name	(str): New name of the flow (max. 100 characters)
        rename flowdock flow

        Only adminstrators can modify certain parts of the flow metadata.
        """
        qdata = self.Configuration.flow.get('update_flow')
        qdata.update({'payload': {'name': new_flow_name} })
        qdata.update({'api':qdata['api'].format(flow=current_flow_name)})
        
        return self.ApiClient.client(qdata)
    
    def delete_flow(self, name):
        """
        Parameters:
        name	(str):  parameterized_name of the flow to disable

        When set to true, the flow will disappear from users, \
        users will no longer be able to send messages to it \
        and users will not be able to join the flow. \
        The flow can be considered to be archived.

        Only adminstrators can modify certain parts of the flow metadata.
        """
        qdata = self.Configuration.flow.get('update_flow')
        qdata.update({'payload': {'disabled': 'true'} })
        qdata.update({'api':qdata['api'].format(flow=name)})
        return self.ApiClient.client(qdata)
    
    def flow_access_mode(self, name, access_mode):
        """
        Parameters:
        name (str):  parameterized_name of the flow
        access_mode	(str): How users see and access the flow. \
            Possible values are invitation (the flow is invite-only – \
            new members have to be explicitly invited or added by existing members),\
            link (anyone can join the flow by using the join_url) or organization \
            (in addition to using the link, anyone in the organization can join the flow.

        Only adminstrators can modify certain parts of the flow metadata.
        """
        qdata = self.Configuration.flow.get('update_flow')
        qdata.update({'payload': {'access_mode': access_mode} })
        qdata.update({'api':qdata['api'].format(flow=name)})
        return self.ApiClient.client(qdata)
