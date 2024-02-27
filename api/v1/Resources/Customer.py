from flask import jsonify
from flask_restful import Resource, abort, marshal_with, reqparse
from models.customer import Customer
from api.v1.app import api


customer_post_args = reqparse.RequestParser()
customer_post_args.add_argument('first_name', type=str, required=True, help='First Name is required')
customer_post_args.add_argument('last_name', type=str, required=True, help='Last Name is required')
customer_post_args.add_argument('email', type=str, required=True, help='Email is required')
customer_post_args.add_argument('phone', type=str, required=True, help='Phone is required')
customer_post_args.add_argument('address', type=str, required=True, help='Address is required')
customer_post_args.add_argument('status', type=str, required=True, help='Status is required')


class CustomerResource(Resource):
    def post(self, customer_id=None):
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
        return jsonify(customer_obj), 201

    def get(self, customer_id):
        customer = Customer.query.filter_by(id=customer_id).first()
        if not customer:
            abort(404, message="Customer not found")
        return jsonify(customer)

    def put(self, customer_id):
        args = customer_post_args.parse_args()
        customer = Customer.query.filter_by(id=customer_id).first()
        if not customer:
            abort(404, message="Customer not found")
        customer.first_name = args['first_name']
        customer.last_name = args['last_name']
        customer.email = args['email']
        customer.phone = args['phone']
        customer.address = args['address']
        customer.status = args['status']
        # db.session.commit()
        return jsonify(customer)

    def delete(self, customer_id):
        customer = Customer.query.filter_by(id=customer_id).first()
        if not customer:
            abort(404, message="Customer not found")
        # db.session.delete(customer)
        # db.session.commit()
        return '', 204



api.add_resource(CustomerResource, '/customer/<int:customer_id>')
