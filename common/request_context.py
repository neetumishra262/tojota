"""
Copyright Cerence, Inc. 2020.
All rights reserved.
The following software and implementation are protected by a number of pending patents.
"""

from structlog import get_logger
from contextvars import ContextVar

request_ctx = ContextVar("request_ctx")

class RequestContext:
    """
    Request context class for keeping track of information used during a request
    """

    def __init__(self):
        self.logger = get_logger()
        self.events = {}

    def set_logger(self, new_logger):
        self.logger = new_logger
