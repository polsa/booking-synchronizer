# Booking Synchronizer
#
# (c) 2025 Werneuchen IT - Filip Polsakiewicz
#
# File: main.py
# Desc: Main FastAPI entrypoint
#

from fastapi import FastAPI

app = FastAPI(
    title="Booking Synchronizer",
    version="0.1.0"
)

@app.get("/")
def read_root():
    return {"message": "Booking Synchronizer API is running 🚀"}
