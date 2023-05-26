from flask_restful import Resource, abort, fields, marshal_with, reqparse, request
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from ..repositories.fornecedor_repository import get_fornecedor, get_fornecedores, add_fornecedor, update_fornecedor, delete_fornecedor

response_fields ={
    "id": fields.Integer,
    "nome": fields.String,
    "endereco": fields.String,
}

request_parser = reqparse.RequestParser(bundle_errors=True)
request_parser.add_argument("nome", type=str, help="", required=True)
request_parser.add_argument("endereco", type=str, help="", required=True)

class FornecedorItem(Resource):
    @marshal_with(response_fields)
    def get(self, id):
        try:
            fornecedor = get_fornecedor(id)
            if not fornecedor:
                abort(404, message="Resource not found")
            return fornecedor, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    def delete(self, id):
        try:
            delete_fornecedor(id)
            return "", 204
        except UnmappedInstanceError:
            abort(404, message = "Resource not found")
        except:
            abort(500, message = "Internal Server Error")
    
    @marshal_with(response_fields)
    def put(self, id):
        try:
            args = request_parser.parse_args(strict=True)
            fornecedor = update_fornecedor(**args, id=id)
            return fornecedor, 200
        except(OperationalError, IntegrityError):
            abort(500, message = "Internal Server Error")

class FornecedorList(Resource):
    @marshal_with(response_fields)
    def get(self):
        try:
            return get_fornecedores(), 200
        except OperationalError:
            abort(500, message = "Internal Server Error")

    @marshal_with(response_fields)
    def post(self):
        try:
            args = request_parser.parse_args(strict=True)
            fornecedor = add_fornecedor(**args)
            return fornecedor, 201
        except (OperationalError, IntegrityError):
            abort(500, message = "Internal Server Error")