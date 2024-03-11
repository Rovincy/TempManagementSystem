from flask import jsonify
from flask_restful import Resource, abort, reqparse
from models.review import Review
from models import storage

review_post_args = reqparse.RequestParser()
review_post_args.add_argument('customer_id', type=int, required=True, help='Customer ID is required')
review_post_args.add_argument('room_id', type=int, required=True, help='Room ID is required')
review_post_args.add_argument('rating', type=int, required=True, help='Rating is required')
review_post_args.add_argument('comment', type=str, required=True, help='Comment is required')
review_post_args.add_argument('date', type=str, required=True, help='Date is required')

class ReviewResource(Resource):
    def post(self, review_id=None):
        if review_id:
            abort(400, message="Review ID must not be provided for post request.")
        args = review_post_args.parse_args()
        review_obj = Review(
            customer_id=args['customer_id'],
            room_id=args['room_id'],
            rating=args['rating'],
            comment=args['comment'],
            date=args['date']
        )
        # save review to database
        storage.new(review_obj)
        storage.save()

        return jsonify(review_obj), 201

    def get(self, review_id=None):
        if not review_id:
            return self.get_all()
        return self.get_review_by_id(review_id)

    def put(self, review_id=None):
        if not review_id:
            abort(400, message="Review ID must be provided for put request.")
        args = review_post_args.parse_args()
        review = Review.query.filter_by(id=review_id).first()
        if not review:
            abort(404, message="Review not found")
        review.customer_id = args['customer_id']
        review.room_id = args['room_id']
        review.rating = args['rating']
        review.comment = args['comment']
        review.date = args['date']
        storage.save()
        return jsonify(review), 200

    def delete(self, review_id=None):
        if not review_id:
            abort(400, message="Review ID must be provided for delete request.")
        review = Review.query.filter_by(id=review_id).first()
        if not review:
            abort(404, message="Review not found")
        storage.delete(review)
        storage.save()
        return '', 204

    def get_all(self):
        reviews = Review.query.all()
        return jsonify(reviews), 200

    def get_review_by_id(self, review_id):
        review = Review.query.filter_by(id=review_id).first()
        if not review:
            abort(404, message="Review not found")
        return jsonify(review), 200
