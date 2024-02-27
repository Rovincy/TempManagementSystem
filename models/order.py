# models/order.py
from api.v1.app import db

class Order(db.Model):
    __tablename__ = 'Order'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
