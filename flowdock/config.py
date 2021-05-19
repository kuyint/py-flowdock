"""py-flowdock config module"""
class FlowdockConfig():
    """py-flowdock config module"""
    def __init__(self, auth=tuple, org=str, ssl_verify=True, proxy=dict):
        """py-flowdock config module"""
        self.base_url = "https://api.flowdock.com"
        self.auth = auth
        self.org = org
        self.ssl_verify = ssl_verify
        self.proxy = proxy
    @property
    def flow(self):
        """
        dict of flow api's
        """
        return {
        'list': {
        'method' : 'GET',
        'api': '/flows'
        },
        'list_all':{
            'method': 'GET',
            'api': '/flows/all'
        },
        'get_flow_id': {
            'method': 'GET',
            'api': '/flows/find?id={flow}'
        },
        'get_flow_name_org': {
            'method': 'GET',
            'api': '/flows/' + self.org + '/{flow}'
        },
        'create_flow': {
            'method': 'POST',
            'api': '/flows/' + self.org,
            'payload': {
                'name': '{flow}'
            }
            },
        'update_flow': {
            'method': 'PUT',
            'api': '/flows/' + self.org + '/{flow}',
            'payload':{
                    "name": '{name}',
                    "disabled": False,
                    "access_mode": "organization",
                    'open' : True
                    }
        },
        }

    @property
    def user(self):
        """
        dict of user api's
        """
        return  {
        'list': {
        'method' : 'GET',
        'api': '/users'
        },
        'list_flow_users': {
        'method' : 'GET',
        'api': '/flows/' + self.org + '/{flow}/users'
        },
        'list_org_users': {
        'method' : 'GET',
        'api': '/organizations/' + self.org + '/users'
        },
        'remove_users_org': {
        'method' : 'DELETE',
        'api': '/organizations/' + self.org + '/users/{id}'
        },
        'get_user': {
        'method' : 'GET',
        'api': '/users/{id}'
        },
        'add_user_flow': {
        'method' : 'POST',
        'api': '/flows/' + self.org + '/{flow}/users',
        'payload': {
            "id": '{id}'
            }
        },
        }

    @property
    def private_conversations(self):
        """
        dict of private api's
        """
        return {
        'list_private_conversations': {
        'method' : 'GET',
        'api': '/private'
        },
        'get_private_conversations': {
        'method' : 'GET',
        'api': '/private/{id}'
        },
        }

    @property
    def organizations(self):
        """
        dict of organizations api's
        """
        return{
            'list_org' : {
                'method': 'GET',
                'api': '/organizations'
            },
            'get_org_name': {
                'method': 'GET',
                'api': '/organizations/{org}'
            },
            'find_org' : {
                'method': 'GET',
                'api': '/organizations/find?id={id}'
            },
            'update_org' : {
                'method': 'PUT',
                'api': '/organizations/{parameterized_name}',
                'payload': {
                    "name": "{displayName}"
                }
            }
        }

    @property
    def private_msg(self):
        return {
            'get_msgs' : {
                'method': 'GET',
                'api': '/private/{user_id}/messages'
            },
            'post_msg' : {
                'method': 'POST',
                'api': '/private/{user_id}/messages'
            },
            'get_msg' : {
                'method': 'GET',
                'api': '/private/{user_id}/messages/{id}',
                'payload': {
                            "event": "message",
                            "content": None
                            }
            },
        }
