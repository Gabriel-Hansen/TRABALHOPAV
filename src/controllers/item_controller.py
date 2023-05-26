from flask_restful import Resource, abort, fields, marshal_with, reqparse, request
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from ..repositories.item_repository import get_item, get_itens, add_item, update_item, delete_item

response_fields ={
    "id": fields.Integer,
    "nome": fields.String,
    "codigo_barras": fields.String,
    "preco": fields.Float,
    "quantidade_estoque": fields.Integer,
    "fornecedor_id": fields.Integer
}

request_parser = reqparse.RequestParser(bundle_errors=True)
request_parser.add_argument("nome", type=str, help="", required=True)
request_parser.add_argument("codigo_barras", type=str, help="", required=True)
request_parser.add_argument("preco", type=float, help="", required=True)
request_parser.add_argument("quantidade_estoque", type=int, help="", required=True)
request_parser.add_argument("fornecedor_id", type=int, help="", required=True)

class ItemItem(Resource):
    @marshal_with(response_fields)
    def get(self, id):
        try:
            item = get_item(id)
            if not item:
                abort(404, message="Resource not found")
            return item, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    def delete(self, id):
        try:
            delete_item(id)
            return "", 204
        except UnmappedInstanceError:
            abort(404, message = "Resource not found")
        except:
            abort(500, message = "Internal Server Error")
    
    @marshal_with(response_fields)
    def put(self, id):
        try:
            args = request_parser.parse_args(strict=True)
            item = update_item(**args, id=id)
            return item, 200
        except(OperationalError, IntegrityError):
            abort(500, message = "Internal Server Error")

class ItemList(Resource):
    @marshal_with(response_fields)
    def get(self):
        try:
            return get_itens(), 200
        except OperationalError:
            abort(500, message = "Internal Server Error")

    @marshal_with(response_fields)
    def post(self):
        try:
            args = request_parser.parse_args(strict=True)
            item = add_item(**args)
            return item, 201
        except (OperationalError, IntegrityError):
            abort(500, message = "Internal Server Error")
