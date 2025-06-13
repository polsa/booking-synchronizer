# Booking Synchronizer
#
# (c) 2025 Werneuchen IT - Filip Polsakiewicz
#
# File: main.py
# Desc: Main FastAPI entrypoint
#

from fastapi import FastAPI
from app.models import Base, engine
from app.models import property, booking, blocked_period
from app.api import booking as booking_api, blocked_period as blocked_period_api, property as property_api
from app.events.event_bus import event_bus
from app.events import handlers

from app.utils.logging_setup import setup_logging
from app.plugins.plugin_manager import load_plugins

setup_logging()
app = FastAPI(
    title="Booking Synchronizer",
    version="0.1.0"
)

app.include_router(booking_api.router)
app.include_router(blocked_period_api.router)
app.include_router(property_api.router)


# Initialize DB
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Booking Synchronizer API is running 🚀"}

# Register example handler
event_bus.subscribe("BookingCreated", handlers.log_event)
event_bus.subscribe("BookingDeleted", handlers.log_event)
event_bus.subscribe("BlockedPeriodCreated", handlers.log_event)
event_bus.subscribe("BlockedPeriodDeleted", handlers.log_event)
event_bus.subscribe("PropertyCreated", handlers.log_event)
event_bus.subscribe("PropertyDeleted", handlers.log_event)

load_plugins()