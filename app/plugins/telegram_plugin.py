# Booking Synchronizer
#
# (c) 2025 Werneuchen IT - Filip Polsakiewicz
#
# File: telegram_plugin.py
# Desc: Example plugin: Telegram notifications

import logging
from app.plugins.plugin_base import PluginBase

logger = logging.getLogger("booking_synchronizer.telegram_plugin")

class TelegramPlugin(PluginBase):
    def __init__(self):
        super().__init__()
        # Hier später Token / ChatID etc. einbauen
        self.enabled = True

    def get_event_handlers(self):
        return {
            "BookingCreated": self.handle_booking_created,
            "BookingDeleted": self.handle_booking_deleted,
        }

    def handle_booking_created(self, payload):
        if self.enabled:
            logger.info(f"[TelegramPlugin] BookingCreated → would send Telegram message with payload: {payload}")

    def handle_booking_deleted(self, payload):
        if self.enabled:
            logger.info(f"[TelegramPlugin] BookingDeleted → would send Telegram message with payload: {payload}")

# Required by PluginManager:
plugin_instance = TelegramPlugin()
