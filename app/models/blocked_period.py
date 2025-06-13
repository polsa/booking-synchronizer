# Booking Synchronizer
#
# (c) 2025 Werneuchen IT - Filip Polsakiewicz
#
# File: blocked_period.py
# Desc: Blocked period model

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.models import Base

class BlockedPeriod(Base):
    __tablename__ = "blocked_periods"

    id = Column(Integer, primary_key=True, index=True)
    property_id = Column(Integer, ForeignKey("properties.id"), nullable=False)
    reason = Column(String, nullable=True)
    block_start_date = Column(Date, nullable=False)
    block_end_date = Column(Date, nullable=False)

    property = relationship("Property")
