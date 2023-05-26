import sqlalchemy
from ..models.models import Funcionario, db  

def get_funcionarios() -> sqlalchemy.orm.query.Query:
    funcionarios = db.session.query(Funcionario).all()
    return funcionarios

def get_funcionario(id: int) -> Funcionario:
    funcionario = db.session.query(Funcionario).get(id)
    return funcionario

def delete_funcionario(id: int):
    funcionario = db.session.query(Funcionario).get(id)
    db.session.delete(funcionario)
    db.session.commit()

def add_funcionario(nome: str, cpf: str, cargo: str, senha: str) -> Funcionario:
    
    funcionario = Funcionario(nome=nome, cpf=cpf, cargo=cargo, senha=senha)
    db.session.add(funcionario)
    db.session.commit()
    return funcionario

def update_funcionario(nome: str, cpf: str, cargo: str, senha: str, id: int) -> Funcionario:
    funcionario = db.session.query(Funcionario).get(id)

    funcionario.nome = nome
    funcionario.cpf = cpf
    funcionario.cargo = cargo
    funcionario.senha = senha

    db.session.commit()
    
    return funcionario