"""exception module for py-flowdock"""
class FlowdockException(Exception):
    """The base exception class for all py-flowdock exception"""

class ApiException(FlowdockException):
    """api exception module for py-flowdock"""
    def __init__(self, response=None):
        """
        Parameters:
        response (<response>): response from flowdock api

        api exception module for py-flowdock
        """
        self.status = response.status_code
        self.reason = response.reason
        self.body = response.content
        self.headers = response.headers
        print(self.status)
        print(self.reason)

    def __str__(self):
        """Custom error messages for exception"""
        error_message = "({0})\n"\
                        "Reason: {1}\n".format(self.status, self.reason)
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(
                self.headers)

        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)

        return error_message

class ApiValueError(FlowdockException):
    """api value error exception for py-flowdock"""
    def __init__(self, msg):
        """
        Parameters:
            msg (str): the exception message
        """
        self.msg = msg
    def __str__(self):
        """Custom error messages for exception"""
        error_message = "error\n"\
                        "Reason: {1}\n".format(self.msg)
        return error_message
