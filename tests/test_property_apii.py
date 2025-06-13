# Booking Synchronizer
#
# (c) 2025 Werneuchen IT - Filip Polsakiewicz
#
# File: test_property_api.py
# Desc: Basic Property API tests

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_property():
    response = client.post(
        "/properties/",
        json={
            "name": "My Test Property",
            "description": "A beautiful place to stay"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "My Test Property"

def test_read_properties():
    response = client.get("/properties/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_delete_property():
    # Assume ID 1 exists (from first test)
    response = client.delete("/properties/1")
    assert response.status_code == 200
    assert response.json()["ok"] is True
