from flask import jsonify
from flask_restful import Resource, abort, reqparse
from models.room import Room
from models import storage

room_post_args = reqparse.RequestParser()
room_post_args.add_argument('room_number', type=int, required=True, help='Room Number is required')
room_post_args.add_argument('room_type', type=str, required=True, help='Room Type is required')
room_post_args.add_argument('room_price_per_night', type=float, required=True, help='Room Price Per Night is required')
room_post_args.add_argument('room_status', type=str, required=True, help='Room Status is required')
room_post_args.add_argument('amenities', type=str, required=True, help='Amenities are required')


class RoomResource(Resource):
    def post(self, room_id=None):
        if room_id:
            abort(400, message="Room ID must not be provided for post request.")
        args = room_post_args.parse_args()
        room_obj = Room(
            room_number=args['room_number'],
            room_type=args['room_type'],
            room_price_per_night=args['room_price_per_night'],
            room_status=args['room_status'],
            amenities=args['amenities']
        )
        # save room to database
        storage.new(room_obj)
        storage.save()

        return jsonify(room_obj), 201

    def get(self, room_id=None):
        if not room_id:
            return self.get_all()
        return self.get_room_by_id(room_id)

    def put(self, room_id=None):
        if not room_id:
            abort(400, message="Room ID must be provided for put request.")
        args = room_post_args.parse_args()
        room = Room.query.filter_by(id=room_id).first()
        if not room:
            abort(404, message="Room not found")
        room.room_number = args['room_number']
        room.room_type = args['room_type']
        room.room_price_per_night = args['room_price_per_night']
        room.room_status = args['room_status']
        room.amenities = args['amenities']
        storage.save()
        return jsonify(room), 200

    def delete(self, room_id=None):
        if not room_id:
            abort(400, message="Room ID must be provided for delete request.")
        room = Room.query.filter_by(id=room_id).first()
        if not room:
            abort(404, message="Room not found")
        storage.delete(room)
        storage.save()
        return '', 204

    def get_all(self):
        rooms = Room.query.all()
        return jsonify(rooms), 200

    def get_room_by_id(self, room_id):
        room = Room.query.filter_by(id=room_id).first()
        if not room:
            abort(404, message="Room not found")
        return jsonify(room), 200
