# Booking Synchronizer
#
# (c) 2025 Werneuchen IT - Filip Polsakiewicz
#
# File: blocked_period.py
# Desc: BlockedPeriod schemas

from pydantic import BaseModel
from datetime import date
from typing import Optional

class BlockedPeriodBase(BaseModel):
    property_id: int
    reason: Optional[str] = None
    block_start_date: date
    block_end_date: date

class BlockedPeriodCreate(BlockedPeriodBase):
    pass

class BlockedPeriod(BlockedPeriodBase):
    id: int

    class Config:
        from_attributes = True
