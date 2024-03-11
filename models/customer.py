"""Customer Model"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
import uuid

from models.Base import Base, BaseModel


class Customer(BaseModel, Base):
    __tablename__ = 'Customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(100), nullable=False)
    address = Column(String(100), nullable=False)
    status = Column(String(100), nullable=False)

    # Relationships
    reservations = relationship('Reservation', backref='customer', lazy=True)
    payments = relationship('Payment', backref='customer', lazy=True)


    def __str__(self):
        return f'<Customer {self.first_name} {self.last_name}>'
