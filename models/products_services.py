from api.v1.app import db


class ProductAndService(db.Model):
    __tablename__ = 'ProductAndService'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price_per_unit = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    payments = db.relationship('Payment', backref='product_and_service', lazy=True)
