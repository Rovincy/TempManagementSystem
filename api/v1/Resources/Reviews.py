from flask import jsonify
from flask_restful import Resource, abort, reqparse
from models.review import Review
from api.v1.app import api
from datetime import datetime

review_post_args = reqparse.RequestParser()
review_post_args.add_argument('customer_id', type=int, required=True, help='Customer ID is required')
review_post_args.add_argument('room_id', type=int, required=True, help='Room ID is required')
review_post_args.add_argument('rating', type=int, required=True, help='Rating is required')
review_post_args.add_argument('comment', type=str, required=True, help='Comment is required')
review_post_args.add_argument('date', type=lambda x: datetime.strptime(x,'%Y-%m-%d %H:%M:%S'), required=True, help='Date is required')

class ReviewResource(Resource):
    def post(self):
        args = review_post_args.parse_args()
        review = Review(
            customer_id=args['customer_id'],
            room_id=args['room_id'],
            rating=args['rating'],
            comment=args['comment'],
            date=args['date']
        )
        # save review to database
        return jsonify(review), 201

    def get(self, review_id):
        review = Review.query.filter_by(id=review_id).first()
        if not review:
            abort(404, message="Review not found")
        return jsonify(review)

    def put(self, review_id):
        args = review_post_args.parse_args()
        review = Review.query.filter_by(id=review_id).first()
        if not review:
            abort(404, message="Review not found")
        review.customer_id = args['customer_id']
        review.room_id = args['room_id']
        review.rating = args['rating']
        review.comment = args['comment']
        review.date = args['date']
        # db.session.commit()
        return jsonify(review)

    def delete(self, review_id):
        review = Review.query.filter_by(id=review_id).first()
        if not review:
            abort(404, message="Review not found")
        # db.session.delete(review)
        # db.session.commit()
        return '', 204

api.add_resource(ReviewResource, '/review/<int:review_id>')
