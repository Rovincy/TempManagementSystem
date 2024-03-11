from flask import jsonify
from flask_restful import Resource, abort, reqparse
from models.order import Order
from models import storage

order_post_args = reqparse.RequestParser()
order_post_args.add_argument('customer_id', type=int, required=True, help='Customer ID is required')
order_post_args.add_argument('date', type=str, required=True, help='Date is required')
order_post_args.add_argument('total', type=int, required=True, help='Total is required')

class OrderResource(Resource):
    def post(self, order_id=None):
        if order_id:
            abort(400, message="Order ID must not be provided for post request.")
        args = order_post_args.parse_args()
        order_obj = Order(
            customer_id=args['customer_id'],
            date=args['date'],
            total=args['total']
        )
        # save order to database
        storage.new(order_obj)
        storage.save()

        return jsonify(order_obj), 201

    def get(self, order_id=None):
        if not order_id:
            return self.get_all()
        return self.get_order_by_id(order_id)

    def put(self, order_id=None):
        if not order_id:
            abort(400, message="Order ID must be provided for put request.")
        args = order_post_args.parse_args()
        order = storage.get(Order, order_id)
        if not order:
            abort(404, message="Order not found")
        order.customer_id = args['customer_id']
        order.date = args['date']
        order.total = args['total']
        storage.save()
        return jsonify(order), 200

    def delete(self, order_id=None):
        if not order_id:
            abort(400, message="Order ID must be provided for delete request.")
        order = storage.get(Order, order_id)
        if not order:
            abort(404, message="Order not found")
        storage.delete(order)
        storage.save()
        return '', 204

    def get_all(self):
        orders = storage.all(Order)
        return jsonify(orders), 200

    def get_order_by_id(self, order_id):
        order = storage.get(Order, order_id)
        if not order:
            abort(404, message="Order not found")
        return jsonify(order), 200
