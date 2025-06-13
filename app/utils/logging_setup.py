# Booking Synchronizer
#
# (c) 2025 Werneuchen IT - Filip Polsakiewicz
#
# File: logging_setup.py
# Desc: Configure logging for the application

import logging
from uvicorn.logging import DefaultFormatter

def setup_logging():
    formatter = DefaultFormatter(fmt="%(levelprefix)s %(message)s", use_colors=True)

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.handlers = []  # Clear existing handlers
    root_logger.addHandler(handler)

    # Booking Synchronizer loggers → ensure INFO level
    logging.getLogger("booking_synchronizer").setLevel(logging.INFO)
    logging.getLogger("booking_synchronizer.events").setLevel(logging.INFO)
    logging.getLogger("booking_synchronizer.handlers").setLevel(logging.INFO)
