from api.v1.app import db


class Room(db.Model):
    __tablename__ = 'Room'
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.Integer, nullable=False)
    room_type = db.Column(db.String(100), nullable=False)
    room_price_per_night = db.Column(db.Float, nullable=False)
    room_status = db.Column(db.String(100), nullable=False)
    amenities = db.Column(db.String(100), nullable=False)

    # Relationships
    reservations = db.relationship('Reservation', backref='room', lazy=True)

    def __str__(self):
        return f'<Room {self.room_number}>'
