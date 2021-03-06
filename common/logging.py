"""
Copyright Cerence, Inc. 2020.
All rights reserved.
The following software and implementation are protected by a number of pending patents.
"""

import uuid
import logging.config
import datetime
import structlog
from common.request_context import request_ctx

def configure_logging(level="INFO") -> None:
    """
    This method configures structured logging for the service by setting up the processors and other properties
    """

    shared_processors = [
        structlog.stdlib.add_log_level,
        structlog.processors.TimeStamper(fmt='%D %H:%M:%S.%f', utc=True),
        structlog.processors.format_exc_info
    ]

    logging.config.dictConfig({
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "structured": {
                "()": structlog.stdlib.ProcessorFormatter,
                "processor": structlog.processors.JSONRenderer(),
                "foreign_pre_chain": shared_processors
            }
        },
        "handlers": {
            "default": {
                "level": level,
                "class": "logging.StreamHandler",
                "formatter": "structured"
            }
        },
        "loggers": {
            "": {
                "handlers": ["default"],
                "level": level,
                "propagate": True
            }
        }
    })

    structlog.configure(
        processors=shared_processors + [
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter
        ],
        context_class=structlog.threadlocal.wrap_dict(dict),
        cache_logger_on_first_use=True,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger
    )

def get_new_id() -> str:
    """
    Generates an unique request identifier so a request could be traced through the logs.

    @return: Unique request identifier
    """

    return str(uuid.uuid4())

def set_session_event(name: str, timestamp: float = None) -> None:
    """
    Adds an event to the request session events entry.
    """
    ctx = request_ctx.get()

    event_time = timestamp
    if event_time is None:
        event_time = datetime.datetime.utcnow().timestamp()
    event_time = int(event_time * 1000)

    ctx.events["sessionEventTimes"].append({name: event_time})
