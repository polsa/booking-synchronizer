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
from app.api import booking as booking_api, blocked_period as blocked_period_api
app = FastAPI(
    title="Booking Synchronizer",
    version="0.1.0"
)

app.include_router(booking_api.router)
app.include_router(blocked_period_api.router)

# Initialize DB
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Booking Synchronizer API is running 🚀"}
