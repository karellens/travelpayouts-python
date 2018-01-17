"""
Defines exceptions.
"""


class ApiError(Exception):
    """Represents an exception returned by the remote API."""
    def __init__(self, status, message=None):
        self.status = status
        self.message = message

    def __str__(self):
        if self.message is None:
            return self.status
        else:
            return "%s (%s)" % (self.status, self.message)