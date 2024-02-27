from api.v1.app import db

class Employee(db.Model):
    __tablename__ = 'Employee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    date_of_employment = db.Column(db.DateTime, nullable=False)
    salary = db.Column(db.Float, nullable=False)
    address = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    reservations = db.relationship('Reservation', backref='employee', lazy=True)

    def __str__(self):
        return f'<Employee {self.name}>'
