from sqlalchemy import create_engine, Column, Integer, String, Date, Float, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base


Base = declarative_base()
db = SQLAlchemy()

class Funcionario(Base):
    __tablename__ = 'funcionarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    cpf = Column(String)
    cargo = Column(String)
    senha = Column(String)
   
    cpf_unique_constraint = UniqueConstraint(cpf)
    name_unique_constraint = UniqueConstraint(nome)
    
class Item(Base):
    __tablename__ = 'itens'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    codigo_barras = Column(String)
    preco = Column(Float)
    quantidade_estoque = Column(Integer)
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))
    fornecedor = relationship("Fornecedor", back_populates="itens")
    
    name_unique_constraint = UniqueConstraint(nome)
    codigo_barras_unique_constraint = UniqueConstraint(codigo_barras)
    
class Fornecedor(Base):
    __tablename__ = 'fornecedores'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    endereco = Column(String)
    itens = relationship("Item", back_populates="fornecedor")
    
    name_unique_constraint = UniqueConstraint(nome)
    endereco_unique_constraint = UniqueConstraint(endereco)

class Venda(Base):
    __tablename__ = 'vendas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    item_id = Column(Integer, ForeignKey('itens.id'))
    item = relationship("Item")
    funcionario_id = Column(Integer, ForeignKey('funcionarios.id'))
    funcionario = relationship("Funcionario")
    quantidade_vendida = Column(Integer)
    total_vendido = Column(Integer)
    data_venda = Column(Date)

engine = create_engine('sqlite:///mercado.db')
Base.metadata.create_all(engine)