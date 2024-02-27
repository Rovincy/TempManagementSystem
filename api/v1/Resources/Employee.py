from flask import jsonify
from flask_restful import Resource, abort, reqparse
from models.payment import Employee
from api.v1.app import api
from datetime import datetime

employee_post_args = reqparse.RequestParser()
employee_post_args.add_argument('name', type=str, required=True, help='Name is required')
employee_post_args.add_argument('email', type=str, required=True, help='Email is required')
employee_post_args.add_argument('position', type=str, required=True, help='Position is required')
employee_post_args.add_argument('date_of_employment', type=lambda x: datetime.strptime(x,'%Y-%m-%d %H:%M:%S'), required=True, help='Date of employment is required')
employee_post_args.add_argument('salary', type=float, required=True, help='Salary is required')
employee_post_args.add_argument('address', type=str, required=True, help='Address is required')
employee_post_args.add_argument('phone', type=str, required=True, help='Phone number is required')
employee_post_args.add_argument('role', type=str, required=True, help='Role is required')

class EmployeeResource(Resource):
    def post(self):
        args = employee_post_args.parse_args()
        employee = Employee(
            name=args['name'],
            email=args['email'],
            position=args['position'],
            date_of_employment=args['date_of_employment'],
            salary=args['salary'],
            address=args['address'],
            phone=args['phone'],
            role=args['role']
        )
        # save employee to database
        return jsonify(employee), 201

    def get(self, employee_id):
        employee = Employee.query.filter_by(id=employee_id).first()
        if not employee:
            abort(404, message="Employee not found")
        return jsonify(employee)

    def put(self, employee_id):
        args = employee_post_args.parse_args()
        employee = Employee.query.filter_by(id=employee_id).first()
        if not employee:
            abort(404, message="Employee not found")
        employee.name = args['name']
        employee.email = args['email']
        employee.position = args['position']
        employee.date_of_employment = args['date_of_employment']
        employee.salary = args['salary']
        employee.address = args['address']
        employee.phone = args['phone']
        employee.role = args['role']
        # db.session.commit()
        return jsonify(employee)

    def delete(self, employee_id):
        employee = Employee.query.filter_by(id=employee_id).first()
        if not employee:
            abort(404, message="Employee not found")
        # db.session.delete(employee)
        # db.session.commit()
        return '', 204

api.add_resource(EmployeeResource, '/employee/<int:employee_id>')
