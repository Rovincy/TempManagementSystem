from api.v1.app import db


class Reservation(db.Model):
    __tablename__ = 'Reservation'
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    check_in_date = db.Column(db.DateTime, nullable=False)
    check_out_date = db.Column(db.DateTime, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(100), nullable=False)
    payment_status = db.Column(db.String(100), nullable=False)
    date_issued = db.Column(db.DateTime, nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)

    def __str__(self):
        return f'<Reservation {self.id}>'
