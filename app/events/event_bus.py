# Booking Synchronizer
#
# (c) 2025 Werneuchen IT - Filip Polsakiewicz
#
# File: event_bus.py
# Desc: Simple Event Bus for publishing and subscribing to application events

import logging
from typing import Callable, Dict, List, Any

logger = logging.getLogger("booking_synchronizer.events")

class EventBus:
    def __init__(self):
        self._subscribers: Dict[str, List[Callable[[Any], None]]] = {}

    def subscribe(self, event_type: str, handler: Callable[[Any], None]):
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        self._subscribers[event_type].append(handler)
        logger.info(f"Subscribed handler {handler.__name__} to event {event_type}")

    def publish(self, event_type: str, payload: Any):
        logger.info(f"Publishing event {event_type} with payload {payload}")
        handlers = self._subscribers.get(event_type, [])
        for handler in handlers:
            try:
                handler(payload)
            except Exception as e:
                logger.error(f"Error handling event {event_type} in {handler.__name__}: {e}")

# Singleton instance
event_bus = EventBus()
