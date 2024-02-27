from api.v1.app import db


class Customer(db.Model):
    __tablename__ = 'Customer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)

    # Relationships
    reservations = db.relationship('Reservation', backref='customer', lazy=True)
    payments = db.relationship('Payment', backref='customer', lazy=True)

    def __str__(self):
        return f'<Customer {self.first_name} {self.last_name}>'
