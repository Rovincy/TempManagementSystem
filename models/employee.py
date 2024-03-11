"""Employee Model"""

from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
import uuid

from models.Base import Base, BaseModel


class Employee(BaseModel, Base):
    __tablename__ = 'Employees'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    position = Column(String(100), nullable=False)
    date_of_employment = Column(DateTime, nullable=False)
    salary = Column(Float, nullable=False)
    address = Column(String(100), nullable=False)
    phone = Column(String(100), nullable=False)
    role = Column(String(100), nullable=False)
    reservations = relationship('Reservation', backref='employee', lazy=True)


    def __str__(self):
        return f'<Employee {self.name}>'
