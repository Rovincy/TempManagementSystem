from flask import jsonify
from flask_restful import Resource, abort, reqparse
from models.products_services import ProductAndService
from api.v1.app import api

Product_post_args = reqparse.RequestParser()
Product_post_args.add_argument('name', type=str, required=True, help='Name is required')
Product_post_args.add_argument('price_per_unit', type=float, required=True, help='Price per unit is required')
Product_post_args.add_argument('quantity', type=int, required=True, help='Quantity is required')


class ProductResource(Resource):
    def post(self):
        args = Product_post_args.parse_args()
        product = ProductAndService(
            name=args['name'],
            price_per_unit=args['price_per_unit'],
            quantity=args['quantity']
        )
        # save product to database
        return jsonify(product), 201

    def get(self, Product_id):
        product = ProductAndService.query.filter_by(id=Product_id).first()
        if not product:
            abort(404, message="product not found")
        return jsonify(product)

    def put(self, Product_id):
        args = Product_post_args.parse_args()
        product = ProductAndService.query.filter_by(id=Product_id).first()
        if not product:
            abort(404, message="Product not found")
        product.name = args['name']
        product.price_per_unit = args['price_per_unit']
        product.quantity = args['quantity']
        # db.session.commit()
        return jsonify(product)

    def delete(self, Product_id):
        product = ProductAndService.query.filter_by(id=Product_id).first()
        if not product:
            abort(404, message="Product not found")
        # db.session.delete(Product)
        # db.session.commit()
        return '', 204


api.add_resource(ProductResource, '/Product/<int:Product_id>')




# from models.payment import Payment
#
# class ProductResource(Resource):
#     # existing methods...
#
#     def purchase(self, Product_id, quantity):
#         product = ProductAndService.query.filter_by(id=Product_id).first()
#         if not product:
#             abort(404, message="Product not found")
#
#         if product.quantity < quantity:
#             return {"message": "Not enough quantity available"}, 400
#
#
#         # update the quantity of the product
#         product.quantity -= quantity
#         # save product to database
#
#         return product.price_per_unit * quantity
