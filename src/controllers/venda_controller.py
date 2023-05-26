from flask_restful import Resource, abort, fields, marshal_with, reqparse, request
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from ..repositories.venda_repository import get_venda, get_vendas, add_venda, update_venda, delete_venda

response_fields ={
    "id": fields.Integer,
    "item_id": fields.Integer,
    "funcionario_id": fields.Integer,
    "quantidade_vendida": fields.Integer,
    "total_vendido": fields.Integer,
    "data_venda": fields.String
}

request_parser = reqparse.RequestParser(bundle_errors=True)
request_parser.add_argument("item_id", type=int, help="", required=True)
request_parser.add_argument("funcionario_id", type=int, help="", required=True)
request_parser.add_argument("quantidade_vendida", type=int, help="", required=True)
request_parser.add_argument("total_vendido", type=int, help="", required=True)
request_parser.add_argument("data_venda", type=str, help="", required=True)

class VendaItem(Resource):
    @marshal_with(response_fields)
    def get(self, venda_id):
        try:
            venda = get_venda(venda_id)
            if not venda:
                abort(404, message="Resource not found")
            return venda, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    def delete(self, venda_id):
        try:
            delete_venda(venda_id)
            return "", 204
        except UnmappedInstanceError:
            abort(404, message = "Resource not found")
        except:
            abort(500, message = "Internal Server Error")
    
    @marshal_with(response_fields)
    def put(self, venda_id):
        try:
            args = request_parser.parse_args(strict=True)
            venda = update_venda(**args, venda_id=venda_id)
            return venda, 200
        except(OperationalError, IntegrityError):
            abort(500, message = "Internal Server Error")

class VendaList(Resource):
    @marshal_with(response_fields)
    def get(self):
        try:
            return get_vendas(), 200
        except OperationalError:
            abort(500, message = "Internal Server Error")

    @marshal_with(response_fields)
    def post(self):
        try:
            args = request_parser.parse_args(strict=True)
            venda = add_venda(**args)
            return venda, 201
        except (OperationalError, IntegrityError):
            abort(500, message = "Internal Server Error")

