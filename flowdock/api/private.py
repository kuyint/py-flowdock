"""Private api module for py-flowdock."""
#from flowdock.exceptions import FlowdockException
from flowdock.api import Configuration
from flowdock.api_client import ApiClient

class PrivateConv():
    """A private conversation in CA Flowdock is like a chat room for only two users."""
    def __init__(self):
        """A private conversation in CA Flowdock is like a chat room for only two users."""
        self.Configuration = Configuration
        self.ApiClient = ApiClient(Configuration)

    def list_private_conversations(self):
        """
        Lists the private conversations of the authenticated user.
        """
        return self.ApiClient.client(self.Configuration.private_conversations.get('list_private_conversations'))

    def get_private_conversations(self, msg_id):
        """
        Parameters:
        msg_id (int): flowdock private conversations id

        Get a private conversation.
        If no existing conversation between users is found, \
            a new conversation is automatically created with open attribute set to false.
        """
        qdata = self.Configuration.private_conversations.get('get_private_conversations')
        qdata.update({'api':qdata['api'].format(id=msg_id)})
        return self.ApiClient.client(qdata)

class PrivateMsg():
    """Private message is a sub-resource for Private conversation. It should always be accessed in a private conversation’s context. """
    def __init__(self, user_id):
        """Private message is a sub-resource for Private conversation. It should always be accessed in a private conversation’s context. """
        self.Configuration = Configuration
        self.ApiClient = ApiClient(Configuration)
        self.user_id   = user_id

    def get_msgs(self, filter):
        """
        Lists messages from a Private conversation, filtered by parameters.
        """
        qdata = self.Configuration.private_msg.get('get_msgs')
        qdata.update({'api':qdata['api'].format(user_id=self.user_id)})
        return self.ApiClient.client(qdata)

    def get_msg(self, msg_id):
        """
        Parameters:
        msg_id (int): flowdock private message id

        Retrieve a message with the specified id.
        """
        qdata = self.Configuration.private_msg.get('get_msg')
        qdata.update({'api':qdata['api'].format(user_id=self.user_id, id=msg_id)})
        return self.ApiClient.client(qdata)
    
    def post_msg(self, content):
        """
        Parameters:
        content (str): message content

        Send a private chat message to the specified user.
        """
        qdata = self.Configuration.private_msg.get('post_msg')
        qdata.update({'api':qdata['api'].format(user_id=self.user_id)})
        qdata.update({'payload': { "event": "message", "content": content}})
        return self.ApiClient.client(qdata)
