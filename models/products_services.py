"""Product and service Model"""

import uuid
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship

from models.Base import Base, BaseModel


class ProductAndService(BaseModel, Base):
    __tablename__ = 'ProductsAndServices'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price_per_unit = Column(Float, nullable=False)
    Stock = Column(Integer, nullable=False)
    payments = relationship('Payment', backref='product_and_service', lazy=True)


    def __init__(self):
        self.id = uuid.uuid4()
