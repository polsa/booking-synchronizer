# Booking Synchronizer
#
# (c) 2025 Werneuchen IT - Filip Polsakiewicz
#
# File: booking.py
# Desc: Booking API routes

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.models import booking as booking_model
from app.models import SessionLocal
from app.schemas import booking as booking_schema

router = APIRouter(prefix="/bookings", tags=["bookings"])

# Dependency → DB Session bereitstellen
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Booking
@router.post("/", response_model=booking_schema.Booking)
def create_booking(booking: booking_schema.BookingCreate, db: Session = Depends(get_db)):
    db_booking = booking_model.Booking(**booking.dict())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

# List all Bookings
@router.get("/", response_model=List[booking_schema.Booking])
def read_bookings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(booking_model.Booking).offset(skip).limit(limit).all()

# Get Booking by ID
@router.get("/{booking_id}", response_model=booking_schema.Booking)
def read_booking(booking_id: int, db: Session = Depends(get_db)):
    db_booking = db.query(booking_model.Booking).filter(booking_model.Booking.id == booking_id).first()
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return db_booking

# Delete Booking by ID
@router.delete("/{booking_id}")
def delete_booking(booking_id: int, db: Session = Depends(get_db)):
    db_booking = db.query(booking_model.Booking).filter(booking_model.Booking.id == booking_id).first()
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    db.delete(db_booking)
    db.commit()
    return {"ok": True}
