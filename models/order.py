"""Order Model"""

from sqlalchemy import Column, Integer, ForeignKey, DateTime
from models.Base import Base, BaseModel
import uuid


class Order(BaseModel, Base):
    __tablename__ = 'Orders'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    date = Column(DateTime, nullable=False)
    total = Column(Integer, nullable=False)
