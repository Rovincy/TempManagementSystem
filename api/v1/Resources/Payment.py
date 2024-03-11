from flask import jsonify
from flask_restful import Resource, abort, reqparse
from models.payment import Payment
from models import storage

payment_post_args = reqparse.RequestParser()
payment_post_args.add_argument('guest_id', type=int, required=True, help='Guest ID is required')
payment_post_args.add_argument('amount', type=float, required=True, help='Amount is required')
payment_post_args.add_argument('date', type=str, required=True, help='Date is required')

class PaymentResource(Resource):
    def post(self, payment_id=None):
        if payment_id:
            abort(400, message="Payment ID must not be provided for post request.")
        args = payment_post_args.parse_args()
        payment_obj = Payment(
            guest_id=args['guest_id'],
            amount=args['amount'],
            date=args['date']
        )
        # save payment to database
        storage.new(payment_obj)
        storage.save()

        return jsonify(payment_obj), 201

    def get(self, payment_id=None):
        if not payment_id:
            return self.get_all()
        return self.get_payment_by_customer_id(payment_id)

    def delete(self, payment_id=None):
        if not payment_id:
            abort(400, message="Payment ID must be provided for delete request.")
        payment = Payment.query.filter_by(id=payment_id).first()
        if not payment:
            abort(404, message="Payment not found")
        storage.delete(payment)
        storage.save()
        return '', 204

    def get_all(self):
        payments = storage.all(Payment)
        return jsonify(payments), 200

    def get_payment_by_customer_id(self, payment_id):
        payment = storage.get(Payment, payment_id)
        if not payment:
            abort(404, message="Payment not found")
        return jsonify(payment), 200
