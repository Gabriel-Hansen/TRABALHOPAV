import sqlalchemy
from ..models.models import Fornecedor, db

def get_fornecedores() -> sqlalchemy.orm.query.Query:
    fornecedores = db.session.query(Fornecedor).all()
    return fornecedores

def get_fornecedor(id: int) -> Fornecedor:
    fornecedor = db.session.query(Fornecedor).get(id)
    return fornecedor

def delete_fornecedor(id: int):
    fornecedor = db.session.query(Fornecedor).get(id)
    db.session.delete(fornecedor)
    db.session.commit()

def add_fornecedor(nome: str, endereco: str) -> Fornecedor:
    
    fornecedor = Fornecedor(nome=nome, endereco=endereco)
    db.session.add(fornecedor)
    db.session.commit()
    return fornecedor
    
def update_fornecedor(nome: str, endereco: str, id: int) -> Fornecedor:
    fornecedor = db.session.query(Fornecedor).get(id)

    fornecedor.nome = nome
    fornecedor.endereco = endereco

    db.session.commit()
    
    return fornecedor