"""Payment Model"""

from sqlalchemy import Column, Integer, ForeignKey, Float, DateTime
from models.Base import Base, BaseModel
import uuid


class Payment(BaseModel, Base):
    __tablename__ = 'Payments'
    id = Column(Integer, primary_key=True)
    guest_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(DateTime, nullable=False)
