import json


class ApiError(Exception):
    """Represents an exception returned by the remote API."""
    def __init__(self, message):
        self.message = message

    def __str__(self):
        if isinstance(self.message, str):
            return self.message
        else:
            return json.dumps(self.message)
