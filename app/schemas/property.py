# Booking Synchronizer
#
# (c) 2025 Werneuchen IT - Filip Polsakiewicz
#
# File: property.py
# Desc: Property schemas

from pydantic import BaseModel
from typing import Optional

class PropertyBase(BaseModel):
    name: str
    description: Optional[str] = None

class PropertyCreate(PropertyBase):
    pass

class Property(PropertyBase):
    id: int

    class Config:
        from_attributes = True
