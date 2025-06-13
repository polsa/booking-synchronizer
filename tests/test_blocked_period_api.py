# Booking Synchronizer
#
# (c) 2025 Werneuchen IT - Filip Polsakiewicz
#
# File: test_blocked_period_api.py
# Desc: Basic BlockedPeriod API tests

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_blocked_period():
    response = client.post(
        "/blocked_periods/",
        json={
            "property_id": 1,
            "reason": "Maintenance",
            "block_start_date": "2025-07-01",
            "block_end_date": "2025-07-05"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["property_id"] == 1
    assert data["reason"] == "Maintenance"

def test_read_blocked_periods():
    response = client.get("/blocked_periods/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_delete_blocked_period():
    # Assume ID 1 exists (from first test)
    response = client.delete("/blocked_periods/1")
    assert response.status_code == 200
    assert response.json()["ok"] is True
