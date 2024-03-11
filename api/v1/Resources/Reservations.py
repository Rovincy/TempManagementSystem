from flask import jsonify
from flask_restful import Resource, abort, reqparse

from models import storage
from models.reservation import Reservation

reservation_post_args = reqparse.RequestParser()
reservation_post_args.add_argument('room_id', type=int, required=True, help='Room ID is required')
reservation_post_args.add_argument('customer_id', type=int, required=True, help='Customer ID is required')
reservation_post_args.add_argument('check_in_date', type=str, required=True, help='Check-in Date is required')
reservation_post_args.add_argument('check_out_date', type=str, required=True, help='Check-out Date is required')
reservation_post_args.add_argument('total_amount', type=float, required=True, help='Total Amount is required')
reservation_post_args.add_argument('status', type=str, required=True, help='Status is required')
reservation_post_args.add_argument('payment_status', type=str, required=True, help='Payment Status is required')
reservation_post_args.add_argument('date_issued', type=str, required=True, help='Date Issued is required')
reservation_post_args.add_argument('staff_id', type=int, required=True, help='Staff ID is required')


class ReservationResource(Resource):
    def post(self, reservation_id=None):
        if reservation_id:
            abort(400, message="Reservation ID must not be provided for post request.")
        args = reservation_post_args.parse_args()
        reservation_obj = Reservation(
            room_id=args['room_id'],
            customer_id=args['customer_id'],
            check_in_date=args['check_in_date'],
            check_out_date=args['check_out_date'],
            total_amount=args['total_amount'],
            status=args['status'],
            payment_status=args['payment_status'],
            date_issued=args['date_issued'],
            staff_id=args['staff_id']
        )
        # save reservation to database
        storage.new(reservation_obj)
        storage.save()

        return jsonify(reservation_obj), 201

    def get(self, reservation_id=None):
        if not reservation_id:
            return self.get_all()
        return self.get_reservation_by_id(reservation_id)

    def put(self, reservation_id=None):
        if not reservation_id:
            abort(400, message="Reservation ID must be provided for put request.")
        args = reservation_post_args.parse_args()
        reservation = Reservation.query.filter_by(id=reservation_id).first()
        if not reservation:
            abort(404, message="Reservation not found")
        reservation.room_id = args['room_id']
        reservation.customer_id = args['customer_id']
        reservation.check_in_date = args['check_in_date']
        reservation.check_out_date = args['check_out_date']
        reservation.total_amount = args['total_amount']
        reservation.status = args['status']
        reservation.payment_status = args['payment_status']
        reservation.date_issued = args['date_issued']
        reservation.staff_id = args['staff_id']
        storage.save()
        return jsonify(reservation), 200

    def delete(self, reservation_id=None):
        if not reservation_id:
            abort(400, message="Reservation ID must be provided for delete request.")
        reservation = Reservation.query.filter_by(id=reservation_id).first()
        if not reservation:
            abort(404, message="Reservation not found")
        storage.delete(reservation)
        storage.save()
        return '', 204

    def get_all(self):
        reservations = Reservation.query.all()
        return jsonify(reservations), 200

    def get_reservation_by_id(self, reservation_id):
        reservation = Reservation.query.filter_by(id=reservation_id).first()
        if not reservation:
            abort(404, message="Reservation not found")
        return jsonify(reservation), 200
