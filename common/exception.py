"""
Copyright Cerence, Inc. 2020.
All rights reserved.
The following software and implementation are protected by a number of pending patents.
"""


class ModelError(Exception):
    def __init__(self, msg, **kwargs):
        super().__init__()
        self.msg = msg
        self.kwargs = kwargs

    def __str__(self):
        return self.msg


class BadRequest(ModelError):
    def __init__(self, msg, **kwargs):
        super().__init__(msg, **kwargs)


class VersionNotFoundError(ModelError):
    def __init__(self, msg, **kwargs):
        super().__init__(msg, **kwargs)


class SessionNotFoundError(ModelError):
    def __init__(self, msg, **kwargs):
        super().__init__(msg, **kwargs)
