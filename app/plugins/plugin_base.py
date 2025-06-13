# Booking Synchronizer
#
# (c) 2025 Werneuchen IT - Filip Polsakiewicz
#
# File: plugin_base.py
# Desc: Base interface for plugins

from typing import Callable, Dict, Any

class PluginBase:
    def __init__(self):
        pass

    def get_event_handlers(self) -> Dict[str, Callable[[Any], None]]:
        """
        Should return a dict of event_type -> handler function
        Example:
        {
            "BookingCreated": self.handle_booking_created,
            "BookingDeleted": self.handle_booking_deleted,
        }
        """
        return {}
