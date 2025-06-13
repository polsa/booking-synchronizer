# Booking Synchronizer
#
# (c) 2025 Werneuchen IT - Filip Polsakiewicz
#
# File: handlers.py
# Desc: Example event handlers (Logger)

import logging

logger = logging.getLogger("booking_synchronizer.handlers")

def log_event(payload):
    logger.info(f"[EVENT] Received event with payload: {payload}")
