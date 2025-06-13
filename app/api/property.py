# Booking Synchronizer
#
# (c) 2025 Werneuchen IT - Filip Polsakiewicz
#
# File: property.py
# Desc: Property API routes

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.models import property as property_model
from app.models import SessionLocal
from app.schemas import property as property_schema

from app.events.event_bus import event_bus

router = APIRouter(prefix="/properties", tags=["properties"])

# Dependency → DB Session bereitstellen
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Property
@router.post("/", response_model=property_schema.Property)
def create_property(property: property_schema.PropertyCreate, db: Session = Depends(get_db)):
    db_property = property_model.Property(**property.dict())
    db.add(db_property)
    db.commit()
    event_bus.publish("PropertyCreated", db_property.id)
    db.refresh(db_property)
    return db_property

# List all Properties
@router.get("/", response_model=List[property_schema.Property])
def read_properties(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(property_model.Property).offset(skip).limit(limit).all()

# Get Property by ID
@router.get("/{property_id}", response_model=property_schema.Property)
def read_property(property_id: int, db: Session = Depends(get_db)):
    db_property = db.query(property_model.Property).filter(property_model.Property.id == property_id).first()
    if db_property is None:
        raise HTTPException(status_code=404, detail="Property not found")
    return db_property

# Delete Property by ID
@router.delete("/{property_id}")
def delete_property(property_id: int, db: Session = Depends(get_db)):
    db_property = db.query(property_model.Property).filter(property_model.Property.id == property_id).first()
    if db_property is None:
        raise HTTPException(status_code=404, detail="Property not found")
    db.delete(db_property)
    db.commit()
    event_bus.publish("PropertyDeleted", property_id)
    return {"ok": True}
