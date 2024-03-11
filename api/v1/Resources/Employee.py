from flask import jsonify
from flask_restful import Resource, abort, marshal_with, reqparse
from models.employee import Employee
from models import storage


employee_post_args = reqparse.RequestParser()
employee_post_args.add_argument('name', type=str, required=True, help='Name is required')
employee_post_args.add_argument('email', type=str, required=True, help='Email is required')
employee_post_args.add_argument('position', type=str, required=True, help='Position is required')
employee_post_args.add_argument('date_of_employment', type=str, required=True, help='Date of Employment is required')
employee_post_args.add_argument('salary', type=float, required=True, help='Salary is required')
employee_post_args.add_argument('address', type=str, required=True, help='Address is required')
employee_post_args.add_argument('phone', type=str, required=True, help='Phone is required')
employee_post_args.add_argument('role', type=str, required=True, help='Role is required')


class EmployeeResource(Resource):
    def post(self, employee_id=None):
        if employee_id:
            abort(400, message="Employee ID must not be provided for post request.")
        args = employee_post_args.parse_args()
        employee_obj = Employee(
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
        storage.new(employee_obj)
        storage.save()

        return jsonify(employee_obj), 201

    def get(self, employee_id=None):
        if not employee_id:
            return self.get_all()
        return self.get_employee_by_id(employee_id)

    def put(self, employee_id=None):
        if not employee_id:
            abort(400, message="Employee ID must be provided for put request.")
        args = employee_post_args.parse_args()
        employee = storage.get(Employee, employee_id)
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
        storage.save()
        return jsonify(employee), 201

    def delete(self, employee_id=None):
        if not employee_id:
            abort(400, message="Employee ID must be provided for delete request.")
        employee = storage.get(Employee, employee_id)
        if not employee:
            abort(404, message="Employee not found")
        storage.delete(employee)
        storage.save()
        return '', 204

    def get_all(self):
        employees = storage.all(Employee)
        return jsonify(employees), 200

    def get_employee_by_id(self, employee_id):
        employee = storage.get(Employee, employee_id)
        if not employee:
            abort(404, message="Employee not found")
        return jsonify(employee), 200
