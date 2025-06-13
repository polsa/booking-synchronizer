# Booking Synchronizer
#
# (c) 2025 Werneuchen IT - Filip Polsakiewicz
#
# File: test_booking_api.py
# Desc: Basic Booking API tests

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_booking():
    response = client.post(
        "/bookings/",
        json={
            "property_id": 1,
            "guest_name": "Test User",
            "guest_email": "test@example.com",
            "guest_phone": "123456789",
            "number_of_guests": 1,
            "special_requests": "None",
            "check_in_date": "2025-06-15",
            "check_out_date": "2025-06-16",
            "income": 100.0,
            "fees": 10.0,
            "notes": "Test Booking"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["property_id"] == 1
    assert data["guest_name"] == "Test User"

def test_read_bookings():
    response = client.get("/bookings/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_delete_booking():
    # Assume ID 1 exists (from first test)
    response = client.delete("/bookings/1")
    assert response.status_code == 200
    assert response.json()["ok"] is True
