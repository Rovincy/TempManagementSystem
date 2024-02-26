from app import db
from datetime import datetime


class Booking(db.Model):
    __tablename__ = 'Bookings'
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)
    #customer_name = db.Column(db.String(100), nullable=False)
    check_in_date = db.Column(db.Date, nullable=False)
    check_out_date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    employee_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)

    # Relationships
    room = db.relationship("Room", back_populates="bookings")
    guest = db.relationship("Guest", back_populates="bookings")

    def __str__(self):
        return f'<Booking {self.id}>'
