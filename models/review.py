"""Review model"""

from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
import uuid
from models.Base import Base, BaseModel


class Review(BaseModel, Base):
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    room_id = Column(Integer, ForeignKey('room.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(String(100), nullable=False)
    date = Column(DateTime, nullable=False)
