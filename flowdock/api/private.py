"""Private api module for py-flowdock."""
#from flowdock.exceptions import FlowdockException
from flowdock.api import Configuration
from flowdock.api_client import ApiClient

class Private():
    """Private api module for py-flowdock."""
    def __init__(self):
        """Private api module for py-flowdock."""
        self.Configuration = Configuration
        self.ApiClient = ApiClient(Configuration)

    def list_private_conversations(self):
        """
        Lists the private conversations of the authenticated user.
        """
        return self.ApiClient.client(self.Configuration.private.get('list_private_conversations'))

    def get_private_conversations(self, msg_id):
        """
        Parameters:
        msg_id (int): flowdock private conversations id

        Get a private conversation.
        If no existing conversation between users is found, \
            a new conversation is automatically created with open attribute set to false.
        """
        qdata = self.Configuration.private.get('get_private_conversations')
        qdata.update({'api':qdata['api'].format(id=msg_id)})
        return self.ApiClient.client(qdata)
