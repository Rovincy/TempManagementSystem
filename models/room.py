"""Room model"""

from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship
import uuid
from models.Base import Base, BaseModel


class Room(BaseModel, Base):
    __tablename__ = 'Room'
    id = Column(Integer, primary_key=True)
    room_number = Column(Integer, nullable=False)
    room_type = Column(String(100), nullable=False)
    room_price_per_night = Column(Float, nullable=False)
    room_status = Column(String(100), nullable=False)
    amenities = Column(String(100), nullable=False)

    # Relationships
    reservations = relationship('Reservation', backref='room', lazy=True)

    def __str__(self):
        return f'<Room {self.room_number}>'
