from flask import jsonify
from flask_restful import Resource, abort, marshal_with, reqparse
from models.customer import Customer
from models import storage


customer_post_args = reqparse.RequestParser()
customer_post_args.add_argument('first_name', type=str, required=True, help='First Name is required')
customer_post_args.add_argument('last_name', type=str, required=True, help='Last Name is required')
customer_post_args.add_argument('email', type=str, required=True, help='Email is required')
customer_post_args.add_argument('phone', type=str, required=True, help='Phone is required')
customer_post_args.add_argument('address', type=str, required=True, help='Address is required')
customer_post_args.add_argument('status', type=str, required=True, help='Status is required')


class CustomerResource(Resource):
    def post(self, customer_id=None):
        if customer_id:
            abort(400, message="Customer ID must not be provided for post request.")
        args = customer_post_args.parse_args()
        customer_obj = Customer(
            first_name=args['first_name'],
            last_name=args['last_name'],
            email=args['email'],
            phone=args['phone'],
            address=args['address'],
            status=args['status']
        )
        # save customer to database
        storage.new(customer_obj)
        storage.save()

        return jsonify(customer_obj), 201

    def get(self, customer_id=None):
        if not customer_id:
            return self.get_all()
        return self.get_customer_by_id(customer_id)

    def put(self, customer_id=None):
        if not customer_id:
            abort(400, message="Customer ID must be provided for put request.")
        args = customer_post_args.parse_args()
        customer = storage.get(Customer, customer_id)
        if not customer:
            abort(404, message="Customer not found")
        customer.first_name = args['first_name']
        customer.last_name = args['last_name']
        customer.email = args['email']
        customer.phone = args['phone']
        customer.address = args['address']
        customer.status = args['status']
        storage.save()
        return jsonify(customer), 201

    def delete(self, customer_id=None):
        if not customer_id:
            abort(400, message="Customer ID must be provided for delete request.")
        customer = storage.get(Customer, customer_id)
        if not customer:
            abort(404, message="Customer not found")
        storage.delete(customer)
        storage.save()
        return '', 204


    def get_all(self):
        customers = storage.all(Customer)
        return jsonify(customers), 200

    def get_customer_by_id(self, customer_id):
        customer = storage.get(Customer, customer_id)
        if not customer:
            abort(404, message="Customer not found")
        return jsonify(customer), 200
