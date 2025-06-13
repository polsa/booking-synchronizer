# Booking Synchronizer
#
# (c) 2025 Werneuchen IT - Filip Polsakiewicz
#
# File: blocked_period.py
# Desc: BlockedPeriod API routes

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.models import blocked_period as blocked_period_model
from app.models import SessionLocal
from app.schemas import blocked_period as blocked_period_schema

from app.events.event_bus import event_bus

router = APIRouter(prefix="/blocked_periods", tags=["blocked_periods"])

# Dependency → DB Session bereitstellen
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create BlockedPeriod
@router.post("/", response_model=blocked_period_schema.BlockedPeriod)
def create_blocked_period(blocked_period: blocked_period_schema.BlockedPeriodCreate, db: Session = Depends(get_db)):
    db_blocked_period = blocked_period_model.BlockedPeriod(**blocked_period.dict())
    db.add(db_blocked_period)
    db.commit()
    event_bus.publish("BookingCreated", db_blocked_period.id)
    db.refresh(db_blocked_period)
    return db_blocked_period

# List all BlockedPeriods
@router.get("/", response_model=List[blocked_period_schema.BlockedPeriod])
def read_blocked_periods(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(blocked_period_model.BlockedPeriod).offset(skip).limit(limit).all()

# Get BlockedPeriod by ID
@router.get("/{blocked_period_id}", response_model=blocked_period_schema.BlockedPeriod)
def read_blocked_period(blocked_period_id: int, db: Session = Depends(get_db)):
    db_blocked_period = db.query(blocked_period_model.BlockedPeriod).filter(blocked_period_model.BlockedPeriod.id == blocked_period_id).first()
    if db_blocked_period is None:
        raise HTTPException(status_code=404, detail="BlockedPeriod not found")
    return db_blocked_period

# Delete BlockedPeriod by ID
@router.delete("/{blocked_period_id}")
def delete_blocked_period(blocked_period_id: int, db: Session = Depends(get_db)):
    db_blocked_period = db.query(blocked_period_model.BlockedPeriod).filter(blocked_period_model.BlockedPeriod.id == blocked_period_id).first()
    if db_blocked_period is None:
        raise HTTPException(status_code=404, detail="BlockedPeriod not found")
    db.delete(db_blocked_period)
    db.commit()
    event_bus.publish("BlockedPerionDeleted", blocked_period_id)
    return {"ok": True}
