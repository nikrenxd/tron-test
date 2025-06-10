import logging

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelname)s - %(asctime)s - %(name)s - %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": "INFO",
        },
    },
    "loggers": {
        "repositories.wallets": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        }
    },
}


def logging_init_config(logging_config: dict) -> None:
    logging.config.dictConfig(logging_config)
