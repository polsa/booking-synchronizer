# Booking Synchronizer
#
# (c) 2025 Werneuchen IT - Filip Polsakiewicz
#
# File: booking.py
# Desc: Booking schemas

from pydantic import BaseModel
from datetime import date
from typing import Optional

class BookingBase(BaseModel):
    property_id: int
    guest_name: Optional[str] = None
    guest_email: Optional[str] = None
    guest_phone: Optional[str] = None
    number_of_guests: Optional[int] = None
    special_requests: Optional[str] = None
    check_in_date: date
    check_out_date: date
    income: Optional[float] = None
    fees: Optional[float] = None
    notes: Optional[str] = None

class BookingCreate(BookingBase):
    pass

class Booking(BookingBase):
    id: int

    class Config:
        from_attributes = True
