"""Reservation Model"""

from sqlalchemy import Column, String, Integer, ForeignKey, Float, DateTime
import uuid
from models.Base import Base, BaseModel


class Reservation(BaseModel, Base):
    __tablename__ = 'Reservations'
    id = Column(Integer, primary_key=True)
    room_id = Column(Integer, ForeignKey('room.id'), nullable=False)
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    check_in_date = Column(DateTime, nullable=False)
    check_out_date = Column(DateTime, nullable=False)
    total_amount = Column(Float, nullable=False)
    status = Column(String(100), nullable=False)
    payment_status = Column(String(100), nullable=False)
    date_issued = Column(DateTime, nullable=False)
    staff_id = Column(Integer, ForeignKey('employee.id'), nullable=False)


    def __str__(self):
        return f'<Reservation {self.id}>'
