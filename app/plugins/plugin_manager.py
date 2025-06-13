# Booking Synchronizer
#
# (c) 2025 Werneuchen IT - Filip Polsakiewicz
#
# File: plugin_manager.py
# Desc: Plugin manager to load and register plugins

import logging
from app.events.event_bus import event_bus
from app.plugins import plugin_base
import importlib
import pkgutil
import app.plugins

logger = logging.getLogger("booking_synchronizer.plugins")

def load_plugins():
    logger.info("Loading plugins...")
    for _, module_name, _ in pkgutil.iter_modules(app.plugins.__path__):
        if module_name in ("plugin_base", "plugin_manager"):
            continue  # skip base/manager files
        module = importlib.import_module(f"app.plugins.{module_name}")
        if hasattr(module, "plugin_instance"):
            plugin_instance = getattr(module, "plugin_instance")
            if isinstance(plugin_instance, plugin_base.PluginBase):
                handlers = plugin_instance.get_event_handlers()
                for event_type, handler in handlers.items():
                    event_bus.subscribe(event_type, handler)
                logger.info(f"Registered plugin {module_name} with handlers: {list(handlers.keys())}")
            else:
                logger.warning(f"Plugin {module_name} does not implement PluginBase")
        else:
            logger.warning(f"Plugin {module_name} has no plugin_instance defined")
