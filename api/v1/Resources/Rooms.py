from flask import jsonify
from flask_restful import Resource, abort, reqparse
from models.room import Room
from api.v1.app import api

room_put_args = reqparse.RequestParser()
room_put_args.add_argument('room_number', type=int, required=True, help='Room number is required')
room_put_args.add_argument('room_type', type=str, required=True, help='Room type is required')
room_put_args.add_argument('room_price_per_night', type=float, required=True, help='Room price per night is required')
room_put_args.add_argument('room_status', type=str, required=True, help='Room status is required')
room_put_args.add_argument('amenities', type=str, required=True, help='Amenities are required')


class RoomResource(Resource):
    def get(self, room_id):
        room = Room.query.filter_by(id=room_id).first()
        if not room:
            abort(404, message="Room not found")
        return jsonify(room)

    def put(self, room_id):
        args = room_put_args.parse_args()
        room = Room.query.filter_by(id=room_id).first()
        if not room:
            abort(404, message="Room not found")
        room.room_number = args['room_number']
        room.room_type = args['room_type']
        room.room_price_per_night = args['room_price_per_night']
        room.room_status = args['room_status']
        room.amenities = args['amenities']
        # db.session.commit()
        return jsonify(room)


api.add_resource(RoomResource, '/room/<int:room_id>')
