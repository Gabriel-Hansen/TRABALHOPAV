from flask_restful import Resource, abort, fields, marshal_with, reqparse, request
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from ..repositories.funcionario_repository import get_funcionario, get_funcionarios, add_funcionario, update_funcionario, delete_funcionario

response_fields = {
    "id": fields.Integer,
    "nome": fields.String,
    "cpf": fields.String,
    "cargo": fields.String,
    "senha": fields.String
}

request_parser = reqparse.RequestParser(bundle_errors=True)
request_parser.add_argument("nome", type=str, help="", required=True)
request_parser.add_argument("cpf", type=str, help="", required=True)
request_parser.add_argument("cargo", type=str, help="", required=True)
request_parser.add_argument("senha", type=str, help="", required=True)

class FuncionarioItem(Resource):
    @marshal_with(response_fields)
    def get(self, id):
        try:
            funcionario = get_funcionario(id)
            if not funcionario:
                abort(404, message="Resource not found")
            return funcionario, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    def delete(self, id):
        try:
            delete_funcionario(id)
            return "", 204
        except UnmappedInstanceError:
            abort(404, message = "Resource not found")
        except:
            abort(500, message = "Internal Server Error")
    
    @marshal_with(response_fields)
    def put(self, id):
        try:
            args = request_parser.parse_args(strict=True)
            funcionario = update_funcionario(**args, id=id)
            return funcionario, 200
        except(OperationalError, IntegrityError):
            abort(500, message = "Internal Server Error")

class FuncionarioList(Resource):
    @marshal_with(response_fields)
    def get(self):
        try:
            return get_funcionarios(), 200
        except OperationalError:
            abort(500, message = "Internal Server Error")

    @marshal_with(response_fields)
    def post(self):
        try:
            args = request_parser.parse_args(strict=True)
            funcionario = add_funcionario(**args)
            return funcionario, 201
        except (OperationalError, IntegrityError):
            abort(500, message = "Internal Server Error")
