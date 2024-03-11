#!/usr/bin/env python3

from flask import Flask, render_template
from flask_restful import Api
from flask_cors import CORS
from api.v1.Resources.Customer import CustomerResource
from api.v1.Resources.Employee import EmployeeResource
from api.v1.Resources.Order import OrderResource
from api.v1.Resources.Payment import PaymentResource
from api.v1.Resources.Reviews import ReviewResource
from api.v1.Resources.Rooms import RoomResource
from api.v1.Resources.Reservations import ReservationResource

app = Flask(__name__)
api = Api(app)
CORS(app)
api.add_resource(CustomerResource, '/customers', '/customers/<int:customer_id>')
api.add_resource(EmployeeResource, '/employees', '/employees/<int:employee_id>')
api.add_resource(OrderResource, '/orders', '/orders/<int:order_id>')
api.add_resource(PaymentResource, '/payments', '/payments/<int:payment_id>')
api.add_resource(ReviewResource, '/reviews', '/reviews/<int:review_id>')
api.add_resource(RoomResource, '/rooms', '/rooms/<int:room_id>')
api.add_resource(ReservationResource, '/reservations', '/reservations/<int:reservation_id>')


if __name__ == "__main__":
    app.run(debug=True)
