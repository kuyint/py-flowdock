"""Top-level package for py-flowdock."""

__author__ = """kuint"""
__email__ = 'kuintec@localhost'
__version__ = '0.1.0'

from flowdock import api
from flowdock.api.flow import Flow
from flowdock.api.org import Org
from flowdock.api.private import PrivateConv, PrivateMsg
from flowdock.api.messages import Messages
from flowdock.api.user import User

def Configuration(org, auth, ssl_verify=True, proxy=None):
    """
    Parameters:
    auth (str): flowdock auth(api_token, "") or (username, password)
    api_token (str): flowdock api_token
    ssl_verify (bool): flowdock api ssl verify
    proxy (dict): connect flowdock via proxy
    """
    api.Configuration.auth = auth
    api.Configuration.ssl_verify = ssl_verify
    api.Configuration.proxy = proxy
    api.Configuration.org = org
