"""
Config for LRUCache logger
"""

import sys


log_config = {
    "version": 1,
    "formatters": {
        "file": {
            "format": "%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s"
        },
        "stream": {
            "format": "%(name)s\t%(levelname)s\t%(message)s"
        }
    },
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "lru_cache.log",
            "formatter": "file"
        },
        "stream": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "stream": sys.stderr,
            "formatter": "stream"
        }
    },
    "loggers": {
        "file_logger": {
            "level": "INFO",
            "handlers": ["file"]
        },
        "stream_logger": {
            "level": "INFO",
            "handlers": ["stream"]
        },
    }
}
