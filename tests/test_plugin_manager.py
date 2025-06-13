# Booking Synchronizer
#
# (c) 2025 Werneuchen IT - Filip Polsakiewicz
#
# File: test_plugin_manager.py
# Desc: Basic tests for plugin manager and event publishing

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.events.event_bus import event_bus

client = TestClient(app)

# Helper: Dummy handler to test EventBus publish
test_event_results = []

def dummy_handler(payload):
    test_event_results.append(payload)

def test_plugin_system_load_and_publish():
    # Subscribe dummy handler
    event_bus.subscribe("TestEvent", dummy_handler)

    # Publish TestEvent
    test_payload = {"key": "value"}
    event_bus.publish("TestEvent", test_payload)

    # Assert dummy handler was called with correct payload
    assert len(test_event_results) > 0
    assert test_event_results[-1] == test_payload
